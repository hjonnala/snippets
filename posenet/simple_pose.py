# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw

import numpy as np
import os
from pose_camera import EDGES
import svgwrite

os.system('wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/'
          'Hindu_marriage_ceremony_offering.jpg/'
          '640px-Hindu_marriage_ceremony_offering.jpg -O /tmp/couple.jpg')
pil_image = Image.open('/tmp/couple.jpg').convert('RGB')
engine = PoseEngine(
    'models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')
poses, inference_time = engine.DetectPosesInImage(pil_image)
print('Inference time: %.f ms' % (inference_time * 1000))


svg_canvas = svgwrite.Drawing('', size=pil_image.size)
for pose in poses:
    xys = {}
    if pose.score < 0.4: continue
    print('\nPose Score: ', pose.score)
    for label, keypoint in pose.keypoints.items():
        print('  %-20s x=%-4d y=%-4d score=%.1f' %
              (label.name, keypoint.point[0], keypoint.point[1], keypoint.score))
        kp_x = int(keypoint.point[0])
        kp_y = int(keypoint.point[1])

        xys[label] = (kp_x, kp_y)
        # svg_canvas.add(svg_canvas.circle(center=(int(kp_x), int(kp_y)), r=5,
        #                    fill='cyan', fill_opacity=keypoint.score, stroke='yellow'))

        ImageDraw.Draw(pil_image).point((int(kp_x), int(kp_y)))


    for a, b in EDGES:
        if a not in xys or b not in xys: continue
        ax, ay = xys[a]
        bx, by = xys[b]
        # svg_canvas.add(svg_canvas.line(start=(ax, ay), end=(bx, by), stroke='yellow', stroke_width=2))
        ImageDraw.Draw(pil_image).line([(ax, ay), (bx, by)])
# svg_canvas.saveas('out.jpg')

pil_image.show()