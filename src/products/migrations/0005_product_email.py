# Generated by Django 4.0.6 on 2022-07-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default='distepstar@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]