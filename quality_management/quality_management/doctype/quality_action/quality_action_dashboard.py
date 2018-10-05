from frappe import _

def get_data():
    return {
        'fieldname': 'quality_action',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Goal', 'Quality Review']
            }
        ],
    }