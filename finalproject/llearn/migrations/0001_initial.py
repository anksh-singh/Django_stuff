# Generated by Django 4.0.3 on 2022-03-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField()),
                ('stu_name', models.CharField(max_length=16)),
                ('stu_email', models.EmailField(max_length=20)),
                ('stu_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
