

def common_prefix_length(a: str, b: str) -> int:
    num = 0
    for i in range(min(len(a), len(b))):
        if a[0] == b[0]:
            if a[i] == b[i]:
                num += 1
    return num 

print(common_prefix_length('hola', 'hohobo'))

