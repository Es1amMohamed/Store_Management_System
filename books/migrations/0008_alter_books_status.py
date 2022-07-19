# Generated by Django 4.0.5 on 2022-07-19 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_books_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable'), ('Sold', 'Sold'), ('Rented', 'Rented'), ('Borrowed', 'Borrowed')], max_length=50),
        ),
    ]
