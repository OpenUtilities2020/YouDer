#!/usr/bin/env python3
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
__application__  = "YouDer"
__version__ = "3.0"
__author__ = " Ram Durga Sai "

from PySide2.QtCore import QObject,Signal


class Communication(QObject):
    '''
    Qt Custom Signal to Carry Data from Bakcend Threads to UI
    '''

    status_bar_message = Signal(str)

    getinfo_finished = Signal (bool)

    error_dialog = Signal(str,str)

    video_title = Signal(str)

    video_auther = Signal(str)

    video_length = Signal(str)

    video_views = Signal(str)

    thumbnail = Signal(bool)

    new_format = Signal(str,object,bool)

    show_download_button = Signal(bool)

    transmit_yt = Signal(object)

    progress = Signal(int)

    # New Signals

    video = Signal(dict)

    stream = Signal(dict)

    fetch = Signal(bool)

    download_completed = Signal(object)