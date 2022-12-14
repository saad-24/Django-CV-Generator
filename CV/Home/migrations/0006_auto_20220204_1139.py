# Generated by Django 3.2.11 on 2022-02-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_delete_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Certifications',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AddField(
            model_name='top',
            name='academic_details',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='top',
            name='certificate_name',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='top',
            name='company_name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='top',
            name='content',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='top',
            name='degree',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='top',
            name='description',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='top',
            name='designation',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='top',
            name='institute_name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='top',
            name='period',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='top',
            name='skills',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='top',
            name='tenure',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='top',
            name='email',
            field=models.EmailField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='top',
            name='github_profile',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='top',
            name='linkedin_profile',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='top',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='top',
            name='phone',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='top',
            name='portfolio_link',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='top',
            name='title',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
