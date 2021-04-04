# Generated by Django 3.1.7 on 2021-04-04 12:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuario_id', models.UUIDField(default=uuid.uuid4)),
                ('endereco_id', models.UUIDField(default=uuid.uuid4)),
                ('pizza_id', models.IntegerField()),
                ('pedido_entregue', models.BooleanField(default=False)),
            ],
        ),
    ]