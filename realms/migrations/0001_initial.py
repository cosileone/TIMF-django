# Generated by Django 2.0.1 on 2018-02-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('US', 'US'), ('EU', 'EU'), ('CN', 'CN'), ('TW', 'TW'), ('KR', 'KR')], max_length=2)),
                ('slug', models.CharField(max_length=100)),
                ('house', models.SmallIntegerField()),
                ('population', models.IntegerField()),
            ],
            options={
                'db_table': 'tblRealm',
                'ordering': ['id'],
            },
        ),
    ]
