# Generated by Django 3.0.3 on 2020-08-20 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_store', '0002_auto_20200211_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bookImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bookName',
            new_name='name',
        ),
    ]
