def generate_palindromes(n):
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            yield i

for palindrome in generate_palindromes(100):
    print(palindrome)
