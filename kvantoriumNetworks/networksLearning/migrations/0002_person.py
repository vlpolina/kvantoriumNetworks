# Generated by Django 4.2.2 on 2023-07-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networksLearning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ImageField(upload_to='photos/', verbose_name='Персонажи')),
            ],
            options={
                'verbose_name': 'Персонажи',
                'verbose_name_plural': 'Персонажи',
            },
        ),
    ]
