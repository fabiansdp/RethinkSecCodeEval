from pathlib import Path

function = 'clean_old_logs'
test_cases = [{'log_dir': Path('/tmp/test_logs'), 'num_days': 1}, {'log_dir': Path('/tmp/test_logs'), 'num_days': 0}, {'log_dir': Path('/tmp/test_logs'), 'num_days': 30}, {'log_dir': Path('/nonexistent_directory'), 'num_days': 1}, {'log_dir': Path('/tmp/test_logs'), 'num_days': 1}, {'log_dir': Path('/tmp/test_logs'), 'num_days': 1}]