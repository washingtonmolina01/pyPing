'''
This program is basic ping function to ping your Nodes.
I used the icmplib
please refer to https://pypi.org/project/icmplib for information on the library
For istallation of the library
    sudo pip3 install icmplib
    sudo pip3 install --upgrade icmplib

I used Linux Lubunto for this code. Code needs to be run with Root privileges, feel free to make any changes as you wish
'''

from icmplib import multiping
print("Welcome...Let's try to ping your hosts:\n")

# it ask the user how many host wants to ping
try:
    totalHosts = int(input("How many host you would like to test for connectivity? "))
# This is an index variable where all the host are going to be saved
    totalhost=[]
# This loop will repeat to collect all hosts information. The host information is saved
# in the totalhost[index] variable
    for i in range(totalHosts):
        Nodes = str(input("Please enter the host name or IP address: "))
        totalhost.insert(i,Nodes)
        #Here is where the lybrary take over the code and try to ping the hosts
    hosts = multiping(totalhost)
    for host in hosts:
        if host.is_alive:
            #print(f"We are trying to ping: {host.address}")
            print(f"host {host.address} is alive")
            continue
        else:
            print(f"host {host.address} is dead")
except:
    print("Please enter a valid number... Good Bye")
