import string

def list_ifname_ip():
    mydict = dict()
    myfile = open("running-config.cfg","r")
   # mydict["nameif"] = {}
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
    print(mydict)

list_ifname_ip()
