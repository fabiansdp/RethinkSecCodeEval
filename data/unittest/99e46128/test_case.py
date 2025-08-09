from pathlib import Path

function = 'clean_old_documents'
test_cases = [{'dir_path': Path('/path/to/nonexistent/directory'), 'file_age': 1}, {'dir_path': Path('/path/to/empty/folder'), 'file_age': 1}, {'dir_path': Path('/path/to/non/expired/files'), 'file_age': 365}, {'dir_path': Path('/path/to/expired/files'), 'file_age': 1}, {'dir_path': Path('/path/to/mixed/files'), 'file_age': 7}, {'dir_path': Path('/path/to/source_with_permission_error'), 'file_age': 1}]