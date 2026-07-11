---
icon: material/code-block-braces
---

# Permission Layer
This page provides information on the workings of the permission layer and how to use it.

## Permission tree / path
Everything that is handled by the permission layer is found in the permission tree. 
The tree has its root at ```/```.
The currently only child of the the root is ```command```, and it has all commands as its children.

At then end, this gives you e.g for the command ```spawm``` this tree: ```/``` - ```command``` - ```spawn```.
We can join them into one permission path, which would look like this: ```/command/spawn```

## Whitelisting 
```/perm add whitelist <permissionPath>```

Whitelisting a permission path gives the user not only access to the permission path itself, but also all its children in the tree. 
E.g if you give a user the permission to use ```/command```, this user can now run every command.

## Blacklisting 
```/perm add blacklist <permissionPath>```

Blacklisting works similarly to whitelisting, but instead of allowing the user to use the permission path and all its children, it blocks them. E.g if you add ```/command``` to someone's whitelist, but then you add ```/command/spawn``` to their blacklist, they can run every command except spawn

If a permission is both whitelisted and blacklisted, the blacklist takes priority.
