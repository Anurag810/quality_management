from frappe import _

def get_data():
    return {
        'fieldname': 'audit',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Action', 'Quality Review']
            }
        ],
    }