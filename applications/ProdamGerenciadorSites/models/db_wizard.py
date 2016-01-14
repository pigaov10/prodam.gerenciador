### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_tbl_components',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_uk', type='string',
          label=T('Uk')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('tbl_components',
    Field('name',type='string',label='Nome do componente',required=True),
    Field('uk',type='integer',label='Componente único?'),
    Field('icon',type='string',label='Ícone'),
    Field('tipo',type='string',label='Tipo do componente'),
    Field('manager',type='string',label='Local na estrutura'),
    auth.signature
)

db.define_table('t_tbl_components_archive',db.t_tbl_components,Field('current_record','reference t_tbl_components',readable=False,writable=False))
