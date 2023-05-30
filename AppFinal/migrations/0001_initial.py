# Generated by Django 4.2 on 2023-05-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=900)),
                ('content', models.CharField(max_length=10000)),
                ('category', models.CharField(max_length=45)),
            ],
        ),
    ]
