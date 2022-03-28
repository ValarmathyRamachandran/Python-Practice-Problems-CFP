# Python program to Find day of the week for a given date
import calendar  # module of python to provide useful fucntions related to calendar
import datetime  # module of python to get the date and time


def findDay(date):
    """
    :param date: giving date as parameter
    :return: day of the week
    """

    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    # this statement returns an integer corresponding to the day of the week

    return calendar.day_name[born]
    # this statement returns the corresponding day name to the integer generated in the previous statement


if __name__ == "__main__" :
    date = '30 04 1995'  # this is the input date
    print(findDay(date))  # here we print the final output after calling the fucntion findday
