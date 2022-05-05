import big_o

def calculate_time_complexity(n):
    new_arr = []
    for i in range(n+1):
        for j in range(i):
            k = i+j
            new_arr.append(k)

print(big_o.big_o(calculate_time_complexity, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=100)[0])
print("\nNOTE: 1 microsecond = 1.0E-6 seconds")
