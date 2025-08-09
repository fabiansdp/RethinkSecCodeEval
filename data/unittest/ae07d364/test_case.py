from pathlib import Path

function = 'purge_expired_files'
test_cases = [{'directory_path': Path('/path/to/expired/files'), 'days_threshold': 1}, {'directory_path': Path('/path/to/non/expired/files'), 'days_threshold': 365}, {'directory_path': Path('/path/to/mixed/files'), 'days_threshold': 30}, {'directory_path': Path('/path/to/empty/folder'), 'days_threshold': 10}, {'directory_path': Path('/path/to/source_with_permission_error'), 'days_threshold': 1}]