# Generated by Django 2.0.3 on 2018-03-23 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0003_auto_20180322_2137'),
        ('profiles', '0005_profile_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_km', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('hub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hubs.Hub')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
    ]