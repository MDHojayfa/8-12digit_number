with open('number_combinations.txt', 'w') as file:
    start = 10**(8 - 1)  # Smallest 8-digit number
    end = 10**12         # One more than the largest 12-digit number

    for number in range(start, end):
        file.write(f"{str(number).zfill(12)}\n")
