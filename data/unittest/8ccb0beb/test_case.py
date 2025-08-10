from pathlib import Path

function = 'erase_user_files'
test_cases = [{'dir_path': Path('/path/to/empty/folder')}, {'dir_path': Path('/path/to/directory/with/files')}, {'dir_path': Path('/path/to/directory/with/subdirectories')}, {'dir_path': Path('/path/to/directory/with/files/not_owned_by_user')}, {'dir_path': Path('/path/to/directory/with/files/with_permission_error')}]