"""
1️⃣ Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).
"""

felhasznalo_nev = input("Add meg a user nevedet ")

nagybetus_szo = felhasznalo_nev.capitalize()
print(f"Csupa nagybetűs: {nagybetus_szo}")

kisbetus_szo = felhasznalo_nev.lower()
print(f"Csupa kisbetűs: {kisbetus_szo}")

nagykezdobetus_szo = felhasznalo_nev.capitalize()
print(f"Nagy kezdőbetűs: {nagykezdobetus_szo}")