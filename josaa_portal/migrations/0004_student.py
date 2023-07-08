# Generated by Django 4.2.2 on 2023-07-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josaa_portal', '0003_ques4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institute', models.CharField(max_length=100, null=True)),
                ('Academic', models.CharField(max_length=100, null=True)),
                ('Quota', models.CharField(max_length=100, null=True)),
                ('SeatType', models.CharField(max_length=100, null=True)),
                ('OpeningRank', models.IntegerField(null=True)),
                ('ClosingRank', models.IntegerField(null=True)),
                ('Year', models.IntegerField(null=True)),
                ('Round', models.IntegerField(null=True)),
            ],
        ),
    ]