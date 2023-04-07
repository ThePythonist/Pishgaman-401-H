primes = []

for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:
            # yani morakab e
            break
    else:
        # zamani ejra mishe ke morakab nabashe
        primes.append(i)

print(primes)
