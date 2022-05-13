#!/bin/bash



function func(){
cat cfd.log | while read line
do

    OLD_IFS="$IFS"
    IFS=" "
    array=($line)
    IFS="$OLD_IFS"
    # len=${#array[@]}
    # echo $len
    # if [ "${#array[@]}" -gt "3" ] && [ "${#array[0]}" = "cfdversion" ] ; then
    #    echo "len is 3"
    #    break
    # fi
    if [ "${array[0]}" = "cfdversion" ] ; then
    #    echo "len is 3"
       echo ${array[2]}
        # tmp=${array[2]}
        # num=`echo ${array[2]}`
        # $num=12
       break
    fi

done
}

res=$(func)

echo $res

