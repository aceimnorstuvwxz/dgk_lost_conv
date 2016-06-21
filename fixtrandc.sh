#usage fixtranc.sh thefolder
#繁体-》简体
echo $1

for f in $1/*.srt; do
    echo $f
    opencc -i "$f" -o "${f%.srt}.han.srt" -c t2s.json
    rm "$f"
done
