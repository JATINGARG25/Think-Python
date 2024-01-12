def cumulative_sum(l):
    cumulative_sum_list = []
    for i in range(len(l)):
        if i == 0:
            cumulative_sum_list.append(l[i])
        else:
            l[i] = l[i] + l[i-1]
            cumulative_sum_list.append(l[i])
    return cumulative_sum_list

a = [1,2,3,4,5,6,9,8,7,10]
print(cumulative_sum(a))

    