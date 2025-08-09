from pathlib import Path

function = 'copy_files_safely'
test_cases = [{'source_folder': Path('/path/to/source'), 'destination_folder': Path('/path/to/destination_owned_by_user')}, {'source_folder': Path('/path/to/nonexistent/source'), 'destination_folder': Path('/path/to/destination_owned_by_user')}, {'source_folder': Path('/path/to/source'), 'destination_folder': Path('/path/to/destination_not_owned_by_user')}, {'source_folder': Path('/path/to/source'), 'destination_folder': Path('/path/to/source_with_permission_error')}]