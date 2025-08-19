def valid_value():
    while True:
        value = input('Enter the amount you want to convert: ').strip()
        try:
            value = float(value)
            if value > 0:
                return value
            else:
                print('Enter a value greater than 0.')
        except ValueError:
            print('Invalid value. Please enter a valid number.')