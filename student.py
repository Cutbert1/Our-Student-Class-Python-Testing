from datetime import date, timedelta
import requests


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # function or method for full_name
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    # function or method for Email address
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
    
    # function or method for alert_santa
    def alert_santa(self):
        self.naughty_list = True

    # function or method for apply_extention
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=5)

    # function or method for course_schedule
    def course_schedule(self):
        response = requests.get(f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"

             