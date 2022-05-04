# Generated by Django 4.0.4 on 2022-05-04 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='city_of_count',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='Prices_prod',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='description_prod',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='label_marque_prod',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='label_prod',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='quantity_prod',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='size_prod',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sexe',
        ),
        migrations.AddField(
            model_name='city',
            name='city_of_count',
            field=models.ForeignKey(default='inconnu', on_delete=django.db.models.deletion.CASCADE, to='admin_shop.country'),
        ),
        migrations.AddField(
            model_name='produit',
            name='Prices',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='produit',
            name='description',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='produit',
            name='label',
            field=models.CharField(default='Produit', max_length=250),
        ),
        migrations.AddField(
            model_name='produit',
            name='marque',
            field=models.ForeignKey(default='inconnu', on_delete=django.db.models.deletion.CASCADE, to='admin_shop.marque'),
        ),
        migrations.AddField(
            model_name='produit',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produit',
            name='size',
            field=models.CharField(choices=[('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='L', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Country',
            field=models.ForeignKey(default='inconnu', on_delete=django.db.models.deletion.CASCADE, to='admin_shop.country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='fistname',
            field=models.CharField(default='inconnu', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='inconnu', max_length=200),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
