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

    def _populate_form(self, form):
        users = self.service.get_users()
        users = self._user_list(users['items'])
        form.members.choices = users
        form.callers.choices = users
        return form

    def _map_resources_to_form(self, resources):
        members = self._get_user(resources['paging']['members']['users'])
        callers = self._get_user(resources['paging']['callers']['users'])
        return self.form(data=resources['paging'], members=members, callers=callers)

    def _user_list(self, users):
        return [(user['uuid'], u"{} {}".format(user['firstname'], user['lastname']))
                 for user in users]

    def _get_user(self, users):
        return [user['uuid'] for user in users]
