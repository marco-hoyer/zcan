from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.integrationtest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('copy_resources')
use_plugin('filter_resources')

name = "zcan"

authors = [Author('Marco Hoyer', 'marco_hoyer@gmx.de')]
description = 'zcan - CAN bus adapter daemon for Zehnder ComfoAir Q series ventilation systems'
license = 'APACHE LICENSE, VERSION 2.0'
summary = 'CAN bus adapter daemon for Zehnder ComfoAir Q series ventilation systems'
url = 'https://github.com/marco-hoyer/zcan'
version = '0.0.1'

default_task = ['clean', 'analyze', 'package']


@init
def set_properties(project):
    project.build_depends_on("unittest2")
    project.build_depends_on("mock")
    project.depends_on("argparse")
    project.depends_on("pyyaml")
    project.depends_on("xknx")
    project.depends_on("influxdb")
    project.depends_on("pyserial")
    project.depends_on("click")

    project.set_property('integrationtest_inherit_environment', True)
    project.set_property('coverage_break_build', False)
    project.set_property('install_dependencies_upgrade', True)

    project.set_property('copy_resources_target', '$dir_dist')

    project.get_property('filter_resources_glob').extend(['**/zcan/__init__.py'])
    project.set_property('distutils_console_scripts', ['zcan=zcan.cli:cli'])

    project.set_property('distutils_classifiers', [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration'
    ])
