# Generated by Django 4.2.5 on 2023-09-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_delete_bookingtable_delete_menutable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('num_people', models.IntegerField()),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='Inventory',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='Price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='Title',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default=0, max_length=230),
            preserve_default=False,
        ),
    ]