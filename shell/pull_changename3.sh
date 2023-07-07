#!/bin/bash

#git log --follow --pretty=format:%H cfd_para.hypara | xargs -I{} sh -c 'git show {}:./cfd_para.hypara > C:\\Users\\Administrator\\Desktop\\name_split3\\cfd_para.hypara.{}'

git log --follow --pretty=format:%H cfd_para.hypara >> 'C:\\Users\\Administrator\\Desktop\\name_split3\\hash.txt'