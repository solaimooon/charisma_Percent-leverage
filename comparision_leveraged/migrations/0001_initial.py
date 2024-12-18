# Generated by Django 4.2 on 2024-11-13 20:37

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BaseUnitsTotalNetAssetValue', models.DecimalField(decimal_places=1, max_digits=15)),
                ('SuperUnitsTotalNetAssetValue', models.DecimalField(decimal_places=1, max_digits=15)),
                ('Leverage_percentage', models.DecimalField(decimal_places=1, max_digits=15)),
                ('date', django_jalali.db.models.jDateField()),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comparision_leveraged.fund')),
            ],
        ),
    ]
