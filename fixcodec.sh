#usage fixcodec.sh thefolder
#所有切换到 utf-8
echo $1

#for f in  "$1/*.utf8_dgk.srt"; do
    #文件名 太长 而不一定能跑
#    rm $f
#done

for f in $1/*.srt; do
    echo "$f"
    cod=$(uchardet "$f")
    iconv -f $cod -t utf-8 "$f" > "${f%.srt}.utf8_dgk.srt"
    rm -f "$f"
done
