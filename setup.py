from setuptools import find_packages, setup


setup(
    name='cshealthcheck',
    version='0.1',
    namespace_packages=['cshealthcheck'],
    package_dir={'': 'src'},
    # packages=find_packages(where='src'),
    packages=[
        'cshealthcheck.core',
        'cshealthcheck.cs',
    ],
    entry_points={
        # creates bin/cs-healthcheck
        'console_scripts': [
            'cs-healthcheck = cshealthcheck.core.main:main',
        ],
        # register the plugin with ipa-healthcheck
        'ipahealthcheck.registry': [
            'cshealthcheck.cs = cshealthcheck.cs.plugin:registry',
        ],
        # register the plugin with cs-healthcheck
        'cshealthcheck.registry': [
            'cshealthcheck.cs = cshealthcheck.cs.plugin:registry',
        ],
        # plugin modules for cshealthcheck.cs registry
        'cshealthcheck.cs': [
            'cs_certs = cshealthcheck.cs.certs',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    setup_requires=['pytest-runner',],
    tests_require=['pytest',],
)
