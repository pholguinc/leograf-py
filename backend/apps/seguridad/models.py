from django.db import models

# Create your models here.


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'menus'
