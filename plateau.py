from typing import List, Optional
from enum import Enum
from abc import ABC, abstractmethod

class Plateau:
    """Représente le plateau de jeu Monopoly"""
    def __init__(self):
        self.cases: List[Case] = []
        self._creer_plateau()
    
    def _creer_plateau(self):
        """Crée les 40 cases du plateau Monopoly"""
        # TODO SÉANCE 1: Créer les cases du plateau
        # Version simplifiée pour démarrer:
        self.cases.append(CaseDepart(0))
        self.cases.append(Propriete("Boulevard de Belleville", 1, 60, 2, "marron"))
        self.cases.append(CaseCaisse(2))
        self.cases.append(Propriete("Rue Lecourbe", 3, 60, 4, "marron"))
        self.cases.append(CaseTaxe("Impot sur le revenue", 4, 200))
        self.cases.append(Gare("Gare Montparnasse", 5, 200, 25))
        self.cases.append(Propriete("Rue de Vaugirard", 6, 100, 6, "bleu clair"))
        self.cases.append(CaseChance(7))
        self.cases.append(Propriete("Rue de Courcelles", 8, 100, 6, "bleu clair"))
        self.cases.append(Propriete("Avenue de la République", 9, 120, 8, "bleu clair"))
        self.cases.append(CasePrison(10))
        self.cases.append(Propriete("Boulevard de la Villette", 11, 140, 10, "rose"))
        self.cases.append(Propriete("Compagnie de Distribution d'Électricité", 12, 150, 0, "service"))
        self.cases.append(Propriete("Avenue de Neuilly", 13, 140, 10, "rose"))
        self.cases.append(Propriete("Rue de Paradis", 14, 160, 12, "rose"))
        self.cases.append(Gare("Gare de Lyon", 15, 200, 25))
        self.cases.append(Propriete("Avenue Mozart", 16, 180, 14, "orange"))
        self.cases.append(CaseCaisse(17))
        self.cases.append(Propriete("Boulevard Saint-Michel", 18, 180, 14, "orange"))
        self.cases.append(Propriete("Place Pigalle", 19, 200, 16, "orange"))
        self.cases.append(CaseParc(20))
        self.cases.append(Propriete("Avenue Matignon", 21, 220, 18, "rouge"))
        self.cases.append(CaseChance(22))
        self.cases.append(Propriete("Boulevard Malesherbes", 23, 220, 18, "rouge"))
        self.cases.append(Propriete("Avenue Henri-Martin", 24, 240, 20, "rouge"))
        self.cases.append(Gare("Gare du Nord", 25, 200, 25))
        self.cases.append(Propriete("Faubourg Saint-Honoré", 26, 260, 22, "jaune"))
        self.cases.append(Propriete("Place de la Bourse", 27, 260, 22, "jaune"))
        self.cases.append(Propriete("compagnie des eaux", 28, 150, 0, "service"))
        self.cases.append(Propriete("Rue La Fayette", 29, 280, 24, "jaune"))
        self.cases.append(CaseAllezPrison(30))
        self.cases.append(Propriete("Avenue de Breteuil", 31, 300, 26, "vert"))
        self.cases.append(Propriete("Avenue Foch", 32, 300, 26, "vert"))
        self.cases.append(CaseCaisse(33))
        self.cases.append(Propriete("Boulevard des Capucines", 34, 320, 28, "vert"))
        self.cases.append(Gare("Gare Saint-Lazare", 35, 200, 25))
        self.cases.append(CaseChance(36))
        self.cases.append(Propriete("Avenue des Champs-Élysées", 37, 350, 35, "bleu foncé"))
        self.cases.append(CaseTaxe("Taxe de Luxe", 38, 100))
        self.cases.append(Propriete("Rue de la Paix", 39, 400, 50, "bleu foncé"))

    
    def get_case(self, position: int) -> 'Case':
        """Retourne la case à une position donnée"""
        return self.cases[position % len(self.cases)]

class Case:
    """Classe de base pour toutes les cases du plateau"""
    def __init__(self, nom: str, position: int):
        self.nom = nom
        self.position = position
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        """Action exécutée quand un joueur arrive sur la case"""
        pass

