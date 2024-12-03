
sum=0
for i in range(1 , 31):
    print(i , end=" ")
    sum += i 
    if i % 4 == 0 :
        print("=" , sum)
        sum = 0

        
