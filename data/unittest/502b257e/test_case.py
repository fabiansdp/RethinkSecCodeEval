from pathlib import Path

function = 'adjust_directory_rights'
test_cases = [{'folder': Path('/path/to/destination_owned_by_user'), 'permissions': 0o755}, {'folder': Path('/path/to/destination_owned_by_user'), 'permissions': 0o777}, {'folder': Path('/path/to/destination_not_owned_by_user'), 'permissions': 0o755}, {'folder': Path('/path/to/destination_owned_by_user_with_wrong_perms'), 'permissions': 0o755}, {'folder': Path('/path/to/destination_owned_by_user_with_correct_perms'), 'permissions': 0o755}, {'folder': Path('/path/to/destination_not_owned_by_user'), 'permissions': 0o755}]