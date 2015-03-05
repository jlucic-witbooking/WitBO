# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WitbookingUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('default_db', models.CharField(max_length=64, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'db_table': 'auth_user',
                'swappable': 'AUTH_USER_MODEL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WitbookingPermission',
            fields=[
                ('permission_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='auth.Permission')),
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('establishment', models.CharField(max_length=255, verbose_name='establishment')),
            ],
            options={
            },
            bases=('auth.permission',),
        ),
        migrations.AddField(
            model_name='witbookinguser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='witbooking_auth.WitbookingPermission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
