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
"""Wrapper to enable RPi.GPIO API with periphery."""
from periphery import GPIO
class pGPIO(object):
    # Convert values expected from RPi.GPIO
    IN = "in"
    OUT = "out"
    HIGH = True
    LOW = False
    _gpios = dict()
    def setup(self, channels, mode):
        if isinstance(channels, (list, tuple)):
            for i in channels:
                self._gpios[i] = GPIO(i, mode)
        else:
            self._gpios[channels] = GPIO(channels, mode)
    def output(self, channels, level):
        if isinstance(channels, (list, tuple)):
            for i in channels:
                self._gpios[i].write(level)
        else:
            self._gpios[channels].write(level)
    def input(self, channel):
        return self._gpios[channel].read()
