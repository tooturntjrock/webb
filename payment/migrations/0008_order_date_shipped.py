# Generated by Django 5.0.3 on 2024-06-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]