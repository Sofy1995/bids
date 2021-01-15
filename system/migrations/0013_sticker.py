# Generated by Django 3.1.2 on 2021-01-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_auto_20210112_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_creation', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('v', 'visible'), ('h', 'hidden')], default='v', max_length=1)),
            ],
        ),
    ]
