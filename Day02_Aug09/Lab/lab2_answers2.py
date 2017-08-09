class Clock(object):
    def __init__(self, hours, minutes):
        self.minutes = minutes
        self.hours = hours
    
    def time_to_min(hours, minutes=0):
        if hours >= 0 and hours <=23:
            h_in_m = 60 * hours
            in_m = h_in_m + minutes
        elif hours <= 0 or minutes <= 0:
            hours2 = 24 + hours
            h_in_m = 60 * hours2
            in_m = abs(60 - (h_in_m + minutes))
        else:
            h_in_m = 60 * (hours - 24)
            in_m = h_in_m + minutes
        return in_m
   
    @classmethod
    def at(cls, hours, minutes=0):
        return cls(hours, minutes)

    def __str__(self):
        return "%d:%02d" % (self.hours, self.minutes)

    def __add__(self, minutes):
        time_tmp_in_m = time_to_min(self.hours, self.minutes) + minutes
        hours = time_tmp_in_m / 60
        minutes = time_tmp_in_m % 60
        return "%d:%02d" % (hours, minutes)

    def __sub__(self, minutes):
        time_tmp_in_m2 = time_to_min(self.hours, self.minutes) - minutes
        hours2 = time_tmp_in_m2 / 60
        minutes2 = time_tmp_in_m2 % 60
        return "%d:%02d" % (hours2, minutes2)

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return False
        else:
            return True

time_to_min(25, 30)

clock1 = Clock.at(15, 37)
clock2 = Clock.at(15, 37)

clock1 == clock2

clock1.hours == clock2.hours and clock1.minutes == clock2.minutes

time_to_min(24, 30)

    h_in_m = 60 * hour
    in_m = h_in_m + minutes
    hours = in_m / 60
    minutes = in_m % 60

time_to_min(24, 30)

now = Clock.at(11, 3)
print now

now = Clock.at(1, 7) - 3
print now

now_a = now + 3
print now_a

now = Clock.at(11, 46)
print now 