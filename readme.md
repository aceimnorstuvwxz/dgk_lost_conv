```
========dgk_lost_conv========

chinese conversation corpus

可以用作聊天机器人的训练语料

```



聊天机器人训练语料交流群:

![](qun.png)
[网易云课堂视频课程1-聊天机器人](https://study.163.com/course/introduction/1005049028.htm?utm_source=400000000173015&utm_medium=share&utm_campaign=commission&hideAppEntrance=1)   [网易云课堂视频课程2-知识图谱](https://study.163.com/course/introduction/1004964005.htm?utm_source=400000000173015&utm_medium=share&utm_campaign=commission&hideAppEntrance=1)

```


结果：

dgk_shooter_z.conv 110MB 已分词

dgk_shooter_min.conv 按字分词

lost.conv 1.7MB

fanzxl.conv 2.3MB

fk24.conv 4.5MB

haosys.conv 1.3MB

juemds.conv 793KB

laoyj.conv 1.5MB

prisonb.conv 543KB

内部方法：

asstosrt -s utf-8

ass ----asstosrt---->srt

srt ----cvgen.py---->.conv

特别的shooter73g:

进入shooterwp，

解压缩mirror.x到rawbase下面

执行sel.sh

在跟目录下

fixcodec修正编码

fixtranc繁简处理

genall

.conv 格式:

//M 表示话语，E 表示分割。

E

M 话语 a

M 话语 b

M 话语 c

M 话语 d

E

M 话语 a

M 话语 b

M 话语 c

M 话语 d

License:

MIT

```

