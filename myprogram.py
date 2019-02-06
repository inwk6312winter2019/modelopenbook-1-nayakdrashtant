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

def create_list():
    myfile = open("running-config.cfg","r")
    transit_access_in = []
    fw_management_access_in = []
    global_access = []
    for my in myfile:
        if "transit_access_in" in my:
            my = my.strip()
            transit_access_in.append(my)
        if "fw-management_access_in" in my:
            my = my.strip()
            fw_management_access_in.append(my)
        if "global_access" in my:
            my = my.strip()
            global_access.append(my)

    print("\ntransit_access list:",transit_access_in)
    print("\nfw_management_list:",fw_management_access_in)
    print("\nglobal_access list:",global_access)

print(list_ifname_ip())
replace_str()
create_list()
