# Generated by Django 3.2 on 2021-04-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('rating', models.CharField(max_length=3)),
                ('specs', models.TextField()),
                ('description', models.TextField()),
                ('images', models.TextField()),
                ('reviews', models.TextField()),
                ('product_url', models.URLField()),
            ],
        ),
    ]
