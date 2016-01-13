# -*- coding: utf-8 -*-

################################################
# Controller
# @author: Raphael louria iarussi
# @since jan/2016
# @version 1.0
################################################

def templates_plone():
	'''
	seleciona template plone
	'''

	from plone import Plone
	p = Plone()
	p.create()
	return dict(p='asdsad')