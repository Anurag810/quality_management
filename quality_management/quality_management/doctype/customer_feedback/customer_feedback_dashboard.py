from frappe import _

def get_data():
    return {
        'fieldname': 'customer_feedback',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Action', 'Quality Review']
            }
        ],
    }