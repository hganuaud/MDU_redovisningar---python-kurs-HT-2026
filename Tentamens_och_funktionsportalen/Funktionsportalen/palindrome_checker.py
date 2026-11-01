
def is_palindrome(a: str) -> bool:
    new = ''
    for l in a:
        if l.isalnum():
            new += l
        else: 
            continue
        string = new[::-1].lower()
        if string == new.lower():
            return True
    return False

print(is_palindrome(
   "Step on no pets."
))