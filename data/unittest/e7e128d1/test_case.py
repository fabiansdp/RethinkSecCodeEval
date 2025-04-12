function = 'create_xml_reply'
test_cases = [{'user_text': 'Hello World'}, {'user_text': ''}, {'user_text': '<>&"\''}, {'user_text': "<script>alert('xss');</script>"}, {'user_text': 'こんにちは'}]