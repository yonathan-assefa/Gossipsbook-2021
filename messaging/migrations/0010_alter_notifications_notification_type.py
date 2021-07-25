# Generated by Django 3.2.4 on 2021-07-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_notifications_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notification_type',
            field=models.CharField(blank=True, choices=[('FR', 'FRIEND_REQUEST'), ('VT', 'VOTED_TRUE'), ('VF', 'VOTED_FALSE'), ('GC', 'GOSSIP_COMMENT'), ('CR', 'COMMENT_REPLY')], max_length=2, null=True),
        ),
    ]