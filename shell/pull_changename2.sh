#!/bin/bash

# 1.远程分支按分支名字在本地建立文件夹。name_split用来存放带哈希值的cfd_para文件，name_split2存放带版本号的cfd_para文件
git branch -r | xargs -d/ -n1 | grep -v 'origin' | xargs -I{} sh -c 'mkdir "F:\lgf\name_split\{}"'
git branch -r | xargs -d/ -n1 | grep -v 'origin' | xargs -I{} sh -c 'mkdir "F:\lgf\name_split2\{}"'


#2.读取文件夹中的文件名，并存入列表
i=0
font_name='Branch_'

for dir in $(ls 'F:\lgf\name_split');do
arr[$i]=${dir#*_}
i=$(($i+1))

done

#echo "${arr[@]}"
#echo "${arr[0]}"

for i in ${arr[@]};do
	git log --author=$i --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > F:\\lgf\\name_split\\'$font_name$i'\\cfd_para.hypara.{}'
	
done


# 3.找到主干分支，把里面带有into 'ActiveBranch'字段提交记录的哈希值提取出来，然后文件的命名变为cfd_para.hypara.哈希值
git log --grep="into 'ActiveBranch'" --pretty=format:%H | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > F:\\lgf\\name_split\\ActiveBranch\\cfd_para.hypara.{}'

#i=${arr[1]}
#j=$font_name$i



#git log --first-parent remotes/origin/Branch_helei --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split\\Branch_helei\\cfd_para.hypara.{}'