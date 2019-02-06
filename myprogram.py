import string

def list_ifname_ip():
    mydict = dict()
    myfile = open("running-config.cfg","r")
    counter = 0
    for my in myfile:
        mywhi = my.strip()
        if "ip address" in mywhi:
            if "no ip address" not in mywhi:
                mylist = mywhi.split()
                ip = mylist[2]
                mask = mylist[3]
                key = "nameif" + str(counter)
                counter += 1
                com = "(" + str(ip) + "," + str(mask) + ")"
                mydict[key] = com 
    return mydict 
         
def replace_str():
    myfile = open("running-config.cfg","r")
    newfile = open("running-config-new.cfg","w")
    for my in myfile:
        mylist = my.split()
        if "255.255.0.0" in my:
            line = my.replace("255.255.0.0","255.255.255.0")
            newfile.write(line)
        elif "172" in my:
            line = my.replace("172","10")
            newfile.write(line)
        elif "192" in my:
            line = my.replace("192","10")
            newfile.write(line)
        else:
            newfile.write(my)
#      newfile.close() 

print(list_ifname_ip())
replace_str()
