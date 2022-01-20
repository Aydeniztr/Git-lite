#!/usr/bin/python3

from os import remove,
import sys 
import wget
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
if len(sys.argv) <= 1:
	
	print(about + help)
	exit()

#elif sys.argv[1] != '--hel
else:

#________________________
#user_name = sys.argv[1]

#repo_name = sys.argv[2]

#repo = str('https://github.com/%s/%s/archive/master.zip' % (user_name,repo_name))

#filename = wget.download(repo,'%s.zip' % repo_name)
#________________________

	url = sys.argv[1]
	
	cwd = os.getcwd()
	
	print('download started use ctrl-c to stop it ...')
	
	x = url + '/archive/refs/heads/main.zip'
	 
	filename = wget.download(x,cwd)
	
	file = (filename)

# open the zip file in read mode
	with ZipFile(file, 'r') as zip: 

    # list all the contents of the zip file
		zip.printdir()
		print('extraction...')
		zip.extractall()
		print('Done!')
		
		os.remove(cwd + 'main.zip')
