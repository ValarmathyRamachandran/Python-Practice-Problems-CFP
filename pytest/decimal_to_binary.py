# Recursive Function to convert decimal to binary

def decimal_to_binary(ip_val):
    if not ip_val:
        return ''

        # recursive function call
        # printing remainder from each function call
    return decimal_to_binary(ip_val // 2) + str(ip_val % 2)


if __name__ == '__main__':
    # decimal value
    ip_val = 24

    # Calling special function
    print(decimal_to_binary(ip_val))
