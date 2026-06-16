import os, sys, subprocess, time, re, json, urllib.request, urllib.error, shutil, tempfile, zipfile

STARTER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools', 'starter.py')

GITHUB_REPO  = 'Wumpusuhq/Wumpus-multitool'
BRANDING_URL = 'https://github.com/Wumpusuhq/Wumpus-multitool'

TOOLS_DIR  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
STAR_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'star')
THEME_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.theme')

# ══════════════════════════════════════════════════════════════
#  THÈMES
# ══════════════════════════════════════════════════════════════

THEMES = {
    'blue': {
        'name': 'Blue  ',
        'PRIMARY': ( 30, 100, 255), 'DARK':   ( 15,  50, 160),
        'ACCENT':  ( 80, 180, 255), 'LOCKED': ( 20,  40, 120),
        'STAR':    (255, 190,  60), 'WHITE':  (220, 230, 255),
        'GRAY':    ( 90,  90, 110), 'GREEN':  ( 60, 210, 130),
        'YELLOW':  (255, 190,  60), 'CYAN':   ( 80, 200, 255),
        'banner_grad': [(20, 60, 180), (30, 100, 255), (60, 140, 255)],
    },
    'red': {
        'name': 'Red   ',
        'PRIMARY': (220,  20,  60), 'DARK':   (140,  10,  30),
        'ACCENT':  (255,  80, 100), 'LOCKED': ( 90,  10,  20),
        'STAR':    (255, 190,  60), 'WHITE':  (240, 240, 240),
        'GRAY':    (110, 110, 120), 'GREEN':  ( 80, 220, 120),
        'YELLOW':  (255, 190,  60), 'CYAN':   ( 80, 220, 220),
        'banner_grad': [(90, 0, 0), (180, 10, 20), (220, 20, 60)],
    },
    'green': {
        'name': 'Green ',
        'PRIMARY': ( 20, 200,  80), 'DARK':   ( 10, 110,  40),
        'ACCENT':  ( 80, 255, 140), 'LOCKED': ( 10,  70,  30),
        'STAR':    (255, 220,  50), 'WHITE':  (210, 255, 220),
        'GRAY':    ( 80, 110,  85), 'GREEN':  ( 60, 220, 120),
        'YELLOW':  (200, 255,  80), 'CYAN':   ( 80, 255, 200),
        'banner_grad': [(10, 80, 30), (15, 140, 55), (20, 200, 80)],
    },
    'purple': {
        'name': 'Purple',
        'PRIMARY': (160,  40, 240), 'DARK':   ( 80,  15, 130),
        'ACCENT':  (200, 100, 255), 'LOCKED': ( 60,  10, 100),
        'STAR':    (255, 200,  60), 'WHITE':  (235, 215, 255),
        'GRAY':    (100,  80, 120), 'GREEN':  ( 80, 220, 150),
        'YELLOW':  (255, 200,  60), 'CYAN':   (180, 100, 255),
        'banner_grad': [(50, 10, 100), (110, 25, 180), (160, 40, 240)],
    },
    'orange': {
        'name': 'Orange',
        'PRIMARY': (255, 120,  20), 'DARK':   (160,  65,   5),
        'ACCENT':  (255, 180,  60), 'LOCKED': (100,  45,   5),
        'STAR':    (255, 240,  80), 'WHITE':  (255, 240, 220),
        'GRAY':    (120, 100,  80), 'GREEN':  ( 80, 220, 120),
        'YELLOW':  (255, 230,  60), 'CYAN':   (255, 160,  40),
        'banner_grad': [(100, 40, 5), (200, 80, 10), (255, 120, 20)],
    },
    'cyan': {
        'name': 'Cyan  ',
        'PRIMARY': ( 20, 210, 220), 'DARK':   ( 10, 110, 120),
        'ACCENT':  ( 80, 240, 250), 'LOCKED': ( 10,  70,  80),
        'STAR':    (255, 210,  50), 'WHITE':  (210, 250, 255),
        'GRAY':    ( 80, 110, 115), 'GREEN':  ( 80, 230, 160),
        'YELLOW':  (200, 255, 100), 'CYAN':   ( 60, 220, 240),
        'banner_grad': [(10, 80, 90), (15, 150, 160), (20, 210, 220)],
    },
    'white': {
        'name': 'White ',
        'PRIMARY': (200, 200, 210), 'DARK':   (130, 130, 145),
        'ACCENT':  (240, 240, 255), 'LOCKED': ( 90,  90, 100),
        'STAR':    (255, 210,  50), 'WHITE':  (245, 245, 255),
        'GRAY':    (150, 150, 160), 'GREEN':  ( 80, 220, 120),
        'YELLOW':  (255, 200,  60), 'CYAN':   (160, 200, 255),
        'banner_grad': [(130, 130, 145), (175, 175, 185), (220, 220, 230)],
    },
}

