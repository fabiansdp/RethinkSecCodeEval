from pathlib import Path

function = 'set_file_permissions'
test_cases = [{'file_path': Path('/path/to/file1'), 'file_permissions': 644}, {'file_path': Path('/path/to/file2'), 'file_permissions': 755}, {'file_path': Path('/path/to/file3'), 'file_permissions': 700}, {'file_path': Path('/path/to/file4'), 'file_permissions': 600}]