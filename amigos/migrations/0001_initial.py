# Generated by Django 3.2.14 on 2022-07-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_amigo', models.CharField(max_length=200)),
                ('telefone_amigo', models.TextField()),
                ('email_amigo', models.TextField()),
                ('sugestao_presente_amigo', models.TextField(blank=True)),
            ],
        ),
    ]
