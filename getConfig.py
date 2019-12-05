#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import sys


root = Tk()
root.title("Vlan Config Helper")
content = ttk.Frame(root, padding=(10,10,120,120))

buildingsubnet =''
buildingdes =''
buildingvlanip =''
buildingvlanid =''
buildinggateway =''


# Build out the form
bvldeslbl = ttk.Label(content, text="Enter Building Vlan Description: ")
bdes = ttk.Entry(content, textvariable=buildingdes)
#buildingdes = bdes.get()

bvlidlbl = ttk.Label(content, text="Enter Building Vlan Id: ")
bvlanid = ttk.Entry(content, textvariable=buildingvlanid)
#buildingvlanid = bvlanid.get()

bvliplbl = ttk.Label(content, text="Enter Building Vlan IP: ")
bvlanip = ttk.Entry(content, textvariable=buildingvlanip)
#buildingvlanip = bvlanip.get()

bvlsnlbl = ttk.Label(content, text="Enter Building Vlan subnet: ")
bsubnet = ttk.Entry(content, textvariable=buildingsubnet)
#buildingsubnet = bsubnet.get()

bvlgwlbl = ttk.Label(content, text="Enter Building Vlan gateway: ")
bgateway = ttk.Entry(content, textvariable=buildinggateway)
#buildinggateway = bgateway.get()




def closeWindow():
    exit()

BuildingRouting.from_input = ['buildingsubnet', 'buildingdes', 'buildingvlanip', 'buildingvlanid', 'buildinggateway']


submit = ttk.Button(content, text="Submit", command=BuildingRouting.from_input())

#Cancel Button Works ----- dont invoke the function...
cancel =ttk.Button(content, text="Cancel", command=closeWindow)
# Do not Change


#setting up the Grid
content.grid(column=0, row=0, sticky=(N, S, E, W))

bvldeslbl.grid(column=1, row=1, columnspan=1, sticky=(N, W), padx=5)
bdes.grid(column=2, row=1, columnspan=2, sticky=(N, S, E, W), pady=5, padx=5)

bvlidlbl.grid(column=1, row=2, columnspan=1, sticky=(N, W), padx=5)
bvlanid.grid(column=2, row=2, columnspan=2, sticky=(N, S, E, W), pady=5, padx=5)

bvliplbl.grid(column=1, row=3, columnspan=1, sticky=(N, W), padx=5)
bvlanip.grid(column=2, row=3, columnspan=2, sticky=(N, S, E, W), pady=5, padx=5)

bvlsnlbl.grid(column=1, row=4, columnspan=1, sticky=(N, W), padx=5)
bsubnet.grid(column=2, row=4, columnspan=2, sticky=(N, S, E, W), pady=5, padx=5)

bvlgwlbl.grid(column=1, row=5, columnspan=1, sticky=(N, W), padx=5)
bgateway.grid(column=2, row=5, columnspan=2, sticky=(N, S, E, W), pady=5, padx=5)

submit.grid(column=3, row=6)
cancel.grid(column=4, row=6)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.columnconfigure(5, weight=3)
content.columnconfigure(6, weight=3)
content.rowconfigure(1, weight=1)

#Build out building vlans.


class BuildingRouting:
    def __init__(self, buildingdes, buildingvlanid, buildingvlanip, buildingsubnet,buildinggateway):
        self.buildingdes = buildingdes
        self.buildingvlanid = buildingvlanid
        self.buildingvlanip = buildingvlanip
        self.buildingsubnet = buildingsubnet
        self.buildinggateway = buildinggateway

    def buildingroutingvlan(self):
         with open("mycommands.txt", "w") as f:
            f.write('interface Vlan ' + self.buildingvlanid + '\n')
            f.write(' description ' + self.buildingdes + '\n')
            f.write(' vrf forwarding XXXX\n')
            f.write(' ip address ' + self.buildingvlanip + ' ' + self.buildingsubnet + '\n')
            f.write(' ip helper-address 4.4.4.4\n')
            f.write(' ip helper-address 8.8.8.8\n')
            f.write(' no ip redirects\n')
            f.write(' ip pim passive\n')
            f.write(' standby version 2\n')
            f.write(' standby ' + self.buildingvlanid + ' ip ' + self.buildinggateway + '\n')
            f.write(' standby ' + self.buildingvlanid + ' priority 250\n')
            f.write(' standby ' + self.buildingvlanid + ' preempt\n')
            f.write(' standby ' + self.buildingvlanid + ' authentication md5 key-string nice-auth\n')
            f.write(' ip ospf xxxx area 1.2.3.4\n')
            f.write(' shutdowm\n')
            f.close()

    @classmethod
    def from_input(cls):
        return cls(
            buildingdes = bdes.get(),
            buildingvlanid = bvlanid.get(),
            buildingvlanip = bvlanip.get(),
            buildingsubnet = bsubnet.get(),
            buildinggateway = bgateway.get()
       )


# class Buildingvoip:
#     def __init__(self, buildingvlandes, vlanid):
#         self.buildingname = buildingnameBlue
#         self.vlanid = vlanid

#     def myfunc(self):
#         print('My building is ' + self.name + 'my vlan is ' + self.vlanid) 



#Build out OSPF Routing

class TN2routing:
    pass

class VoIProuting:
    pass

class Camerarouting:
    pass




print =(BuildingRouting.buildingroutingvlan())





root.mainloop()




