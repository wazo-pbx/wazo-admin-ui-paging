# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class PagingService(BaseConfdService):

    resource = 'paging'
    confd_resource = 'pagings'

    def create(self, resources):
        paging = resources.get(self.resource)
        members = paging.get('members')
        callers = paging.get('callers')

        paging = self._confd.pagings.create(paging)

        if members:
            self.add_members_to_paging(paging, self._generate_users(members))
        if callers:
            self.add_callers_to_paging(paging, self._generate_users(callers))

    def get_users(self):
        return self._confd.users.list()

    def add_members_to_paging(self, paging, members):
        return self._confd.pagings.relations(paging).update_user_members(members)

    def add_callers_to_paging(self, paging, callers):
        return self._confd.pagings.relations(paging).update_user_callers(callers)

    def _generate_users(self, users):
        return [{'uuid': user } for user in users]
