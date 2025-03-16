# Öğrenci Kayıt Sistemi
class Ogrenci:
    def __init__(self, ad, soyad, ogrenci_no, dersler=None):
        self.ad = ad
        self.soyad = soyad
        self.ogrenci_no = ogrenci_no
        self.dersler = dersler if dersler is not None else []
    
    def ders_ekle(self, ders_adi):
        self.dersler.append(ders_adi)
    
    def bilgileri_goster(self):
        print(f"{self.ad} {self.soyad} - {self.ogrenci_no}")
        print("Aldığı Dersler:", ", ".join(self.dersler))

# Kullanım
ogr1 = Ogrenci("Ali", "Demir", "2023001")
ogr1.ders_ekle("Matematik")
ogr1.ders_ekle("Fizik")
ogr1.bilgileri_goster()