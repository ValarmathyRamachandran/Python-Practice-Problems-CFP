# Python program to calculate WC
import math


def wind_chill(temp, wi_sp):
    wci = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(wi_sp, 0.16)
    return wci


# Taking the Air Temperature (Ta)
temp = 42

# Taking the Wind Speed (v)
wi_sp = 150

print("The Wind Chill is", int(round(wind_chill(temp, wi_sp))))
