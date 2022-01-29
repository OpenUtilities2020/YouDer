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


from traceback import print_tb
from PySide2.QtCore import QSettings,QObject
from typing import Any, Optional, Set,Union
import PySide2

class Settings(QSettings):
    """
    Class settings : Implementation of Pyside2.QtCore.QSettings Class
    """

    def __init__(self,
                organization:str = __organization__, 
                application:str = __application__,
                *args,**kwargs) -> None:
        """
        @param : organization > string representation of Application's Organization name
        @param : application > string reperesentation of Application name

        @returns : None
        """
        super(Settings, self).__init__(organization,application)

    def get(self, value:str,default_value:Any=None) -> Any:
        """
        @param : value > key
        @param : default_value > value if key not exits 

        @returns : Any > type of dafault_value 

        Simaliar Method of QSettings().value(value,defaultValue,type)
        """
        return super(Settings, self).value(value,default_value)

    def set(self,name,value) :
         super(Settings, self).setValue(name,value)

    def __getattr__(self, __name: str) -> Any:
        """
        @param : __name > Attribute Name
        @return : Any 
        """
        return self.get(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        @param : __name > key 
        @param : __value > value 

        @return : None
        """
        self.set(__name,__value)

if __name__ == "__main__":
    s = Settings()
    # s.theme = "green"
    print(bool(s.dark_mode))
    print(s.dark_mode)





