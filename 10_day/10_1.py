def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        n = input()
        try:
            n = int(n)
            print(n)
            print(end_message)
            return n
        except ValueError:
            print(n)
            print(error_message)
x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
