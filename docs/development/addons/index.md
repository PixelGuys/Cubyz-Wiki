# Addon Creation

This page outlines a guide to creating your own addons.

---

## Basics
Everything in your addon goes in a folder with your addon's name. Depending on what content you want to add, you'll need to create one or more of the following subfolders inside.

* **[Biomes](biomes.md)** - Data for biomes
* **[Blocks](blocks.md)** - Textures and data for blocks
* **[Items](items.md)** - Textures and data for items
* **[Models](models.md)** - Models for blocks
* **[Particles](particles.md)** - Textures and data for particles
* **[Recipes](recipes.md)** - Crafting recipes
* **[SBB](sbb.md)** - "Structure building blocks," data and blueprint files for the generation of structures

Most data is stored in `zig.zon` files. Data in these files are written as fields, each field prefixed by a `.`
