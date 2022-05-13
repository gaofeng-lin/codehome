#coding=UTF-8

# 测试

import difflib


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


print string_similar('csrvist','visual_section')