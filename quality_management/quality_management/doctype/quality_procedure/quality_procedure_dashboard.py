from frappe import _

def get_data():
    return {
        'fieldname': 'procedure',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Goal', 'Quality Audit', 'Quality Review', 'Quality Action']
            }
        ],
    }