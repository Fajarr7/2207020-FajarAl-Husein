class Mahasiswa:
        
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
    
    def tahunLahir(self):
        return 2022 - self.umur
    
saya = Mahasiswa("Fajarr", "2207020",34)
print("Tahun lahir saya adalah", saya.tahunLahir())
print("Saya aceng angkatan", "2207020"[0:2])