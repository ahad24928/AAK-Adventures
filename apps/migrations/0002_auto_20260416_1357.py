from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('booking_type', models.CharField(max_length=20)),
                ('item_id', models.IntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('test', models.CharField(default='ok', max_length=10)),
            ],
        ),
    ]
