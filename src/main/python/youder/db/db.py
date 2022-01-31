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


from sqlite3 import *
class DB:
    CREATE_TABLE = """
    create table  if not EXISTS history(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				video_id varchar,
                url varchar,
				title varchar,
				thumbnail BLOB,
                thumbnail_url varchar,
                author varchar,
				channel_id varchar,
                channel_url varchar,
                description varchar,
				views integer,
				length INTEGER,
                publish_date datetime,
				download_time datetime,
				location varchar
				);
    """
    
    def __init__(self,db_file:str) -> None:

        self.connection = connect(db_file,check_same_thread=False)
        self.cursor = self.connection.cursor()

        self.cursor.execute(self.CREATE_TABLE)
        self.connection.commit()

    
    def add_video(self,**video) -> None:

        command = f"""
        insert into history ({" , ".join(video.keys())}) values (?{" ,?"* (len(video.keys())-1)}) ;"""
        # {" , ".join(['"'+str(value)+'"' for value  in video.values()])}
        
        self.cursor.execute(command,[value for value in video.values()])
        self.connection.commit()

    def select(self,*args):

        command = "select * from history order by datetime(download_time) desc;" if not args else f"""select {" , ".join(args)} from  history order by datetime(download_time) desc;"""

        return self.connection.execute(command).fetchall()

    def delete_all_records(self):
        self.cursor.execute("delete from history;")
        self.connection.commit()

    def remove_video(self,id:int) -> None:
        self.connection.execute(f"delete from history where id={id}")
        self.connection.commit()
        



if __name__ == "__main__":
    # from datetime import datetime
    # db = DB("temp.db")
    # db.add_video(video_id = "dklfjdl",title= "hellow",thumbnail = b'/fjdl/fkld',channel = "channel",views= 8347893,length=3878394,location="path/to/foo/file",download_time=datetime.today())
    # for row in db.select() : print(row)
    #db.delete_all_records()
    pass

        

        
        

        


