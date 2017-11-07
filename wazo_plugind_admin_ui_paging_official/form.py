# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (FieldList,
                            FormField,
                            HiddenField,
                            SubmitField,
                            StringField,
                            BooleanField,
                            SelectMultipleField)

from wtforms.validators import InputRequired, Length, Regexp

from wazo_admin_ui.helpers.form import BaseForm


class UserForm(BaseForm):
    uuid = HiddenField()
    firstname = HiddenField()
    lastname = HiddenField()


class MembersForm(BaseForm):
    user_uuids = SelectMultipleField('Members', choices=[])
    users = FieldList(FormField(UserForm))


class CallersForm(BaseForm):
    user_uuids = SelectMultipleField('Callers', choices=[])
    users = FieldList(FormField(UserForm))


class PagingForm(BaseForm):
    name = StringField('Name', [InputRequired(), Length(max=128)])
    context = StringField(default='default')
    number = StringField('Number', [InputRequired(), Length(max=32), Regexp(r'^[0-9]+$')])
    members = FormField(MembersForm)
    callers = FormField(CallersForm)
    announce_caller = BooleanField('Announce caller')
    announce_sound = StringField('Announce sound', [Length(max=64)])
    caller_notification = BooleanField('Play notification to caller')
    duplex = BooleanField('Duplex audio')
    enabled = BooleanField('Enabled')
    ignore_forward = BooleanField('Ignore forward')
    record = BooleanField('Announce caller')
    submit = SubmitField('Submit')
