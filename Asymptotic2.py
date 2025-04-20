def Ontime(n):
    iteration=0
    for i in range(1, n+1):
        iteration+=5
    print("When n is ",n,"Iterations = ",iteration)

Ontime(5)
Ontime(10)
Ontime(15)
Ontime(200)

print("\nWith every 'n' the time taken and iterations will increase linearly")