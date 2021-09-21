N = [32,3,14,56,8,73,10]
M = len(N) # Создаем переменную M равную длинне списка N
for i in range(1,M):
    for k in range(0,M-i):
        if N[k] > N[k+1]:
            N[k],N[k+1] = N[k+1],N[k]

print("Отсортированный список: ",N)
