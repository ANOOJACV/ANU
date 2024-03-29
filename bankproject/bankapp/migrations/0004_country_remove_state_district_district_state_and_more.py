# Generated by Django 4.1.5 on 2023-01-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='district',
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankapp.state'),
        ),
        migrations.RenameModel(
            old_name='Branch',
            new_name='State',
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankapp.country'),
        ),
    ]
