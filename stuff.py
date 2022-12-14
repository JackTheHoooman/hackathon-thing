## Q 1 - Already taken
def is_triplet(a, b, c):
    if (a**2 + b**2) == c:
        return True


print(is_triplet(3, 4, 25))


## Q 5
def reverser(string_input: str) -> str:
    string_input = string_input.swapcase()
    return string_input[::-1]


print(reverser("Hello World"))


## Q 6
def spacing(list_input: list) -> bool:
    previous_val = list_input[0]
    spacing_correct = True

    list_input.pop(0)

    for value in list_input:
        if value != (previous_val + 10):
            spacing_correct = False

        previous_val = value

    if spacing_correct != False:
        return True

print(spacing([0, 10, 20, 30]))

   

## Q 10
def count_vowels(string_input: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]

    string_input = string_input.lower()

    total = 0

    for vowel in vowels:
        total += string_input.count(vowel)

    return total


print(count_vowels("Celebration"))
