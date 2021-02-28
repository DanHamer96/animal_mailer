import datetime as dt


# this class will format the date nicely for the email output - this also generates the day of the month today.
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
            if self.day_now[-2:] == '11':
                self.suffix = 'th'
            else:
                self.suffix = 'st'
        elif self.day_now[-1:] == '2':
            if self.day_now[-2:] == '12':
                self.suffix = 'th'
            else:
                self.suffix = 'nd'
        elif self.day_now[-1:] == '3':
            if self.day_now[-2:] == '13':
                self.suffix = 'th'
            else:
                self.suffix = 'rd'
        else:
            self.suffix = 'th'

        # formats date outputs
        self.date_today = dt.date.today().strftime('%d' + str(self.suffix) + ' %b %Y')
        self.day_today = dt.date.today().strftime('%d')

        return self.date_today, self.day_today
