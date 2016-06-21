#把 rawbase 里面的逐个，弄到 tmpp 里面，在里面 把 srt 处理出来，放到 desret
#TODO 每个字幕 rar 中，只选其中一个srt，而不是全部。
#加 progress 提示[a/N]

rm -rf desret/*

cnt=0
for f in rawbase/*; do

    echo $f
    unrar e -o+ -p-  $f tmpp/


    #turn ass to srt

    cd tmpp
    asstosrt -s utf-8


    #copy all srt out
    flg=true

    for p in *.srt; do
        if [[ "$p" =~ (.*GB.*)|(.*[Cc][Hh][s].*)|(.*[Cc][Nn].*)  ]] ; then :

            $flg=false
            uuid=$(uuidgen)
            echo $p
            mv "$p" "../desret/$p.$uuid.srt"   #必须加“”，因为名称里面可能有空格 加上原名 是为了有更多信息，比如中英文
            echo $cnt
            cnt=$[ cnt + 1 ]
        fi

    done


    # if [ $flg ]; then:
    #     for p in *.srt; do

    #     ret=$[ chardetect "$p" ];

    #     if [[ "$ret" =~ (.*GB2312.*)  ]] ; then:

    #         uuid=$(uuidgen)
    #         echo $p
    #         mv "$p" "../desret/$p.$uuid.srt"   #必须加“”，因为名称里面可能有空格 加上原名 是为了有更多信息，比如中英文
    #         break;
    #     fi
    
    #     done
    # fi

    cd ..

    rm -f tmpp/*

done
