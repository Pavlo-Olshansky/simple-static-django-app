# Generated by Django 2.0.7 on 2018-07-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='service_icons/')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
