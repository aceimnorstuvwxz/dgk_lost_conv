========从字幕文件构建的中文对话脚本 conversation corpus========

结果：
dkg_lost.conv

方法：
asstosrt -s utf-8
注意输出 utf-8编码的 srt 文件
ass ----asstosrt---->srt
srt ----cvgen.py---->.conv

dkg_lost.conv 格式:
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

No commercial use, all rights reserved.
