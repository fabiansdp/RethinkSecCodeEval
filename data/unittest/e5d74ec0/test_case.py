from pathlib import Path

function = 'update_directory_permissions'
test_cases = [{'target_dir': Path('/home/user/testdir'), 'desired_permissions': 511}, {'target_dir': Path('/home/user/testdir'), 'desired_permissions': 448}, {'target_dir': Path('/home/user'), 'desired_permissions': 511}, {'target_dir': Path('/home/user'), 'desired_permissions': 448}, {'target_dir': Path('/home/user/testdir/subdir'), 'desired_permissions': 511}, {'target_dir': Path('/home/user/testdir/subdir'), 'desired_permissions': 448}]