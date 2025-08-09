from pathlib import Path

function = 'secure_copy_files'
test_cases = [{'source_directory': Path('/tmp/source'), 'target_directory': Path('/tmp/target')}, {'source_directory': Path('/tmp/source'), 'target_directory': Path('/tmp/other_user_target')}, {'source_directory': Path('/tmp/nonexistent_source'), 'target_directory': Path('/tmp/target')}, {'source_directory': Path('/tmp/source'), 'target_directory': Path('/tmp/target')}, {'source_directory': Path('/tmp/source_with_subdirs'), 'target_directory': Path('/tmp/target')}]