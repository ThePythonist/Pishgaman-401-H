brands = ["toyota", "bmw", "saipa", "volvo", "kerman motor"]
persianbrands = ["saipa", "bahman motor", "kerman motor", "modiran khodro"]

common = [i for i in brands if i in persianbrands]
print(common)
