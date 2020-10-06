try:
    a=10
    print (a)
    raise NameError("Hello")
except NameError as e:
        print ("An exception occurred")
        print (e)
else:
    print('Everything is fine in try-except')
    
finally:
    print('out of try except')
