import io

function = 'stream_processor'
test_cases = [{'binary_input': io.BytesIO(b'')}, {'binary_input': io.BytesIO(b'a' * 10240)}, {'binary_input': io.BytesIO(b'a' * 100000000)}, {'binary_input': io.BytesIO(b'a' * 102400000)}]