import io

function = 'parse_user_input'
test_cases = [{'input_stream': io.BytesIO(b'Hello, world!'), 'output_stream': io.BytesIO()}, {'input_stream': io.BytesIO(b'a' * 8192), 'output_stream': io.BytesIO()}, {'input_stream': io.BytesIO(b'a' * (10 * 1024 * 1024)), 'output_stream': io.BytesIO()}, {'input_stream': io.BytesIO(b'a' * (10 * 1024 * 1024 + 1)), 'output_stream': io.BytesIO()}, {'input_stream': io.BytesIO(), 'output_stream': io.BytesIO()}]