THEME_ORDER = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'white']
_T = {}

def _apply_theme(name: str):
    global _T
    _T = dict(THEMES.get(name, THEMES['blue']))

def load_theme() -> str:
    try:
        with open(THEME_FILE) as f:
            name = f.read().strip()
        if name in THEMES:
            _apply_theme(name)
            return name
    except: pass
    _apply_theme('blue')
    return 'blue'

def save_theme(name: str):
    with open(THEME_FILE, 'w') as f:
        f.write(name)

def c(text, color):
    r, g, b = color
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

_ANSI_RE = re.compile(r'\033\[[0-9;]*m')

def visible_len(text: str) -> int:
    """Longueur visible (sans les codes ANSI couleur)."""
    return len(_ANSI_RE.sub('', text))

def banner_gradient(text: str) -> str:
    grad  = _T.get('banner_grad', [(20, 60, 180), (30, 100, 255), (60, 140, 255)])
    lines = text.splitlines()
    n     = max(len(lines) - 1, 1)
    out   = ""
    for i, line in enumerate(lines):
        t_val = i / n
        if t_val <= 0.5:
            a, b_ = grad[0], grad[1]; s = t_val * 2
        else:
            a, b_ = grad[1], grad[2]; s = (t_val - 0.5) * 2
        r  = int(a[0] + (b_[0] - a[0]) * s)
        g_ = int(a[1] + (b_[1] - a[1]) * s)
        bv = int(a[2] + (b_[2] - a[2]) * s)
        out += f"\033[38;2;{r};{g_};{bv}m{line}\033[0m\n"
    return out

WHITE_FIXED = (240, 240, 240)
GREEN_FIXED = ( 80, 220, 120)
RED_FIXED   = (220,  20,  60)

BANNER = r"""
 ██╗    ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗███████╗
 ██║    ██║██║   ██║████╗ ████║██╔══██╗██║   ██║██╔════╝
 ██║ █╗ ██║██║   ██║██╔████╔██║██████╔╝██║   ██║███████╗
 ██║███╗██║██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║╚════██║
 ╚███╔███╔╝╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝███████║
  ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝
              M U L T I T O O L  v 2 . 0
"""

# ══════════════════════════════════════════════════════════════
#  HELPERS UI
# ══════════════════════════════════════════════════════════════

BOX_W  = 70
INNER  = BOX_W - 2

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    cls()
    print(banner_gradient(BANNER))
    print(c(f"  {BRANDING_URL}", _T['ACCENT']))
    _divider()
    print()

def _divider(left='', right=''):
    print(c(f"  {'─' * (BOX_W - 4)}", _T['DARK']))

def _box_top(title=''):
    if title:
        pad = (INNER - len(title) - 2) // 2
        ext = '' if (INNER - len(title) - 2) % 2 == 0 else '─'
        line = '┌' + '─' * pad + f' {title} ' + '─' * pad + ext + '┐'
    else:
        line = '┌' + '─' * INNER + '┐'
    print(c(f"  {line}", _T['PRIMARY']))

