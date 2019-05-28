import os
import sys
import datetime
from moviepy.editor import VideoFileClip

times=[]

def tranverse_video_file(video_path):
    names = os.listdir(video_path)
    for name in names:
        sub_name=os.path.join(video_path, name)
        if os.path.isdir(sub_name):
            tranverse_video_file(sub_name)
        else:
            if sub_name.endswith('.avi'):
                clip = VideoFileClip(sub_name)
                print('{0}-----{1}'.format(name,datetime.timedelta(seconds=clip.duration)))
                # global times  #全局变量未进行赋值操作，这句可以省略
                times.append(clip.duration)
                clip.reader.close()
                clip.audio.reader.close_proc()

             

def print_total_time():
    # global times #全局变量未进行赋值操作，这句可以省略
    total=sum(times)
    print('total time-----{0}'.format(datetime.timedelta(seconds=total)))   

def excetue():
    if len(sys.argv)!=2:
        print('input 1 parameter:video_path')
        return
    tranverse_video_file(sys.argv[1])
    print_total_time()

if __name__ == '__main__':
    excetue()
