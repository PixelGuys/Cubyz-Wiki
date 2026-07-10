---
icon: material/arrow-down-bold-box-outline
---

# Installation

To play Cubyz, you can either **download a ready-to-run release** or **compile the latest development version yourself**.

## Requirements

TODO: Add requirements here

## Downloading a release version

To download a release version, head to the [Cubyz release page on GitHub](http://github.com/PixelGuys/Cubyz/releases/latest) and download the latest version for your operating system.

Once downloaded, extract the archive file using your file explorer or your favorite command-line tool.

Inside the extracted folder, make sure you see these **three key files**:

*   `Cubyz` (or `Cubyz.exe`)
*   `launchConfig.zon`
*   `assets`

These files must stay in the same folder for the game to run.

To launch Cubyz, run the executable:

=== "Linux"
    ```sh
    chmod +x Cubyz # make binary executable
    ./Cubyz
    ```

=== "Windows"
    Simply double-click `Cubyz.exe`, or run it via terminal:

    **Command Prompt**
    ```cmd
    Cubyz.exe
    ```

    **PowerShell**
    ```powershell
    .\Cubyz.exe
    ```

## Building from Source

#### The Easy Way (no tools needed)
**NOTE**: This builds the absolute latest experimental version of the game. It may contain bugs!

1. Download the latest [source code zip](https://codeload.github.com/PixelGuys/Cubyz/zip/refs/heads/master).
2. Extract the `.zip` file.
3. Open the extracted folder and run the launch script for your system:

=== "Linux"
    ```sh
    ./run_linux.sh
    ```

=== "Windows"
    ```cmd
    run_windows.bat
    ```

Congrats: You just compiled your first program!

#### The Better Way (Using Git)
**NOTE**: This method makes updating the game incredibly easy without re-downloading files every time.

First, select your operating system below to install **Git** and download the code:

=== "Windows"
    Open **PowerShell** or **Command Prompt** as Administrator and run:
    ```cmd
    winget install --id Git.Git -e --source winget
    ```
    
    Once Git is ready, open a normal terminal and run:
    ```sh
    # Download the repository
    git clone https://github.com/pixelguys/Cubyz
    
    # Enter the game folder
    cd Cubyz
    
    # Compile and run
    run_windows.bat
    ```

=== "Arch Linux"
    ```sh
    # Install Git
    sudo pacman -S git

    # Download the repository
    git clone https://github.com/pixelguys/Cubyz
    
    # Enter the game folder
    cd Cubyz

    # Compile and run
    ./run_linux.sh
    ```

=== "Ubuntu / Debian"
    ```sh
    # Install Git
    sudo apt update && sudo apt install git -y

    # Download the repository
    git clone https://github.com/pixelguys/Cubyz
    
    # Enter the game folder
    cd Cubyz

    # Compile and run
    ./run_linux.sh
    ```

=== "Fedora"
    ```sh
    # Install Git
    sudo dnf install git -y

    # Download the repository
    git clone https://github.com/pixelguys/Cubyz
    
    # Enter the game folder
    cd Cubyz

    # Compile and run
    ./run_linux.sh
    ```

#### How to Update Later
Whenever you want to pull the latest updates, you don't need to download anything manually again. Just open your terminal inside the `Cubyz` folder and run:

```sh
git pull
```
### Crashes

If Cubyz crashes or doesn't run, you can ask the community for help by joining the [Cubyz Discord Server](https://discord.com/invite/stBh54hF7U) or creating an issue on the [Cubyz issue board](https://github.com/pixelguys/cubyz/issues).
