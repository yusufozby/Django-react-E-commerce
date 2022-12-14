# Generated by Django 4.1.2 on 2022-10-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
        ),
    ]
