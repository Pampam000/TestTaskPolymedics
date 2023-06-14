student_create_example = {
    'correct': {
        'value': {
            'name': 'Bob',
            'birthdate': '2003-10-10',
            'group_id': 1
        }
    },
    'invalid': {
        'value': {
            'name': 'Insanely long title which length is more then 50 '
                    'symbols',
            'birthdate': '2013-10-10',
            'group_id': -1
        }
    }
}

student_update_example = {
    'update any single filed': {
        'value': {
            'name': 'Bob'
        }
    },
    'update any several fields': {
        'value': {
            'name': 'Bob',
            'birthdate': '2003-10-10'
        }
    },
    'update all fields': {
        'value': {
            'name': 'Bob',
            'birthdate': '2003-10-10',
            'group_id': 1,
            'is_graduated': True,
            'is_expelled': False
        }
    },
    'invalid': {
        'value': {
            'name': 'Insanely long title which length is more then 50 '
                    'symbols',
            'birthdate': '2013-10-10',
            'group_id': -1
        }
    }
}
