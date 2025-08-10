from pathlib import Path

function = 'modify_file_permissions'
test_cases = [{'target_path': Path('/path/to/file1'), 'perm_value': 644}, {'target_path': Path('/path/to/file2'), 'perm_value': 755}, {'target_path': Path('/path/to/file3'), 'perm_value': 700}, {'target_path': Path('/path/to/file4'), 'perm_value': 600}, {'target_path': Path('/path/to/file5'), 'perm_value': 444}]