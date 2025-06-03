{
    'name': 'CRM Custom Program',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Customize CRM with program filtering',
    'depends': ['crm'],
    'data': [
        'data/crm_program_config_data.xml',   # dữ liệu mẫu
        'views/crm_lead_views.xml',           # view tùy chỉnh
    ],
    'installable': True,
    'application': False,
}
