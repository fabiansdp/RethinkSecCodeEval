from pathlib import Path

function = 'purge_user_files'
test_cases = [{'target_directory': Path('/path/to/empty/folder')}, {'target_directory': Path('/path/to/non/user/files')}, {'target_directory': Path('/path/to/user/files')}, {'target_directory': Path('/path/to/subdirectories/with/user/files')}, {'target_directory': Path('/path/to/permission/denied/files')}]