def _box_bot():
    print(c(f"  └{'─' * INNER}┘", _T['PRIMARY']))

def _box_row(text='', color=None):
    color = color or _T['WHITE']
    pad   = max(0, INNER - visible_len(text) - 1)
    print(
        c("  │", _T['PRIMARY']) +
        c(f" {text}", color) +
        ' ' * pad +
        c("│", _T['PRIMARY'])
    )

def _box_sep():
    print(c(f"  ├{'─' * INNER}┤", _T['PRIMARY']))

def ok(msg):   print(c(f"  [+] {msg}", _T['GREEN']))
def err(msg):  print(c(f"  [-] {msg}", RED_FIXED))
def info(msg): print(c(f"  [i] {msg}", _T['CYAN']))
def ask(prompt): return input(c(f"  [?] {prompt} ", _T['CYAN'])).strip().upper()

# ══════════════════════════════════════════════════════════════
#  LANGUE
# ══════════════════════════════════════════════════════════════

_COUNTRY_CACHE = None

def get_country() -> str:
    global _COUNTRY_CACHE
    if _COUNTRY_CACHE is not None: return _COUNTRY_CACHE
    try:
        req = urllib.request.Request('https://ipinfo.io/json', headers={'User-Agent': 'wumpus-launcher'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())
        _COUNTRY_CACHE = data.get('country', 'EN').upper()
    except:
        _COUNTRY_CACHE = 'EN'
    return _COUNTRY_CACHE

_LANG_MAP = {'FR': 'fr', 'BE': 'fr', 'CH': 'fr', 'CA': 'fr', 'ES': 'es', 'PT': 'pt'}

STRINGS = {
    'fr': {
        'gh_title':       'CONFIGURATION GITHUB TOKEN + STAR',
        'gh_saved':       'Token sauvegardé trouvé',
        'gh_use':         'Utiliser ce token ? (O/n) :',
        'gh_confirmed':   '⭐ Star confirmé — STAR TOOLS DÉBLOQUÉS !',
        'gh_not_starred': "Tu n'as pas encore starré le repo.",
        'gh_star_here':   '→ Mets une étoile ici :',
        'gh_paste':       'Colle ton token (vide pour annuler) :',
        'star_locked_msg':'Ce tool est réservé aux starreurs',
        'star_hint':      '☆ Star le repo pour débloquer →',
        'exit':           'Quitter',
        'enter':          'ENTRÉE pour continuer',
        'invalid':        'Numéro invalide',
        'not_a_number':   'Entre un numéro',
        'page_next':      'Page Suiv.',
        'page_prev':      'Page Préc.',
        'theme_menu':     'Changer le thème',
        'theme_title':    'CHOIX DU THÈME',
        'theme_current':  'Thème actuel',
        'theme_applied':  'Thème appliqué',
    },
    'en': {
        'gh_title':       'GITHUB TOKEN + STAR SETUP',
        'gh_saved':       'Saved token found',
        'gh_use':         'Use this token? (Y/n) :',
        'gh_confirmed':   '⭐ Star confirmed — STAR TOOLS UNLOCKED!',
        'gh_not_starred': "You haven't starred the repo yet.",
        'gh_star_here':   '→ Star it here:',
        'gh_paste':       'Paste your token (blank to cancel) :',
        'star_locked_msg':'This tool is for starrers only',
        'star_hint':      '☆ Star the repo to unlock →',
        'exit':           'Exit',
        'enter':          'ENTER to continue',
        'invalid':        'Invalid number',
        'not_a_number':   'Enter a number',
        'page_next':      'Next',
        'page_prev':      'Prev',
        'theme_menu':     'Change theme',
        'theme_title':    'THEME SELECTOR',
        'theme_current':  'Current theme',
        'theme_applied':  'Theme applied',
    }
}

def t(key: str) -> str:
    if '_LANG_CACHE' not in globals():
        lang = _LANG_MAP.get(get_country(), 'en')
        globals()['_LANG_CACHE'] = STRINGS.get(lang, STRINGS['en'])
    return globals()['_LANG_CACHE'].get(key, key)

# ══════════════════════════════════════════════════════════════
#  AUTO-UPDATE
# ══════════════════════════════════════════════════════════════

def get_remote_sha():
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/commits/main"
        req = urllib.request.Request(url, headers={'User-Agent': 'wumpus-launcher', 'Accept': 'application/vnd.github+json'})
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read().decode()).get('sha')
    except: return None

