def sum_of_lists(N): 
    total = 0
    for i in range(6): 
        L = [j ^ ( j >> i) for j in range(N)] 
        total += sum(L)
    return total