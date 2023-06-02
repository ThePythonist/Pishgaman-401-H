from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

# today = JalaliDateTime(1402, 3, 12, 8, 59, 10, 0, pytz.utc).strftime("%c")
# print(today.split()[0])

today = JalaliDateTime(1402, 3, 12, 8, 59, 10, 0, pytz.utc).strftime("%A")
print(today)
