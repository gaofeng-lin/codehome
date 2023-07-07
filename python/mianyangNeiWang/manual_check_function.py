#coding=UTF-8

# 相同变量


import xml.dom.minidom
import re
import os
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

def manual_check(new_version_num,old_version_unique,new_version_unique):
    
    tree=ET.parse('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')
    root=tree.getroot()


    for i in old_version_unique:
        for j in new_version_unique:

            index_old=old_version_unique.index(i)
            index_new=new_version_unique.index(j)
            if i!=0 and j!=0 and index_old==index_new :
                if old_version_unique[index_old-1]==0 and old_version_unique[index_old+1]==0 and new_version_unique[index_new+1]==0 and new_version_unique[index_new-1]==0:

                    tag1_name=tree.find(i)
                    newnode=ET.Element('version')
                    # version=ET.Element('version')
                    newnode.attrib={'v':new_version_num}
                    newnode.text=j

                    tag1_name.append(newnode)

                    # newnode.append(version)
                    # root.append(newnode)
                    tree.write('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')
                    break

if __name__ == '__main__':
    new_version_num=12
    old_version_unique=[0,0,'nStatisticalStep',0]
    new_version_unique=[0,0,'startStatisticStep',0]
    manual_check(new_version_num,old_version_unique,new_version_unique)

