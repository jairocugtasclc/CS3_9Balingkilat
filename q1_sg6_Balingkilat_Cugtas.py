'''
Cugtas, Jairo Vincent M.
9 - Balingkilat
09/03/26
SG6: Challenge 1: The Lab Manager Mission
'''

class Technician:
    def __init__(self,name,assigned_lab=None):
        self.name = name
        self.assigned_lab = assigned_lab
    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj
    
        
    

class Lab:
    def __init__(self, room_number):
        self.room_number = room_number


#testing

chem_lab = Lab("Room 302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(f"Technician {mr_cruz.name} is accessing: {mr_cruz.assigned_lab.room_number}.")
