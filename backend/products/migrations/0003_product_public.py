# Generated by Django 4.1.4 on 2023-12-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
