#!/usr/bin/env python3


#Build out building vlans.


class BuildingRouting:
    def __init__(self, buildingdes, buildingvlanid, buildingvlanip):
        self.buildingdes = buildingdes
        self.buildingvlanid = buildingvlanid
        self.buildingvlanip = buildingvlanip

    def buildingroutingvlan(self):
        print('My building is ' + self.buildingdes + ' My vlan is:  ' + self.buildingvlanid + ' My building IP is: ' + self.buildingvlanip)

    @classmethod
    def from_input(cls):
        return cls(
            buildingdes = input('Enter Building Description: '),
            buildingvlanid = input('Enter Building VLAN: '),
            buildingvlanip = input('Please enter the building vlan IP:')
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
