# Elektrikli Araba Alt Sınıfı
from class_ornek import Araba

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        super().__init__(marka, model, yil)
        self.batarya_kapasitesi = batarya_kapasitesi
        self.sarj_durumu = 0
    
    def sarj_et(self, yuzde):
        self.sarj_durumu += yuzde
        print(f"Şarj Durumu: %{self.sarj_durumu}")

# Kullanım
tesla = ElektrikliAraba("Tesla", "Model S", 2023, 100)
tesla.bilgileri_goster()
tesla.sarj_et(80)