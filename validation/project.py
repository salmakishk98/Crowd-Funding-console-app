from datetime import datetime


def validate_date(date):
    format = "%d-%m-%Y"
    try:
        res = bool(datetime.strptime(date, format))
    except ValueError:
        res = False
    if res:
        return True
    print("not valid date")
    return  False


def compare_date(st_date,en_date):
    st_date = list(st_date.split("-"))
    st_date = datetime(int(st_date[2]),int(st_date[1]),int(st_date[0]))
    en_date = list(en_date.split("-"))
    en_date = datetime(int(en_date[2]), int(en_date[1]), int(en_date[0]))
    if st_date < en_date:
        return True
    print("end date must be after start date")
    return  False

