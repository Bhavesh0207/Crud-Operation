# Generated by Django 5.0 on 2024-02-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_carttable_cartstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carttable',
            name='orderid',
            field=models.IntegerField(null=True),
        ),
    ]
