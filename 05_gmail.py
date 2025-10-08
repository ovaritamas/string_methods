"""
5️⃣ Szó elejének/végének ellenőrzése – email ellenőrzés
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.
"""

email = input("Adj meg egy email címet: ")

gmail = email.endswith("gmail.com")

if gmail == True:
    print("Ez egy gmailes cím")

else:
    print("Ez nem gmailes cím")