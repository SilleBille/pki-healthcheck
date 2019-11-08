#
# Copyright (C) 2019 FreeIPA Contributors see COPYING for license
#

from ipahealthcheck.core.plugin import Plugin, Registry


class CSPlugin(Plugin):
    def __init__(self, registry):
        super(CSPlugin, self).__init__(registry)


class CSRegistry(Registry):
    def initialize(self, framework):
        pass


registry = CSRegistry()
