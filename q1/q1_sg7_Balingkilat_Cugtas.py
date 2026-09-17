'''
#10 - Cugtas, Jairo Vincent M.
September 10, 2026
'''

class Glassware:
    def __init__(self, type: str):
        self.type = type

class Beaker(Glassware):
    def __init__(self, type: str):
        Glassware.__init__(self, type)
        
class Tray:
    def __init__(self, type: str):
        self.beakers = [Beaker(type) for i in range(5)]
    def __del__(self):
        print("The Tray has been deleted")

my_tray = Tray("Glass")
print("Number of beakers in tray:", {len(my_tray.beakers)})
del my_tray
print("Number of beakers in tray:", {len(my_tray.beakers)})
