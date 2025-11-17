from plateau import Plateau

class Joueur:
    """Représente un joueur de Monopoly"""
    def __init__(self, nom: str, argent_initial: int = 1500):
        self.nom = nom
        self.argent = argent_initial
        self.position = 38
        self.en_prison = False
        self.tours_en_prison = 0
        self.est_en_faillite = False

    def deplacer(self, nombre_cases: int, plateau_taille: int = 40):
        """Déplace simplement le joueur"""
        self.position = self.position + nombre_cases
        if self.position >= 40:
            self.argent += 200
            print(f"{self.nom} gagne 200€, il a donc {self.argent}€")
        self.position = self.position % plateau_taille
        print(f"{self.nom} avance de {nombre_cases} cases → Case {self.position}")
