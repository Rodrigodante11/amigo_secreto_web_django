# Generated by Django 3.2.14 on 2022-07-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amigos', '0005_alter_amigo_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='foto_amigo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]