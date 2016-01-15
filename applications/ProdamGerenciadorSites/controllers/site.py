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
	return dict(p='Templates')

@auth.requires_membership('admin')
def create():
	if request.post_vars.site:
		post = request.post_vars.site
		from skeleton import Skeleton
		s = Skeleton(post)

	return dict()

def count():
    components = db(db.tbl_components).select()
    return dict(components=components)

def teste():
	return dict()