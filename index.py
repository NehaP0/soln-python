def revstr(str) :
    s = ''
    for i in str : 
        s = i + s
    return s


str = "Python is fun"
print(revstr(str))
