# Generated by Django 4.1.1 on 2022-09-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_author_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField()),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
