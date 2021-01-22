class student:
    def __init__(self, age, prenom, nom, ects_obtenu, bloc1, cycle):
        self.age = age
        self.prenom = prenom
        self.email = prenom + '.' + nom + '@student.uliege.be'
        self.nom = nom
        self.ects_obtenu = ects_obtenu
        self.bloc1 = bloc1
        self.cycle = cycle
        
    
    def proba_reussite(self): 
        pr = (self.age/self.ects_obtenu)
        return pr 
        
    
s932810 = student(20, 'John', 'Smith', 30, True, 'bachelier')
s493304 = student(22, 'Jane', 'Doe', 30, False, 'Master')