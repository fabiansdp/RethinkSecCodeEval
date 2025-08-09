from pathlib import Path

function = 'delete_user_files'
test_cases = [{'directory': Path('/empty_directory')}, {'directory': Path('/files_owned_by_user')}, {'directory': Path('/files_not_owned_by_user')}, {'directory': Path('/directory_with_subdirectories')}, {'directory': Path('/permission_denied_directory')}]