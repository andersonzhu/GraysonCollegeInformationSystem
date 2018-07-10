# Generated by Django 2.0.5 on 2018-05-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectionItemByYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('isFall', models.IntegerField(choices=[(1, 'Fall'), (0, 'Spring')])),
                ('semester', models.CharField(max_length=20)),
                ('numberOfStudents', models.IntegerField()),
                ('attemptedCredits', models.IntegerField()),
                ('contactHours', models.IntegerField()),
                ('unemploymentRateLastYear', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
