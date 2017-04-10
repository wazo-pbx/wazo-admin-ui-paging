# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import SubmitField, StringField, BooleanField, SelectMultipleField

from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.form import BaseForm


class PagingForm(BaseForm):
    name = StringField('Name', [InputRequired()])
    context = StringField(default='default')
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
