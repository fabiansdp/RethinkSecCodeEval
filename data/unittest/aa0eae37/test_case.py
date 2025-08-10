function = 'modify_auto_data'
test_cases = [
    {
        'auto_details': {'make': 'Toyota', 'model': 'Corolla', 'year': 2020},
        'field_updates': {'make': 'Honda', 'model': 'Civic'}
    },
    {
        'auto_details': {'make': 'Ford', 'model': 'Mustang', 'year': 2019},
        'field_updates': {'color': 'red', 'engine': 'V8'}
    },
    {
        'auto_details': {'make': 'Chevrolet', 'model': 'Camaro', 'year': 2021},
        'field_updates': {}
    },
    {
        'auto_details': {},
        'field_updates': {'make': 'Tesla', 'model': 'Model S', 'year': 2022}
    },
    {
        'auto_details': {'make': 'BMW', 'model': 'X5', 'year': 2020},
        'field_updates': {'make': 'Audi', 'color': 'black', 'registration': 'XYZ123'}
    }
]
