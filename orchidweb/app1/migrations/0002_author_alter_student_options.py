# Generated by Django 4.1.1 on 2022-09-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, null=True)),
                ('experience', models.IntegerField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
    ]