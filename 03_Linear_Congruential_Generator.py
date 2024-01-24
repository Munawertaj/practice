import sys

def linearCongruentialGenerator(a, b, seed, mod):
    randomNumbers = []
    val = seed

    while True:
        randomNumbers.append(val)
        val = (a * val + b) % mod
        if val == seed:
            break

    return randomNumbers


def showOutput(nums):
    with open('output.txt', 'w') as output_file:
        sys.stdout = output_file

        for i in range(len(nums)):
            print(f"X{i} = {nums[i]}")


def main():
    with open('input.txt', 'r') as input_file:

        multiplicativeConstant = int(input_file.readline().strip())
        additiveConstant = int(input_file.readline().strip())
        seed = int(input_file.readline().strip())
        mod = int(input_file.readline().strip())

    numbers = linearCongruentialGenerator(multiplicativeConstant, additiveConstant, seed, mod)
    showOutput(numbers)


if __name__ == "__main__":
    main()
