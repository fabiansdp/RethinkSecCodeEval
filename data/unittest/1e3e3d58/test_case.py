from pathlib import Path

function = 'modify_dir_perms'
test_cases = [{'specified_dir': Path('/home/user/testdir'), 'octal_permissions': 493}, {'specified_dir': Path('/home/user/testdir'), 'octal_permissions': 511}, {'specified_dir': Path('/home/user'), 'octal_permissions': 493}, {'specified_dir': Path('/home/user'), 'octal_permissions': 448}]