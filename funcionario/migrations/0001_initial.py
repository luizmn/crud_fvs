# Generated by Django 2.1.5 on 2019-01-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnc_nome', models.CharField(max_length=100)),
                ('fnc_matricula', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
