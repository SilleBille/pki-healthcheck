#
# Copyright (C) 2019 FreeIPA Contributors see COPYING for license
#

from cshealthcheck.cs.plugin import CSPlugin, registry
from ipahealthcheck.core.plugin import Result, duration
from ipahealthcheck.core import constants


@registry
class CSExpirationCheck(CSPlugin):

    @duration
    def check(self):
        yield Result(self, constants.SUCCESS)
