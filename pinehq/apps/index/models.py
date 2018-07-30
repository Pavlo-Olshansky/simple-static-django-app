from django.db import models


class Service(models.Model):
    icon = models.ImageField(
        upload_to='service_icons/',
        null=True,
        blank=True,
    )
    title = models.CharField(
        'Title',
        max_length=256,
        blank=True,
        null=True,
    )
    description = models.CharField(
        'Description',
        max_length=2048,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'index'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
