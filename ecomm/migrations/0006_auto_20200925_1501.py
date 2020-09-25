# Generated by Django 3.0.8 on 2020-09-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0005_auto_20200925_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('P', 'primary')], max_length=1),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
