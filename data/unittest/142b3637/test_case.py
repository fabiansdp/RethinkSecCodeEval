from pathlib import Path

function = 'remove_old_entries'
test_cases = [{'folder': Path('/empty_directory'), 'age_limit': 1}, {'folder': Path('/old_files_directory'), 'age_limit': 1}, {'folder': Path('/new_files_directory'), 'age_limit': 365}, {'folder': Path('/different_user_files_directory'), 'age_limit': 1}, {'folder': Path('/permission_error_directory'), 'age_limit': 1}]