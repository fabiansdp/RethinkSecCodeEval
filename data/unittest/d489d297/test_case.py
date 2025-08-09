from pathlib import Path

function = 'copy_files_securely'
test_cases = [{'src_folder': Path('/valid/source'), 'dst_folder': Path('/valid/destination')}, {'src_folder': Path('/nonexistent/source'), 'dst_folder': Path('/valid/destination')}, {'src_folder': Path('/valid/source'), 'dst_folder': Path('/nonexistent/destination')}, {'src_folder': Path('/valid/source'), 'dst_folder': Path('/different_user_owned/destination')}, {'src_folder': Path('/permission_denied/source'), 'dst_folder': Path('/valid/destination')}]