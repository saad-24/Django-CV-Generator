# Generated by Django 3.2.11 on 2022-02-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20220131_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('academic_details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenure', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=20)),
                ('linkedin_profile', models.CharField(max_length=50)),
                ('github_profile', models.CharField(max_length=50)),
                ('portfolio_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
