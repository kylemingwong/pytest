prime =  []
for num in range(2,100):
    if num == 3:
        prime.append(num)
    for i in range(2,int(num/2+1)):
        if num%i == 0:
            break;
        elif i == int(num/2):
            prime.append(num)
print prime