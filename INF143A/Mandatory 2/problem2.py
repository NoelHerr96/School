n = 0
prime_list = []


def prime_check(n):
    if n <= 1:
        return False

    for i in range (2,n):
        if n % i == 0:
            return False
        else:
            prime_list.append(n)
    return True


while True:
    n+=1
    prime_check(n)

    if len(prime_list) == 50:
        print(prime_list)
        break


# print("true") if prime_check(11) else print("false")
# print("true") if prime_check(14) else print("false")