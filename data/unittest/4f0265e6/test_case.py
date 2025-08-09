from pathlib import Path

function = 'purge_outdated_files'
test_cases = [{'dir_path': Path('/path/to/directory'), 'threshold_days': 30}, {'dir_path': Path('/path/to/directory'), 'threshold_days': 0}, {'dir_path': Path('/path/to/directory'), 'threshold_days': 1000}, {'dir_path': Path('/nonexistent/directory'), 'threshold_days': 30}, {'dir_path': Path('/path/to/directory'), 'threshold_days': -1}]