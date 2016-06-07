for f in all/*.srt; do
  echo $f;
  ./cvgen.py "$f" "$f.conv"
done

rm dkg_lost.conv
for f in all/*.conv; do
  echo $f;
  cat $f >> dkg_lost.conv
done
