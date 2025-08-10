from pathlib import Path

function = 'update_file_permissions'
test_cases = [{'path_to_file': Path('/path/to/file1'), 'permissions_val': 644}, {'path_to_file': Path('/path/to/file2'), 'permissions_val': 755}, {'path_to_file': Path('/path/to/file3'), 'permissions_val': 700}, {'path_to_file': Path('/path/to/file4'), 'permissions_val': 600}, {'path_to_file': Path('/path/to/file5'), 'permissions_val': 444}]