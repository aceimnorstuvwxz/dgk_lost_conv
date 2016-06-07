
asstosrt -s utf-8
注意输出 utf-8编码的 srt 文件
ass ----asstosrt---->srt

srt ----cvgen.py---->.conv

.conv 格式
一行表示一个单边语句，一个对话由来回的多个行组成。在每个行的开头做标记，M 表示话语，E 表示分割。
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
E
