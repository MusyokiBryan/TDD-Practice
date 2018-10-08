# def is_prime(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#
#     return True
# def prime(n):
#     result =[2]
#     for i in range (0, n):
#         if is_prime(i):
#             result.append(i)
#     return result
# print (prime(30))

def prime(n):
    return [2]

    if n == 0:
        return []

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
    return True