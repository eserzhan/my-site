# Generated by Django 2.0.13 on 2019-08-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190809_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(null=None, upload_to='images/'),
        ),
    ]