class Propriete(Case):
    """Case représentant une propriété achetable"""
    def __init__(self, nom: str, position: int, prix: int, loyer: int, couleur: str):
        super().__init__(nom, position)
        self.prix = prix
        self.loyer_base = loyer
        self.couleur = couleur
        self.proprietaire: Optional['Joueur'] = None
        self.nb_maisons = 0
        self.a_hotel = False
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        """Action lorsqu'un joueur arrive sur une propriété"""
        if self.proprietaire is None:
            joueur.acheter_propriete(self)
            self.proprietaire = joueur
            return
        elif self.proprietaire == joueur:
            print(f"{joueur.nom} est arrivé sur sa propre propriété {self.nom}.")
            return
        else:
            loyer = self.calculer_loyer()
            joueur.payer_loyer(loyer)
            self.proprietaire.recevoir_argent(loyer)
            print(f"{joueur.nom} paye {loyer}€ de loyer à {self.proprietaire.nom}. il lui reste {joueur.argent}€.")
    
    def calculer_loyer(self) -> int:
        return self.loyer_base

class Gare(Propriete):
    """Case représentant une gare"""
    def __init__(self, nom: str, position: int, prix: int, loyer: int):
        super().__init__(nom, position, prix, loyer, "Gare")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        if self.proprietaire is None:
            joueur.acheter_propriete(self)
            self.proprietaire = joueur
            return
        elif self.proprietaire == joueur:
            print(f"{joueur.nom} est arrivé sur sa propre propriété {self.nom}.")
            return
        else:
            loyer_gare = self.calculer_loyer()
            joueur.payer_loyer(loyer_gare)
            self.proprietaire.recevoir_argent(loyer_gare)
            print(f"{joueur.nom} paye {loyer_gare}€ de loyer à {self.proprietaire.nom}. il lui reste {joueur.argent}€.")
    
    
    def calculer_loyer(self) -> int:
        if self.proprietaire is None:
            return 0 

        nb_gares = sum(
            1 for p in self.proprietaire.proprietes
            if isinstance(p, Gare)
        )

        if nb_gares == 1:
            return 25
        elif nb_gares == 2:
            return 50
        elif nb_gares == 3:
            return 100
        elif nb_gares == 4:
            return 200
        return 0

class CaseSpeciale(Case, ABC):
    """Cases comme Départ, Prison, Taxe, etc."""
    def __init__(self, nom: str, position: int, type_case: str):
        super().__init__(nom, position)
        self.type_case = type_case
    
    @abstractmethod
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        pass

class CaseDepart(CaseSpeciale):
    def __init__(self, position: int = 0):
        super().__init__("Départ", position, "depart")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        joueur.recevoir_argent(200)

class CasePrison(CaseSpeciale):
    def __init__(self, position: int = 10):
        super().__init__("Prison", position, "prison")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        print(f"{joueur.nom} est juste de passage en Prison.")

class CaseTaxe(CaseSpeciale):
    def __init__(self,nom: str, position: int = 38, montant: int = 100):
        super().__init__(nom, position, "taxe")
        self.montant = montant
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        joueur.argent -= self.montant
        print(f"{joueur.nom} paie une taxe de {self.montant}€. Il lui reste {joueur.argent}€.")

class CaseAllezPrison(CaseSpeciale):
    def __init__(self, position: int = 30):
        super().__init__("Allez en Prison", position, "allez_prison")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        joueur.aller_en_prison()

class CaseChance(CaseSpeciale):
    def __init__(self, position: int):
        super().__init__("Chance", position, "chance")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        print(f"{joueur.nom} tire une carte Chance. (Action non implémentée)")
    
class CaseCaisse(CaseSpeciale):
    def __init__(self, position: int):
        super().__init__("Caisse de communauté", position, "caisse")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        print(f"{joueur.nom} tire une carte Caisse de Communauté. (Action non implémentée)")

class CaseParc(CaseSpeciale):
    def __init__(self, position: int = 20):
        super().__init__("Parc Gratuit", position, "parc")
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        print(f"{joueur.nom} est sur le Parc Gratuit. Rien ne se passe.")


class TypeCase(Enum):
    DEPART = "depart"
    PRISON = "prison"
    TAXE = "taxe"
    Impot = "impot"
    CHANCE = "chance"
    CAISSE = "caisse"
    PARC = "parc"
    ALLEZ_PRISON = "allez_prison"