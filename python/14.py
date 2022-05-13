#coding=UTF-8

# 从绝对路径提取某个数字

import os,re

s='C:/Users/76585/Desktop/shell/cfdname2/cfd_para_383.txt'

new_line=re.split(r'[/]',str(s))
new_line=new_line[-1]
# re.sub是 替换函数，将非数字替换为空格
end=re.sub('\D','',new_line)

# print type(new_line)
print end