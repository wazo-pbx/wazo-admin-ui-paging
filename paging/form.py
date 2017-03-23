# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import StringField
from wtforms.fields import BooleanField
from wtforms.fields import SelectMultipleField

from wtforms.validators import InputRequired


class PagingForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    number = StringField('Number', [InputRequired()])
    members = SelectMultipleField('Members', choices=[])
    callers = SelectMultipleField('Callers', choices=[])
    announce_caller = BooleanField('Announce caller')
    announce_sound = StringField('Announce sound')
    caller_notification = BooleanField('Play notification to caller')
    duplex = BooleanField('Duplex audio')
    enabled = BooleanField('Enabled')
    ignore_forward = BooleanField('Ignore forward')
    record = BooleanField('Announce caller')
    submit = SubmitField('Submit')
