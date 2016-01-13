# -*- coding: utf-8 -*-

import os, sys
from gluon.http import HTTP

def mkdir():
	try:
		path = "josoa/"
		os.mkdir(path, 0755 );
	except Exception, e:
		raise HTTP(500,e)