# 🎮 Roblox Anti-AFK

**Auteur :** tago0_

Un script Python simple et efficace pour éviter d'être kické pour AFK (inactivité) sur Roblox.

## 📋 Fonctionnalités

- ✅ Actions **aléatoires** toutes les 5 minutes
- ✅ Simule une activité humaine naturelle
- ✅ Actions disponibles : Espace, W, A, S, D, mouvement souris, clic souris
- ✅ Détection automatique de la fenêtre Roblox
- ✅ Arrêt d'urgence : souris en haut à gauche ou Ctrl+C
- ✅ Affichage du compte à rebours en temps réel

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

1. **Cloner le repo**
   ```bash
   git clone https://github.com/ton-username/roblox-anti-afk.git
   cd roblox-anti-afk
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv .venv
   ```

3. **Activer l'environnement virtuel**
   - Windows (PowerShell) :
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows (CMD) :
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - Linux/Mac :
     ```bash
     source .venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dépendances

- `pyautogui` - Contrôle de la souris
- `pynput` - Contrôle du clavier
- `pygetwindow` - Gestion des fenêtres

## 🎮 Utilisation

### Méthode 1 : Directement
```bash
python auto_clicker.py
```

### Méthode 2 : Avec l'environnement virtuel
```bash
.\.venv\Scripts\python.exe auto_clicker.py
```

### Méthode 3 : Avec run.bat (Windows)
```bash
run.bat
```

## ⚙️ Configuration

Ouvrez `auto_clicker.py` et modifiez :

```python
INTERVAL_SECONDS = 300      # Intervalle en secondes (300 = 5 minutes)
```

**Exemples :**
- 10 secondes : `INTERVAL_SECONDS = 10`
- 2 minutes : `INTERVAL_SECONDS = 120`
- 5 minutes : `INTERVAL_SECONDS = 300`

## ⚠️ Important

- **Vérifiez les conditions d'utilisation** de votre serveur Roblox
- Ce script est fourni **à titre éducatif**
- L'auteur n'est **pas responsable** des bans ou sanctions
- Utilisez à vos **propres risques**

## 🛑 Comment arrêter

- Appuyez sur **Ctrl+C** dans le terminal
- Ou déplacez la souris vers le **coin haut-gauche** de l'écran

## 📝 Notes

- Le script essaie automatiquement de mettre Roblox au premier plan
- Les actions sont complètement **aléatoires** pour éviter la détection
- Un délai de 3 secondes au démarrage pour que vous mettez Roblox en focus

## 💡 Tips

- Laissez le script tourner en fond pendant que vous jouez normalement
- Plus naturel que simplement appuyer sur Espace toutes les 5 min
- Fonctionne avec n'importe quel jeu Roblox

## 📄 Licence

MIT - Libre d'utilisation

---

**Créé par :** tago0_
**Dernière mise à jour :** 2026-06-13
