# NAME = "Event spammer "
import requests
import time
import random
import base64
from datetime import datetime, timedelta, timezone
from io import BytesIO
from PIL import Image
# ====================== CARACTÈRES INVISIBLES ======================
INVISIBLE_CHARS = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF', '\u180E']

def add_invisible_chars(text, intensity=5):
    if not text:
        return text
    result = list(text)
    for _ in range(random.randint(4, intensity * 6)):
        pos = random.randint(0, len(result))
        result.insert(pos, random.choice(INVISIBLE_CHARS))
    if random.random() > 0.35:
        result.append(random.choice(INVISIBLE_CHARS))
    return ''.join(result)

print("🔧 Event Spammer")
print("⚠️  ATTENTION : Self-bot = risque élevé de ban permanent ! Utilise à tes risques.")
print("=" * 100)

# ====================== CONFIGURATION AU LANCEMENT ======================
token = input("➤ Entre ton token Discord : ").strip()
guild_id = input("➤ Entre l'ID du serveur : ").strip()

name_base = input("➤ Nom de base de l'événement : ").strip()
description = input("➤ Description de l'événement (laisser vide si aucune) : ").strip()
image_url = input("➤ URL de l'image de couverture (laisser vide si aucune) : ").strip()

minutes_future = int(input("➤ Dans combien de minutes commencer ? (ex: 5) : ") or 5)
end_minutes = int(input("➤ Durée de l'événement en minutes (ex: 100000 ou laisser vide) : ") or 0)

print("\nType d'événement :")
print("   1 → Stage")
print("   2 → Salon vocal")
print("   3 → Externe (lien)")
entity_type = int(input("➤ Ton choix (1-3) : ") or 3)

if entity_type == 3:
    location = input("➤ Lieu / lien externe : ").strip()
else:
    location = None
    channel_id = input("➤ ID du salon vocal/stage : ").strip()

num_events = int(input("\n➤ Nombre d'événements à créer : ") or 50)
batch_size = int(input("➤ Taille des lots (recommandé 5-10) : ") or 6)
delay_base = float(input("➤ Délai de base entre chaque création (recommandé 6.0 - 10.0) : ") or 7.0)

use_offset = input("➤ Décaler légèrement chaque événement ? (o/n) : ").strip().lower() == 'o'
offset_minutes = float(input("➤ Décalage par événement en minutes (ex: 0.2) : ") or 0.15) if use_offset else 0

intensity = int(input("➤ Intensité des caractères invisibles (1 faible - 6 très fort) : ") or 5)

print(f"\n🚀 Lancement de {num_events} événements avec protections maximales...\n")

# ====================== CALCUL DATES ======================
start_time = datetime.now(timezone.utc) + timedelta(minutes=minutes_future)
start_iso = start_time.isoformat().replace("+00:00", "Z")

end_iso = None
if end_minutes > 0:
    end_time = start_time + timedelta(minutes=end_minutes)
    end_iso = end_time.isoformat().replace("+00:00", "Z")

# ====================== IMAGE ======================
def get_image_data(url):
    if not url:
        return None
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        img = Image.open(BytesIO(r.content))
        buffered = BytesIO()
        fmt = img.format or "PNG"
        img.save(buffered, format=fmt)
        b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return f"data:image/{fmt.lower()};base64,{b64}"
    except:
        print("⚠️ Impossible de charger l'image → pas d'image")
        return None

image_data = get_image_data(image_url)

# ====================== HEADERS ======================
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwidGltZV96b25lIjoiRXVyb3BlL1BhcmlzIn0=",
    "Referer": "https://discord.com/channels/@me",
    "Origin": "https://discord.com",
}

url = f"https://discord.com/api/v10/guilds/{guild_id}/scheduled-events"

success = 0
consecutive_429 = 0
backoff_multiplier = 1.0

for i in range(num_events):
    current_name = add_invisible_chars(name_base, intensity)
    current_desc = add_invisible_chars(description, intensity)

    current_start = start_time + timedelta(minutes=offset_minutes * i) if use_offset else start_time
    current_start_iso = current_start.isoformat().replace("+00:00", "Z")

    payload = {
        "name": current_name,
        "description": current_desc,
        "scheduled_start_time": current_start_iso,
        "scheduled_end_time": end_iso if end_iso else None,
        "privacy_level": 2,
        "entity_type": entity_type,
        "image": image_data,
    }

    if entity_type == 3 and location:
        payload["entity_metadata"] = {"location": location}
    elif entity_type in [1, 2] and 'channel_id' in locals():
        payload["channel_id"] = channel_id

    response = requests.post(url, headers=headers, json=payload, timeout=20)

    if response.status_code == 201:
        success += 1
        consecutive_429 = 0
        backoff_multiplier = 1.0
        print(f"✅ {i+1}/{num_events} créé")
    elif response.status_code == 429:
        consecutive_429 += 1
        retry_after = float(response.json().get("retry_after", 20))
        is_global = response.headers.get("X-RateLimit-Global") == "true"

        wait_time = retry_after + 12 + (consecutive_429 ** 2) * 5
        if is_global:
            wait_time += 35
            print(f"🌍 GLOBAL RATE LIMIT ! Pause très longue ({wait_time:.1f}s)")
        else:
            print(f"⏸️ Rate limit ! Pause de {wait_time:.1f}s (consecutive: {consecutive_429})")

        time.sleep(wait_time)
        backoff_multiplier = min(backoff_multiplier * 1.7, 6.0)
        continue
    else:
        print(f"❌ {i+1}/{num_events} → Code {response.status_code}")
        print(response.text[:300])

    # Délai ultra prudent
    sleep_time = delay_base + random.uniform(1.5, 5.0) + (backoff_multiplier * 2)
    sleep_time = max(sleep_time, 5.8)
    time.sleep(sleep_time)

    # Pause entre lots
    if (i + 1) % batch_size == 0 and (i + 1) < num_events:
        lot_pause = random.uniform(80, 130)
        print(f"⏳ Lot terminé → Pause sécurité {lot_pause:.1f}s")
        time.sleep(lot_pause)

print("\n🎉 FINI !")
print(f"   {success}/{num_events} événements créés avec succès.")