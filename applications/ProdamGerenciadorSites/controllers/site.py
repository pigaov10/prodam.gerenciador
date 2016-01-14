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
	return dict(p='asdsad')

def create():
	if request.post_vars.site:
		post = request.post_vars.site
		from skeleton import Skeleton
		s = Skeleton(post)

	return dict()

def count():
    # session.counter = (session.counter or 0) + 1
    user = db(db.auth_user).select()
    return dict(counter=user)

def teste():
	return dict()