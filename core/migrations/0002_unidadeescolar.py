# Generated by Django 5.1.4 on 2024-12-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INEP', models.IntegerField(verbose_name='INEP')),
                ('UE', models.CharField(max_length=150, verbose_name='Unidade Escolar')),
            ],
        ),
    ]