# Generated by Django 3.2.16 on 2023-12-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preg', models.FloatField()),
                ('gluc', models.FloatField()),
                ('blood', models.FloatField()),
                ('skin', models.FloatField()),
                ('ins', models.FloatField()),
                ('bmi', models.FloatField()),
                ('dbf', models.FloatField()),
                ('age', models.FloatField()),
                ('result', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='DiabetesRecord',
        ),
    ]