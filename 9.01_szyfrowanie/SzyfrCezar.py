string = input()
y = int(input())
limit = 122
start = 97

def moczywor(string,y):
    result = ''
    for i in range(0, len(string)):
        x = ord(string[i])
        m = x + y
        if m > limit:
            m = start + (m - limit - 1)
        result += chr(m)
    return result

print(moczywor(string,y))
