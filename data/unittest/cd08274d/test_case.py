from pathlib import Path

function = 'clean_user_files'
test_cases = [{'root_dir': Path('/empty_directory')}, {'root_dir': Path('/directory_with_current_user_files')}, {'root_dir': Path('/directory_with_other_user_files')}, {'root_dir': Path('/directory_with_permission_error')}]