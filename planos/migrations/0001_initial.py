from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacoteRepublica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoas', models.PositiveSmallIntegerField()),
                ('kg_semana', models.PositiveIntegerField()),
                ('preco_morador', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ciclos', models.PositiveSmallIntegerField()),
                ('coletas_semana', models.PositiveSmallIntegerField(default=1)),
                ('destaque', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'pacote de república',
                'verbose_name_plural': 'pacotes de república',
                'ordering': ['pessoas'],
            },
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('kg_mes', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('coletas_semana', models.PositiveSmallIntegerField(default=1)),
                ('prazo', models.CharField(max_length=40)),
                ('beneficios', models.TextField(blank=True, help_text='Um benefício por linha.')),
                ('destaque', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['preco'],
            },
        ),
    ]
