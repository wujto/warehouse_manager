# Generated by Django 4.0.2 on 2022-06-01 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_manager_base', '0014_alter_customusermodel_localization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='localization',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET, related_name='users', to='warehouse_manager_base.localizationmodel'),
        ),
    ]
