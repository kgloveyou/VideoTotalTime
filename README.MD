### 功能描述：

    统计文件夹中avi视频文件的总时长。

### 执行命令如下：

```
python video_total_time.py F:\download\2018.03《Python3全栈工程师》_技术能力内训
```

如果报错：

```
Traceback (most recent call last):
  File "video_total_time.py", line 39, in <module>
    excetue()
  File "video_total_time.py", line 35, in excetue
    tranverse_video_file(sys.argv[1])
  File "video_total_time.py", line 19, in tranverse_video_file
    clip = VideoFileClip(sub_name)
  File "C:\Python37\lib\site-packages\moviepy\video\io\VideoFileClip.py", line 91, in __init__
    fps_source=fps_source)
  File "C:\Python37\lib\site-packages\moviepy\video\io\ffmpeg_reader.py", line 33, in __init__
    fps_source)
  File "C:\Python37\lib\site-packages\moviepy\video\io\ffmpeg_reader.py", line 262, in ffmpeg_parse_infos
    infos = proc.stderr.read().decode('utf8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 1545: invalid continuation byte
```

**解决办法**：
请修改 ffmpeg_reader.py 262行，改成.decode('utf8','ignore')即可

