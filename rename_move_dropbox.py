#!/usr/bin/env python
# coding: utf-8

import os, sys, re, shutil

path = '/Users/sonic883b/Dropbox/'
pic_dir = path+'pictures'

jpg = re.compile(".[j|J][p|P][g|G]-*")
ext_jpg = 'jpg'
png = re.compile(".png-*")
ext_png = 'png'


filelist = os.listdir(path)
if not os.path.exists(pic_dir):
	os.mkdir(pic_dir)

for file in filelist:
	if jpg.search(file):
		name, ext = os.path.splitext(file)
		rename = path+name+'.'+ext_jpg
		os.rename(path+file, rename)	
		shutil.move(rename, pic_dir)	
	if png.search(file):
		name, ext = os.path.splitext(file)
		rename = path+name+'.'+ext_png
		os.rename(path+file, rename)	
		shutil.move(rename, pic_dir)	
