from django.db import models


class CipherText(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'