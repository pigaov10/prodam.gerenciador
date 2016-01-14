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

    def create_request_project(self):
		"""
		MÉTODO RESPONSÁVEL POR GERAR A ESTRUTURA DE DIRETORIOS 
		"""
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

		#browser
		path += xpaths[2]
		mkdir(path);
		
		# viewlets
		path += xpaths[1]
		mkdir(path);
		print path
		# zcml file
		self.add_configure_file(path,str(self._post) + str(self.request))

		# templates
		path += xpaths[4]
		mkdir(path);

    def add_configure_file(self,path,project_name,param1='IPortalHeader',param2='IProdamPortal'):
		"""
		MÉTODO RESPONSÁVEL POR GERAR O ARQUIVO ZCML 
		"""
		try:
			#seta nó para configuração dos namespaces
			configure = tree_element_first.Element('configure')
			configure.set('xmlns','http://namespaces.zope.org/zope')
			configure.set('xmlns:browser','http://namespaces.zope.org/browser')
			configure.set('i18n_domain','prodam.portal')

			#seta nó para configuração das Viewlets do Plone
			browser = tree_element_first.SubElement(configure,"browser:viewlet")
			browser.set("name","plone.logo")
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
