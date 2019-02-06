import string

# 1 - Write a Python function called "list_ifname_ip" to scan the configuration and return a dictionary that contains the "nameif" as the key and "IPaddress,NetMask" tuple as the value.

def replace_my_strings(line):
    mylist = ["255.255.0.0","255.255.255.0","172","192"]
    myrepl = ["255.0.0.0","255.0.0.0","10","10"]
    for rep in range(len(mylist)):
        line = line.replace(mylist[rep],myrepl[rep])
    return line

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

# 2 - Create a new configuration file that replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." and also change the netmask from ("255.255.0.0"/"255.255.255.0") to "255.0.0.0"         
def replace_str():
    myfile = open("running-config.cfg","r")
    newfile = open("running-config-new.cfg","w")
    for my in myfile:
     #   mylist = my.split()
     #   if "255.255.0.0" in my:
     #       line = my.replace("255.255.0.0","255.0.0.0")
     #       newfile.write(line)
     #   elif "255.255.255.0" in my:
     #       line  = my.replace("255.255.255.0","255.0.0.0")
     #       newfile.write(line)
     #   elif "172" in my:
     #       line = my.replace("172","10")
     #       newfile.write(line)
     #   elif "192" in my:
     #       line = my.replace("192","10")
     #       newfile.write(line)
     #   else:
     #       newfile.write(my)
        my = replace_my_strings(my)
        newfile.write(my)
    
# 3 - Create a individual python-list of "access-list" for "transit_access_in","fw-management_access_in" and "global_access"
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
