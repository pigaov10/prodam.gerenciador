response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Criar site'),URL('site','templates_plone')==URL(),URL('site','templates_plone'),[]),
(T('Plone Componentes'),URL('default','tbl_components_manage')==URL(),URL('default','tbl_components_manage'),[]),
]
