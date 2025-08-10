from pathlib import Path

function = 'adjust_file_permissions'
test_cases = [{'target_path': Path('/path/to/file1'), 'new_permissions': 644}, {'target_path': Path('/path/to/file2'), 'new_permissions': 755}, {'target_path': Path('/path/to/file3'), 'new_permissions': 700}, {'target_path': Path('/path/to/file4'), 'new_permissions': 600}]