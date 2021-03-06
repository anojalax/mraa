#!/usr/bin/env python

# Author: Alex Tereschenko <alext.mkrs@gmail.com>
# Copyright (c) 2016 Alex Tereschenko.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import mraa as m
import unittest as u

from uart_checks_shared import *

class UartChecksSetBaudrate(u.TestCase):
  def setUp(self):
    self.uart = m.Uart(MRAA_UART_DEV_NUM)

  def tearDown(self):
    del self.uart

  def test_uart_baudrate_115200(self):
    TEST_BAUDRATE = 115200
    self.assertEqual(self.uart.setBaudRate(TEST_BAUDRATE),
                     m.SUCCESS,
                     "Setting baudrate to %d did not return success" % TEST_BAUDRATE)

  def test_uart_baudrate_invalid_bigger_than_max(self):
    TEST_BAUDRATE = 10000000
    self.assertEqual(self.uart.setBaudRate(TEST_BAUDRATE),
                     m.ERROR_INVALID_PARAMETER,
                     "Setting baudrate to %d did not return INVALID_PARAMETER" % TEST_BAUDRATE)

if __name__ == "__main__":
  u.main()
