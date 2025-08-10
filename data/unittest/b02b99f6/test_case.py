from pathlib import Path

function = 'change_file_permissions'
test_cases = [{'file_loc': Path('/path/to/file1'), 'perm_mode': 644}, {'file_loc': Path('/path/to/file2'), 'perm_mode': 755}, {'file_loc': Path('/path/to/file3'), 'perm_mode': 777}, {'file_loc': Path('/path/to/file4'), 'perm_mode': 444}, {'file_loc': Path('/path/to/file5'), 'perm_mode': 0}]