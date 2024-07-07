from django.db import models

class Pembeli(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=20)

class Rujak(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

class BahanRujak(models.Model):
    nama = models.CharField(max_length=255)
    jumlah = models.IntegerField()