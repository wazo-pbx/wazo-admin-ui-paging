# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import PagingForm


class PagingSchema(BaseSchema):

    context = fields.String(default='default')

    class Meta:
        fields = extract_form_fields(PagingForm)


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

    def _map_resources_to_form(self, resources):
        members = self._get_user(resources['paging']['members']['users'])
        callers = self._get_user(resources['paging']['callers']['users'])
        form = self.form(data=resources['paging'], members=members, callers=callers)
        form.members.choices = self._build_setted_choices(resources['paging']['members']['users'])
        form.callers.choices = self._build_setted_choices(resources['paging']['callers']['users'])
        return form

    def _get_user(self, users):
        return [user['uuid'] for user in users]

    def _build_setted_choices(self, users):
        results = []
        for user in users:
            if user.get('lastname'):
                text = '{} {}'.format(user.get('firstname'), user['lastname'])
            else:
                text = user.get('firstname')
            results.append((user['uuid'], text))
        return results
