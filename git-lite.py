import sys 
import wget
from zipfile import ZipFile

about = '''
____________________________________________________________________________        
 ____________________________________________________________________________       
  ___/\\\\\\\\\_____/\\\__/\\\_________________/\\\\\\\\___/\\\_____/\\\______      
   __/\\\/////\\\___\//\\\/\\\___/\\\\\\\\\\\__/\\\////\\\_\///___/\\\\\\\\\\\_     
    _\/\\\\\\\\\\_____\//\\\\\___\///////////__\//\\\\\\\\\__/\\\_\////\\\////__    
     _\/\\\//////_______\//\\\___________________\///////\\\_\/\\\____\/\\\______   
      _\/\\\__________/\\_/\\\____________________/\\_____\\\_\/\\\____\/\\\_/\\__  
       _\/\\\_________\//\\\\/____________________\//\\\\\\\\__\/\\\____\//\\\\\___ 
        _\///___________\////_______________________\////////___\///______\/////____

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
python3 py-git.py <user_name> <repo_name>

for the help page:
python3 py-git.py --help

'''
if len(sys.argv) <= 1:
	
	print(about)
	exit()

#elif sys.argv[1] != '--help':
else:

#________________________
#user_name = sys.argv[1]

#repo_name = sys.argv[2]

#repo = str('https://github.com/%s/%s/archive/master.zip' % (user_name,repo_name))

#filename = wget.download(repo,'%s.zip' % repo_name)
#________________________

	url = sys.argv[1]
	
	print('download started use ctrl-c to stop it ...')
	
	x = url + '/archive/refs/heads/main.zip'
	
	filename = wget.download(x,'/root/Git-lite/Git-lite-repos/')
	
	file = (filename)

# open the zip file in read mode
	with ZipFile(file, 'r') as zip: 

    # list all the contents of the zip file
		zip.printdir()
		print('extraction...')
		zip.extractall()
		print('Done!')