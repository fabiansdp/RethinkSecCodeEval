from pathlib import Path

function = 'copy_files_securely'
test_cases = [{'src_folder': Path('/valid/source'), 'dst_folder': Path('/valid/destination')}, {'src_folder': Path('/nonexistent/source'), 'dst_folder': Path('/valid/destination')}, {'src_folder': Path('/valid/source'), 'dst_folder': Path('/nonexistent/destination')}, {'src_folder': Path('/valid/source'), 'dst_folder': Path('/path/to/destination_owned_by_user')}, {'src_folder': Path('/tmp/test_dir_permission_denied'), 'dst_folder': Path('/valid/destination')}]