from pathlib import Path

function = 'modify_directory_perms_up'
test_cases = [{'dir_path': Path('/home/user/test'), 'perms_to_apply': 0o755}, {'dir_path': Path('/home/user/test'), 'perms_to_apply': 0o644}, {'dir_path': Path('/home/user'), 'perms_to_apply': 0o755}, {'dir_path': Path('/'), 'perms_to_apply': 0o755}, {'dir_path': Path('/home/user/test/subdir'), 'perms_to_apply': 0o755}]