# Addon Creation

This page outlines a guide to creating your own addons.

---

## Basics
Everything in your addon goes in a folder with your addon's name. Depending on what content you want to add, you'll need to create one or more of the following subfolders inside.

* **[Biomes](addons/biomes.md)** - Data for biomes
* **[Blocks](addons/blocks.md)** - Textures and data for blocks
* **[Items](addons/items.md)** - Textures and data for items
* **[Models](addons/models.md)** - Models for blocks
* **[Particles](addons/particles.md)** - Textures and data for particles
* **[Recipes](addons/recipes.md)** - Crafting recipes
* **[SBB](addons/SBB.md)** - "Structure building blocks," data and blueprint files for the generation of structures

Most data is stored in `zig.zon` files. Data in these files are written as fields, each field prefixed by a `.`
