def bestFit(weight, n, c): 
      
    res = 0; #빈의 개수
  
    bin_rem = [0]*n; 
  
   
    for i in range(n): 
          
        # weight[i] 
        j = 0; 
          
        min = c + 1; 
        bi = 0; 
  
        for j in range(res): 
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min): 
                bi = j; 
                min = bin_rem[j] - weight[i]; 
              
        if (min == c + 1): 
            bin_rem[res] = c - weight[i]; 
            res += 1; 
        else:  
            bin_rem[bi] -= weight[i]; 
    return res; 
  

if __name__ == '__main__': 
    weight = [ 7, 5, 6, 4, 2, 3, 7, 5 ]; 
    c = 10; 
    n = len(weight); 
    print("bestFit에서 필요한 통의 개수 : ", bestFit(weight, n, c)); 
      

