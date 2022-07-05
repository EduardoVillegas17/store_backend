


from ctypes import addressof


def run_test():
    print("Running test...")


    me = {
        "first": "Eduardo",
        "last": "Villegas",
        "age": 36,
        "hobbies": [],
        "address": {
            "street": "Benito Juarez",
            "number":"22-B",
            "city": "Tijuana",
            "state": "CA",
            "zip": "123"
        }
    }
    print (me)

    print(me["first"])

    #print full name
    print(me["first"]+""+ me["last"])

    #change values
    me["age"] = me["age"] + 1
    me["age"]=99

    #add new keys
    me["preferred_color"] = "gray"

    #read if exist
    if "middle_name" in me:#checks for existence
        print(me["middle_name"])

    address = me["address"]
    print("---------- address ---------")
    print(address)
    print(type(address))

    print(f'{address["street"]}#{address["number"]}, {address["city"]}, {address["state"]}, {address["zip"]}')
    
run_test()