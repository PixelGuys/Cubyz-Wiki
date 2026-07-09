To play Cubyz, you can either '''download a Release Version''', or '''compile''' the latest development version yourself.

== Release Versions ==
Release version of Cubyz are '''finished versions''' that are player-ready. You can download the latest release on the [https://github.com/PixelGuys/Cubyz/releases Github Releases page].

As of this writing, the current latest version of Cubyz is {{ReleaseVersion}}.

To run Cubyz, download the .zip file that matches your operating system and computing architecture from the [https://github.com/PixelGuys/Cubyz/releases Github Releases page], then extract the downloaded .zip file. Inside the extracted .zip file you can find "Cubyz.exe" (or "Cubyz" on Unix-based systems) inside the "Cubyz" folder, which is the Cubyz Executable. On Unix-based systems, you may need to make the file executable.
== Development Versions ==
You can try the latest changes and additions with a self-compiled development version.

=== The Easy Way (no tools needed) ===

# Download the latest source code
# Extract the zip file
# Go into the extracted folder and double click the <code>run_linux.sh</code> or <code>run_windows.bat</code> depending on your operating system.
# Congratulations: You just compiled your first program!

=== It doesn't work? ===

* If it doesn't work and keeps running for more than 10 minutes without doing anything it can help to kill and restart the process. A few people seem to experience this, and the cause is unknown. It might also help to delete the <code>zig-cache</code> folder.
* If you see an error message in the terminal, please report it in the Github Issues tab or on the Discord server.
* Otherwise you can always ask for help on the Discord server. If you are unable to get it compiling on your machine, you can also ask on the Discord server and we may compile a release for you.

=== The Better Way ===

# Install [https://git-scm.com/ Git]
# Clone the Cubyz Github repository: <code>git clone <nowiki>https://github.com/pixelguys/Cubyz</nowiki></code>
# Run <code>run_linux.sh</code> or <code>run_windows.bat</code>, if you already have Zig installed on your computer (it must be a compatible version) you can also just use <code>zig build run</code>
# When you want to update your local version you can use <code>git pull</code>. This keeps everything in one place, avoiding repeatedly downloading the compiler on every update.