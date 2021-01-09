# Generated by Django 3.1.5 on 2021-01-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
