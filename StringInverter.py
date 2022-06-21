def invert(string):
    if string is None:
        return ''
    if len(string) == 0:
        return ''
    if len(string) == 1:
        return string
    return string[::-1]
print(invert("example"))
