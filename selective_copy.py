import os
import shutil, os, re

folder = input('Folder path: ')
extension = input('Extension must start with dot! :')

def selectiveCopy(folder, extension):
    folder = os.path.abspath(folder)
    newfolder = 'copies of ' + extension[1:] + ' files by Python'
    os.makedirs(newfolder)
    newfolder = os.path.abspath(newfolder)
    print('Copying all files with the extension %s in to \'%s\'...' % (extension, newfolder))

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('_copy' + extension):
                continue
            if filename.endswith(extension):
                regex = re.compile(r'(.*)(%s$)' % extension)
                mo = regex.search(filename)
                currentFile = foldername + '/' + filename
                newfileName = newfolder + '/' + mo.group(1) + '_copy' + extension
                shutil.copy(currentFile, newfileName)

selectiveCopy(folder, extension)

result=input("\nDo you want to restart the program? [y/n] > ")
if result=='y':
     os.system('python "selective_copy.py"')
else:
     print("\nThe program will be closed...")