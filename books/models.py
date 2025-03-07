from django.db import models
from django.urls import reverse

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='cover/', blank=True)

    def __str__(self):
        return f'{self.title} نوشته: {self.author}'
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.pk])

