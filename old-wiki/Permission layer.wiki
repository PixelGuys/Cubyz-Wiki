This page provides information on the workings of the permission layer and how to use it.

== Permission tree / path ==
Everything that is handled by the permission layer is found in the permission tree. 
The tree has its root at <code>/</code>.
The currently only child of the the root is <code>command</code>, and it has all commands as its children.

At then end, this gives you e.g for the command <code>spawm</code> this tree: <code>/</code> - <code>command</code> - <code>spawn</code>.
We can join them into one permission path, which would look like this: <code>/command/spawn</code>

== Whitelisting ==
<code>/perm add whitelist <permissionPath></code>

Whitelisting a permission path gives the user not only access to the permission path itself, but also all its children in the tree. 
E.g if you give a user the permission to use <code>/command</code>, this user can now run every command.

== Blacklisting ==
<code>/perm add blacklist <permissionPath></code>

Blacklisting works similarly to whitelisting, but instead of allowing the user to use the permission path and all its children, it blocks them. E.g if you add <code>/command</code> to someone's whitelist, but then you add <code>/command/spawn</code> to their blacklist, they can run every command except spawn

If a permission is both whitelisted and blacklisted, the blacklist takes priority.