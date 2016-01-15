# -*- coding: utf-8 -*-

###################################################################
# this class creates a skeleton plone  

# Author: Raphael Iarussi jan/16
###################################################################

from helpers import mkdir
from helpers import xml_ident
from xml.etree.ElementTree import ParseError
from gluon.http import HTTP
import xml.etree.cElementTree as tree_element_first

class Skeleton:
    """Skeleton site class"""

    def __init__(self,request):
    	self._post = "prodam.gerenciador."
    	self.request = request
    	self.create_request_project()

	# ##########################################################
	# ## auxiliary functions
	# ###########################################################

    def create_request_project(self):
		'''
		This is a docstring. The following 3 lines are a doctest:
		>>> request.vars.name='Max'
		>>> index()
		{'name': 'Max'}
		'''
		xpaths = ['sites','/viewlets','/browser','/src','/templates']

		mkdir(str(self._post) + str(self.request))
		path = str(self._post) + str(self.request)
		path  += xpaths[3]
		mkdir(path) # directory src

		#split do nome do site separado por .
		directories = (str(self._post) + str(self.request)).split(".")
		for directory in directories:
			path += "/"+directory
			mkdir(path);

		# profiles
		profiles = path
		mkdir(profiles+"/profiles");
		mkdir(profiles+"/profiles/default/");
		self.add_profile_file(path)
		#browser
		path += xpaths[2]
		mkdir(path);
		
		# viewlets
		path += xpaths[1]
		mkdir(path);
		
		# zcml file
		self.add_configure_file(path,str(self._post) + str(self.request))
		
		# python file configure
		self.add_viewlets_file(path)
		
		# templates
		path += xpaths[4]
		mkdir(path);
		# pt file 
		self.add_template_file(path)

	# ##########################################################
	# ## auxiliary functions
	# ###########################################################

    def add_configure_file(self,path,project_name,param1='IPortalHeader',param2='IProdamPortal',param3='prodam.gerenciador.cet'):
		'''
		This is a docstring. The following 3 lines are a doctest:
		>>> request.vars.name='Max'
		>>> index()
		{'name': 'Max'}
		'''
		try:
			#seta nó para configuração dos namespaces
			configure = tree_element_first.Element('configure')
			configure.set('xmlns','http://namespaces.zope.org/zope')
			configure.set('xmlns:browser','http://namespaces.zope.org/browser')
			configure.set('i18n_domain','prodam.portal')

			#seta nó para configuração das Viewlets do Plone
			browser = tree_element_first.SubElement(configure,"browser:viewlet")
			browser.set("name",param3)
			browser.set("manager","plone.app.layout.viewlets.interfaces."+param1)
			browser.set("class",".logo.LogoViewlet")
			browser.set("permission","zope2.View")
			browser.set("layer",project_name+".interfaces."+param2)

			tree = tree_element_first.ElementTree(configure)
			configure_name = "/configure.zcml"
			xml_ident(configure)
			tree.write('sites/'+path+configure_name,encoding="utf-8")
		except ParseError, e:
			raise HTTP(500,e)

	# ##########################################################
	# ## auxiliary functions
	# ###########################################################

    def add_template_file(self,path):
		'''
		This is a docstring. The following 3 lines are a doctest:
		>>> request.vars.name='Max'
		>>> index()
		{'name': 'Max'}
		'''
		try:
			handle = open('sites/'+path+"/alerta.pt","a+")
		except IOError, e:
			raise HTTP(500,e) 
		else:
			with handle:
				handle.close()
		# text = open('sites/components/alerta.pt','r').read()
		# file.write(text)

	# ##########################################################
	# ## auxiliary functions
	# ###########################################################

    def add_profile_file(self,path):
		'''
		This is a docstring. The following 3 lines are a doctest:
		>>> request.vars.name='Max'
		>>> index()
		{'name': 'Max'}
		'''
		#seta nó para configuração dos namespaces
		xml_object = tree_element_first.Element('object')

		tree = tree_element_first.ElementTree(xml_object)
		configure_name = "/profiles/default/viewlets.xml"
		xml_ident(xml_object)
		tree.write('sites/'+path+configure_name,encoding="utf-8")

	# ##########################################################
	# ## auxiliary functions
	# ###########################################################

    def add_viewlets_file(self,path):
		'''
		This is a docstring. The following 3 lines are a doctest:
		>>> request.vars.name='Max'
		>>> index()
		{'name': 'Max'}
		'''
		try:
			handle = open('sites/'+path+"/viewlets.py","a+")
		except IOError, e:
			raise HTTP(500,e) 
		else:
			with handle:
				handle.close()
