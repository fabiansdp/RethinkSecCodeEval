from pathlib import Path

function = 'change_file_access'
test_cases = [{'path_to_file': Path('/path/to/file1'), 'access_bits': 438}, {'path_to_file': Path('/path/to/file2'), 'access_bits': 511}, {'path_to_file': Path('/path/to/file3'), 'access_bits': 0}, {'path_to_file': Path('/path/to/file4'), 'access_bits': 777}]