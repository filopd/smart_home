# Generated by Django 3.2.10 on 2022-01-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(default='', max_length=30)),
                ('home_member', models.CharField(choices=[('usr1', 'User1'), ('usr2', 'User2'), ('usr3', 'User3')], default='', max_length=4)),
                ('comment', models.CharField(default='', max_length=200)),
                ('docfile', models.FileField(upload_to='documents/<django.db.models.fields.CharField>/')),
            ],
        ),
    ]
