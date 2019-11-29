#!/usr/bin/env python3
from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("Build Routing Config")



submitbutton =Button(window, text="Submit",fg="white",bg='black', relief="groove", font=("arial",12))
submitbutton.place(x=110,y=110)
window.mainloop()
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


buildingroute = BuildingRouting.from_input()

BuildingRouting.buildingroutingvlan(buildingroute)





