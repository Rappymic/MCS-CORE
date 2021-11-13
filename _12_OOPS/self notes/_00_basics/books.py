class Books:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def info(self):
        return f"{self.name} is a book of '{self.subject}' and written by {self.author}"

core_python = Books("Core Python Programming", "Computer science", "Nageshwara rao")
rs_maths = Books("Introduction to Mathematics", "Mathematics", "RS Agarwal")

print(core_python.info())
print(rs_maths.info())