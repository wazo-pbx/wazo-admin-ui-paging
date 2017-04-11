# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class PagingService(BaseConfdService):

    resource_confd = 'pagings'

    def create(self, resource):
        paging_created = super(PagingService, self).create(resource)
        resource['id'] = paging_created['id']
        self._update_members_callers(resource)

    def update(self, resource):
        super(PagingService, self).update(resource)
        self._update_members_callers(resource)

    def _update_members_callers(self, paging):
        members = paging.get('members')
        callers = paging.get('callers')

        if members:
            self._update_members_to_paging(paging, self._generate_users(members))
        if callers:
            self._update_callers_to_paging(paging, self._generate_users(callers))

    def _update_members_to_paging(self, paging, members):
        return confd.pagings.relations(paging).update_user_members(members)

    def _update_callers_to_paging(self, paging, callers):
        return confd.pagings.relations(paging).update_user_callers(callers)

    def _generate_users(self, users):
        return [{'uuid': user} for user in users]
