from pathlib import Path

function = 'remove_expired_files'
test_cases = [{'folder': Path('/path/to/empty/folder'), 'age_threshold': 1}, {'folder': Path('/path/to/non/expired/files'), 'age_threshold': 1}, {'folder': Path('/path/to/expired/files'), 'age_threshold': 0}, {'folder': Path('/path/to/mixed/files'), 'age_threshold': 1}, {'folder': Path('/path/to/permission/denied/file'), 'age_threshold': 0}, {'folder': Path('/path/to/destination_not_owned_by_user'), 'age_threshold': 0}]