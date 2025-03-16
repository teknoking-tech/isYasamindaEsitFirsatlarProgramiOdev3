from abc import ABC, abstractmethod

# Çalışan Yönetim Sistemi
class Calisan(ABC):
    @abstractmethod
    def maas_hesapla(self):
        pass

class TamZamanli(Calisan):
    def __init__(self, saatlik_ucret, calisma_saati):
        self.saatlik_ucret = saatlik_ucret
        self.calisma_saati = calisma_saati
    
    def maas_hesapla(self):
        return self.saatlik_ucret * self.calisma_saati

class SerbestCalisan(Calisan):
    def __init__(self, proje_ucreti):
        self.proje_ucreti = proje_ucreti
    
    def maas_hesapla(self):
        return self.proje_ucreti

# Kullanım
calisan1 = TamZamanli(150, 160)
calisan2 = SerbestCalisan(25000)
print("Tam Zamanlı Maaş:", calisan1.maas_hesapla())
print("Serbest Çalışan Maaş:", calisan2.maas_hesapla())