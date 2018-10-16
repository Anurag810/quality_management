from frappe import _

def get_data():
    return {
        'fieldname': 'frequency',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Goal']
            }
        ],
    }