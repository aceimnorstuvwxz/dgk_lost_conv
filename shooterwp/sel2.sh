#把 rawbase 里面的逐个，弄到 tmpp 里面，在里面 把 srt 处理出来，放到 desret
#TODO 每个字幕 rar 中，只选其中一个srt，而不是全部。
#加 progress 提示[a/N]


a="sdfsdgdfgdf.GB.chs.sfdsgdg"
echo $a

if [[ "$a" =~ (.*GBA.*)|(.*chs.*)  ]] || false; then :
    echo $a

fi
