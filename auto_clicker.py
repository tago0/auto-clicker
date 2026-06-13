import time
import pyautogui
from pynput.keyboard import Controller, Key
import pygetwindow as gw
import random

# ── Configuration ──────────────────────────────────────────
INTERVAL_SECONDS = 300      # Intervalle entre chaque action (en secondes) - 300 = 5 min
ROBLOX_WINDOW_NAME = "Roblox"  # Nom de la fenêtre Roblox
# ───────────────────────────────────────────────────────────

pyautogui.FAILSAFE = True   # Déplacer la souris en haut à gauche pour stopper d'urgence

keyboard = Controller()  # Clavier virtuel robuste
running = True
click_count = 0

def countdown(seconds):
    """Affiche un compte à rebours dans le terminal."""
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"\r  ⏱  Prochain appui dans : {mins:02d}:{secs:02d}   ", end="", flush=True)
        time.sleep(1)
        if not running:
            break
    print()

def focus_roblox_window():
    """Essaye de mettre la fenêtre Roblox au premier plan."""
    try:
        # Cherche toutes les fenêtres ouvertes
        all_windows = gw.getAllWindows()
        
        # Cherche Roblox (essaye plusieurs variations)
        roblox_variants = ["Roblox", "ROBLOX", "roblox", "PlayerAuthToken"]
        for variant in roblox_variants:
            roblox_windows = [w for w in all_windows if variant.lower() in w.title.lower()]
            if roblox_windows:
                window = roblox_windows[0]
                print(f"  🎮 Fenêtre trouvée : {window.title}")
                window.activate()
                time.sleep(0.5)
                return True
        
        print(f"  ⚠️  Fenêtres disponibles : {[w.title[:30] for w in all_windows[:5]]}")
        return False
    except Exception as e:
        print(f"  ⚠️  Erreur : {e}")
        return False

def random_action():
    """Effectue une action aléatoire pour éviter AFK."""
    actions = [
        ("Espace", lambda: (keyboard.press(Key.space), time.sleep(0.05), keyboard.release(Key.space))),
        ("W", lambda: (keyboard.press('w'), time.sleep(0.1), keyboard.release('w'))),
        ("A", lambda: (keyboard.press('a'), time.sleep(0.1), keyboard.release('a'))),
        ("D", lambda: (keyboard.press('d'), time.sleep(0.1), keyboard.release('d'))),
        ("S", lambda: (keyboard.press('s'), time.sleep(0.1), keyboard.release('s'))),
        ("Souris", lambda: pyautogui.moveTo(pyautogui.position()[0] + random.randint(-50, 50), 
                                            pyautogui.position()[1] + random.randint(-50, 50), duration=0.3)),
        ("Clic", lambda: pyautogui.click()),
    ]
    
    action_name, action_func = random.choice(actions)
    action_func()
    return action_name

def auto_clicker():
    global click_count, running
    interval_seconds = INTERVAL_SECONDS

    print("=" * 50)
    print("   🎮 Anti-AFK Roblox  —  Actions Aléatoires")
    print("=" * 50)
    print(f"  Intervalle : {INTERVAL_SECONDS // 60} minute(s)")
    print("  Actions    : Aléatoires (W, A, S, D, Espace, Souris, Clic)")
    print("  Arrêter    : Ctrl+C  ou  souris coin haut-gauche")
    print("=" * 50)
    print("\n  ⏳ Mettez Roblox en focus...")
    
    # Délai de démarrage pour que l'utilisateur mette Roblox en focus
    time.sleep(3)

    try:
        while running:
            # Met Roblox au premier plan avant chaque action
            focus_roblox_window()
            
            countdown(interval_seconds)
            if not running:
                break
            
            # Met à nouveau au premier plan avant d'agir
            focus_roblox_window()
            
            # Effectue une action aléatoire
            action_name = random_action()
            time.sleep(0.2)
            
            click_count += 1
            now = time.strftime("%H:%M:%S")
            print(f"  ✅ [{now}]  Action : {action_name}  (total : {click_count})")
    except KeyboardInterrupt:
        pass
    finally:
        running = False
        print(f"\n  Arrêté. Actions effectuées : {click_count}")

if __name__ == "__main__":
    auto_clicker()
