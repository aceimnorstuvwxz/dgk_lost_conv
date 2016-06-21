#usage genall.sh thefolder output.conv
echo $1
echo $2
fold=$1
outf=$2
rm $fold/*.conv
rm $outf
cnt=0

for f in $fold/*.srt; do
  echo $cnt;
  ./cvgen.py "$f" "$f.conv";
  cnt=$[ cnt + 1 ];
done

for f in $fold/*.conv; do
  echo "$f";
  cat "$f" >> "$outf";
done
