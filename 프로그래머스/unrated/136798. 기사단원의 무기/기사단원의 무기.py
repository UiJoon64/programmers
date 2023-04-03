import collections

# def solution(number, limit, power):

#     def real_func(number):
#         list1=[]
#         mok=0
#         ans = 1
#         while(mok!=1):
#             for k in range(2,number+1,1):
#                 mok = number // k
#                 namugi = number%k
#                 if namugi == 0:
#                     number = mok
#                     list1.append(k)
#                     break
#         dap = [x+1 for x in collections.Counter(list1).values()]
#         for n in dap:
#             ans *= n
#         return ans
    
#     def real_func(number):
#         primes = []
#         factors = {}
#         for i in range(2, number+1):
#             if i not in primes:
#                 factors[i] = 1
#                 for j in range(i*i, number+1, i):
#                     primes.append(j)
#                     factors[i] += 1
#         ans = 1
#         for n in factors.values():
#             ans *= n
#         return ans
    
#     answer_list=[]
#     for i in range(2,number+1,1):
#         print(f"{i}의 약수의 개수는 {real_func(i)}")
#         tres = real_func(i)
        
#         if tres>limit:
#             answer_list.append(power)
#         else:
#             answer_list.append(tres)

#     answer=sum(answer_list)+1

#     return answer
import math

def real_func(number):
    primes = []
    d = 2
    while d * d <= number:
        while (number % d) == 0:
            primes.append(d)
            number //= d
        d += 1
    if number > 1:
        primes.append(number)
    return math.prod([x+1 for x in collections.Counter(primes).values()])



def solution(number, limit, power):
    factor_counts = {}
    answer_list = []
    
    for i in range(2, number+1):
        if i not in factor_counts:
            factor_counts[i] = real_func(i)
        tres = factor_counts[i]
        if tres > limit:
            answer_list.append(power)
        else:
            answer_list.append(tres)
            
    return sum(answer_list) + 1