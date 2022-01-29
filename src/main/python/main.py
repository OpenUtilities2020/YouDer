# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Open Utilities
# Created by : Ram Durga Sai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE

__organization__ = "OpenUtilites"
__application__ = "YouDer"
__version__ = "3.0"
__author__ = " Ram Durga Sai "


import sys

from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property

from youder.youder import YouDer

class AppContext(ApplicationContext):
    '''Class Application Context'''
    def run(self):
        self.main_window.show()
        return self.app.exec_()
    @cached_property
    def main_window(self):
        return YouDer(self)
    @cached_property
    def dark(self):
        '''Returns Dark .css file path '''
        return (self.get_resource('resources/dark.css'))
    @cached_property
    def dark_frame(self):
         return self.get_resource('resources/dark_frame.css')
    @cached_property
    def white(self):
        '''Returns White.css file path'''
        return (self.get_resource('resources/white.css'))
    @cached_property
    def resources(self):
        '''Returns resources dir path  '''
        return (self.get_resource('resources'))
    @cached_property
    def log(self):
        '''Returns log.txt file to store log data into a file'''
        return (self.get_resource('resources/log.txt'))

    @cached_property
    def ffmpeg(self):
        '''Returns ffmpeg.exe file path

        The size of official build of ffmpeg is  80Mb
        So Small and tiny version of ffmpeg is taken from the Following Github Page
        https://github.com/n00mkrad/smol-ffmpeg/'''
        return (self.get_resource('resources/ffmpeg.exe'))

    @cached_property
    def db(self): return (self.get_resource('resources/db.db'))

if __name__ == "__main__":
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)