from django.db import models
class dbb(models.Model):
    n = models.CharField(max_length=25)
    em = models.EmailField(primary_key=True)
    p = models.CharField(max_length=15)
    food = models.CharField(max_length=15)
    place = models.CharField(max_length=20)
    sportsman = models.CharField(max_length=15)
    actor = models.CharField(max_length=15)
    game = models.CharField(max_length=15)
    song = models.CharField(max_length=15)
    movie = models.CharField(max_length=15)
    sports = models.CharField(max_length=15)
    enter = models.CharField(max_length=15)
    person = models.CharField(max_length=15)
    contact = models.CharField(max_length=50)
    about = models.TextField(max_length=2000)
    def __str__(self):
        return self.em