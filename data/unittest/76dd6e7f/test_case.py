from pathlib import Path

function = 'remove_user_files'
test_cases = [{'path_dir': Path('/tmp/test_remove_user_files_empty')}, {'path_dir': Path('/tmp/test_remove_user_files_owned')}, {'path_dir': Path('/tmp/test_remove_user_files_not_owned')}, {'path_dir': Path('/tmp/test_remove_user_files_mixed')}, {'path_dir': Path('/tmp/test_remove_user_files_subdirs')}, {'path_dir': Path('/tmp/test_remove_user_files_permission_error')}, {'path_dir': Path('/non_existent_directory')}]