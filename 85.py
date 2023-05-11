phone_number = input("Enter your phone number : ")

if phone_number[0] == "0":
    phone_number = phone_number.replace("0", "+98", 1)
else:
    # phone_number = f"+98{phone_number}"
    phone_number = "+98{pn}".format(pn=phone_number)

print(phone_number)
