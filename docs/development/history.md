## Early History
---

On the 22nd of August of 2018, **zenith391** and **ZaUserA** created Cubz.
(That's not a mistake! It was called 'Cubz'). After a slow transition, **zenith391** and
**ZaUserA** lost interest in Cubz (sometime during the year of 2020) the
project is currently maintained mainly by **QuantumDeveloper** (also referred
to as **IntegratedQuantum**) (and also maintained by others).

## "Cubyz"
---

Initially, Cubyz was named "Cubz" by **zenith391** and **ZaUserA**, but on
the 17th of March of 2019 (at 6:00PM GMT, Sunday), **zenith391** suggests the
new name "Cubyz". You can find the link to that message [here](https://discord.com/channels/443805812390100992/475297969609113600/556899803758329886).
If the message is no longer available, you can find a screenshot [here](/images/history/zenith-message-1.png) and [here](/images/history/zenith-message-2.png).

> "they will merge under the new name Cubyz"
>
> — **zenith391**, March 17 2019 at 6:00PM GMT (Sunday)

## Early Development Builds
---

Sometime in 2019, @QuantumDeveloper found a project on Github called Cubz. He
joined and implemented features like an **Inventory**, **Terrain
Generation,** the **Crafting System** (which back then was a 2x2 grid like in
Minecraft) and the [Workbench](#) which was inspired by
[Tinkers Construct](https://modrinth.com/mod/tinkers-construct), a Minecraft mod
that allowed you to "[put] tools together in a wide variety of ways". He also
added a **Multicolored Lighting System**, the **Block Rotation System** and
the **Addons** system.

![Initial Player Model](/images/history/Initial_Player_Model.png)
![The Last Water House](/images/history/The_Last_Water_House.png)
![Snowy Cubyz](/images/history/Snowy_Cubyz.png)
![Desert](/images/history/Desert.png)

<style>
img[alt="Initial Player Model"], [alt="The Last Water House"], [alt="Snowy Cubyz"], [alt="Desert"] {
    width: 350px;
}
</style>

Source to screenshots can be found at
[www.youtube.com/watch?v=0TDcqLFwQrE](https://www.youtube.com/watch?v=0TDcqLFwQrE).

## The Great Zig Rewrite
---

There was an attempt to rewrite Cubyz in C++ and Vulkan, but that was abandoned
(you can read below why).

On the 8th of November of 2022, @QuantumDeveloper posted a video on his personal
channel explaining why Cubyz should be re-coded. You can watch that at
[youtube.com/watch?v=PxUkTxA8OWU](https://www.youtube.com/watch?v=PxUkTxA8OWU).

The re-code was mainly because of the Java Garbage collector, because when the
upper memory link limit was hit, Java would try to free up memory, which would
freeze the game for some time. @QuantumDeveloper also explains that the lag
spikes were not his only problem with Java, and also explains project
"Valhalla", a project that tries to fix some of his issues with Java.

@QuantumDeveloper then goes on to explain the alternatives that sounded like
viable options: C++ 20 (due to the new "modules" feature), but not viable
because the feature was not supported by the best compilers (like GCC or Clang).
Rust which @QuantumDeveloper found kind of annoying due to its "power checker".

And after @QuantumDeveloper's last rewrite attempt, **zenith391** showed
@QuantumDeveloper a new language: [Zig](https://ziglang.org). One of the features
that really impressed @QuantumDeveloper was the **cross-compilation** support
out-of-the-box since he could build for Windows and test it with
[Wine](https://winehq.org) without having to worry about the Windows-related OS-
specific stuff.

## Zig 0.0.0!
On October the 5th 2025, Cubyz version `0.0.0` is released.
You can find the release announcement [here (Github)](https://github.com/PixelGuys/Cubyz/releases/tag/0.0.0) and [here (Discord)](https://discord.com/channels/443805812390100992/481475033621856266/1424480988960129178). Screenshot of the Discord message [here](/images/history/quantum-message-1.png).

QuantumDeveloper also released a youtube video which as of July 11th 2026 has `199k views` on youtube.
You can whatch the video [here](https://youtu.be/jm_0nRQEn_o?si=skWJxRfMtx7hJxxp), Enjoy!

## Sources
---

**Early History**

[README.md](https://github.com/PixelGuys/Cubyz/blob/e0dac4995dca8150423949b04f036274bd7dbee2/README.md) and @QuantumDeveloper himself.

**"Cubyz"**

@QuantumDeveloper

**Early Development Builds**

[https://www.youtube.com/watch?v=0TDcqLFwQrE](https://www.youtube.com/watch?v=0TDcqLFwQrE) (watch this, it's really good!)

[https://modrinth.com/mod/tinkers-construct](https://modrinth.com/mod/tinkers-construct)

**The Great Zig Rewrite**

[https://www.youtube.com/watch?v=PxUkTxA8OWU](https://www.youtube.com/watch?v=PxUkTxA8OWU)

**Cubyz 0.0.0**
[https://github.com/PixelGuys/Cubyz/releases/tag/0.0.0](https://github.com/PixelGuys/Cubyz/releases/tag/0.0.0)
[https://youtu.be/jm_0nRQEn_o?si=skWJxRfMtx7hJxxp](https://youtu.be/jm_0nRQEn_o?si=skWJxRfMtx7hJxxp)