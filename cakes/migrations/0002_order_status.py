# Generated by Django 4.0.4 on 2022-04-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[(None, 'Укажите статус заказа'), ('n', 'Новый'), ('a', 'Принят'), ('p', 'Готовится'), ('d', 'Передан в доставку'), ('c', 'Выполнен')], max_length=20, verbose_name='Статус заказа'),
        ),
    ]
