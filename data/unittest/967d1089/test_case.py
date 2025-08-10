import io

function = 'process_form_data'
test_cases = [{'form_stream': io.BytesIO(b''), 'storage_stream': io.BytesIO()}, {'form_stream': io.BytesIO(b'a' * 8192), 'storage_stream': io.BytesIO()}, {'form_stream': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'storage_stream': io.BytesIO()}, {'form_stream': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'storage_stream': io.BytesIO()}, {'form_stream': io.BytesIO(b'a' * (2 * 8192)), 'storage_stream': io.BytesIO()}]