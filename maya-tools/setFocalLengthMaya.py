from pymel.core import *
import sys, os

maya_file = sys.argv[1]
focal = sys.argv[2]
print maya_file
print focal

openFile(maya_file, force=True)
command = 'setAttr "camProperties.focalLength" %s'%(focal)
print command
Mel.eval(command)
saveFile(force=True)
os._exit(0)