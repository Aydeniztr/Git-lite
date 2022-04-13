#!/usr/bin/python3

from os import getcwd,mkdir
from sys import argv
from wget import download
from shutil import rmtree
from zipfile import ZipFile

about = '''

 author: Ahmet Yigit AYDENIZ | Aydeniztr
 
 py-git is a program for who uses a very slow computer to install a repo using git-cli 
 like ish users on ios and IPados or you have a poor connection or you want to save data
 via without surfing on github instead just installing just what you want from command line
 

 github:https://github.com/Aydeniztr
 Website:https://www.aydeniz.tk
 Chat:https://www.aydeniz.tk/chat.html
  
''' 

help = '''
argumants

usage:
python3 py-git.py <repo_link>

example:
python3 py-git.py https://github.com/Aydeniztr/Git-lite

for the help page:
python3 py-git.py --help

'''
cwd = getcwd()

def main(cwd):
	
	url = argv[1]
	
	mkdir(cwd + 'main')
	
	print('download started use ctrl-c to stop it ...')
	
	x = url + '/archive/refs/heads/main.zip'
	 
	filename = download(x,cwd + '/main')
	
	file = (filename)

# open the zip file in read mode
	with ZipFile(file, 'r') as zip: 

    # list all the contents of the zip file
		zip.printdir()
		print('extraction...')
		zip.extractall()
		print('Done!')
		
		rmtree(cwd + '/main')
	
if len(argv) <= 1:
	
	print(about + help)
	exit()
	
else:
	try:
		main()
	except:
		rmtree(cwd+'/main')

