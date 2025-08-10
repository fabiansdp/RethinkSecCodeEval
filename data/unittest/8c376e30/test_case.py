from pathlib import Path

function = 'modify_file_permissions'
test_cases = [{'file_location': Path('/path/to/file1'), 'updated_permissions': 644}, {'file_location': Path('/path/to/file2'), 'updated_permissions': 755}, {'file_location': Path('/path/to/file3'), 'updated_permissions': 700}, {'file_location': Path('/path/to/file4'), 'updated_permissions': 600}]