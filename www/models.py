#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Models for user, north, south.
'''

import time, uuid

from transwarp.db import next_id, week_id
from transwarp.orm import Model, StringField, BooleanField, FloatField, TextField

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(updatable=False, ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(updatable=False, default=time.time)

class North(Model):
    __table__ = 'plan_north'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    site = StringField(ddl='varchar(50)')
    type = StringField(ddl='varchar(50)')
    item = StringField(ddl='varchar(500)')
    progress = StringField(ddl='varchar(50)')
    details =  TextField()
    ttcm = StringField(ddl='varchar(500)')
    owner = StringField(ddl='varchar(50)')
    week = StringField(ddl='varchar(50)', default=week_id)
    created_at = FloatField(updatable=False, default=time.time)

class South(Model):
    __table__ = 'plan_south'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    site = StringField(ddl='varchar(50)')
    type = StringField(ddl='varchar(50)')
    item = StringField(ddl='varchar(500)')
    progress = StringField(ddl='varchar(50)')
    details =  TextField()
    ttcm = StringField(ddl='varchar(500)')
    owner = StringField(ddl='varchar(50)')
    week = StringField(ddl='varchar(50)', default=week_id)
    created_at = FloatField(updatable=False, default=time.time)
