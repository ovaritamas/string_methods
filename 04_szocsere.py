"""
4️⃣ Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""
bolt = ["körte", ""]
rendeles = input("Add meg a rendelést amával: ")

print(rendeles)
if "alma" in bolt:
    print("Van alma a boltban!")
else:
    modositas = rendeles.replace("alma", "körte")
    print(modositas)