# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import PagingService
from .view import PagingView

paging = create_blueprint('paging', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        PagingView.service = PagingService(config['confd'])
        PagingView.register(paging, route_base='/pagings')
        register_flaskview(paging, PagingView)

        core.register_blueprint(paging)
