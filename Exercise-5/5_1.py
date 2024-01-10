# # # # def even_odd(a):

# # # #     if a%2 == 0:
# # # #         print("Number is Even")
# # # #     else:
# # # #         print("Number is Odd")

# # # # even_odd(19)
# # # x = int(input("Enter the number : "))

# # # if x>0 and x<10:
# # #     print("Number is positive and single digit.")

# # # else:
# # #     print("Number not meet the requirements.")

# # def count_down(n):
# #     if n <= 0:
# #         print("Blastoff")
# #     else:
# #         print(n)
# #         count_down(n-1)

# # count_down(5)

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)

# print_n("Jatin",5)

def print_n():
    print("hello")

def do_n(f,n):
    if n<=0:
        return
    else:
        f()
        do_n(f,n-1)

do_n(print_n,5)