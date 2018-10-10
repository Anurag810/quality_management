from frappe import _

def get_data():
    return {
        'fieldname': 'review',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Action']
            }
        ],
    }