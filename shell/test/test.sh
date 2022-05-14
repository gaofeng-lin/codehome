#!/bin/bash

function func(){
cat cfd.log | while read line
do

    OLD_IFS="$IFS"
    IFS=" "
    array=($line)
    IFS="$OLD_IFS"
    if [ "${array[0]}" = "cfdversion" ] ; then
       echo ${array[2]}
       break
    fi

done
}

res=$(func)

echo $res

