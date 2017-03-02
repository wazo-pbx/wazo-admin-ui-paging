# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema

from .form import PagingForm


class PagingSchema(BaseSchema):

    context = fields.String(default='default')

    class Meta:
        fields = ('name',
                  'number')


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'paging'

    paging = fields.Nested(PagingSchema)


class PagingView(BaseView):

    form = PagingForm
    resource = 'paging'
    schema = AggregatorSchema

    @classy_menu_item('.pagings', 'Pagings', order=4, icon="bullhorn")
    def index(self):
        return super(PagingView, self).index()
