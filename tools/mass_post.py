import requests
import time
import random

print("🔧 Créateur de masse de Posts dans Forum Discord - Version Configurable + Anti-RateLimit")
print("⚠️  ATTENTION : Self-bot = contre les ToS Discord → Risque élevé de ban permanent !")
print("=" * 100)

# ====================== CONFIGURATION AU LANCEMENT ======================
token = input("➤ Entre ton token Discord : ").strip()
guild_id = input("➤ Entre l'ID du serveur : ").strip()
forum_channel_id = input("➤ Entre l'ID du salon Forum : ").strip()

name_base = input("➤ Nom de base des posts (ex: Discussion Leak) : ").strip()
content_base = input("➤ Contenu/message de chaque post (ex: lien ou texte) : ").strip()

num_posts = int(input("\n➤ Nombre de posts à créer : ") or 50)
batch_size = int(input("➤ Taille des lots (recommandé 5-10) : ") or 6)
delay_base = float(input("➤ Délai de base entre chaque post (recommandé 6.0 - 10.0 secondes) : ") or 7.0)

use_offset = input("➤ Ajouter un numéro au nom des posts ? (o/n) : ").strip().lower() == 'o'
intensity = int(input("➤ Intensité des caractères invisibles (1-6) : ") or 4)

print(f"\n🚀 Lancement de la création de {num_posts} posts dans le forum...\n")

# ====================== CARACTÈRES INVISIBLES ======================
INVISIBLE_CHARS = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF', '\u180E']

def add_invisible_chars(text, intensity=4):
    if not text:
        return text
    result = list(text)
    for _ in range(random.randint(3, intensity * 5)):
        pos = random.randint(0, len(result))
        result.insert(pos, random.choice(INVISIBLE_CHARS))
    if random.random() > 0.4:
        result.append(random.choice(INVISIBLE_CHARS))
    return ''.join(result)

# ====================== HEADERS ======================
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

url = f"https://discord.com/api/v10/channels/{forum_channel_id}/threads"

success = 0
consecutive_429 = 0

for i in range(num_posts):
    # Nom du post avec caractères invisibles + numéro optionnel
    post_name = name_base
    if use_offset:
        post_name = f"{name_base} {i+1}"
    current_name = add_invisible_chars(post_name, intensity)
    
    current_content = add_invisible_chars(content_base, intensity) if content_base else "Post créé automatiquement."

    payload = {
        "name": current_name,
        "auto_archive_duration": 60,        # 1 heure (tu peux mettre 1440 pour 1 jour)
        "rate_limit_per_user": 0,
        "message": {
            "content": current_content
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=20)

    if response.status_code == 201:
        success += 1
        consecutive_429 = 0
        print(f"✅ Post {i+1}/{num_posts} créé : {current_name[:50]}...")
    elif response.status_code == 429:
        consecutive_429 += 1
        retry_after = float(response.json().get("retry_after", 15))
        wait_time = retry_after + 8 + (consecutive_429 ** 2) * 4
        print(f"⏸️  Rate limit ! Pause de {wait_time:.1f}s (consecutive: {consecutive_429})")
        time.sleep(wait_time)
        continue
    else:
        print(f"❌ Échec post {i+1} → Code {response.status_code}")
        print(response.text[:300])

    # Délai prudent
    sleep_time = delay_base + random.uniform(1.0, 4.5)
    sleep_time = max(sleep_time, 5.0)
    time.sleep(sleep_time)

    # Pause entre lots
    if (i + 1) % batch_size == 0 and (i + 1) < num_posts:
        lot_pause = random.uniform(45, 90)
        print(f"⏳ Lot de {batch_size} terminé → Pause sécurité {lot_pause:.1f}s")
        time.sleep(lot_pause)

print("\n🎉 FINI !")
print(f"   {success}/{num_posts} posts créés avec succès dans le forum.")
print("   Conseil : Si tu as beaucoup de 429, augmente le délai_base à 8 ou 10 secondes.")