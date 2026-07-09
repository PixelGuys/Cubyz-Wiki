{{Stub}}

This page outlines a guide to creating your own [[addons]].

== Basics ==
Everything in your addon goes in a folder with your addon's name. Depending on what content you want to add, you'll need to create one or more of the following subfolders inside.

* <code>biomes</code> - Data for biomes
* <code>blocks</code> - Textures and data for blocks
* <code>items</code> - Textures and data for items
* <code>models</code> - Models for blocks
* <code>particles</code> - Textures and data for particles
* <code>recipes</code> - Crafting recipes
* <code>sbb</code> - "Structure building blocks," data and blueprint files for the generation of structures

Most data is stored in <code>zig.zon</code> files. Data in these files are written as fields, each field prefixed by a <code>.</code>.

== Biomes ==
Every biome is defined by a <code>zig.zon</code> file that contains all the data the world generator needs to generate it.

=== <code>zig.zon</code> Fields ===

==== <code>properties: GenerationProperties</code> ====
Basic information about the biome that helps the game decide where it should be generated.

Example usage:

 .properties = .{
     .cold,
     .wet,
 },

List of valid fields:
* <code>.hot</code>/<code>.temperate</code>/<code>.cold</code>
* <code>.inland</code>/<code>.land</code>/<code>.ocean</code>
* <code>.wet</code>/<code>.neitherWetNorDry</code>/<code>.dry</code>
* <code>.barren</code>/<code>.balanced</code>/<code>.overgrown</code>
* <code>.mountain</code>/<code>.lowTerrain</code>/<code>.antiMountain</code>

You can include fields not on the above list, but they won't have any effect on world generation.

==== <code>isCave: bool</code> ====
Whether the biome is a cave biome. <code>true</code> if the biome is a cave biome, <code>false</code> if it's a surface biome.

==== <code>radius: f32</code> ====
The size of the biome. If variance in biome size is desired, instead use <code>minRadius</code> and <code>maxRadius</code>. Defaults to 256.

==== <code>minRadius: f32</code> ====
The minimum radius the biome can have.

==== <code>maxRadius: f32</code> ====
The maximum radius the biome can have.

==== <code>minHeight: i32</code> ====
The ''lowest'' point this biome's terrain can go.

==== <code>maxHeight: i32</code> ====
The ''highest'' point this biome's terrain can go.

==== <code>minHeightLimit: i32</code> ====
In some cases due to interpolation, a biome's terrain can reach outside the limits specified by <code>minHeight</code> and <code>maxHeight</code>. This setting is a ''hard limit'' on the lowest point terrain in this biome can go.

==== <code>maxHeightLimit: i32</code> ====
''Hard limit'' on the highest point terrain in this biome can go.

==== <code>smoothBeaches: bool</code> ====
Defaults to <code>false</code>.

==== <code>interpolation: Interpolation</code> ====
The type of interpolation to use on the borders between biomes. Defaults to <code>.square</code>. <code>.smooth</code> is often used in the base game, but this resolves to <code>.square</code> because <code>.smooth</code> isn't a valid <code>Interpolation</code>. Valid values are:

* <code>.none</code> - No interpolation
* <code>.linear</code> - Linear interpolation
* <code>.square</code> - Square (smooth) interpolation

==== <code>interpolationWeight: f32</code> ====
Defaults to 1, minimum value is <code>std.math.floatMin(f32)</code>.

==== <code>roughness: f32</code> ====
Applies a pass of roughness to terrain, where blocks get scattered.

==== <code>hills: f32</code> ====
Shapes the biome with rolling hills.

==== <code>mountains: f32</code> ====
Shapes the biome with spiky mountains.

==== <code>keepOriginalTerrain: f32</code> ====
How much of the base biome's terrain is kept in the subbiome. A value of 1 keeps the same terrain from the base biome, while 0.5 would mix the two biomes' terrain 50-50.

==== <code>caves: f32</code> ====

==== <code>caveRadiusFactor: f32</code> ====

==== <code>crystals: u32</code> ====
The average number of random crystals to be placed within the biome. Hardcoded to randomly select Glow Crystals.

==== <code>soilCreep: f32</code> ====
How much of the surface structure should be eroded depending on the slope. For example, a nearly vertical cliff shouldn't generate dirt on the way up, it should just be made of stone.

==== <code>stoneBlock: main.blocks.Block</code> ====
The underlying block that this biome is contructed with. Default is [[slate]].

==== <code>fogLower: f32</code> ====

==== <code>fogHigher: f32</code> ====

==== <code>fogDensity: f32</code> ====

==== <code>fogColor: vec3f</code> ====

==== <code>skyColor: vec3f</code> ====
The color of the sky in this biome, in RGB. Default is <code>.{0.46, 0.7, 1.0}</code>.

==== <code>stripes: []Stripe</code> ====

==== <code>subBiomes: main.utils.AliasTable(*const Biome)</code> ====

==== <code>parentBiomes: []struct{id: []const u8, chance: f32}</code> ====
Example:

 .parentBiomes = .{
     .{
         .id = "namespace:biome1",
         .chance = 0.1,
     },
     .{
         .id = "namespace:biome2",
         .chance = 4,
     },
 },

If left unspecified, the <code>.chance</code> is 1.

==== <code>transitionBiomes: []TransitionBiome</code> ====

