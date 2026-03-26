def prime(inp):
    if inp < 2:
        return False
    elif inp == 2:
        return True
    elif inp % 2 == 0:
        return False
    for i in range(3, round(inp ** (1 / 2) + 1), 2):
        if inp % i == 0 :
            return False
    return True

num= input()
if (prime(int(num))):
    print('простое')
else:
    print('ох не простое...')