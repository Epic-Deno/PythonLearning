'''
Description: 文件搬运
Purpose: Powered By Fantastic Artwork Vue.js @ Evan You.
Version: 2.6.1
Author: PONY ZHANG
Date: 2021-04-11 16:01:31
LastEditors: PONY ZHANG
LastEditTime: 2021-04-12 11:13:31
motto: 「あなたに逢えなくなって、錆びた時計と泣いたけど…」
topic: # Carry Your World #
Github: Epic-Deno
Blogs: https://epic-deno.github.io/deno.github.io/
Pony: http://scorpionz.gitee.io/pony-zhang/
Juejin: https://juejin.im/user/1151943917713623
Zhihu: https://www.zhihu.com/people/zhang-zhen-36-44
'''
# encoding: utf-8
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

# 需要追踪的文件夹
folder_to_track = "/Users/zhangzhen/downloads" 
#图片文件夹
folder_destination_pic = "/Users/zhangzhen/pictures/newPictures"
#音乐文件
folder_destination_music = "/Users/zhangzhen/music/newMusic"
#视频文件
folder_destination_movies = "/Users/zhangzhen/Movies/newMoives"
#文档文件夹
folder_destination_documents = "/Users/zhangzhen/Documents/dailyDocuments"
#代码文件压缩包
folder_destination_code = "/Users/zhangzhen/learns/CodeReview"

# 创建文件监听器
class Myhandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" +filename
            if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("jpeg") or filename.endswith("gif"):
                new_destination = folder_destination_pic + "/" + filename
            elif filename.endswith("mp3"):
                new_destination = folder_destination_music + "/" + filename
            elif filename.endswith("mp4") or filename.endswith("avi") or filename.endswith("webm"):
                new_destination = folder_destination_movies + "/" + filename
            elif filename.endswith("xlsx") or filename.endswith("ppt") or filename.endswith("text") or filename.endswith("xls") or filename.endswith("doc") or filename.endswith("docx") or filename.endswith("xmd") or filename.endswith("cvs"):
                new_destination = folder_destination_documents + "/" + filename
            elif filename.__contains__("code") or filename.__contains__("vue") or filename.__contains__("react") or filename.__contains__("py") or filename.__contains__('js') or filename.__contains__('html') or filename.__contains__('css') or filename.__contains__("zip") or filename.__contains__("rar"):
                new_destination = folder_destination_code + "/" + filename
            else:
                new_destination = folder_to_track + "/" + filename

            os.rename(src, new_destination)
            
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
        observer.stop()
    
observer.join()