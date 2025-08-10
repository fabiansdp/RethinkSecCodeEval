from pathlib import Path

function = 'update_permissions_for_dirs'
test_cases = [{'path_dir': Path('/home/user/testdir'), 'new_perms': 511}, {'path_dir': Path('/home/user/testdir'), 'new_perms': 448}, {'path_dir': Path('/home/user'), 'new_perms': 511}, {'path_dir': Path('/home/user'), 'new_perms': 448}, {'path_dir': Path('/home/user/testdir/subdir'), 'new_perms': 511}, {'path_dir': Path('/home/user/testdir/subdir'), 'new_perms': 448}]