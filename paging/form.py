# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import TextField

from wtforms.validators import InputRequired


class PagingForm(FlaskForm):
    name = TextField('Name', [InputRequired()])
    number = TextField('Number', [InputRequired()])
    submit = SubmitField('Submit')
