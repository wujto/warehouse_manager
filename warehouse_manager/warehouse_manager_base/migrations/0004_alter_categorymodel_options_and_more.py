# Generated by Django 4.0.2 on 2022-02-12 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_manager_base', '0003_alter_productmodel_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['name'], 'permissions': [('is_manager', 'Can create, edit and delete')], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='customusermodel',
            options={'ordering': ['first_name'], 'permissions': [('is_admin', 'Can create and delete')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='localizationmodel',
            options={'ordering': ['name'], 'permissions': [('is_manager', 'Can create, edit and delete')], 'verbose_name': 'localization', 'verbose_name_plural': 'localizations'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['name'], 'permissions': [('is_manager', 'Can create, edit and delete')], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productsetmodel',
            options={'ordering': ['name'], 'permissions': [('is_manager', 'Can create, edit and delete')], 'verbose_name': 'products set', 'verbose_name_plural': 'products sets'},
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='localization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='warehouse_manager_base.localizationmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='warehouse_manager_base.categorymodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='localization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='warehouse_manager_base.localizationmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='warehouse_manager_base.productsetmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ConfirmationOfTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('REJECTED', 'Rejected')], max_length=15)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_confirmations', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='confirmations', to='warehouse_manager_base.productmodel')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient_confirmations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'confirmation',
                'verbose_name_plural': 'confirmations',
                'ordering': ['-date'],
                'permissions': [('is_owner', 'Can create and delete'), ('is_recipient', 'Can edit status and delete')],
            },
        ),
    ]
