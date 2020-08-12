class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set! please set it using setter."

        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print('Setting now...')
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


anindo_dey = Employee("Anindo", "Dey")

print(anindo_dey.email)
anindo_dey.fname = "BB"

print(anindo_dey.email)

# email setter
anindo_dey.email = "this.that@gmail.com"
print(anindo_dey.email)

# email deleter
del anindo_dey.email

print(anindo_dey.email)

