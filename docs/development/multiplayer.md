This page provides information on server setup, maintenance, updates, and permissions.

---

## Installation & Setup

Start by downloading the version of Cubyz you want to host [here](https://github.com/PixelGuys/Cubyz/releases). After downloading, extract the files to your preferred directory.

### Method 1: In-Game Hosting

This method allows you to start hosting really quickly, but requires that you keep your game running. The moment you leave the world, or close the game, all other players will be disconnected. 
While hosting a server in this way you can play the game in the same window with no issues.

1. Run the game, click the **Multiplayer** button, and select **Host World**.
2. Here Create & Configure your world settings (game mode, world seed, etc.) and launch the world.
3. Once inside, open the menu and click **Invite Player**.
4. Then click on **Invite** to let players outside your local network connect.
5. Note your public IP address and port displayed on this screen; external players will need this to join.

> **NOTE:** To allow external players to connect, you must port forward the displayed port. See the [Networking Section](#networking) for details.

!!! note

    To run the game your computer must meet [minimal requirements](../installation.html)


### Method 2: Headless Setup (Dedicated Server)

Headless servers are preferred when you want to host a server as a background task. Usually this is how you would host a full time server with use of [VPS](https://en.wikipedia.org/wiki/Virtual_private_server) or dedicated hardware. Healdess servers do not have an UI you can use to play the game, however if you wish to play Cubyz on same machine you use for hosting, you can open a separate Cubyz window and connect to the server this way.

1. Open the Cubyz directory and locate the `launchConfig.zig` file.
2. Set `.headlessServer =` to `true`.
3. Change `.autoEnterWorld =` to the exact name of your world.

> **NOTE:** A world must already exist on your system before completing this step. Run the game in normal mode to create one if you haven't already, then enter its name here.

#### Changing the Default Port (Optional)
If you need to change the server port from its default (47649):

1. Navigate to the `src` folder inside your Cubyz directory.
2. Open `settings.zig`.
3. Modify the line `defaultPort: u16 = 47649;` to your preferred port number.
4. *Remember to update your port forwarding rules to match this new port.*

---

## Networking

### Port Forwarding
To allow external players to connect to your Cubyz server, you need to port forward. This requires logging into your home router's admin panel using your router's local IP address and login details.

#### 1. Find Your Router's IP Address (Default Gateway)
Open your system's command line or terminal and run the appropriate command for your operating system:

* **Windows:** Open CMD or PowerShell and type `ipconfig`. Look for **Default Gateway**.
* **Linux:** Open a terminal and type `ip route | grep default` (or `ip a`) and look for the **Gateway IP**.

Once you have this IP address (usually something like `192.168.1.1` or `192.168.0.1`), paste it directly into your web browser's address bar and press **Enter** to open the router's login page.

#### 2. Find Your Router's Login Details
* **Default Credentials:** The default username and password are usually printed on a sticker on the back or bottom of your physical router.
* **Resetting the Router:** If the default details don't work and you forgot your custom password, locate the small pinhole reset button on the router. Press and hold it with a paperclip for 10–30 seconds until the lights flash. This resets the router to its factory defaults.

#### 3. Locate the Port Forwarding Section
The name of this section varies depending on your router brand. Look through the **Advanced**, **Security**, or **LAN** menus for labels such as **Port Forwarding**, **Port Mapping**, **NAT Forwarding**, **Virtual Server**, or **Port Triggering**.
#### 4. Configure the Port Forward Rule
Create a new rule with the following details:

* **Internal/Local IP Address:** This is the local IP of the machine actually hosting the server. You can find it using the same terminal commands from Step 1 (labeled as **IPv4 Address**, usually starting with `192.168.x.x` or `10.0.x.x`).
* **Port:** Enter the port used by your server. By default, Cubyz uses `47649` (or whichever port is shown in-game under the "Invite Players" menu).
* **Protocol:** Select **UDP**.

Save your changes, and your server is ready for external connections!

---

## Permissions

To manage player permissions using the permission layer, use the following commands:

* **Grant Permissions:** `/perm add whitelist @<playerIndex> <path>`
* **Remove Permissions:** `/perm remove whitelist @<playerIndex> <path>`

### Command Parameters
* `@<playerIndex>`: The unique ID of the player. You can find this by enabling "Show Player ID" in the in-game Social tab. Alternatively, as a server owner, you can check the `players` folder inside your world save directory (config files are named after each player's ID).
* `<path>`: The specific permission path you want to modify. 
  * `/` — Grants full administrator privileges.
  * `/command/spawn` — Grants access specifically to the `/spawn` command.

---

## Security & Maintenance

### Updating to a New Version
Updates are currently manual. Download the latest release, extract the files, and manually copy over any custom configurations from your previous server directory.

### World Backup
Currently, backups must be done manually. To back up your progress, create a copy of your specific world folder found here:

* **Windows:** `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`
* **Linux:** `/home/USERNAME/.cubyz/saves/WORLD_NAME`

### Server Security
Port forwarding and sharing your public IP address exposes your local network to the internet, making you vulnerable to DDoS attacks and unauthorized network access. Consider the following methods to protect your server:

* **Use a VPS (Virtual Private Server):** Hosting your server on a VPS keeps your home IP private and isolates the server from your personal devices. *Note: VPS hosting requires a monthly or annual subscription fee.*
* **Use a Domain Name & Proxy:** Services like Cloudflare can mask your real IP address and provide DDoS mitigation. This requires purchasing a cheap custom domain name (typically around £10/year from providers like Namecheap) so players connect via an address like `ashframe.net`.
* **Use a Relay (VPS Proxy):** You can route traffic through a cheap VPS proxy to hide your home IP, it may slightly increase player latency.

>  **Additional Precautions:** Always keep your host machine's firewall active, limit open ports to only what is strictly necessary, and run the server application in an isolated environment if possible.

---

## Third-Party Services & Add-ons

### Add-ons
Add-ons are community-made extensions that modify or introduce new content to Cubyz, such as items, biomes, recipes and other.

#### 1. Downloading Add-ons
You can download add-ons directly from the official Discord server in the [#addons-mods](https://discord.com/invite/jM96g8pr25) channel, or browse the online community asset marketplace [here](https://addons.ashframe.net/).

#### 2. Installing Add-ons

**Step 1:** Navigate to your world save directory:
<br>• **Windows:** `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`
<br>• **Linux:** `/home/USERNAME/.cubyz/saves/WORLD_NAME`

**Step 2:** Extract the downloaded add-on archive.

**Step 3:** Place the extracted folder directly into the `assets` folder inside your specific world folder.

> **NOTE:** If you install add-ons on a dedicated server, they will automatically sync and download for connecting players.

---

### Discord Bot ([Mercur](https://github.com/AMerkuri))
Mercur provides bi-directional chat communication between your Discord server and your Cubyz server, and also can transmits server status data to the [Cubyz Server List](#cubyz-server-list-inikko).
### Installation

Install the required dependencies.
### Debian / Ubuntu

```bash
sudo apt update
sudo apt install nodejs npm
```
### Arch Linux
```bash
sudo pacman -S nodejs npm
```
### Setup
1. Create a folder for the bot (for example, `Mercur_Bot`).
2. Open a terminal inside that folder.
3. Run:
```bash
npx cubyz-discord-relay@latest
```
If no `config.json` file is found, the bot will automatically generate one and then exit.
### Configuration
1. Open the generated `config.json` file.
2. Update all required fields. See the [Cubyz Server List](#cubyz-server-list-inikko) section for information about the server list configuration.
3. After saving your changes, run the bot again:
```bash
npx cubyz-discord-relay@latest
```
> **Note:** If you are running **Cubyz 0.0.0**, use `@2.4.3` instead of `@latest`.
```bash
npx cubyz-discord-relay@2.4.3
```
### Updating

To update the bot, simply run:

```bash
npx cubyz-discord-relay@latest
```

If a newer version includes changes to the configuration file:

1. Rename your current `config.json` (for example, to `old_config.json`).
2. Generate a new configuration file by running:

   ```bash
   npx cubyz-discord-relay@latest
   ```

3. Copy your settings from `old_config.json` into the newly generated `config.json`.

Your bot is now updated and ready to use.

---


### Cubyz Server List ([iNiKKo](https://github.com/iNiKKo))

Mercur can automatically submit your server information to the [Cubyz Server List](https://servers.ashframe.net/).

### Configuration

Enable or disable server list integration:

```json
enabled: true
```

- `true` – Broadcast your server information to the [Cubyz Server List](https://servers.ashframe.net/).
- `false` – Disable server list integration.

Configure the remaining fields in your `config.json`:

```json
serverName: "NAME_OF_YOUR_SERVER",
serverIp: "HOSTNAME_OR_IP_ADDRESS",
serverPort: YOUR_GAME_PORT,
description: "SHORT_SERVER_DESCRIPTION",
iconUrl: "DIRECT_URL_TO_IMAGE",
discordServer: "DISCORD_INVITE_LINK",
customClientDownloadUrl: "CUSTOM_CLIENT_DOWNLOAD_LINK"
```


### Server Icon

Upload your server icon to an image hosting service such as [ImgBB](https://imgbb.com/), then copy the **direct image URL** into the `iconUrl` field.

> **Note:** `discordServer` and `customClientDownloadUrl` are currently not displayed on the Cubyz Server List website, but they are reserved for future use.
