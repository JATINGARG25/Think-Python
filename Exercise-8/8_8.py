# # takes only first character --- which means funtion is wrong

# # def any_lowercase1(s):
# #     for c in s:
# #         print(c)
# #         if c.islower():
# #             return True
# #         else:
# #             return False

# # print(any_lowercase1("jatinn"))

# wrong because it only checks the 'c' which is always lower

# def any_lowercase2(s):
#     for c in s:
#         print(c)
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'

# print(any_lowercase2("Jatinn"))

# also wrong

# def any_lowercase3(s):
#     for c in s:
#         print(c)
#         flag = c.islower()
#         return flag

# print(any_lowercase3("Jatinn"))

def any_lowercase4(s):
    flag = False
    for c in s:
        print(c)
        flag = flag or c.islower()
    return flag

# def any_lowercase5(s):
#     for c in s:
#         print(c)
#         if not c.islower():
#             return False
#     return True

print(any_lowercase4("JaTIN"))

# all the commented function are wrong


    
