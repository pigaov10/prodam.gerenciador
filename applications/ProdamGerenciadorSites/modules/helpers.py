# -*- coding: utf-8 -*-

###################################################################
# helpers  

# Author: Raphael Iarussi jan/16
###################################################################

import os, sys
from gluon.http import HTTP

def mkdir(xpath,root='sites/'):
	try:
		os.makedirs(root+str(xpath),0775)
	except Exception, e:
		raise HTTP(500,e)

def xml_ident(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            xml_ident(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i