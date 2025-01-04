# Generated by Django 5.1.4 on 2024-12-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_unidadeescolar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
            ],
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='Cargo',
            new_name='cargo',
        ),
    ]