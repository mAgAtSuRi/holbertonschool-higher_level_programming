#!/usr/bin/python3


def uniq_add(my_list=[]):
    return sum(set(my_list))

# my technique:
# uniqu_list = []
#     for num in my_list:
#         if num not in uniqu_list:
#             uniqu_list.append(num)
#     sum = 0
#     for num in uniqu_list:
#         sum += num
#     return sum