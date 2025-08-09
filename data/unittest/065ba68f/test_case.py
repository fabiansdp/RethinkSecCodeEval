from pathlib import Path

function = 'safe_copy_files'
test_cases = [{'src_directory': Path('/path/to/source'), 'dest_directory': Path('/path/to/destination_owned_by_user')}, {'src_directory': Path('/path/to/source_with_no_files'), 'dest_directory': Path('/path/to/destination_owned_by_user')}, {'src_directory': Path('/path/to/source_with_permission_error'), 'dest_directory': Path('/path/to/destination_owned_by_user')}, {'src_directory': Path('/path/to/source'), 'dest_directory': Path('/path/to/destination_not_owned_by_user')}]