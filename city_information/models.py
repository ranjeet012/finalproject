from django.db import models

# Create your models here.
class cityinfo(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    datetime=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title