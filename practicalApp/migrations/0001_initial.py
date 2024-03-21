# Generated by Django 2.2 on 2024-03-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('numberOfCats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicalApp.Student')),
            ],
        ),
    ]