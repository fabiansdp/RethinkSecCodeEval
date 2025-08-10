import io

function = 'manage_user_input'
test_cases = [{'input_stream_data': io.BytesIO(b''), 'output_stream_data': io.BytesIO()}, {'input_stream_data': io.BytesIO(b'a' * 8192), 'output_stream_data': io.BytesIO()}, {'input_stream_data': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'output_stream_data': io.BytesIO()}, {'input_stream_data': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'output_stream_data': io.BytesIO()}, {'input_stream_data': io.BytesIO(b'a' * 16384), 'output_stream_data': io.BytesIO()}, {'input_stream_data': io.BytesIO(b'a' * (8192 * 1024)), 'output_stream_data': io.BytesIO()}]