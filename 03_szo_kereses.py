"""
3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""
user = input("Adj egy szöveget, amiben szerepel a Python szó: ")
szamlalo = user.count("Python")
print(szamlalo)