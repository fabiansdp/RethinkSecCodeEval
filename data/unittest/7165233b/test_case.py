from pathlib import Path

function = 'change_directory_permissions_up'
test_cases = [{'directory': Path('/home/user/testdir'), 'folder_permissions': 511}, {'directory': Path('/home/user/testdir'), 'folder_permissions': 448}, {'directory': Path('/home/user'), 'folder_permissions': 511}, {'directory': Path('/'), 'folder_permissions': 511}]