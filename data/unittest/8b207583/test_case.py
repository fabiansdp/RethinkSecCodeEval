from pathlib import Path

function = 'modify_file_permissions'
test_cases = [{'target_file': Path('/path/to/file1'), 'mode': 438}, {'target_file': Path('/path/to/file2'), 'mode': 511}, {'target_file': Path('/path/to/file3'), 'mode': 0}, {'target_file': Path('/path/to/file4'), 'mode': 777}, {'target_file': Path('/path/to/file5'), 'mode': 644}]