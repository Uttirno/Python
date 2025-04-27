def longestConsecutiveOnes(n):
    binary = bin(n)[2:]
    print(f"Binary Representation of {n} is {binary}")

    ones_sequence = binary.split('0')
    max_length = (len(seq) for seq in ones_sequence)

    return max_length

number = int(input())
result = longestConsecutiveOnes(number)
print(result)