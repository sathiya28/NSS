from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camp',
            fields=[
                ('title', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapling', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=160)),
                #  ('start_date', models.DateField()),
                #  ('end_date',models.DateField()),
                ('images', models.ImageField('images')),
               
            ],
        ),
    ]