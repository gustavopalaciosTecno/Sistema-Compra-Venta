# Generated by Django 4.2.3 on 2024-01-27 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]