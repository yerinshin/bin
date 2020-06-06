def nextfit(weight, c): 
    res = 0
    rem = c 
    for _ in range(len(weight)): 
        if rem >= weight[_]: 
            rem = rem - weight[_] 
        else: 
            res += 1
            rem = c - weight[_] 
    return res 
  
 
weight = [7, 5, 6, 4, 2, 3, 7, 5] 
c = 10
  
print("Next Fit에 필요한 통의 개수 :",  
                           nextfit(weight, c)) 
