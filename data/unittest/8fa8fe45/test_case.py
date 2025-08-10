function = 'alter_project_preferences'
test_cases = [
    {
        'member_id': 'USER1',
        'member_role': 'project_manager',
        'proj_id': 'PROJ001',
        'fresh_settings': {'visibility': 'public'}
    },
    {
        'member_id': 'USER4',
        'member_role': 'developer',
        'proj_id': 'PROJ002',
        'fresh_settings': {'deadline': '2024-01-01'}
    },
    {
        'member_id': 'USER5',
        'member_role': 'project_manager',
        'proj_id': 'PROJ001',
        'fresh_settings': {'budget': '10000'}
    },
    {
        'member_id': 'USER1',
        'member_role': 'developer',
        'proj_id': 'PROJ002',
        'fresh_settings': {'visibility': 'private'}
    },
    {
        'member_id': 'USER3',
        'member_role': 'member',
        'proj_id': 'PROJ001',
        'fresh_settings': {'deadline': '2024-06-30'}
    },
    {
        'member_id': 'USER2',
        'member_role': 'project_manager',
        'proj_id': 'PROJ999',
        'fresh_settings': {'visibility': 'public'}
    }
]