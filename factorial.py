
def factorial(n):
    if not isinstance(n,int):
        raise TypeError('Number must be an integer')
    if n<0:
        raise ValueError('Number must be a positive integer')
    
    result=1
    for i in range(2,n+1):
        result*=i

    return result    