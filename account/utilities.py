def phone_number_validator(phone_number: str):
    if not phone_number.isnumeric:
        raise ValueError('Phone number must be numerical.')

    elif len(phone_number) != 10:
        raise ValueError('Phone number must be 10 digits.')

    elif phone_number[0] != '9':
        raise ValueError('Please enter a valid phone number.')
