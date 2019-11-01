#
# Copyright (C) 2019 FreeIPA Contributors see COPYING for license
#

import json
import logging
import pkg_resources
import sys

from ipahealthcheck.core.main import (
    find_plugins,
    run_service_plugins,
    run_plugins,
    list_sources,
    parse_options,
    limit_results)
from ipahealthcheck.core.config import read_config
from ipahealthcheck.core.plugin import json_to_results
from ipahealthcheck.core.output import output_registry
from ipahealthcheck.core import constants

logging.basicConfig(format='%(message)s')
logger = logging.getLogger()


def find_registries():
    return {
        ep.name: ep.resolve()
        for ep in pkg_resources.iter_entry_points('cshealthcheck.registry')
    }


def main():
    framework = object()
    plugins = []
    output = constants.DEFAULT_OUTPUT

    logger.setLevel(logging.INFO)

    options = parse_options(output_registry)

    if options.debug:
        logger.setLevel(logging.DEBUG)

    # Note that this reads the ipa-healthcheck config, override as needed
    config = read_config()
    if config is None:
        sys.exit(1)

    for name, registry in find_registries().items():
        try:
            registry.initialize(framework)
        except Exception as e:
            print("Unable to initialize %s: %s" % (name, e))
            sys.exit(1)
        for plugin in find_plugins(name, registry):
            plugins.append(plugin)

    for out in output_registry.plugins:
        if out.__name__.lower() == options.output:
            output = out(options)

    if options.list_sources:
        return list_sources(plugins)

    if options.infile:
        try:
            with open(options.infile, 'r') as f:
                raw_data = f.read()

            json_data = json.loads(raw_data)
            results = json_to_results(json_data)
            available = ()
        except Exception as e:
            print("Unable to import '%s': %s" % (options.infile, e))
            sys.exit(1)
        if options.source:
            results = limit_results(results, options.source, options.check)
    else:
        results, available = run_service_plugins(plugins, config,
                                                 options.source,
                                                 options.check)
        results.extend(run_plugins(plugins, config, available,
                                   options.source, options.check))

    if options.source and len(results.results) == 0:
        if options.check:
            print("Check '%s' not found in Source '%s'" %
                  (options.check, options.source))
        else:
            print("Source '%s' not found" % options.source)
        sys.exit(1)

    try:
        output.render(results)
    except Exception as e:
        logger.error('Output raised %s: %s', e.__class__.__name__, e)

    return_value = 0
    for result in results.results:
        if result.result != constants.SUCCESS:
            return_value = 1
            break

    sys.exit(return_value)
