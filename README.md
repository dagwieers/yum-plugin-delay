yum-plugin-delay
================

Delay updating packages that are newer than X hours.

This yum plugin makes it possible to delay packages for a certain time after they have hit the repository. This could be useful when you like to automatically update servers by default, but want to have some protection against rogue packages.

By using a different delay for a set of servers, one can avoid having all systems impacted by a specific bug at roughly the same time.

In case rogue packages may be pulled from a repository, delaying the installation of packages for a specific time might help them not affect your systems. (e.g. on Red Hat Network or Red Hat Satellite, packages are never pulled, but when using mrepo/rhnget, you can still have this benefit)


Use case
--------
Consider a set of hardened minimal jumphosts. For security it is a requirement that security updates are applied as soon as they are available, however since these servers are considered 'sensitive' privileged access is restricted and made hard. However since these servers also provide (direct) access to all other systems, it is also essential that they are high-available.

By having a different delay (in this case up to 3 days), we can guarantee that in case there is a problematic update, not all servers will have this problematic package, while still having automatic updates enabled and an acceptable timeframe in which unavailability is detectable by the users.


Usage
-----
The configuration file lets you enable/disable the plugin, and configure a delay time (in hours).

On the command line you have the option to override the delay time (e.g. to disable the plugin by setting the delay to 0).

    yum update --delay 0

When the plugin is actived, it will clearly display the delay for packages:

    Delaying packages newer than 72 hours

And if packages are being delayed, the plugin will provide you with all the required information to see what is going on:

    --> Delaying firefox-25.0.1-1.el6.remi.x86_64 for 12 more hours (updated on 2013-11-16 13:00)
    --> Delaying xulrunner-last-25.0.1-1.el6.remi.x86_64 for 12 more hours (updated on 2013-11-16 13:00)


Feedback
--------
Send your feedback, ideas or bugfixes to:

    https://github.com/dagwieers/yum-plugin-delay/issues
