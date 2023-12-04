{
    'name': "Logic Custody",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base','mail','logic_base'],
    'data': [
        'security/users.xml',
        'security/ir.model.access.csv',
        # 'security/record_rules.xml',
        'views/custody.xml',
        'views/properties.xml',
        'views/assets.xml',
        'views/total_assets.xml',
        'views/custody_type.xml',
        # 'data/task_types.xml',

    ],
    'demo': [],
    'summary': "Logic Custody",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}