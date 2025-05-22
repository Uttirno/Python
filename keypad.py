keypad = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqr", "rst", "wxyz"]

def printCombination(combination, output, current, n):

    if current == n:
        print(*output, sep=",")
        return

    for i in range(len(keypad[combination[current]])):
        output.append(keypad[combination[current]][i])
        printCombination(combination, output, current+1, n)
        output.pop()

        if (combination[current] == 0 or combination[current] == 1):
            return


combination = [4, 3, 4]

n = len(combination)

printCombination(combination, [], 0, n)

