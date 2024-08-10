# Generated by Django 5.1 on 2024-08-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('show', 'Show'), ('teatro', 'Apresentação Teatral'), ('orquestra', 'Orquestra'), ('musical', 'Musical'), ('humor', 'Show de Humor'), ('magica', 'Mágica'), ('arte', 'Arte'), ('tecnologia', 'Tecnologia'), ('gastronomia', 'Gastronomia'), ('esporte', 'Esporte'), ('cinema', 'Cinema'), ('workshop', 'Workshop')], max_length=50),
        ),
    ]
