from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primary Key')),
                ('description', models.CharField(max_length=100, verbose_name='좌석 정보')),
                ('name', models.CharField(max_length=30, verbose_name='카테고리 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primary Key')),
                ('name', models.CharField(max_length=30, verbose_name='가게 이름')),
                ('introduction', models.TextField(verbose_name='가게 설명')),
                ('address', models.CharField(max_length=30, verbose_name='가게 주소')),
                ('number', models.CharField(max_length=30, verbose_name='가게 전화번호')),
                ('waiting_state', models.IntegerField(default=1)),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('end_time', models.IntegerField(blank=True, null=True)),
                ('start_time', models.IntegerField(null=True)),
                ('end_time', models.IntegerField(null=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_store', to='whytingapp.store')),
            ],
        ),
        migrations.CreateModel(
            name='SeatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='store_image')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_image', to='whytingapp.seat')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_store', to='whytingapp.store'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='store_image')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_image', to='whytingapp.store')),
            ],
        ),
    ]
