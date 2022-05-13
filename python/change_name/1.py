#coding=UTF-8

import os

def file_name(file_dir):
    l=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            l.append(os.path.join(root,file))
    
    return l

if __name__ == '__main__':
    x=[]
    x=file_name('C:\Users\76585\Desktop\cfdname')
    print x

# for filename in os.listdir('C:\Users\76585\Desktop\cfdname'):
#     print filename
