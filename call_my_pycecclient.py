#! /usr/bin/python3
from my_pycecclient import *
#import sys
def tv_tog(num):
    lib =  pyCecClass()
    lib.InitLibCec(num)
    return
#tv_tog(3)

# tv_tog(1) = hdmi 1
# 2 =hdmi 2 
# 3= hdmi 3
# 4 = power toggle
#
#modules = dir()
#
#print(modules)
