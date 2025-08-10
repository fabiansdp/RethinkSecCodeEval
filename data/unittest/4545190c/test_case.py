from pathlib import Path

function = 'clean_user_files'
test_cases = [{'dir_path': Path('/tmp/test_dir_with_user_files')}, {'dir_path': Path('/tmp/test_dir_with_non_user_files')}, {'dir_path': Path('/tmp/test_dir_with_permission_error')}, {'dir_path': Path('/tmp/empty_test_dir')}]