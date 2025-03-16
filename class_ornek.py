# Temel Sınıf Örneği: Araba Modelleme
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0
    
    def bilgileri_goster(self):
        print(f"{self.yil} {self.marka} {self.model}")
    
    def hizi_arttir(self, miktar):
        self.hiz += miktar
        print(f"Yeni hız: {self.hiz} km/s")

# Kullanım
araba1 = Araba("Toyota", "Corolla", 2022)
araba1.bilgileri_goster()
araba1.hizi_arttir(30)