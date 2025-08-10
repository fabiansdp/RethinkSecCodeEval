import io

function = 'handle_stream_data'
test_cases = [{'stream_source': io.BytesIO(b'x' * 9999999)}, {'stream_source': io.BytesIO(b'x' * 10000001)}, {'stream_source': io.BytesIO(b'')}, {'stream_source': io.BytesIO(b'x' * 10240)}, {'stream_source': io.BytesIO(b'x' * 50000000)}]