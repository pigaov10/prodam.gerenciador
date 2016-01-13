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

db.define_table('t_tbl_components_archive',db.t_tbl_components,Field('current_record','reference t_tbl_components',readable=False,writable=False))
