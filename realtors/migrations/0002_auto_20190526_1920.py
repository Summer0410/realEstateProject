# Generated by Django 2.2.1 on 2019-05-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(max_length=20, upload_to=''),
        ),
    ]