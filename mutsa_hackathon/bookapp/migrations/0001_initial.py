from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('whytingapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whytingapp', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primary Key')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_customer', to=settings.AUTH_USER_MODEL)),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_seat', to='whytingapp.seat')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_store', to='whytingapp.store')),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_time', to='whytingapp.time')),
            ],
        ),
    ]
