"""
2️⃣ Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll.
Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

uzenet = input("Kérek egy üzenetet: ")

uzenet_hosszusag = len(uzenet)

print(f"Az üzeneted hossza {uzenet_hosszusag} karakter")