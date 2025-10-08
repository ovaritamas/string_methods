"""
4️⃣ Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""
rendeles = input("Add meg a rendelést amával: ")
modositas = rendeles.replace("alma, körte")
print(modositas)