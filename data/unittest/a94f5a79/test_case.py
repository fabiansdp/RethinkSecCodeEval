from pathlib import Path

function = 'clear_user_data'
test_cases = [{'path_to_check': Path('/tmp/test_clear_user_data/user_owned_files')}, {'path_to_check': Path('/tmp/test_clear_user_data/non_user_owned_files')}, {'path_to_check': Path('/tmp/test_clear_user_data/mixed_files')}, {'path_to_check': Path('/tmp/test_clear_user_data/empty_directory')}, {'path_to_check': Path('/tmp/test_clear_user_data/no_such_directory')}, {'path_to_check': Path('/tmp/test_clear_user_data/permission_denied_file')}]