def get_local_sha():
    sha_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.last_sha')
    try:
        with open(sha_path) as f: return f.read().strip()
    except: return None

def save_local_sha(sha: str):
    sha_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.last_sha')
    with open(sha_path, 'w') as f: f.write(sha)

def download_and_apply_update(sha: str) -> bool:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_url  = f"https://github.com/{GITHUB_REPO}/archive/refs/heads/main.zip"
    info("Téléchargement de la mise à jour...")
    try:
        tmp_zip = os.path.join(tempfile.gettempdir(), 'wumpus_update.zip')
        req = urllib.request.Request(zip_url, headers={'User-Agent': 'wumpus-launcher'})
        with urllib.request.urlopen(req, timeout=30) as r, open(tmp_zip, 'wb') as f:
            shutil.copyfileobj(r, f)
    except Exception as e:
        err(f"Erreur téléchargement : {e}"); return False
    info("Application des fichiers...")
    try:
        with zipfile.ZipFile(tmp_zip, 'r') as z:
            root_in_zip = z.namelist()[0].split('/')[0] + '/'
            for member in z.namelist():
                rel  = member[len(root_in_zip):]
                if not rel: continue
                dest = os.path.join(base_dir, rel)
                if member.endswith('/'):
                    os.makedirs(dest, exist_ok=True); continue
                if os.path.normpath(dest) == os.path.normpath(os.path.abspath(__file__)): continue
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with z.open(member) as src, open(dest, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
        os.remove(tmp_zip)
    except Exception as e:
        err(f"Erreur extraction : {e}"); return False
    save_local_sha(sha)
    return True

def auto_update():
    _box_top('AUTO-UPDATE')
    _box_row(c("  Vérification des mises à jour...", _T['GRAY']))
    _box_bot()
    remote_sha = get_remote_sha()
    if not remote_sha:
        print(c("  [!] Pas de connexion — mise à jour ignorée.", _T['YELLOW']))
        time.sleep(0.8); return
    local_sha = get_local_sha()
    if local_sha == remote_sha:
        print(c("  [✓] Déjà à jour.", _T['GREEN']))
        time.sleep(0.5); return
    print(c("  [!] Nouvelle version détectée !", _T['YELLOW']))
    if download_and_apply_update(remote_sha):
        ok("Mise à jour appliquée avec succès !")
    else:
        print(c("  [!] Mise à jour échouée, lancement avec la version actuelle.", _T['YELLOW']))
    time.sleep(1)

# ══════════════════════════════════════════════════════════════
#  SCAN TOOLS
# ══════════════════════════════════════════════════════════════

def get_name(filepath):
    if filepath.endswith('.exe'):
        return os.path.splitext(os.path.basename(filepath))[0].replace("_", " ").title()
    PAT = re.compile(r'''(?x) ^ \#? \s* NAME \s* = \s* (?P<q> ["']) (.+?) (?P=q) ''')
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                m = PAT.match(line.strip())
                if m: return m.group(2).strip()
    except: pass
    return os.path.splitext(os.path.basename(filepath))[0].replace("_", " ").title()

def scan_folder(folder, is_star=False):
    if not os.path.isdir(folder): return []
    EXTS = ('.py', '.exe')
    return [
        (os.path.join(folder, f), is_star)
        for f in sorted(os.listdir(folder))
        if any(f.endswith(e) for e in EXTS) and not f.startswith('_')
    ]

# ══════════════════════════════════════════════════════════════
#  STAR CHECK
# ══════════════════════════════════════════════════════════════

_STAR_CACHE = None

def _check_star_github() -> bool:
    global _STAR_CACHE
    if _STAR_CACHE is not None: return _STAR_CACHE
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.gh_token')
    if not os.path.isfile(token_path):
        _STAR_CACHE = False; return False
    try:
        with open(token_path) as f:
            token = f.read().strip()
        if not token:
            _STAR_CACHE = False; return False
    except:
        _STAR_CACHE = False; return False
    req = urllib.request.Request(
        f"https://api.github.com/user/starred/{GITHUB_REPO}",
        headers={'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json', 'User-Agent': 'wumpus-launcher'}
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            _STAR_CACHE = (r.status == 204)
    except:
        _STAR_CACHE = False
    return _STAR_CACHE

def save_token(token):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.gh_token')
    with open(path, 'w') as f: f.write(token.strip())
    ok(f"Token sauvegardé → {path}")

# ══════════════════════════════════════════════════════════════
#  SÉLECTEUR DE THÈME
# ══════════════════════════════════════════════════════════════

def theme_selector():
    current = load_theme()
    while True:
        show_banner()
        _box_top(t('theme_title'))
        _box_row()
        _box_row(f"  {t('theme_current')} : {THEMES[current]['name'].strip().upper()}", _T['ACCENT'])
        _box_row()
        _box_sep()
        _box_row()
        for i, key in enumerate(THEME_ORDER, 1):
            th     = THEMES[key]
            swatch = c("██", th['PRIMARY']) + c("█", th['ACCENT']) + c("█", th['STAR'])
            marker = c("  ◄ actif", _T['GREEN']) if key == current else ""
            row    = f"  [{i}]  {swatch}  {th['name'].strip():<8}{marker}"
            _box_row(row)
        _box_row()
        _box_row(f"  [0]  Retour", _T['GRAY'])
        _box_row()
        _box_bot()
        print()
        choice = ask("Thème >>")
        if choice == '0': return
        try:
            n = int(choice)
            if 1 <= n <= len(THEME_ORDER):
                chosen = THEME_ORDER[n - 1]
                _apply_theme(chosen)
                save_theme(chosen)
                current = chosen
                ok(f"{t('theme_applied')} : {THEMES[chosen]['name'].strip()}")
                time.sleep(0.5)
            else:
                err(t('invalid')); time.sleep(0.4)
        except ValueError:
            err(t('not_a_number')); time.sleep(0.4)

# ══════════════════════════════════════════════════════════════
#  GITHUB SETUP
# ══════════════════════════════════════════════════════════════

def github_setup():
    global _STAR_CACHE
    show_banner()
    _box_top(t('gh_title'))
    _box_row()
    _box_row("  1. Mets une ★ sur le repo (obligatoire)", _T['WHITE'])
    _box_row(f"     https://github.com/{GITHUB_REPO}", _T['STAR'])
    _box_row()
    _box_row("  2. Va sur   https://github.com/settings/tokens", _T['WHITE'])
    _box_row("  3. Generate new token (classic)", _T['WHITE'])
    _box_row("  4. Scope    ✓ read:user", _T['WHITE'])
    _box_row("  5. Copie le token", _T['WHITE'])
    _box_row()
    _box_bot()
    print()
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.gh_token')
    if os.path.isfile(token_path):
        with open(token_path) as f:
            saved = f.read().strip()
        if saved:
            info(f"{t('gh_saved')} : {saved[:8]}{'*' * (len(saved) - 8)}")
            if ask(t('gh_use')).lower() not in ('n', 'no', 'non'):
                if _check_star_github():
                    ok(t('gh_confirmed'))
                else:
                    err(t('gh_not_starred'))
                input(c(f"\n  [{t('enter')}]", _T['GRAY']))
                return
    token = input(c(f"\n  {t('gh_paste')} ", _T['CYAN'])).strip()
    if not token: return
    save_token(token)
    print()
    if _check_star_github():
        ok(t('gh_confirmed'))
    else:
        err(t('gh_not_starred'))
        print(c(f"\n  {t('gh_star_here')} https://github.com/{GITHUB_REPO}", _T['CYAN']))
    input(c(f"\n  [{t('enter')}]", _T['GRAY']))

# ══════════════════════════════════════════════════════════════
#  TUTO STAR
# ══════════════════════════════════════════════════════════════

def show_star_tutorial():
    show_banner()
    _box_top('COMMENT DÉBLOQUER LES STAR TOOLS')
    _box_row()
    _box_row("  1. Va sur le repo :", _T['WHITE'])
    _box_row(f"     https://github.com/{GITHUB_REPO}", _T['STAR'])
    _box_row()
    _box_row("  2. Clique sur ★ 'Star' en haut à droite", _T['WHITE'])
    _box_row("  3. Reviens ici → [G] pour configurer ton token", _T['WHITE'])
    _box_row()
    _box_bot()
    print()
    info("Une fois la star mise, utilise [G] pour ajouter ton token.")
    input(c(f"\n  [{t('enter')}]", _T['GRAY']))

# ══════════════════════════════════════════════════════════════
#  LAUNCH
# ══════════════════════════════════════════════════════════════

def launch(filepath):
    try:
        if filepath.endswith('.exe'):
            if os.name == 'nt':
                subprocess.run([filepath], check=False)
            else:
                if shutil.which('wine'):
                    subprocess.run(['wine', filepath], check=False)
                else:
                    err("wine n'est pas installé — impossible de lancer un .exe sur Linux/Mac")
                    info("Installe wine : https://www.winehq.org/")
                    time.sleep(2)
        else:
            subprocess.run([sys.executable, filepath], check=False)
    except FileNotFoundError:
        err("Fichier introuvable ou wine manquant"); time.sleep(1)
    except Exception as e:
        err(f"Erreur lors du lancement : {e}"); time.sleep(1)

# ══════════════════════════════════════════════════════════════
#  GRILLE 3 COLONNES
# ══════════════════════════════════════════════════════════════

COLS           = 3
ITEMS_PER_PAGE = 24
CELL_VIS       = 28
SEP_VIS        = 3
LABEL_W_STAR   = 18
LABEL_W_FREE   = 21
FLAG           = "🇨🇦"

def _pad(text: str, width: int) -> str:
    return text[:width] if len(text) >= width else text + " " * (width - len(text))

def _star_color() -> tuple:
    p = _T['PRIMARY']
    return (220, 20, 60) if (p[0] > 200 and p[1] > 100 and p[2] < 80) else (255, 190, 60)

def _render_grid(page_tools, start_idx, star_ok):
    padded = list(page_tools)
    while len(padded) % COLS != 0:
        padded.append(None)
    rows     = len(padded) // COLS
    star_col = _star_color()

    # top border
    top = '┌' + ('─' * CELL_VIS + '┬') * (COLS - 1) + '─' * CELL_VIS + '┐'
    print(c(f"  {top}", _T['PRIMARY']))

    for row in range(rows):
        line = ""
        for col in range(COLS):
            idx   = row * COLS + col
            entry = padded[idx]
            line += c("│", _T['PRIMARY'])
            if entry is None:
                line += " " * CELL_VIS
            else:
                fp, is_star = entry
                num         = start_idx + idx + 1
                name        = get_name(fp)
                num_str     = f"[{num:>2}]"
                if is_star:
                    raw   = _pad(name, LABEL_W_STAR)
                    col_n = star_col
                    col_l = star_col if star_ok else (int(star_col[0]*0.5), int(star_col[1]*0.5), int(star_col[2]*0.5))
                    cell_colored = f" {c(num_str, col_n)} {c(raw, col_l)} {FLAG}"
                else:
                    raw          = _pad(name, LABEL_W_FREE)
                    cell_colored = f" {c(num_str, _T['PRIMARY'])} {c(raw, _T['WHITE'])}"
                # Pad to exactly CELL_VIS visible chars
                vis = visible_len(cell_colored)
                cell_colored += " " * max(0, CELL_VIS - vis)
                line += cell_colored
        line += c("│", _T['PRIMARY'])
        print(f"  {line}")

        # separator between rows (not after last)
        if row < rows - 1:
            mid = '├' + ('─' * CELL_VIS + '┼') * (COLS - 1) + '─' * CELL_VIS + '┤'
            print(c(f"  {mid}", _T['DARK']))

    bot = '└' + ('─' * CELL_VIS + '┴') * (COLS - 1) + '─' * CELL_VIS + '┘'
    print(c(f"  {bot}", _T['PRIMARY']))

# ══════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════

def main_menu():
    page = 1
    while True:
        star_tools = scan_folder(STAR_DIR, is_star=True)
        free_tools = scan_folder(TOOLS_DIR, is_star=False)
        all_tools  = star_tools + free_tools

        star_ok     = _check_star_github()
        total       = len(all_tools)
        total_pages = max(1, (total - 1) // ITEMS_PER_PAGE + 1)
        page        = max(1, min(page, total_pages))

        start      = (page - 1) * ITEMS_PER_PAGE
        page_tools = all_tools[start:start + ITEMS_PER_PAGE]

        show_banner()

        # page / stats header
        _box_top(f"PAGE {page}/{total_pages}  ──  {total} tools")
        _box_row()

        if all_tools:
            _box_bot()
            print()
            _render_grid(page_tools, start, star_ok)
        else:
            _box_row("  Aucun tool trouvé dans ./tools ou ./star", _T['YELLOW'])
            _box_row()
            _box_bot()

        # commandes
        print()
        cmds  = c("  [G]", _T['ACCENT']) + c(" GitHub/Star", _T['WHITE'])
        cmds += "   " + c("[C]", _T['ACCENT']) + c(f" {t('theme_menu')}", _T['WHITE'])
        if total_pages > 1:
            cmds += "   " + c("[N]", _T['ACCENT']) + c(f" {t('page_next')}", _T['WHITE'])
            cmds += "   " + c("[P]", _T['ACCENT']) + c(f" {t('page_prev')}", _T['WHITE'])
        cmds += "   " + c("[0]", _T['GRAY']) + c(f" {t('exit')}", _T['GRAY'])
        print(cmds)
        print()

        choice = ask(">>")

        if choice == '0':
            cls()
            print(c(f"\n  Bye — {BRANDING_URL}\n", _T['PRIMARY']))
            sys.exit(0)
        elif choice == 'G':
            github_setup()
            global _STAR_CACHE
            _STAR_CACHE = None
        elif choice == 'C':
            theme_selector()
        elif choice == 'N' and total_pages > 1:
            page = min(page + 1, total_pages)
        elif choice == 'P' and total_pages > 1:
            page = max(page - 1, 1)
        else:
            try:
                n = int(choice)
                if 1 <= n <= total:
                    fp, is_star_tool = all_tools[n - 1]
                    if is_star_tool and not star_ok:
                        show_star_tutorial()
                    else:
                        launch(fp)
                else:
                    err(t('invalid')); time.sleep(0.4)
            except ValueError:
                err(t('not_a_number')); time.sleep(0.4)

# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    try:
        load_theme()
        cls()
        print(banner_gradient(BANNER))
        time.sleep(0.6)
        auto_update()
        if os.path.isfile(STARTER_PATH):
            subprocess.Popen([sys.executable, STARTER_PATH])
        main_menu()
    except KeyboardInterrupt:
        cls()
        print(c(f"\n  Bye — {BRANDING_URL}\n", _T['PRIMARY']))
        sys.exit(0)