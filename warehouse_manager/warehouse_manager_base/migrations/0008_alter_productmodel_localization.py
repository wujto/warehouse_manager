# Generated by Django 4.0.2 on 2022-05-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_manager_base', '0007_alter_productmodel_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='localization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='warehouse_manager_base.localizationmodel'),
        ),
    ]
