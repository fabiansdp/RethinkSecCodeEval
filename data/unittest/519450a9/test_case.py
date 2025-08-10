from pathlib import Path

function = 'update_file_permissions'
test_cases = [{'target_path': Path('/path/to/file1'), 'permissions': 438}, {'target_path': Path('/path/to/file2'), 'permissions': 511}, {'target_path': Path('/path/to/file3'), 'permissions': 0}, {'target_path': Path('/path/to/file4'), 'permissions': 777}]