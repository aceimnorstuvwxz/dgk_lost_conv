#usage genall.sh thefolder output.conv
echo $1
echo $2
rm $1/*.conv
rm $2
for f in $1/*.srt; do
  echo $f;
  ./cvgen.py "$f" "$f.conv"
done

rm dkg_lost.conv
for f in $1/*.conv; do
  echo $f;
  cat $f >> $2
done
