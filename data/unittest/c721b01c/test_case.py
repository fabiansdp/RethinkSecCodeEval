import io

function = 'manage_form_submission'
test_cases = [{'form_source': io.BytesIO(b'Hello world'), 'form_destination': io.BytesIO()}, {'form_source': io.BytesIO(b'a' * 8192), 'form_destination': io.BytesIO()}, {'form_source': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'form_destination': io.BytesIO()}, {'form_source': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'form_destination': io.BytesIO()}, {'form_source': io.BytesIO(b'a' * (16384)), 'form_destination': io.BytesIO()}]