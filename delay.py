#!/usr/bin/python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Copyright 2013 by Dag Wieers

from yum.plugins import TYPE_CORE
import time

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

def timefmt(secs):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(secs))

def config_hook(conduit):
    global delay_time
    delay_time = int(conduit.confString('main', 'delay'))

    parser = conduit.getOptParser()
    if not parser:
        return

    if hasattr(parser, 'plugin_option_group'):
        parser = parser.plugin_option_group

    def delay(opt, key, val, parser):
        global delay_time
        delay_time = int(val)

    parser.add_option('--delay', action='callback',
                      callback=delay, dest='delay', default=0, type=int,
                      help='Delay updates newer than DELAY hours')

def exclude_hook(conduit):
    if delay_time == 0:
        conduit.info(1, 'Delaying disabled on command line')
        return

    conduit.info(1, 'Delaying packages newer than %d hours' % delay_time)
    for pkg in conduit._base.doPackageLists(pkgnarrow='updates'):

        if conduit._base.conf.debuglevel > 2:
            conduit.info(1, 'delay:Package %s has filetime %s, buildtime %s and committime %s' %
                (pkg.ui_envra, timefmt(pkg.filetime), timefmt(pkg.buildtime), timefmt(pkg.committime)))

        if hasattr(pkg, 'filetime'):
            pkgtime = pkg.filetime
        elif hasattr(pkg, 'buildtime'):
            pkgtime = pkg.buildtime
        else:
            pkgtime = pkg.committime

        age = time.time() - pkgtime
        if age <= delay_time * 60 * 60:
            delay = ( delay_time * 60 * 60 - age ) / 60 / 60
            conduit.info(1, '--> Delaying %s for %d more hours (updated on %s)' % (pkg.ui_envra, delay, timefmt(pkgtime)))
            conduit.delPackage(pkg)