==== <code>ground_structure: [][]const u8</code> ====

==== <code>structures: []SimpleStructureModel</code> ====

==== <code>maxSubBiomeCount: f32</code> ====
The maximum number of sub-biomes that are allowed to generate in each instance of this biome.

==== <code>music: []const u8</code> ====
Music file that loops while the player is in this biome.

==== <code>isValidPlayerSpawn: bool</code> ====
Whether the player's default spawn point can be in this biome. This is used to ensure the player spawns in a biome with trees, so they are able to progress.

==== <code>chance: f32</code> ====

== Blocks ==
Every block has a <code>zig.zon</code> file containing all the properties of each block.

==== <code>transparent: bool</code> ====

==== <code>collide: bool</code> ====

==== <code>blockHealth: f32</code> ====

==== <code>blockResistance: f32</code> ====

==== <code>replaceable: bool</code> ====

==== <code>selectable: bool</code> ====

==== <code>blockDrops: []BlockDrops</code> ====

==== <code>degradable: bool</code> ====

==== <code>viewThrough: bool</code> ====

==== <code>alwaysViewThrough: bool</code> ====

==== <code>hasBackface: bool</code> ====

==== <code>selectable: bool</code> ====

==== <code>tags: []Tag</code> ====

==== <code>emittedLight: u32</code> ====

==== <code>absorption: u32</code> ====

==== <code>onInteract: ClientBlockCallback</code> ====

==== <code>rotation: RotationMode</code> ====
[[Rotation Modes#List of Rotation Modes|List of Rotation Modes]]

==== <code>lodReplacement: u16</code> ====
The block that this block is replaced by in <code>LOD1</code> and greater.
==== <code>opaqueVariant: []Tag</code> ====
The opaque variant of the block to use in <code>LOD0.5</code> and for the Leaves Quality option.

==== <code>friction: f32</code> ====

==== <code>bounciness: f32</code> ====

==== <code>density: f32</code> ====

==== <code>terminalVelocity: f32</code> ====

==== <code>mobility: f32</code> ====

==== <code>allowOres: bool</code> ====
If ores are able to generate on this block.

==== <code>ore: struct</code> ====

* <code>size: f32</code> - Average size of a vein in blocks
* <code>density: f32</code> - Average density of a vein
* <code>veins: f32</code> - Average veins per chunk
* <code>maxHeight: f32</code> - Highest point this ore will generate
* <code>minHeight: f32</code> - Lowest point this ore will generate

==== <code>item:</code> ====
Some item parameters are able to be applied to blocks, such as item textures or material values.

== Items ==
Every item has a <code>zig.zon</code> file containing all the properties of the item.

==== <code>texture: texturePath</code> ====

==== <code>tags: []Tag</code> ====

==== <code>stackSize: u16</code> ====
The maximum number of this item that can be held in one slot. Default is 120.

==== <code>material: u16</code> ====
These are the values used for procedural tool crafting.

* <code>durability: f32</code> - The amount of durability the material provides
* <code>massDamage: f32</code> - How much damage the material provides based on its mass
* <code>hardnessDamage: f32</code> - How much damage the material provides based on its hardness
* <code>swingSpeed: f32</code> - The speed of one swing
* <code>textureRoughness: f32</code> - A pass of roughness to the texture
* <code>colors:</code> - Palette of 5 colors from darkest to lightest
* <code>modifiers:</code> - [[Modifiers|Modifiers]]

== Models ==
Cubyz loads <code>obj</code> files for block models, which you can make in your preferred 3D modelling software (i.e. [https://www.blockbench.net/ Blockbench] or [https://www.blender.org/ Blender].) However, there are some things to keep in mind when creating your model:
* Cubyz uses Z up
* Block model UVs are mapped to a 64x64 texture with 16 texture slots:

[[File:Block_uv_template_faces.png|128px]]
[[File:Block_uv_template_numbers.png|128px]]

Once you're ready to use your model ingame, split the grid into the individual textures you need, and in your block's zig.zon, specify the file path of your textures in the following fields:

{| class="mw-collapsible mw-collapsed wikitable"
! colspan="2" | List of Texture Fields
|-
| <code>texture</code> (Applied to all faces)
|-
| <code>texture_top</code> OR <code>texture0</code>
|-
| <code>texture_bottom</code> OR <code>texture1</code>
|-
| <code>texture_front</code> OR <code>texture2</code>
|-
| <code>texture_back</code> OR <code>texture3</code>
|-
| <code>texture_right</code> OR <code>texture4</code>
|-
| <code>texture_left</code> OR <code>texture5</code>
|-
| <code>texture6</code>
|-
| <code>texture7</code>
|-
| <code>texture8</code>
|-
| <code>texture9</code>
|-
| <code>texture10</code>
|-
| <code>texture11</code>
|-
| <code>texture12</code>
|-
| <code>texture13</code>
|-
| <code>texture14</code>
|-
| <code>texture15</code>
|}

To give a block your model, specify the file path of your model in the block's <code>zig.zon</code>'s <code>model</code> field.

== Particles ==
Support for particles is very limited in 0.0.0, however they do exist even if you can't do anything with them.

Every particle has a <code>zig.zon</code> file containing all of the particle's properties.

== Recipes ==

== Structure Building Blocks (sbbs) ==