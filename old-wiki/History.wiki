== Early History ==
On the 22nd of August of 2018, '''zenith391''' and '''ZaUserA''' created Cubz. (The initial name for cubyz). After a slow transition, '''zenith391''' and '''ZaUserA''' lost interest in Cubz (sometime during the year of 2020) the project is currently maintained mainly by '''QuantumDeveloper''' (also referred to as '''IntegratedQuantum''') (and also maintained by others).

== "Cubyz" ==

Initially, Cubyz was named "Cubz" by '''zenith391''' and '''ZaUserA''', but on the 17th of March of 2019 (at 6:00PM GMT, Sunday), '''zenith391''' suggests the new name "Cubyz". You can find the link to that message [https://discord.com/channels/443805812390100992/475297969609113600/556899803758329886 here].<blockquote>"they will merge under the new name Cubyz"

- '''zenith391''', March 17 2019 at 6:00PM GMT (Sunday)</blockquote>

== Early Development Builds ==
Sometime in 2019, @QuantumDeveloper found a project on Github called Cubz. He joined and implemented features like an '''Inventory''', '''Terrain Generation,''' the '''Crafting System''' (which back then was a 2x2 grid like in Minecraft) and the [[Workbench]] which was inspired by [https://modrinth.com/mod/tinkers-construct Tinkers Construct], a Minecraft mod that allowed you to "[put] tools together in a wide variety of ways". He also added a '''Multicolored Lighting System''', the '''Block Rotation System''' and the '''Addons''' system.
[[File:Initial Player Model.png|alt=Initial Player Model|thumb|First Player Model (Cubyz Java Development Versions)]]
[[File:Trees.png|thumb|Trees (Cubyz Java Development Versions)]]
[[File:Desert.png|thumb|Desert (Cubyz Java Development Versions)]]
[[File:Snowy Cubyz.png|thumb|Snowy Cubyz (Cubyz Java Development Versions)]]
[[File:The Last Water House.png|thumb|THE Last Water House (Cubyz Java Development Versions)]]
[[File:Sc3.png|thumb|Trees (Cubyz Java Development Versions)]]


Source to screenshots can be found at [https://www.youtube.com/watch?v=0TDcqLFwQrE www.youtube.com/watch?v=0TDcqLFwQrE].

== The Great Zig Rewrite ==
There was an attempt to rewrite Cubyz in C++ and Vulkan, but that was abandoned (you can read below why).

On the 8th of November of 2022, @QuantumDeveloper posted a video on his personal channel explaining why Cubyz should be re-coded. You can watch that at [https://www.youtube.com/watch?v=PxUkTxA8OWU youtube.com/watch?v=PxUkTxA8OWU].

The re-code was mainly because of the Java Garbage collector, because when the upper memory link limit was hit, Java would try to free up memory, which would freeze the game for some time. @QuantumDeveloper also explains that the lag spikes were not his only problem with Java, and also explains project "Valhalla", a project that tries to fix some of his issues with Java.

@QuantumDeveloper then goes on to explain the alternatives that sounded like viable options: C++ 20 (due to the new "modules" feature), but not viable because the feature was not supported by the best compilers (like GCC or Clang). Rust which @QuantumDeveloper found kind of annoying due to its "power checker".

And after @QuantumDeveloper's last rewrite attempt, '''zenith391''' showed @QuantumDeveloper a new language: [https://ziglang.org Zig]. One of the features that really impressed @QuantumDeveloper was the '''cross-compilation''' support out-of-the-box since he could build for Windows and test it with [https://winehq.org Wine] without having to worry about the Windows-related OS-specific stuff.

== Sources ==
'''Early History'''

[https://github.com/PixelGuys/Cubyz/blob/e0dac4995dca8150423949b04f036274bd7dbee2/README.md README.md] for the creation info and @QuantumDeveloper (also known as @IntegratedQuantum) for the info about creating, etc...

'''"Cubyz"'''

@QuantumDeveloper sent a link to the message sent by zenith391

'''Early Development Builds'''

https://www.youtube.com/watch?v=0TDcqLFwQrE (watch this, it's really good!)

https://modrinth.com/mod/tinkers-construct

'''The Great Zig Rewrite'''

https://www.youtube.com/watch?v=PxUkTxA8OWU