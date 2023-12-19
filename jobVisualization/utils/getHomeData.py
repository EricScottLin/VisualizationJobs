from .getPublicData import *

import time


def getCurrentTime():
    timeFormatter = time.localtime()
    year = timeFormatter.tm_year
    mon = timeFormatter.tm_mon
    date = timeFormatter.tm_mday
    weekday = timeFormatter.tm_wday
    hour = timeFormatter.tm_hour
    min = timeFormatter.tm_min
    sec = timeFormatter.tm_sec
    return year, monthList[mon-1], date, weekList[weekday-1], hour, min, sec