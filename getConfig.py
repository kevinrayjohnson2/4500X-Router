#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import sys


root = Tk()
root.title("Vlan Config Helper")
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
bvlidlbl = ttk.Label(content, text="Enter Building Vlan")
buildingvlanid = ttk.Entry(content)

def closeWindow():
    exit()

ok = ttk.Button(content, text="Okay")
ok.invoke()

cancel = ttk.Button(content, text="Cancel")
cancel.invoke()

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
bvlidlbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
buildingvlanid.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
root.mainloop()
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
            f.write(' standby ' + self.buildingvlanid + ' ip ' + self.Housebuildinggateway + '\n')
            f.write(' standby ' + self.buildingvlanid + ' priority 250\n')
            f.write(' standby ' + self.buildingvlanid + ' preempt\n')
            f.write(' standby ' + self.buildingvlanid + ' authentication md5 key-string nice-auth\n')
            f.write(' ip ospf xxxx area 1.2.3.4\n')
            f.write(' shutdowm\n')
            f.close()

    @classmethod
    def from_input(cls):
        return cls(
            buildingdes = input('Enter Building Description: '),
            buildingvlanid = input('Enter Building VLAN: '),
            buildingvlanip = input('Please enter the building vlan IP:'),
            buildingsubnet = input('Please enter the building subnet:'),
            buildinggateway = input('Please enter the building gateway:')
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


#buildingroute = BuildingRouting.from_input()

#BuildingRouting.buildingroutingvlan(buildingroute)





