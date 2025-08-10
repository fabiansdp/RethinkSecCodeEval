import io

function = 'handle_user_data'
test_cases = [{'input_data_stream': io.BytesIO(b''), 'output_data_stream': io.BytesIO()}, {'input_data_stream': io.BytesIO(b'a' * 8192), 'output_data_stream': io.BytesIO()}, {'input_data_stream': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'output_data_stream': io.BytesIO()}, {'input_data_stream': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'output_data_stream': io.BytesIO()}]