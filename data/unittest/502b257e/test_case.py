from pathlib import Path

function = 'adjust_directory_rights'
test_cases = [{'folder': Path('/path/to/destination_owned_by_user'), 'permissions': '0o755'}, {'folder': Path('/path/to/destination_owned_by_user'), 'permissions': '0o777'}, {'folder': Path('/path/to/destination_not_owned_by_user'), 'permissions': '0o755'}, {'folder': Path('/path/to/destination_owned_by_user-with-wrong-perms'), 'permissions': '0o755'}, {'folder': Path('/path/to/destination_owned_by_user-with-correct-perms'), 'permissions': '0o755'}, {'folder': Path('/path/to/destination_not_owned_by_user'), 'permissions': '0o755'}]