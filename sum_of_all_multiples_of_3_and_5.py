def odd_multiples():
    all_odd_multiples=[]
    x=1
    y=1
    counter=0
    while (x<1000) and (y<1000):
    	if (x%3==0):
        	all_odd_multiples.append(x)
        	x+=1
    	else:
        	x+=1
    	if y in all_odd_multiples:
        	y+=1
    	else:
            if (y%5==0):
            	all_odd_multiples.append(y)
            	y+=1
            else:
            	y+=1
    for i in range(len(all_odd_multiples)):
        counter+=all_odd_multiples[i]
    return counter
print odd_multiples()