from pathlib import Path

function = 'remove_old_files'
test_cases = [{'folder': Path('/path/to/folder'), 'max_days': 30}, {'folder': Path('/path/to/folder'), 'max_days': 0}, {'folder': Path('/path/to/folder'), 'max_days': -5}, {'folder': Path('/nonexistent/folder'), 'max_days': 30}, {'folder': Path('/path/to/folder'), 'max_days': 1}]