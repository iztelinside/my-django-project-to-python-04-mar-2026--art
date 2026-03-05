from django.db import models


class Art(models.Model):
    title = models.CharField("Art Name",max_length=100)
    content = models.TextField("Art Content")
    input = models.TextField("Art Input")
    date = models.DateTimeField("Art Date")

    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Art"
        verbose_name_plural = "Arts"
# Create your models here.
