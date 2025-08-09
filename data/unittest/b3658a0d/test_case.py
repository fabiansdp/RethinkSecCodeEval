from pathlib import Path

function = 'discard_old_files'
test_cases = [{'path': Path('/tmp/test_dir'), 'limit_days': 1}, {'path': Path('/tmp/test_dir'), 'limit_days': 0}, {'path': Path('/tmp/test_dir'), 'limit_days': -1}, {'path': Path('/tmp/nonexistent_dir'), 'limit_days': 1}, {'path': Path('/tmp/empty_dir'), 'limit_days': 1}, {'path': Path('/tmp/mixed_dir'), 'limit_days': 1}]