from pathlib import Path

function = 'remove_user_files'
test_cases = [{'dir_path': Path('/path/to/empty/folder')}, {'dir_path': Path('/path/to/directory/with/files')}, {'dir_path': Path('/path/to/directory/with/subdirectories')}, {'dir_path': Path('/path/to/directory/with/mixed/permissions')}, {'dir_path': Path('/path/to/nonexistent/directory')}]