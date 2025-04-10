# Generated by Django 5.1.1 on 2024-11-12 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='achievement',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='core.badge'),
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.testchoices')),
            ],
            options={
                'verbose_name': 'Choice Answer',
                'verbose_name_plural': 'Choice Answers',
            },
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testchoices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testquestion'),
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.usernotes')),
                ('TestScore', models.IntegerField(default=0)),
                ('TestTotalScore', models.IntegerField(default=0)),
                ('TestDateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'User Test',
                'verbose_name_plural': 'User Test',
            },
        ),
        migrations.AddField(
            model_name='usernotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userflashcards',
            name='noteID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usernotes'),
        ),
        migrations.AlterUniqueTogether(
            name='achievement',
            unique_together={('user', 'badge')},
        ),
        migrations.AddField(
            model_name='testquestion',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usertest'),
        ),
    ]
