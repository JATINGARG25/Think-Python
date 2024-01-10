def eval_loop():
    while True:
        a = input("Enter the expression which you need to evaluate : ")
        if a == 'done':
            break
        result = eval(a)
        print(result)

    return result

print(eval_loop())