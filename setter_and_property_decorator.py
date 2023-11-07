class Employee:
    def __init__(self, fname, lname, mail):
        self.fname = fname
        self.lname = lname
        #self.mail = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def printemail(self):
        return f"{fname}.{lname}@gmail.com"

id_101 = Employee("Nikita", "Bansal")
id_102 = Employee("Namrata", "Gupta")
print(id_101.explain())    