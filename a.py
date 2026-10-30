sorted_list = [9,13,1,99,133,78,2,64,60,3]
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list) - 1):
        if sorted_list[i] > sorted_list[i + 1]:
            swap = sorted_list[i]
            sorted_list[i] = sorted_list[i + 1]
            sorted_list[i + 1] = swap
            stop_flag = True

print(sorted_list)