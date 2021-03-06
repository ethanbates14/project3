# Generated by Django 2.0.7 on 2018-08-02 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180802_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='toppings',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_options',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Options'),
        ),
        migrations.AddField(
            model_name='topping',
            name='option_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Options'),
        ),
    ]
