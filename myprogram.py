import string

def list_ifname_ip():
    mydict = dict()
    myfile = open("running-config.cfg","r")
    for my in myfile:
        print(my.strip())


list_ifname_ip()
