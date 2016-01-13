# -*- coding: utf-8 -*-

###################################################################
# this class creates a skeleton plone  

# Author: Raphael Iarussi jan/16
###################################################################

from helpers import mkdir

class Plone:
    """Skeleton site class"""
    folders = ['sites','/viewlets','/browser','/src','/templates']

    def create(self):
    	mkdir()
        return 'a'