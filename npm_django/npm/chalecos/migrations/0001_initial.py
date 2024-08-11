# Generated by Django 5.1 on 2024-08-11 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chalecos',
            fields=[
                ('serial', models.IntegerField(primary_key=True, serialize=False)),
                ('beneficiario_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chalecos', to='beneficiarios.beneficiarios')),
            ],
        ),
    ]
