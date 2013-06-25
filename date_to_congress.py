import datetime

def convert_date_to_congress(date):
    '''
    Takes a datetime.date object and returns an integer corresponding to the Congress
    in session on that date. Based on: http://en.wikipedia.org/wiki/List_of_United_States_Congresses
    '''
    first = [datetime.date(i,3,4) for i in range(1789,1935,2)]
    second = [datetime.date(i,1,3) for i in range(1935,datetime.date.today().year+3,2)]
    start_dates = {i:num+1 for num,i in enumerate(first+second)}
    start_date_list = sorted(start_dates.keys())
    if date < datetime.date(1789,3,4):
        raise ValueError("Pre-dates first U.S. Congress")
    elif date > datetime.date.today():
        raise ValueError("Date is in the future")
    else:
        for num,start_date in enumerate(start_date_list[:-1]):
            if start_date <= date < start_date_list[num+1]:
                congress_number = start_dates[start_date]
            
    return congress_number
