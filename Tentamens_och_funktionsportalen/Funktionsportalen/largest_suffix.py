
def longest_common_prefix(a: str, b: str) -> str:
    string = ' '
    for letter in range(min(len(a), len(b))):
        if a[-1] == b[-1]:
            if a[letter] == b[letter]:
                string += a[letter]
    return string 

print(longest_common_prefix('heo', 'hepo'))