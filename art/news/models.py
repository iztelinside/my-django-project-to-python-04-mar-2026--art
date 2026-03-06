from django.db import models


class Art(models.Model):
    title = models.CharField("Art Name",max_length=100)
    content = models.TextField("Art Content")
    input = models.TextField("Art Input")
    date = models.DateTimeField("Art Date")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f"/news/{self.id}/"


    class Meta:
        verbose_name = "Art"
        verbose_name_plural = "Arts"
# Create your models here.
