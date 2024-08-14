class Utilisateur():
    def __init__(self,identifiant, motDePasse):
        self.identifiant = identifiant
        self.motDePasse = motDePasse
    
    def connex(self):
        return(f"Utilisateur(identifiant={self.identifiant},motDePasse={self.motDePasse} )")
        """if self.identifiant == "admin" and self.motDePasse == "admin":
            return True
        else:
            return False"""
        