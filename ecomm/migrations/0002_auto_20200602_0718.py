# Generated by Django 3.0.6 on 2020-06-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='ecomm/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]