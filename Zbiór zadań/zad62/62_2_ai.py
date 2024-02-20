def naj_ciag(numbers):
    max_length = 1
    current_length = 1
    start_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                start_index = i - max_length
            current_length = 1

    # Check if the last sequence is the longest
    if current_length > max_length:
        max_length = current_length
        start_index = len(numbers) - max_length

    return numbers[start_index], max_length

def zczytywanie_liczby(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

if __name__ == "__main__":
    numbers = zczytywanie_liczby("liczby2.txt")
    first_number, length = naj_ciag(numbers)

print(f"Pierwszy element najdłuższego niemalejącego ciągu: {first_number}")
print(f"Liczba elementów w ciągu: {length}")