import jdatetime

today = str(jdatetime.datetime.now())
today = today.split()
print(f"Emrooz {today[0]} ast va saat {today[1][:5]} ast")
