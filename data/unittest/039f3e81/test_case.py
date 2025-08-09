from pathlib import Path

function = 'delete_old_files'
test_cases = [{'directory': Path('/path/to/directory'), 'days_old': 30}, {'directory': Path('/path/to/directory'), 'days_old': 0}, {'directory': Path('/path/to/directory'), 'days_old': -5}, {'directory': Path('/nonexistent/directory'), 'days_old': 30}, {'directory': Path('/path/to/directory'), 'days_old': 1000000}]