#
# Copyright (C) 2019 FreeIPA Contributors see COPYING for license
#

import json
import logging
import pkg_resources
import sys

from ipahealthcheck.core.core import RunChecks

logging.basicConfig(format='%(message)s')
logger = logging.getLogger()


def main():
    checks = RunChecks(['pkihealthcheck.registry'],
             '/etc/pki/healthcheck.conf')
    sys.exit(checks.run_healthcheck())
