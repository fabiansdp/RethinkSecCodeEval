import io

function = 'stream_data_handler'
test_cases = [{'incoming_stream': io.BytesIO(b'')}, {'incoming_stream': io.BytesIO(b'a' * 10240)}, {'incoming_stream': io.BytesIO(b'a' * (100 * 1024 * 1024))}, {'incoming_stream': io.BytesIO(b'a' * (101 * 1024 * 1024))}, {'incoming_stream': io.BytesIO(b'a' * (5 * 10240))}]