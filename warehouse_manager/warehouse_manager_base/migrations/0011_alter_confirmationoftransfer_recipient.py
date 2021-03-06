# Generated by Django 4.0.2 on 2022-05-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_manager_base', '0010_alter_confirmationoftransfer_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationoftransfer',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='recipient_confirmations', to=settings.AUTH_USER_MODEL),
        ),
    ]
