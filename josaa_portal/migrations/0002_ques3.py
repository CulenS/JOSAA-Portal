# Generated by Django 4.2.2 on 2023-06-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josaa_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ques3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNumber', models.IntegerField(null=True)),
                ('DataFloat', models.IntegerField(null=True)),
                ('DataInt', models.IntegerField(null=True)),
            ],
        ),
    ]
