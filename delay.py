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

def config_hook(conduit):
    global delay_time
    delay_time = int(conduit.confString('main', 'delay'))

def exclude_hook(conduit):
    conduit.info(3, "Delaying packages newer than %d hours" % delay_time)
    for pkg in conduit._base.doPackageLists(pkgnarrow='updates'):
        age = time.time() - pkg.committime
        if age <= delay_time * 60 * 60:
            delay = ( delay_time  * 60 * 60 - age ) / 60 / 60
            conduit.info(3, "--> delaying %s.%s for %d more hours" % (pkg.name, pkg.arch, delay))
            conduit.delPackage(pkg)
