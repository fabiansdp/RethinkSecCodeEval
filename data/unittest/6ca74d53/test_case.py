import io

function = 'process_form_data'
test_cases = [{'user_input_stream': io.BytesIO(b''), 'user_output_stream': io.BytesIO()}, {'user_input_stream': io.BytesIO(b'a' * 8192), 'user_output_stream': io.BytesIO()}, {'user_input_stream': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'user_output_stream': io.BytesIO()}, {'user_input_stream': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'user_output_stream': io.BytesIO()}]