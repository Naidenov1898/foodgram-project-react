# Generated by Django 4.0 on 2022-07-07 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, default='#', max_length=7, null=True, validators=[django.core.validators.MinLengthValidator(6, 'Цветовой HEX-код')], verbose_name='Цветовой HEX-код'),
        ),
    ]