from django.db import models

# Create your models here.



class PecaXadrez(models.Model):
      cor = models.CharField(max_length=6)

      def __str__(self):
        return self.cor