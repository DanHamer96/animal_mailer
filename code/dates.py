import datetime as dt


# this class will format the date nicely for the email output. This class also generates the day of the month today.
class Dates(object):

    def __init__(self):
        # get today's date
        self.day_now = dt.date.today().strftime('%d')
        self.suffix = None
        self.date_today = None
        self.day_today = None

    def get_dates(self):
        # this if/else loop will guarantee the correct suffix given today's date (e.g. 1st, 11th, 21st)
        if self.day_now[-1:] == '1':
            if self.day_now == '11':
                self.suffix = 'th'
            else:
                self.suffix = 'st'
        elif self.day_now[-1:] == '2':
            if self.day_now == '12':
                self.suffix = 'th'
            else:
                self.suffix = 'nd'
        elif self.day_now[-1:] == '3':
            if self.day_now == '13':
                self.suffix = 'th'
            else:
                self.suffix = 'rd'
        else:
            self.suffix = 'th'

        # format date outputs - remove leading 0 on first 9 days of the month & add suffix on date string.
        if self.day_now[0] == '0':
            self.day_today = self.day_now[1]
        else:
            self.day_today = self.day_now

        self.date_today = dt.date.today().strftime(str(self.day_today) + str(self.suffix) + ' %b %Y')

        return self.date_today, self.day_today
