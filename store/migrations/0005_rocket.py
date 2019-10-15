# Generated by Django 2.2.5 on 2019-10-14 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20191015_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('desc_short', models.CharField(max_length=200)),
                ('desc_long', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('image', models.ImageField(upload_to='images')),
                ('hero', models.BooleanField()),
            ],
        ),
    ]
