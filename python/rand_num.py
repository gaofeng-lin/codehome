#coding=UTF-8
import os
import re
import json
import shutil
import random

for i in range(0,7):

    # 输入取值范围，比如100~350
    value = (random.uniform(0.02, 0.09))

    # 确定随机小数点位数，比如.3f，表示小数点为3位小数
    value = format(value, '.3f')

    print(value)     #将这个随机数打印出来，或者和其他的组成字符串来执行sql语句的操作





