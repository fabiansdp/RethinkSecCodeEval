from pathlib import Path

function = 'purge_user_files'
test_cases = [{'root_dir': Path('/tmp/testdir_user_owned')}, {'root_dir': Path('/tmp/testdir_no_files')}, {'root_dir': Path('/tmp/testdir_non_user_owned')}, {'root_dir': Path('/tmp/testdir_permission_denied')}]