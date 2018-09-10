#!/usr/bin/env python
from datetime import datetime, date, timedelta, time
import math
import numpy as np


class TimeServer():


    def __init__(self, period=None):
        self.period = period
        self.SAT = 0.75
        self.SUN = 0.5


    def get_time_remaining(self):

        today = date.today()
        eoy = date(2018, 12, 31)
        week_days = np.busday_count(today, eoy)
        tot_days = (eoy - today).days - 1
        wkend_days = tot_days - week_days
        if wkend_days % 2 == 1:
            vir_days = week_days + self.SAT*((wkend_days-1)/2) + self.SUN*((wkend_days+1)/2)
        else:
            vir_days = week_days + self.SAT*(wkend_days/2) + self.SUN*(wkend_days/2)

        tomorrow = date.today() + timedelta(1)
        midnight = datetime.combine(tomorrow, time())
        now = datetime.now()
        if datetime.today().weekday() == 5:
            vir_hours = self.SAT*((midnight - now).seconds / (60*60*24))
        elif datetime.today().weekday() == 6:
            vir_hours = self.SUN*((midnight - now).seconds / (60*60*24))
        else:
            vir_hours = ((midnight - now).seconds / (60*60*24))
        return vir_days + vir_hours


    def convert_to_virtual_time(self, r):
        now = datetime.now()
        seconds_gone = int(now.hour*60*60 + now.minute*60 + now.second)
        sleep_time = 24*60*60*r
        full_day = 24*60*60
        if seconds_gone + sleep_time < full_day: # same day
            if datetime.today().weekday() == 5:
                return r * full_day / self.SAT
            elif datetime.today().weekday() == 6:
                return r * full_day / self.SUN
            else:
                return r
        else: # day overlap
            if datetime.today().weekday() == 4: # Friday
                fri_seconds_left = 60*60*24 - seconds_gone
                sat_seconds_left = (60*60*24*r - fri_seconds_left) / self.SAT
                return fri_seconds_left + sat_seconds_left
            if datetime.today().weekday() == 5: # Saturday
                sat_seconds_left = (60*60*24 - seconds_gone) / self.SAT
                sun_seconds_left = (60*60*24*r - sat_seconds_left) / self.SUN
                return sat_seconds_left + sun_seconds_left
            elif datetime.today().weekday() == 6: # Sunday
                sun_seconds_left = (60*60*24 - seconds_gone) / self.SUN
                mon_seconds_left = 60*60*24*r - sun_seconds_left
                return sun_seconds_left + mon_seconds_left
            else:
                return r * fullday
