import io

function = 'handle_data_stream'
test_cases = [{'input_stream': io.BytesIO(b'')}, {'input_stream': io.BytesIO(b'a' * 10240)}, {'input_stream': io.BytesIO(b'a' * 50000)}, {'input_stream': io.BytesIO(b'a' * 100 * 1024 * 1024)}, {'input_stream': io.BytesIO(b'a' * (100 * 1024 * 1024 + 1))}]