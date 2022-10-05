while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        evenMedian = 0
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    if len(numbers) % 2 == 0:
        evenMedian = numbers[len(numbers)] + numbers[len(numbers)+1] / 2
        print(evenMedian)
    elif len(numbers) % 2 != 0:
        evenMedian = -(numbers[len(numbers)] / 2);
print(evenMedian)
