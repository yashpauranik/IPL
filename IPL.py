def get_key():
        dict1 ={
                "India" : ["Kohli" , "Rohit", "Bumrah"] ,
                "Aus" : ["Warner" , "Maxwell", "Smith" ],
                "Eng" : ["Buttler" , "Stokes" , "Curran"]
        }
        dict2 ={
                "RCB":["Kohli","Faf","Hazelwood"] ,
                "RR":["Buttler" , "Chahal" ,"Ashwin"],
                "DC":["Warner","Avesh","Axar"]
        }
        a = dict2.values()
        b = dict1.values()
        akey = dict2.keys()
        bkey = dict1.keys()
        for element in a :
                for i in element :
                     for element1 in b:
                             for i1 in element1:
                                 if i ==i1:
                                          print(string for team,name in dict1.items() if name == 'i')
get_key()