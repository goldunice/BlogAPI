from django.db import models
from django.contrib.auth.models import AbstractUser


class Muallif(AbstractUser):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveIntegerField(null=True)
    kasb = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    matn = models.TextField()
    korish_soni = models.PositiveIntegerField(default=0)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
