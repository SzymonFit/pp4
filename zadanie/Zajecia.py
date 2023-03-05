class Zajecia():
    
    def __init__(self):
        self.students = []
    
    
    def addStudent(self, newStudent):
        if len(self.students) < 10:
            self.students.append(newStudent)
            return True
        else:
            return False
        
z1 = Zajecia()

z1.addStudent("Jan")
z1.addStudent("Mateusz")
z1.addStudent("Olga")
z1.addStudent("Julia")
z1.addStudent("Szymon")
z1.addStudent("Klaudia")
z1.addStudent("Marek")
z1.addStudent("Krzysztof")
z1.addStudent("Aneta")
z1.addStudent("Izabela")
z1.addStudent("Katarzyna")
z1.addStudent("Iwona")
z1.addStudent("Filip")
print(z1.students)
z1.addStudent("Michał")
print(z1.students)
