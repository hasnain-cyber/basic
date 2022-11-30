import basic

while True:
    text = input('basic > ')

    # get parsed tokens and error (if any)
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
