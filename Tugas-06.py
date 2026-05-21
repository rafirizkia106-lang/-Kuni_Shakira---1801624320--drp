from datetime import datetime

print("Hi!")
print("coba kamu lihat, disini ada beberapa pilihan")
print("sarapan")
print("pergi kerja")

aktivitas = input("pilih aktivitas yang kamu inginkan:")

if aktivitas.lower() == "sarapan":
    
    print("disini ada beberapa pilihan menu makanan, silahkan dipilih ya!")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("mau sarapan dengan menu apa?")

    if menu.lower() == "telur"or menu.lower () == "ikan" or menu.lower() == "nugget":
        print(f"oke, {menu} tersedia, silahkan dimasak!")
    else:
        print(f"kamu harus beli bahannya dulu")

elif aktivitas.lower()== "pergi kerja":
    waktu = datetime.now()
    print("kamu pergi kerja pukul 08.00 pagi ya")
    print(f"sekarang sudah pukul {waktu}")

    if waktu.hour < 08.00:
                print("masih ada waktu nih, masih bisa bersiap!")
    elif waktu.hour == 08.00:
                print("sudah jam 08.00 nih, yuk pergi kerja!")
    else:
                print("yah, kamu sudah terlambat, lain kali kamu harus tepat waktu ya!")