# Python3 program to represent  
# a given number as sum of  
# minimum possible psuedobinary  
# numbers 
  
# function to represent a  
# given number as sum of 
# minimum possible 
# psuedobinary numbers 
def psuedoBinary(n): 
    arrayResult=[];
    while (n > 0): 
          
        temp = n; 
        m = 0; 
        p = 1; 
        while (temp): 
            rem = temp % 10; 
            temp = int(temp / 10); 
              
            if (rem != 0): 
                m += p; 
            p *= 10; 
        arrayResult.append(m);  
        #print(m,end=" "); 
        n = n - m;
    arrayResult.reverse();
    print(len(arrayResult),end="\n");
    for x in arrayResult:
       print(x,end=" ");
 
  
 
n = 21; 
psuedoBinary(n); 

#input 21
#output 10 11
#exaplanation 10+11=21
#input 4
#output 1111
#exaplanation 1+1+1+1=4
