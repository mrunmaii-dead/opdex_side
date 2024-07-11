# Generated by Django 5.0.6 on 2024-06-22 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docui', '0002_medicine_remove_appointment_medcine_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='medcines',
            new_name='medicines',
        ),
        migrations.CreateModel(
            name='AppointmentMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docui.appointment')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docui.medicine')),
            ],
        ),
    ]