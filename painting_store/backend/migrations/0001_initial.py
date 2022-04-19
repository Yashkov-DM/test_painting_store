# Generated by Django 4.0.4 on 2022-04-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='paint_name')),
                ('year', models.DateTimeField(verbose_name='create_year')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлерея',
            },
        ),
    ]