from django.db import models


class Project(models.Model):
    name = models.CharField(
        'Name',
        max_length=256,
        blank=True,
        null=True,
    )
    screenshot = models.ImageField(
        upload_to='project_screenshots/',
        null=True,
        blank=True,
    )
    description = models.CharField(
        'Description',
        max_length=2048,
        blank=True,
        null=True,
    )
    year_development = models.PositiveIntegerField(
        'Year development',
        null=True,
        blank=True,
    )
    optional_url = models.CharField(
        max_length=2048,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'portfolio'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
