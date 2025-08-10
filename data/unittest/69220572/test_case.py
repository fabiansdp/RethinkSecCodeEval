function = 'create_event_invitation'
test_cases = [
    {
        'title_of_event': 'Annual Tech Conference',
        'event_details': 'Join us for the latest in technology advancements.',
        'scheduled_date': 'October 15, 2023',
        'extra_info': 'Refreshments will be provided.'
    },
    {
        'title_of_event': "<script>alert('XSS')</script>",
        'event_details': 'Details <b>in bold</b>',
        'scheduled_date': '2023-10-15',
        'extra_info': 'Info &amp; Details'
    },
    {
        'title_of_event': '',
        'event_details': '',
        'scheduled_date': '',
        'extra_info': ''
    },
    {
        'title_of_event': 'Very Long Event Title That Should Be Escaped Properly Very Long Event Title That Should Be Escaped Properly Very Long Event Title That Should Be Escaped Properly',
        'event_details': 'Event details with special characters: & < > " \'',
        'scheduled_date': 'Today',
        'extra_info': 'Extra info with new lines\nand tabs\t'
    }
]
