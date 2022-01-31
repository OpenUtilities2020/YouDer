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

import sys
from pathlib import Path
from os import environ, makedirs,path,mkdir
from os.path import join,isdir
from typing import Union

from PySide2.QtWidgets import QMessageBox,QFileDialog
def user_profile(*dirs):
    '''Check Operating System for Path of Video'''
    if sys.platform == "linux" or sys.platform == "linux2" or  sys.platform == "darwin": user_dir = Path.home()
    elif sys.platform == "win32": user_dir = environ['USERPROFILE']

    for dir in dirs : user_dir = path.join(user_dir,dir)
    return user_dir

def ask_to_choose_directory() -> Union[str,None]:
    """
    @returns: path [Stirng | None]
    """
    dailog = QFileDialog()
    return dailog.getExistingDirectory()

def create_dir(path:str) -> str:
    """
    creates Directory for path
    :param path: directory path
    """
    if not isdir(path) : mkdir(path)
    return path

    