from pathlib import Path

function = 'change_file_permissions'
test_cases = [{'file_location': Path('/path/to/file1'), 'new_perms': 644}, {'file_location': Path('/path/to/file2'), 'new_perms': 755}, {'file_location': Path('/path/to/file3'), 'new_perms': 700}, {'file_location': Path('/path/to/file4'), 'new_perms': 600}, {'file_location': Path('/path/to/file5'), 'new_perms': 444}]