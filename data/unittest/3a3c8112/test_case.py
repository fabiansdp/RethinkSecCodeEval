function = 'construct_html_response'
test_cases = [{'content': 'Hello, World!'}, {'content': ''}, {'content': "<script>alert('XSS');</script>"}, {'content': 'This is a test with special characters: & < > " \''}, {'content': '1234567890'}, {'content': 'Line1\nLine2'}, {'content': 'Line1\r\nLine2'}, {'content': 'Line1\rLine2'}, {'content': '\tTabbed line'}, {'content': 'Mixed \t Tabs \n and \r\n Newlines'}]

for t in test_cases:
    print(t)
