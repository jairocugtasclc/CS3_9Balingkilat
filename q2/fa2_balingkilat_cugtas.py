'''
Jairo Vincent M. Cugtas
9 - Balingkilat
22/10/26
CS3 Q2 FA2
'''

# classes
class Patient:
    name = ""
    bill_amount = 0.0

    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = float(bill_amount)

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, value):
        if value > 0:
            self.bill_amount = value

    def calculate_bill(self, original_bill=None):
        if original_bill == None:
            original_bill = self.bill_amount
        else:
            original_bill = original_bill
        self.bill_amount = self.bill_amount
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{original_bill:.2f}")
        print(f"Final Bill: ₱{self.bill_amount:.2f}")


class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.bill_amount = bill_amount - (bill_amount * 0.20)


class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.bill_amount = bill_amount - (bill_amount * 0.15)


# set values
patient1 = Patient("Max Verstappen", 15000)
patient2 = Senior_Patient("Fernando Alonso", 15000)
patient3 = PhilHealth_Patient("Lewis Hamilton", 15000)

patient4 = Patient("Kimi Antonelli", 19500)  # additional stuff
patient5 = Senior_Patient("Charles Leclerc", 67670)
patient6 = PhilHealth_Patient("Michael Schumacher", 5330)


# main code
print("Hospital Billing System")
print("-----------------------")

patient1.calculate_bill(15000)
print("")
patient2.calculate_bill(15000)
print("")
patient3.calculate_bill(15000)
print("")
patient4.calculate_bill(19500)
print("")
patient5.calculate_bill(67670)
print("")
patient6.calculate_bill(5330)
