from periphery import GPIO
import time
import argparse
import contextlib
import fcntl
import os
import select
import sys
import termios
import threading

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')

from functools import partial
from gi.repository import GLib, GObject, Gst, GstBase
from PIL import Image



GObject.threads_init()
Gst.init(None)

WIDTH = 2592
HEIGHT = 1944

FILENAME_PREFIX = 'img'
FILENAME_SUFFIX = '.png'
AF_SYSFS_NODE = '/sys/module/ov5645_camera_mipi_v2/parameters/ov5645_af'
CAMERA_INIT_QUERY_SYSFS_NODE = '/sys/module/ov5645_camera_mipi_v2/parameters/ov5645_initialized'
HDMI_SYSFS_NODE = '/sys/class/drm/card0/card0-HDMI-A-1/status'

# No of initial frames to throw away before camera has stabilized
SCRAP_FRAMES = 1

SRC_WIDTH = 2592
SRC_HEIGHT = 1944
SRC_RATE = '15/1'
SRC_ELEMENT = 'v4l2src'

SINK_WIDTH = 2592
SINK_HEIGHT = 1944
SINK_ELEMENT = ('appsink name=appsink sync=false emit-signals=true '
                'max-buffers=1 drop=true')
SCREEN_SINK = 'glimagesink sync=false'
FAKE_SINK = 'fakesink sync=false'

SRC_CAPS = 'video/x-raw,format=YUY2,width={width},height={height},framerate={rate}'
SINK_CAPS = 'video/x-raw,format=RGB,width={width},height={height}'
LEAKY_Q = 'queue max-size-buffers=1 leaky=downstream'

PIPELINE = '''
    {src_element} ! {src_caps} ! {leaky_q} ! tee name=t
    t. ! {leaky_q} ! {screen_sink}
    t. ! {leaky_q} ! videoconvert ! {sink_caps} ! {sink_element}
    '''


def on_bus_message(bus, message, loop):
  t = message.type
  if t == Gst.MessageType.EOS:
    loop.quit()
  elif t == Gst.MessageType.WARNING:
    err, debug = message.parse_warning()
    sys.stderr.write('Warning: %s: %s\n' % (err, debug))
  elif t == Gst.MessageType.ERROR:
    err, debug = message.parse_error()
    sys.stderr.write('Error: %s: %s\n' % (err, debug))
    loop.quit()
  return True


def on_new_sample(sink, snapinfo):

  if not snapinfo.save_frame():
    # Throw away the frame
    return Gst.FlowReturn.OK

  sample = sink.emit('pull-sample')

  buf = sample.get_buffer()
  result, mapinfo = buf.map(Gst.MapFlags.READ)
  if result:
    imgfile = snapinfo.get_filename()
    caps = sample.get_caps()
    width = WIDTH
    height = HEIGHT
    img = Image.frombytes('RGB', (width, height), mapinfo.data, 'raw')
    img.save(imgfile)
    img.close()
  buf.unmap(mapinfo)
  return Gst.FlowReturn.OK


def run_pipeline(snapinfo):
  src_caps = SRC_CAPS.format(width=SRC_WIDTH, height=SRC_HEIGHT, rate=SRC_RATE)
  sink_caps = SINK_CAPS.format(width=SINK_WIDTH, height=SINK_HEIGHT)
  screen_sink = FAKE_SINK


  pipeline = PIPELINE.format(
      leaky_q=LEAKY_Q,
      src_element=SRC_ELEMENT,
      src_caps=src_caps,
      sink_caps=sink_caps,
      sink_element=SINK_ELEMENT,
      screen_sink=screen_sink)

  pipeline = Gst.parse_launch(pipeline)
  appsink = pipeline.get_by_name('appsink')
  appsink.connect('new-sample', partial(on_new_sample, snapinfo=snapinfo))

  loop = GObject.MainLoop()

  # Set up a pipeline bus watch to catch errors.
  bus = pipeline.get_bus()
  bus.add_signal_watch()
  bus.connect('message', on_bus_message, loop)

  # Connect the loop to the snaphelper
  snapinfo.connect_loop(loop)

  # Run pipeline.
  pipeline.set_state(Gst.State.PLAYING)

  try:
    loop.run()
  except:
    pass

  # Clean up.
  pipeline.set_state(Gst.State.NULL)
  while GLib.MainContext.default().iteration(False):
    pass



class SnapHelper:

  def __init__(self, sysfs, prefix='img', oneshot=True, suffix='jpg'):
    self.prefix = prefix
    self.oneshot = oneshot
    self.suffix = suffix
    self.snap_it = oneshot
    self.num = 0
    self.scrapframes = SCRAP_FRAMES
    self.sysfs = sysfs



  def get_filename(self):
    while True:
      filename = self.prefix + str(self.num).zfill(4) + '.' + self.suffix
      self.num = self.num + 1
      if not os.path.exists(filename):
        break
    return filename

  #def check_af(self):
    #try:
    #  self.sysfs.seek(0)
    #  v = self.sysfs.read()
    #  if int(v) != 0x10:
    #    print('NO Focus')
    #except:
     # pass

  # def refocus(self):
   # try:#
   #   self.sysfs.write('1')
   #   self.sysfs.flush()
   # except:
   #   pass

  def save_frame(self):
    # We always want to throw away the initial frames to let the
    # camera stabilize. This seemed empirically to be the right number
    # when running on desktop.
    if self.scrapframes > 0:
      self.scrapframes = self.scrapframes - 1
      return False

    if self.snap_it:
      self.snap_it = False
      retval = True
    else:
      retval = False

    if self.oneshot:
       self.loop.quit()

    return retval

  def connect_loop(self, loop):
    self.loop = loop


def take_picture(snap):
    start_time = int(round(time.time()))
    run_pipeline(snap)
    print(time.time()- start_time)


def main():
    button = GPIO(138, "in")
    last_state = False

    with open(AF_SYSFS_NODE, 'w+') as sysfs:
      snap = SnapHelper(sysfs, 'test', 'oneshot', 'jpg')
      sysfs.write('2')

    while 1:
        button_state = button.read()

        if(button_state==True and last_state == False):


            snap = SnapHelper(sysfs, 'test', 'oneshot', 'jpg')
            take_picture(snap)

        last_state = button_state


if __name__== "__main__":
    main()
    sys.exit()
