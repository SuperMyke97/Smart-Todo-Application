from dateutil import parser
import dateparser
import pendulum
from datetime import datetime

def date_parsing(date: str):
    day = {"monday":pendulum.MONDAY,
           "tuesday":pendulum.TUESDAY,
           "wednesday":pendulum.WEDNESDAY,
           "thursday":pendulum.THURSDAY,
           "friday": pendulum.FRIDAY,
           "saturday":pendulum.SATURDAY,
           "sunday":pendulum.SUNDAY}
    

    if "next week" in date or "nextweek" in date:
        for k,v in day.items():
            if k in date:
                date = pendulum.now().next(v).date()
                return date
    # elif datetime.strptime(date, "%Y-%m-%d"):
    #     date = datetime.strftime(date, "%Y-%m-%d")
    #     return date                
    else:
        date = dateparser.parse(date).date()
        return date
        
if __name__ == '__main__':
    print(date_parsing('tomorrow'))

