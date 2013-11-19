yum-plugin-delay
================

Delay updating packages that are newer than X hours.

This yum plugin makes it possible to delay packages for a certain time after they have hit the repository. This could be useful when you like to automatically update servers by default, but want to have some protection against rogue packages.

By using a different delay for a set of servers, one can avoid having all systems impacted by a specific bug at roughly the same time.

Use case
--------
Consider a set of hardened minimal jumphosts. For security it is a requirement that security updates are applied as soon as they are available, however since these servers are considered 'sensitive' privileged access is restricted and made hard. However since these servers also provide (direct) access to all other systems, it is also essential that they are high-available.

By having a different delay (in this case up to 3 days), we can guarantee that in case there is a problematic update, not all servers will have this problematic package, while still having automatic updates enabled and an acceptable timeframe in which unavailability is detectable by the users.
