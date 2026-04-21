kitoblar = [
    "alisher navoiy - Xamsa",
    "abdula qodiriy - Otkan kunlar"
    "cholpon - kecha va kunduz",
    "otkir hoshimov - ikki eshik orasi",
    "paolo cohelo - alkimyogar",
]
print("boshidagi royhat")
print(kitoblar)
kitoblar[0] = "Alisher navoiy - lisonut tayr"
print("ozgargan kn")
print(kitoblar)

kitoblar.remove("Abdulla qodiriy - Otkan kunlar")
print("ochrldi")
print(kitoblar)

kitoblar.append("Sherzod yangi asar")
print("qoshildi kn")
print(kitoblar)
print("son:", len(kitoblar))
print("1 chi:", kitoblar[0])
print("oxrgi:", kitoblar[-1])