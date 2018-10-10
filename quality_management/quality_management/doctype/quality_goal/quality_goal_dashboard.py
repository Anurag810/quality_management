from frappe import _

def get_data():
    return {
        'fieldname': 'goal',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Review', 'Quality Action']
            }
        ],
    }