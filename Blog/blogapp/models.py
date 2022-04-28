from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    matn = models.TextField()

    def __str__(self):
        return self.sarlavha

class Rasm(models.Model):
    photo = models.FileField(upload_to='rasmlar')
    maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE)