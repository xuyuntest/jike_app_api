#coding=utf-8
__author__ = 'yun'

import os,sys;

html = open('index.html', 'w')
html.write("""
<html>
<head>
  <title>Test</title>
  <style>img{float:left;margin:5px;}</style>
</head>
<body>
""")

files = os.listdir('.')

# 首先处理文本
for f in files:
    if f.lower().endswith('.log'):
        fp = open(f)
        for a in fp.readlines():
            html.write("<p>%s</p>" % a)
        fp.close()




# 然后处理图片
'''
for f in files:
    if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
        html.write("<img src='%s' />" % f)
        '''

html.write('</body></html>')
html.close()
