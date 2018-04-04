# Generated by Django 2.0.1 on 2018-03-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('cod_availability', models.BooleanField(default=False)),
                ('seller', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_pic')),
                ('department', models.ForeignKey(default='Specials', on_delete=django.db.models.deletion.SET_DEFAULT, to='basic_app.Department')),
            ],
        ),
    ]
