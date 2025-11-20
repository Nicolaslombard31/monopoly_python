from plateau import Propriete, Plateau

class Joueur:
    def __init__(self, nom: str, plateau: Plateau, argent_initial: int = 1500):
        self.nom = nom
        self.argent = argent_initial
        self.position = 0
        self.en_prison = False
        self.tours_en_prison = 0
        self.est_en_faillite = False
        self.plateau = plateau  # <-- AJOUT

    def deplacer(self, nombre_cases: int, plateau_taille: int = 40):
        """Déplace simplement le joueur"""
        self.position = self.position + nombre_cases
        if self.position >= 40:
            self.plateau.get_case(0).action(self, None)
        self.position = self.position % plateau_taille
        print(f"{self.nom} avance de {nombre_cases} cases → Case {self.position}")
        case = self.plateau.get_case(self.position)
        case.action(self, None)
            
    
    def acheter_propriete(self, propriete: Propriete) -> bool:
        """Achète une propriété si le joueur a assez d'argent"""
        if self.argent < propriete.prix:
            self.est_en_faillite = True
            return False
        
        self.argent -= propriete.prix

        print(f"{self.nom} a acheté {propriete.nom} pour {propriete.prix}€. Il lui reste {self.argent}€.")
        return True
    
    def payer_loyer(self, propriete: Propriete) -> bool:
        """Paye le loyer à un autre joueur"""
        loyer = propriete.loyer_base
        if self.argent < loyer:
            self.est_en_faillite = True
            return False
        
        self.argent -= loyer
        return True
    
    def recevoir_argent(self, montant: int):
        """Reçoit de l'argent (ex: passage par la case Départ)"""
        self.argent += montant
        print(f"{self.nom} reçoit {montant}€. Il a maintenant {self.argent}€.")
    
    def aller_en_prison(self):
        """Met le joueur en prison"""
        self.en_prison = True
        self.position = 10  # Position de la case Prison
        self.tours_en_prison = 0
        print(f"{self.nom} va en Prison!")
    
    def possede_quartier_entier(self, couleur: str) -> bool:
        """Vérifie si le joueur possède toutes les propriétés d'une couleur donnée"""
        
        pass