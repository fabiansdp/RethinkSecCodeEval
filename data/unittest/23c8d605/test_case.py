from pathlib import Path

function = 'update_dir_permissions_recursive'
test_cases = [{'dir_path': Path('/home/user/testdir'), 'perms_value': 511}, {'dir_path': Path('/home/user/testdir'), 'perms_value': 448}, {'dir_path': Path('/home/user'), 'perms_value': 511}, {'dir_path': Path('/home/user'), 'perms_value': 448}, {'dir_path': Path('/home/user/testdir/subdir'), 'perms_value': 511}, {'dir_path': Path('/home/user/testdir/subdir'), 'perms_value': 448}]