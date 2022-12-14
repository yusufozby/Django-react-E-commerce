# Generated by Django 4.1.2 on 2022-10-25 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_productsmodel_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.categorymodel'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='img',
            field=models.FileField(null=True, upload_to='products/'),
        ),
    ]
