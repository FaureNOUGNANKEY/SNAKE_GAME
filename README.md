 # 🐍 Snake Game

Un jeu Snake classique développé en Python avec la bibliothèque **Pygame**.

![Python](https://img.shields.io/badge/Python-3.13.1-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-green?logo=python&logoColor=white)
---

## 📋 Description

Ce projet est une implémentation du célèbre jeu **Snake** en Python. Le joueur contrôle un serpent qui doit manger de la nourriture pour grandir et augmenter son score, tout en évitant les murs et son propre corps.

---
<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/24c55e89-6013-424e-b066-56b8cd668fe9" />
<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/8b0979b5-db9b-4b4e-9a78-022a559bf453" />
<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/9d6df0a8-7fda-4a92-9d76-d4e72624316a" />

## 🎮 Fonctionnalités

- Déplacement fluide du serpent avec les touches directionnelles
- Génération aléatoire de la nourriture
- Détection des collisions (murs et corps du serpent)
- Affichage du score en temps réel
- Écran de Game Over avec le score final
- Possibilité de rejouer ou quitter après une partie
- Système de pause (touche `P` ou `Espace`)

---


## ⚙️ Prérequis

- Python 3.13.1
- Pygame

---

## Installation

**1. Cloner le dépôt**

```bash
git clone https://github.com/FaureNOUGNANKEY/SNAKE_GAME.git
cd snake-game
```

**2. Installer les dépendances**

```bash
pip install pygame
```

**3. Lancer le jeu**

```bash
python snake.py
```

---

## 🕹️ Contrôles

| Touche | Action |
|--------|--------|
| ⬆️ Flèche Haut | Aller vers le haut |
| ⬇️ Flèche Bas | Aller vers le bas |
| ⬅️ Flèche Gauche | Aller vers la gauche |
| ➡️ Flèche Droite | Aller vers la droite |
| `P` ou `Espace` | Mettre en pause / Reprendre |
| `R` | Rejouer après Game Over |
| `Q` | Quitter après Game Over |

---

## 📁 Structure du projet

```
snake-game/
│
├── snake.py          # Fichier principal du jeu
└── README.md         # Documentation
```

---

## 🧩 Architecture du code

Le projet est structuré autour de fonctions indépendantes :

| Fonction | Rôle |
|----------|------|
| `initialiser_pygame()` | Initialise la fenêtre Pygame |
| `initialiser_jeu()` | Crée l'état initial du jeu |
| `deplacer_serpent()` | Met à jour la position du serpent |
| `collusion_serpent()` | Détecte les auto-collisions |
| `collusion_murs()` | Détecte les collisions avec les bords |
| `generer_nourriture()` | Place la nourriture aléatoirement |
| `manger_nourriture()` | Vérifie si le serpent mange |
| `gerer_clavier()` | Gère les entrées du joueur |
| `afficher_game_over()` | Affiche l'écran de fin de partie |
| `afficher_pause()` | Affiche l'écran de pause |
| `boucle_principale()` | Boucle de jeu principale |

---

## 🛠️ Paramètres configurables

Dans le fichier `snake.py`, vous pouvez modifier les constantes suivantes :

```python
longueur    = 800   # Largeur de la fenêtre (pixels)
largeur     = 600   # Hauteur de la fenêtre (pixels)
taille_case = 20    # Taille d'une case (pixels)
fps         = 10    # Vitesse du jeu (images/seconde)
```
---

## 👤 Auteur

Développé par **NOUGNANKEY Faure dit Codeur de la jungle** — n'hésitez pas à contribuer ou signaler des bugs via les [Issues](https://github.com/FaureNOUGNANKEY/SNAKE_GAME/issues) !
