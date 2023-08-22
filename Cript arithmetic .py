from itertools import permutations

def is_solution_valid(letters, assigned_digits, words, result_word):
    if any(assigned_digits[letter] == 0 for letter in words[0]):
        return False

    values = []
    for word in words:
        value = 0
        for letter in word:
            value = value * 10 + assigned_digits[letter]
        values.append(value)

    result_value = 0
    for letter in result_word:
        result_value = result_value * 10 + assigned_digits[letter]

    return sum(values[:-1]) == result_value

def solve_cryptarithmetic(equation):
    equation = equation.replace(' ', '')  a
    
    words, result_word = equation.split('=')
    words = words.split('+')

    unique_letters = set(''.join(words) + result_word)
    if len(unique_letters) > 10:
        return None 

    letters = list(unique_letters)
    digit_permutations = permutations(range(10), len(letters))

    for perm in digit_permutations:
        assigned_digits = dict(zip(letters, perm))
        if is_solution_valid(letters, assigned_digits, words, result_word):
            return assigned_digits

    return None

if __name__ == "__main__":
    equation = "SEND + MORE = MONEY"
    solution = solve_cryptarithmetic(equation)

    if solution:
        print("Solution:")
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
    else:
        print("No solution found.")
