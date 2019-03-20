import math
def century(input):
    result = ''
    x = len(input)
    for i in x:
       for j in i+1:
           if j==0:
               result+=str.capitalize(input[i])
            #else:
            #    result+=str.lower(input[i])
        #if i!=x-1:
        #    result+='-'

    return result