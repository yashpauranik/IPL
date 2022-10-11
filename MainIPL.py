import time

def get_key():
    dict1 ={
        "Kohli": "India","Rohit" : "India", "Bumrah":"India" ,
        "Warner": "Aus", "Maxwell" : "Aus","Smith" :"Aus" ,
        "Buttler":"Eng","Stokes":"Eng","Curran":"Eng"
    }
    dict2 ={
        "Kohli":"RCB","Faf":"RCB","Hazelwood":"RCB" ,
        "Buttler":"RR","Chahal":"RR","Ashwin":"RR",
        "Warner":"DC","Avesh":"DC","Axar":"DC"
    }
    a = dict2.keys()
    bkey = dict1.keys()
    for keys in dict2 :
            for key in bkey:
                if keys ==key:

                    print(keys,dict1[key])
start = time.time()
get_key()
end = time.time()
print(end - start)

