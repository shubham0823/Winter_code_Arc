def name (*args, **kwargs):
    # print(args[0])
    for i in args:
        print (i)
    
    for keys,values in kwargs.items(): #why .items() used here 
        print (keys, values) 
    

StudentNames = ("shubham", "komal" , "rohan" , "mayank" )
StudentClass = {"shubham" : 25,
                "komal" : 18,
                "rohan" : 28,
                "mayank" : 26
                }

name(*StudentNames, **StudentClass)