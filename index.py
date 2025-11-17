import random
from typing import List
from joueurs import Joueur
from plateau import Plateau

class Monopoly:
    """Classe principale qui gère une partie de Monopoly"""
    def __init__(self, noms_joueurs: List[str]):
        self.plateau = Plateau()
        self.joueurs = [Joueur(nom) for nom in noms_joueurs]
        self.joueur_actuel_index = 0
        self.tour_numero = 0
    
    def lancer_des(self) -> tuple:
        """Lance deux dés et retourne les valeurs"""
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        return de1, de2
    
    def jouer_tour(self, joueur: Joueur):
        """Joue un tour complet pour un joueur"""
        # TODO SÉANCE 2: Implémenter la logique complète d'un tour
        print(f"\n--- Tour de {joueur.nom} ---")
        print(f"Position: {joueur.position}, Argent: {joueur.argent}€")
        
        de1, de2 = self.lancer_des()
        total = de1 + de2
        print(f" Dés: {de1} + {de2} = {total}")
        joueur.deplacer(total)
        pass

game = Monopoly(["Alice", "Bob"])

joueur = game.jouer_tour(game.joueurs[0])
