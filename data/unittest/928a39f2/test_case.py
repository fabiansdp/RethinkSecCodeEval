import io

function = 'handle_user_data'
test_cases = [{'data_stream': io.BytesIO(b''), 'result_stream': io.BytesIO()}, {'data_stream': io.BytesIO(b'a' * 8192), 'result_stream': io.BytesIO()}, {'data_stream': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'result_stream': io.BytesIO()}, {'data_stream': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'result_stream': io.BytesIO()}, {'data_stream': io.BytesIO(b'a' * (8192 * 2)), 'result_stream': io.BytesIO()}]