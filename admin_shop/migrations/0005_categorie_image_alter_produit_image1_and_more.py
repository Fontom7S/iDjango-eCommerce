# Generated by Django 4.0.4 on 2022-05-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_shop', '0004_profile_facebook_urls_profile_linkded_urls_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image1',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
