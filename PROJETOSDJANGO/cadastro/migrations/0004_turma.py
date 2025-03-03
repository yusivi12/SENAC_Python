# Generated by Django 4.2.7 on 2024-10-16 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateTimeField()),
                ('dataTermino', models.DateTimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.curso')),
            ],
        ),
    ]
