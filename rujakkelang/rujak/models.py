from django.db import models

class Pembeli(models.Model):
    nama = models.CharField(max_length=100)
    # tambahkan lebih banyak atribut jika perlu

class Rujak(models.Model):
    pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    # tambahkan atribut lainnya
    # misal: harga, tanggal_pembelian, dll

class BahanRujak(models.Model):
    rujak = models.ForeignKey(Rujak, on_delete=models.CASCADE)
    nama_bahan = models.CharField(max_length=100)
    # tambahkan atribut lainnya
    # misal: jumlah, harga, dll
