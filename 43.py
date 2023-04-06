brands = ["toyota", "bmw", "saipa", "volvo", "kerman motor"]
persianbrands = ["saipa", "bahman motor", "kerman motor", "modiran khodro"]

# for i in brands :
#     if i in persianbrands:
#         print(i)

for i in brands:
    for j in persianbrands:
        if i == j:
            print(i)

