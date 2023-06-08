def show_jalali_age(shamsi):
    from persiantools.jdatetime import JalaliDate, JalaliDateTime
    import pytz
    thisyear = int(JalaliDateTime(1402, 3, 12, 8, 59, 10, 0, pytz.utc).strftime("%Y"))
    age = thisyear - shamsi
    print(age)


# show_jalali_age(int(input("Enter your birth year : ")))

def show_miladi_age(miladi):
    import datetime
    thisyear = datetime.date.today().year
    age = thisyear - miladi
    print(age)


# show_miladi_age(int(input("Enter your birth year : ")))

# if __name__ == "__main__":
#     show_jalali_age(int(input("Enter your birth year : ")))
print(__name__)