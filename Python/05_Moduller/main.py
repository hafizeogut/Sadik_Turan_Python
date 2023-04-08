 
def factoriyel(x):
    x=int(x)
    
    if x<0:
        raise ValueError('Negatif Değer')
        
    result=1
    
    for i in range(1,x+1):
        result *=i
        
    return result

for x in [5,10,3,-1,'-10a']:

    try:
        y=factoriyel(x)
        
    except ValueError as err:
        print(err)
        
print(factoriyel(y))
