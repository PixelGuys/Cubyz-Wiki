This page provides information on server setup, maintenance, updates, and permissions. (for v[[0.2.0]] and up)

== Requirements ==
The game requires a GPU with drivers supporting [https://www.khronos.org/conformance/adopters/conformant-products/opengl OpenGL 4.6]. Supported operating systems include Windows and Linux (macOS is not currently supported).

== Installation & Setup ==
Start by selecting which version of Cubyz you want to host the server for (e.g., [[0.2.0]] or the master branch). You can download the game [https://github.com/PixelGuys/Cubyz/releases here].

After extracting the files, run the game and create a world. Here, you can configure the game mode, world seed, and other settings. You can read more in the Configuration section.

Once you are inside the world, open the menu and press the '''“Invite Players”''' button. There you will see your public IP address, including the port. This address is used to allow others to join your server. After scrolling down, you will need to enable '''“Allow Public Access”''' to let players outside your local network connect to your server.

'''NOTE:''' ''You will need to port forward to allow external access which is explained in the Networking Section.''

== Configuration ==

=== Headless Server ===
A headless server allows Cubyz to run without a graphical interface, which is useful for dedicated servers.

Inside the Cubyz directory you will find "'''launchConfig.zig'''" there you can set "'''.headlessServer ='''" to "'''true"''' you will also be required to change "'''.autoEnterWorld''' '''='''" to the name of your world.

=== Changing the Default Port ===
You can change the server port by editing the settings file.

Inside the Cubyz directory you will have to enter the "'''src'''" folder in which you will find "'''settings.zig'''" there you want to change the "'''defaultPort: u16 = 47649''';" to your custom port, note that you will have to update your port forwarding settings.

== Networking ==

=== Port Forwarding ===
To Port forward you will first need to login into your Home Router, to access the admin panel you will need to find your router's local ip address and login details.

==== How to find Router's IP address ====

* Windows - Open CMD or Terminal and type "'''ipconfig'''" then search for "'''Default Gateway'''"
* Linux - Open Terminal and type "'''ip a'''" then search for "'''Gateway IP'''"
* Mac - Open Terminal and type "'''route -n get default'''"

Once you acquire the gateway IP, you want to insert it into a browser url and press enter, this will open up your admin panel.

==== How to find Router's Login Details ====
The default login details are usually printed on a label on the back or bottom of the router.

If these details do not work, you may need to reset the router. To do this, press and hold the reset button (usually a small pinhole) for about 10–30 seconds until the device restarts.

==== How to find Port Forwarding Section ====
Once you have logged into the router’s admin panel, look for the Port Forwarding section. The location and name of this setting can vary depending on the router model.

It may be found under the LAN or Advanced settings menu, and it can also be labeled differently, such as Port Mapping, NAT Forwarding, or Port Triggering.

==== Port Forwarding ====
On this page, you will need to enter your device’s local IP address (the device hosting the game server).

You can find it in the same way as your Default Gateway. It will be labeled as '''IPv4 Address''' and usually looks like <code>192.168.x.x</code> or <code>10.0.x.x</code>, depending on your network.

Then it will ask for the port you want to allow. This should be the same port shown in the “Invite Players” section of the game. (eg.47659)

Then select the UDP Protocol and hit save.

== Permissions ==
To give a player permissions using the [[permission layer]], use the following command:
 /perm add whitelist @<playerIndex> <path>
To remove a player permissions, use the following command:
 /perm remove whitelist @<playerIndex> <path>

==== Explanation ====
<code>@<playerIndex></code> is the player’s ID. You can find it by enabling “Show Player ID” in the social tab, or as a server owner, by checking the <code>players</code> folder (config files are named after the player ID).

<code><path></code> is the permission you want to grant. Some useful examples:

* <code>/</code> - Grants full admin privileges

* <code>/command/spawn</code> - Grants access to the spawn command

== Security & Maintenance ==

=== Updating to a New Version ===
Updates are currently manual. Download the latest version and copy over any add-ons or custom configurations you previously used.

=== World Backup ===
Currently, you need to manually create a copy of your world to back it up, but third-party scripts are available to automate the process, you can find your world saves here:
*Windows - C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME

* Linux - /home/USERNAME/.cubyz/saves/WORLD_NAME

=== Server security ===
Port forwarding and sharing your public IP exposes your network to the internet, making you vulnerable to DDoS attacks, unauthorized access, and other security threats.

Here are some ways to improve your server’s security:

* '''Use a VPS (Virtual Private Server):''' Hosting your server on a VPS keeps your home IP address private and isolates it from your personal network. However, VPS services typically require a monthly or annual fee, and can become more expensive over time compared to hosting locally.
* '''Use a domain''' '''name:''' Services like Cloudflare can hide your real IP address and provide additional protection, such as DDoS mitigation and traffic filtering. This is commonly used with a custom domain name, allowing players to connect using an address like <code>ashframe.net</code> instead of your public IP.  Domain names can be purchased cheaply from providers such as Namecheap, with prices typically around £10 per year.
* '''Use a relay (VPS proxy):''' A VPS can also be used as a relay (proxy) to hide your home IP address by routing player connections through it. However, this only works if direct access to your server is blocked; otherwise, your real IP may still be exposed. This setup can also increase latency, which may negatively impact players.
'''''Note''': Additional precautions include using a firewall to limit access, running the server in an isolated environment, keeping software up to date.''

== Troubleshooting ==

== Third-Party Services and Add-ons ==

=== Add-ons ===
Add-ons are community-made extensions that add or modify content in Cubyz, such as items, biomes, and gameplay features.

==== Downloading Add-ons ====
Add-ons can be downloaded straight from the discord server in the [https://discord.gg/jM96g8pr25 #addons-mods] channel, or you can use a online marketplace available [https://addons.ashframe.net/ here]

==== Installing Add-ons ====
Installing add-ons is straightforward. After downloading an add-on, navigate to your world save folder:

* Windows - C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME

* Linux - /home/USERNAME/.cubyz/saves/WORLD_NAME

Extract the add-on, then place its folder into the <code>assets</code> folder inside your world folder.

'''''Note:''' If you are hosting or connecting to a server that has add-ons installed, they will automatically download for you and other players''.

=== Discord Bot ([https://github.com/AMerkuri Mercur]) ===
Mercur's bot enables bi-directional communication between a Discord server and a Cubyz server. It can also send server status to third-party websites such as the [https://servers.ashframe.net/ Cubyz Server List].

==== Installation ====
Install the required dependencies:

Debian / Ubuntu 
 sudo apt update 
 sudo apt install nodejs npm
Arch Linux
 sudo pacman -S nodejs npm

==== Setup ====
Create a folder for the bot (e.g. <code>Mercur_Bot</code>) open a terminal inside that folder and run the following command:
 npx cubyz-discord-relay@latest
If no <code>config.json</code> file is found, the bot will automatically generate one and exit.

==== Configuration ====
Open the generated <code>config.json</code> file and update all required fields, you can read more in the Cubyz Server List Section under.

After updating the configuration, run the command again:
 npx cubyz-discord-relay@latest
'''''Note''': If you are running Cubyz 0.0.0, use version <code>@2.4.3</code> instead of <code>@latest</code>.''

==== Updating ====
To update the bot you just need to use the same command:
 npx cubyz-discord-relay@latest
To generate the latest <code>config.json</code>, rename your existing file to (e.g. <code>old_config.json</code>), then run the command again. A new config will be created, then copy your settings from the old file into the new one, that's it.

=== Cubyz Server List ([https://github.com/iNiKKo iNiKKo]) ===

==== Requirements ====
<code>iconUrl</code> requirements:

- Resolution: '''318 × 130'''

- Format: '''PNG'''

==== Configuration ====
      <code>enabled:</code> true

True will broadcast the following information on the website, False will disable it.

      <code>serverName:</code> "NAME_OF_YOUR_SERVER",

      <code>serverIp:</code> "HOSTNAME_OR_IP_ADDRESS",

      <code>serverPort:</code> YOUR_GAME_PORT,

      <code>description:</code> "SHORT_SERVER_DESCRIPTION",

      <code>iconUrl:</code> "DIRECT_URL_TO_IMAGE",

''Upload your image to an image hosting service such as [https://imgbb.com/ ImgBB] to obtain a direct image URL.''

      <code>discordServer:</code> "DISCORD_INVITE_LINK",

      <code>customClientDownloadUrl:</code> "CUSTOM_CLIENT_DOWNLOAD_LINK"

'''''Note''': <code>discordServer</code> and <code>customClientDownloadUrl</code> are '''not currently displayed''' on the website.''

=== CubyzHub - Addons ([https://github.com/iNiKKo iNiKKo]) ===