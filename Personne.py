class Personne:
    def __init__(self,id,dateNaissance,ville,prenom,nom):
        self.id = id
        self.dateNaissance = dateNaissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
    
    def __str__(self):
        return f"Personne(id={self.id}, dateNaissance={self.dateNaissance}, ville={self.ville}, prenom={self.prenom}, nom={self.nom})"


class Eleve(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom,classe):
        super().__init__(id, dateNaissance, ville, prenom,nom)
        self.classe = classe

    def __str__(self):
        return f"Eleve(classe={self.classe}, {super().__str__()})"


class Professeur(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom,vacant):
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.vacant = vacant

    def __str__(self):
        return f"Professeur(vacant={self.vacant}, {super().__str__()})"
