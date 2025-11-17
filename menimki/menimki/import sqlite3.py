import sqlite3

conn = sqlite3.connect("evler.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS evler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unvan TEXT,
    sahe INTEGER,
    otaq_sayi INTEGER,
    qiymet REAL,
    satis_tarixi TEXT
)
""")

evler = [
    ("Baki, Nizami", 120, 3, 150000, "2023-05-10"),
    ("Baki, Yasamal", 90, 2, 100000, "2021-07-21"),
    ("Sumqayit", 110, 4, 130000, "2020-09-11"),
    ("Gence", 200, 5, 250000, "2022-03-17"),
    ("Baki, Xetai", 80, 2, 95000, "2021-12-01"),
    ("Quba", 140, 4, 170000, "2023-02-15"),
    ("Sheki", 100, 3, 120000, "2021-06-22"),
    ("Baki, Sabuncu", 75, 2, 85000, "2020-04-09"),
    ("Baki, Binagadi", 95, 3, 105000, "2022-10-10"),
    ("Baki, Sabail", 180, 5, 300000, "2023-04-25"),
    ("Sumqayit, 9-cu mk", 70, 2, 80000, "2021-09-19"),
    ("Baki, Qaradag", 130, 4, 160000, "2019-11-01"),
    ("Baki, Nermanov", 150, 5, 280000, "2023-01-30"),
    ("Gence, Kapaz", 90, 3, 115000, "2020-03-15"),
    ("Baki, Suraxani", 100, 3, 110000, "2022-05-10")
]
cursor.executemany("INSERT INTO evler (unvan, sahe, otaq_sayi, qiymet, satis_tarixi) VALUES (?, ?, ?, ?, ?)", evler)
conn.commit()

def evleri_goster():
    cursor.execute("SELECT unvan, otaq_sayi FROM evler")
    for unvan, otaq in cursor.fetchall():
        print(f"Ünvan: {unvan}, Otaq sayı: {otaq}")

print("📋 Bütün evlər və otaq sayları:")
evleri_goster()

def otaq_3den_cox():
    cursor.execute("SELECT * FROM evler WHERE otaq_sayi > 3")
    print("\n🏠 3-dən çox otaqlı evlər:")
    for ev in cursor.fetchall():
        print(ev)

otaq_3den_cox()

id_input = int(input("\nSatış tarixi dəyişiləcək evin ID-sini daxil et: "))
cursor.execute("UPDATE evler SET satis_tarixi = '2023-09-15' WHERE id = ?", (id_input,))
conn.commit()
print("✅ Satış tarixi yeniləndi!")

unvan_input = input("\nQiyməti artırılacaq ünvanı daxil et: ")
cursor.execute("UPDATE evler SET qiymet = qiymet * 1.1 WHERE unvan LIKE ?", ('%' + unvan_input + '%',))
conn.commit()
print("💰 Qiymətlər 10% artırıldı!")


cursor.execute("DELETE FROM evler WHERE substr(satis_tarixi, 1, 4) < '2021'")
conn.commit()
print("🗑️ 2021-dən əvvəl satılan evlər silindi!")

conn.close()
