from pathlib import Path

function = 'remove_user_files'
test_cases = [{'folder': Path('/nonexistent_folder')}, {'folder': Path('/tmp/test_folder_with_files')}, {'folder': Path('/tmp/test_folder_with_no_files')}, {'folder': Path('/tmp/test_folder_with_symlink_to_file')}, {'folder': Path('/tmp/test_folder_with_permission_denied_file')}]