from setuptools import find_packages, setup


setup(
    name='pkihealthcheck',
    version='0.1',
    namespace_packages=['pkihealthcheck'],
    package_dir={'': 'src'},
    # packages=find_packages(where='src'),
    packages=[
        'pkihealthcheck.core',
        'pkihealthcheck.cs',
    ],
    entry_points={
        # creates bin/pki-healthcheck
        'console_scripts': [
            'pki-healthcheck = pkihealthcheck.core.main:main',
        ],
        # register the plugin with ipa-healthcheck
        'ipahealthcheck.registry': [
            'pkihealthcheck.cs = pkihealthcheck.cs.plugin:registry',
        ],
        # register the plugin with pki-healthcheck
        'pkihealthcheck.registry': [
            'pkihealthcheck.cs = pkihealthcheck.cs.plugin:registry',
        ],
        # plugin modules for pkihealthcheck.cs registry
        'pkihealthcheck.cs': [
            'pki_certs = pkihealthcheck.cs.certs',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    setup_requires=['pytest-runner',],
    tests_require=['pytest',],
)
