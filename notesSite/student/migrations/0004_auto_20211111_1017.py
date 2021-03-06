# Generated by Django 3.2.6 on 2021-11-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=100)),
                ('result_detail', models.CharField(max_length=200)),
                ('uploaded_time', models.CharField(max_length=50)),
                ('related_dep', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='result',
            name='result_detail',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='result',
            name='result_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='material_detail',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='material_title',
            field=models.CharField(max_length=100),
        ),
    ]
