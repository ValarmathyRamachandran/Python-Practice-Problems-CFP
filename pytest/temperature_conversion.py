def temperature_conversion_celsius(celsius):
    """

    :param celsius:
    :return: temparture in fahrenhei
    """
    # celsius = float(input("Temperature value in degree Celsius: "))

    # For Converting the temperature to degree Fahrenheit by using the formula
    celsius_to_fahrenheit = (celsius * 1.8) + 32

    # print the result
    print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'
          % (celsius, celsius_to_fahrenheit))


def temperature_conversion_fahrenheit(fahrenheit):
    #fahrenheit = float(input("Temperature value in degree Fahrenheit: "))

    # For Converting the temperature from degree Fahrenheit to degree Celsius
    # by using the above given formula
    fahrenheit_to_celsius = (fahrenheit - 32) / 1.8

    # Print the result
    #print('The %.2f degree Fahrenheit is equal to: %.2f Celsius'
          #% (fahrenheit, fahrenheit_to_celsius))
    return fahrenheit_to_celsius


if __name__ == "__main__":
    temperature_conversion_celsius(30)
    temperature_conversion_fahrenheit(86)
