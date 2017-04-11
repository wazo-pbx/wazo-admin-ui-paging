# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import PagingForm


class PagingView(BaseView):

    form = PagingForm
    resource = 'paging'

    @classy_menu_item('.pagings', 'Pagings', order=4, icon="bullhorn")
    def index(self):
        return super(PagingView, self).index()

    def _map_resources_to_form(self, resource):
        members = self._get_user(resource['members']['users'])
        callers = self._get_user(resource['callers']['users'])
        form = self.form(data=resource, members=members, callers=callers)
        form.members.choices = self._build_setted_choices(resource['members']['users'])
        form.callers.choices = self._build_setted_choices(resource['callers']['users'])
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

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('paging', {}))
        return form
