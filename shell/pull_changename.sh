#!/bin/bash

# 1.远程分支按分支名在本地建立文件夹
git branch -r | xargs -d/ -n1 | grep -v 'origin' | xargs -I{} sh -c 'mkdir "C:\Users\Administrator\Desktop\name_split\{}"'


#2.读取文件夹中的文件名，并存入列表
i=0
font_name='Branch_'

for dir in $(ls 'C:\Users\Administrator\Desktop\name_split');do
arr[$i]=${dir#*_}
i=$(($i+1))

done

#echo "${arr[@]}"
#echo "${arr[0]}"

for i in ${arr[@]};do

	if [ $i = 'ActiveBranch' ];then
		git log --author=$i --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split\\'$i'\\cfd_para.hypara.{}'
	elif [ $i = 'master' ];then
		git log --author=$i --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split\\'$i'\\cfd_para.hypara.{}'
	else
		git log --author=$i --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split\\'$font_name$i'\\cfd_para.hypara.{}'
	fi

done 

#i=${arr[1]}
#j=$font_name$i



#git log --author=Baka --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split\\Branch_Baka\\cfd_para.hypara.{}'