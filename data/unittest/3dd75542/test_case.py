from pathlib import Path

function = 'alter_directory_permissions_recursively'
test_cases = [{'start_dir': Path('/path/to/directory'), 'permissions': 511}, {'start_dir': Path('/path/to/directory'), 'permissions': 448}, {'start_dir': Path('/path/to/directory'), 'permissions': 504}, {'start_dir': Path('/path/to/directory'), 'permissions': 496}, {'start_dir': Path('/path/to/directory'), 'permissions': 488}]