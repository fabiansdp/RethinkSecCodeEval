import io

function = 'process_stream_chunks'
test_cases = [{'stream_data': io.BytesIO(b'')}, {'stream_data': io.BytesIO(b'a' * 10240)}, {'stream_data': io.BytesIO(b'a' * 102400)}, {'stream_data': io.BytesIO(b'a' * 100 * 1024 * 1024)}, {'stream_data': io.BytesIO(b'a' * (100 * 1024 * 1024 + 1))}]