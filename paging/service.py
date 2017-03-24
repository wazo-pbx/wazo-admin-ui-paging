# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class PagingService(BaseConfdService):

    resource_name = 'paging'
    resource_confd = 'pagings'

    def create(self, resources):
        resource = super(PagingService, self).create(resources)
        self._update_members_callers(resources, resource)

    def update(self, resources):
        super(PagingService, self).update(resources)
        self._update_members_callers(resources)

    def _update_members_callers(self, resources, resource=None):
        paging = resources.get(self.resource_name)
        members = paging.get('members')
        callers = paging.get('callers')

        if resource == None:
            resource = paging['id']

        if members:
            self._update_members_to_paging(resource, self._generate_users(members))
        if callers:
            self._update_callers_to_paging(resource, self._generate_users(callers))

    def get_users(self):
        return self._confd.users.list()

    def _update_members_to_paging(self, paging, members):
        return self._confd.pagings.relations(paging).update_user_members(members)

    def _update_callers_to_paging(self, paging, callers):
        return self._confd.pagings.relations(paging).update_user_callers(callers)

    def _generate_users(self, users):
        return [{'uuid': user} for user in users]
