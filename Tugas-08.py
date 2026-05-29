user = input ("Masukkan Namamu Disini ya!")

print (f"\n 🦋 1. Papan Catur Input Kegiatan {user}")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print ("⬛", end=" ")
        else:
            print ("⬜", end=" ")
    print()

print(f"\n 🦋 2. Daftar Kegiatan {user}🦋")

Daftar_Kegiatan = []
Jumlah_Kegiatan = int(input("Berapa banyak Kegiatan yang ingin kamu lakukan?"))

for i in range(Jumlah_Kegiatan):
    print()
    print(f"\n🦋Tugas ke-{i+1}🦋")

    Nama_Kegiatan = input("Nama Kegiatan: ")
    Bentuk_Kegiatan = input("Bentuk Kegiatan:")
    Pengerjaan_Kegiatan = input("Pengerjaan Kegiatan:")
    Tenggat_Kegiatan = input("Tenggat Kegiatan:")

    Tugas= {
        "Kegiatan": Nama_Kegiatan,
        "Bentuk": Bentuk_Kegiatan,
        "Pengerjaan": Pengerjaan_Kegiatan,
        "Tenggat": Tenggat_Kegiatan
    }
    Daftar_Kegiatan.append (Tugas)
print()

print(f"🦋Daftar Kegiatan yang sudah {user} masukkan🦋")

for i in range(len(Daftar_Kegiatan)):
    print(f"Kegiatan {i + 1}")
    print(f"Nama Kegiatan: {Daftar_Kegiatan[i]['Kegiatan']}")
    print(f"Bentuk Kegiatan: {Daftar_Kegiatan[i]['Bentuk']}")
    print(f"Pengerjaan Kegiatan: {Daftar_Kegiatan[i]['Pengerjaan']}")
    print(f"Tenggat Kegiatan: {Daftar_Kegiatan[i]['Tenggat']}")
    print()
