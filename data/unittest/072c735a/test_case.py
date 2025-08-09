from pathlib import Path

function = 'purge_old_items'
test_cases = [{'target_dir': Path('/tmp/test_dir_no_files'), 'age_days': 1}, {'target_dir': Path('/tmp/test_dir_old_files'), 'age_days': 1}, {'target_dir': Path('/tmp/test_dir_new_files'), 'age_days': 365}, {'target_dir': Path('/tmp/test_dir_other_owner_files'), 'age_days': 1}, {'target_dir': Path('/tmp/test_dir_permission_denied'), 'age_days': 1}]