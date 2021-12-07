# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Drivers for shared functionality provided by the Environment Bonnet."""
import os
import platform
from luma.core.interface.serial import noop, spi
from luma.oled.device import ssd1306
def _get_path(sysfs_name):
    search_path = '/sys/bus/iio/devices/'
    try:
        for fname in os.listdir(search_path):
            with open(search_path + fname + '/name', 'r') as f:
                if sysfs_name in f.read():
                    return search_path + fname
        return ''
    except FileNotFoundError:
        return ''
def _read_sysfs(path, retries=2):
    try:
        with open(path, 'r') as f:
            # Allow multiple attempts in case sensor times out.
            for _ in range(retries):
                try:
                    data = f.read()
                    if data:
                        return float(data)
                except:
                    pass
            return None
    except FileNotFoundError:
        return None
class EnviroBoard():
    """
    An interface for all input and output modules on the Environmental Sensor Board.
    """
    def __init__(self):
        # Obtain the full sysfs path of the IIO devices.
        self._hdc2010 = _get_path('hdc20x0')
        self._bmp280 = _get_path('bmp280')
        self._opt3002 = _get_path('opt3001')
        self._tla2021 = _get_path('ads1015')
        # Create SSD1306 OLED instance, with SPI as the interface.
        plat = platform.platform()
        if 'mendel' in plat:
            from rpi_gpio_periphery import pGPIO
            # Values for the Coral Dev Board (running Mendel Linux).
            # If running legacy kernel (4.9.51), use port 32766.
            port = 32766 if 'Linux-4.9.51-imx' in plat else 0
            self._display = ssd1306(serial_interface=spi(gpio=pGPIO(), port=port, device=0, gpio_DC=388, gpio_RST=394),
                                    gpio=pGPIO(), height=32, rotate=2)
        else:
            # Default to RPi.GPIO in luma and defaults GPIO.
            self._display = ssd1306(serial_interface=spi(),
                                    gpio=noop(), height=32, rotate=2)
    @property
    def temperature(self):
        """
        Gets the current temperature, in Celsius.
        """
        temperature = _read_sysfs(self._hdc2010 + '/in_temp_input')
        if temperature is not None:
            return temperature
        temperature = _read_sysfs(self._bmp280 + '/in_temp_input')
        # BMP280 reports as mC.
        if temperature is not None:
            return temperature / 1000.0
        return None
    @property
    def humidity(self):
        """
        Gets the current relative humidity, in percentage.
        """
        return _read_sysfs(self._hdc2010 + '/in_humidityrelative_input')
    @property
    def ambient_light(self):
        """
        Gets the ambient light, in lux.
        """
        return _read_sysfs(self._opt3002 + '/in_illuminance_input')
    @property
    def pressure(self):
        """
        Gets the current atmospheric pressure, in kPa.
        """
        return _read_sysfs(self._bmp280 + '/in_pressure_input')
    @property
    def grove_analog(self):
        """
        Gets a raw value from a device connected to the board's analog Grove connector.
        .. note::
            ADC is set to +/- 6V range, independent of supply voltage (selected by jumper).
        """
        return _read_sysfs(self._tla2021 + '/in_voltage0_raw')
    @property
    def display(self):
        """
        Gets an instance of :class:`luma.core.device.device` representing the board's OLED display.
        For example, you can write to the display using :class:`luma.core.render.canvas`
        as follows::
            enviro = EnviroBoard()
            update_display(enviro.display, "Hello world")
            def update_display(display, msg):
                with canvas(display) as draw:
                    draw.text((0, 0), msg, fill='white')
        """
        return self._display
