# Generated by Django 2.0.3 on 2018-05-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0008_auto_20180327_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='price_CAPS',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price_barter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]