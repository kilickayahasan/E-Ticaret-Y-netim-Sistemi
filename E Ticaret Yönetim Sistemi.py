def ürün_ekleme():

    ürün = input("Eklenecek ürünü giriniz :")
    fiyat = int(input("Eklenen ürünün fiyatını giriniz : "))

    ürün = f"{ürün},{fiyat}\n"

    with open("Ürün Kataloğu.txt", "a", encoding="utf-8") as file:
        file.write(ürün)

        print("Yeni ürün ve fiyatı ürün kataloğuna eklendi...")

def ürün_cıkarma():
    cıkan_ürün = input("Çıkarılacak ürünü giriniz : ")

    with open("Ürün Kataloğu.txt", "r", encoding="utf-8") as file:

        katalog = file.readlines ()
        yeni_liste = []

        for i in katalog :
            if not i.startswith(cıkan_ürün + ",") :
                yeni_liste.append(i)

    with open("Ürün Kataloğu.txt", "w", encoding="utf-8") as file:

        for i in yeni_liste:
            file.writelines(i)

def ürün_listeleme():
    with open("Ürün Kataloğu.txt", "r", encoding="utf-8") as file:
        for i in file:
            i = i[:-1]
            liste = i.split(",")

            print(f"Ürün : {liste[0]} - Fiyat : {liste[1]} TL")

def kullanıcı_kayıt():
    kullanıcı_adı = input("Kullanıcı adını giriniz : ")
    sifre = int(input("Şifrenizi giriniz : "))

    kullanıcılar = f"{kullanıcı_adı},{sifre}\n"

    with open("Kullanıcı Bilgileri.txt", "a", encoding="utf-8") as file:
        file.write(kullanıcılar)

def kullanıcı_dogrulama():

    kullanıcı_adı = input("Kullanıcı adını giriniz : ")
    sifre = input("Şifrenizi giriniz : ")


    with open("Kullanıcı Bilgileri.txt", "r", encoding="utf-8") as file:
        kullanıcılar = file.readlines()

        for i in kullanıcılar:
            i = i[:-1]
            kayıtlı_adı , kayıtlı_sifre = i.split(",")

            if kayıtlı_adı == kullanıcı_adı and kayıtlı_sifre == sifre:
                print("Kimlik Doprulandı...")
                return


        print("Kullanıcı adı veya şifre hatalı...")

while True:

    print("""

    İşlem seçiniz : 

    1. Kullanıcı adı ve şifre oluşturunuz
    2. Kullanıcı adı ve şifre doğrulayınız
    3. Ürün ve fiyat ekleyiniz
    4. Ürün çıkarınız 
    5. Ürün Listeleyiniz
    6. Sistemden Çıkınız  

    """)

    işlem = int(input("İşlem Seçiniz : "))

    if işlem == 1:
        kullanıcı_kayıt()

    elif işlem == 2:
        kullanıcı_dogrulama()

    elif işlem == 3:
        ürün_ekleme()

    elif işlem == 4:
        ürün_cıkarma()

    elif işlem == 5:
        ürün_listeleme()

    elif işlem == 6:
        print("Sistemden çıkış yapılıyor....")
        break

    else:
        print("Geçersiz İşlem...")
        break



























