---
icon: material/arrow-down-bold-box-outline
tags:
    - install
---

# Installation

To play Cubyz, you can either **download a release** or **compile a development version yourself**.

## Requirements

Cubyz is a very well optimized game, but there is still a limit to what hardware it can run on. As a safe baseline we recommend minimal specification listed below. That hardware and software should be enough to play Cubyz reasonably smoothly in Full HD resolution. If you satisfy hardware requirements listed bellow, yet your game runs poorly or doesn't start at all, consider asking a question on out Discord.

* **OS:** Windows / Linux
* **GPU** Graphics cards such as [Radeon Vega 8](https://www.techpowerup.com/gpu-specs/radeon-vega-8.c3042) / [Intel HD Graphics 530](https://www.techpowerup.com/gpu-specs/hd-graphics-530.c2789) or [NVIDIA GTX 750](https://www.techpowerup.com/gpu-specs/geforce-gtx-750.c1986)
* **CPU:** Dual-core processor (64-bit) such as [Ryzen 3 2200G](https://www.techpowerup.com/cpu-specs/ryzen-3-2200g.c1978) or [Intel i3-6100](https://www.techpowerup.com/cpu-specs/core-i3-6100.c1836)
* **RAM:** At least 4 GB of RAM available.

!!! warning "GPU Requirements"
    Cubyz requires a graphics card with **hardware support** for **OpenGL 4.6** along with up-to-date drivers. 
    
    * Not sure if your hardware qualifies? You can search for your specific model on [TechPowerUp](https://www.techpowerup.com/gpu-specs/) or check the official [OpenGL Support Page](https://www.khronos.org/conformance/adopters/conformant-products/opengl).

!!! warning "Please Note"
    Any hardware below these minimum specifications is not officialy recommended, and your gameplay experience may suffer.
## Downloading a release version

To download a release version, head to the [Cubyz release page on Github](http://github.com/PixelGuys/Cubyz/releases/latest) and download the latest release for your platform.

Once you have donwloaded the file for your computer architecture, extract it. You can extract the file **using your file explorer** or using the command below:

=== "Linux"

    ```sh
    tar -xvzf Linux-x86_64.tar.gz
    ```

=== "Windows"

    ```cmd
    tar -xvzf Windows-x86_64.zip
    ```

Once extracted, go into the extracted directory. In this directory you can find **three files**:<br>
- `Cubyz`<br>
- `launchConfig.zon`<br>
- `assets`<br>

These three files are **required** to run Cubyz. 

To run Cubyz, execute the Cubyz binary:
=== "Linux"

    ```sh
    chmod +x Cubyz # make binary executable
    ./Cubyz
    ```

=== "Windows"

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
**NOTE**: This will run the latest `development` release. Only do this if you know what you are doing!

1. Download the latest [source code](https://codeload.github.com/PixelGuys/Cubyz/zip/refs/heads/master)
2. Extract the `.zip` file
3. Go into the extraced folder and run the executable

=== "Linux"
    ```sh
    ./run_linux.sh
    ```

=== "Windows"
    ```cmd
    run_windows.bat
    ```

Congrats: You just compiled your first program!

#### The Better Way
**NOTE**: This will run the latest `development` release. Only do this if you know what you are doing!

1. Install [Git](https://git-scm.com)
2. Clone this repository `git clone https://github.com/pixelguys/Cubyz`

=== "Linux"
    ```sh
    ./run_linux.sh
    ```

=== "Windows"
    ```cmd
    run_windows.bat
    ```


Whenever you want to update your local version you can use `git pull`. This keeps everything in one place, avoiding repeatedly downloading the compiler on every update.

## Crashes

If Cubyz crashes or doesn't run, you can ask the community for help by joining the [Cubyz Discord Server](/links/discord) or creating an issue on the [Cubyz issue board](https://github.com/pixelguys/cubyz/issues).
