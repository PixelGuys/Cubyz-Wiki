This page outlines a guide to creating your own addons.

---

## Basics
Everything in your addon goes in a folder with your addon's name. Depending on what content you want to add, you'll need to create one or more of the following subfolders inside.

* `biomes` - Data for biomes
* `blocks` - Textures and data for blocks
* `items` - Textures and data for items
* `models` - Models for blocks
* `particles` - Textures and data for particles
* `recipes` - Crafting recipes
* `sbb` - "Structure building blocks," data and blueprint files for the generation of structures

Most data is stored in `zig.zon` files. Data in these files are written as fields, each field prefixed by a `.`

---

## Biomes
Every biome is defined by a `zig.zon` file that contains all the data the world generator needs to generate it.

### `zig.zon` Fields

#### `properties: GenerationProperties`
Basic information about the biome that helps the game decide where it should be generated.

Example usage:
```zig
.properties = .{
    .cold,
    .wet,
},
```

List of valid fields:
 `.hot` / `.temperate` / `.cold`/
 `.inland` / `.land` / `.ocean`/
 `.wet` / `.neitherWetNorDry` / `.dry`/
 `.barren` / `.balanced` / `.overgrown`/
 `.mountain` / `.lowTerrain` / `.antiMountain`

| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `isCave` | `bool` | Whether the biome is a cave biome (`true`) or a surface biome (`false`). | — |
| `radius` | `f32` | Size of the biome. Use `minRadius` and `maxRadius` for variable sizes. | `256` |
| `minRadius` | `f32` | Minimum biome radius. | — |
| `maxRadius` | `f32` | Maximum biome radius. | — |
| `minHeight` | `i32` | Lowest terrain height the biome can generate. | — |
| `maxHeight` | `i32` | Highest terrain height the biome can generate. | — |
| `minHeightLimit` | `i32` | Hard lower terrain limit, even after interpolation. | — |
| `maxHeightLimit` | `i32` | Hard upper terrain limit, even after interpolation. | — |
| `smoothBeaches` | `bool` | Enables smooth beach generation. | `false` |
| `interpolation` | `Interpolation` | Border interpolation method: `.none`, `.linear`, or `.square`. (`.smooth` resolves to `.square`.) | `.square` |
| `interpolationWeight` | `f32` | Strength of biome interpolation. Minimum is `std.math.floatMin(f32)`. | `1` |
| `roughness` | `f32` | Applies terrain roughness by scattering blocks. | — |
| `hills` | `f32` | Controls rolling hill generation. | — |
| `mountains` | `f32` | Controls spiky mountain generation. | — |
| `keepOriginalTerrain` | `f32` | Amount of the parent biome's terrain preserved in a sub-biome (`1` = all, `0.5` = 50%). | — |
| `caves` | `f32` | Cave generation factor. | — |
| `caveRadiusFactor` | `f32` | Multiplier for cave radius. | — |
| `crystals` | `u32` | Average number of randomly placed Glow Crystals. | — |
| `soilCreep` | `f32` | Controls erosion of surface blocks based on terrain slope. | — |
| `stoneBlock` | `main.blocks.Block` | Base block the biome is constructed from. | `slate` |
| `fogLower` | `f32` | Lower fog boundary. | — |
| `fogHigher` | `f32` | Upper fog boundary. | — |
| `fogDensity` | `f32` | Density of biome fog. | — |
| `fogColor` | `vec3f` | Fog color in RGB. | — |
| `skyColor` | `vec3f` | Sky color in RGB. | `.{0.46, 0.7, 1.0}` |
| `stripes` | `[]Stripe` | Stripe definitions used by the biome. | — |
| `subBiomes` | `main.utils.AliasTable(*const Biome)` | Collection of sub-biomes. | — |
| `parentBiomes` | `[]struct{id: []const u8, chance: f32}` | Parent biomes this biome can generate within. `chance` defaults to `1` if omitted. | — |
| `transitionBiomes` | `[]TransitionBiome` | Transition biome definitions. | — |
| `ground_structure` | `[][]const u8` | Ground structure definitions. | — |
| `structures` | `[]SimpleStructureModel` | Structures that can generate in the biome. | — |
| `maxSubBiomeCount` | `f32` | Maximum number of sub-biomes allowed per biome instance. | — |
| `music` | `[]const u8` | Music file that loops while the player is in the biome. | — |
| `isValidPlayerSpawn` | `bool` | Whether players can spawn in this biome. Used to ensure the player starts in a biome with trees. | — |
| `chance` | `f32` | Generation chance or weight. | — |


---

## Blocks
Every block has a `zig.zon` file containing all the properties of each block.

| Property | Type | Description | 
|----------|------|-------------|
| `transparent` | `bool` | Whether the block is transparent. 
| `collide` | `bool` | Whether entities collide with the block. 
| `blockHealth` | `f32` | Health of the block. 
| `blockResistance` | `f32` | Resistance to damage or explosions. 
| `replaceable` | `bool` | Whether the block can be replaced by another block without being broken. 
| `selectable` | `bool` | Whether the block can be targeted and selected. 
| `blockDrops` | `[]BlockDrops` | Items dropped when the block is broken. 
| `degradable` | `bool` | Whether the block can degrade over time. 
| `viewThrough` | `bool` | Whether the player can see through the block. 
| `alwaysViewThrough` | `bool` | Forces the block to always be rendered as view-through. 
| `hasBackface` | `bool` | Whether the block renders back faces. 
| `tags` | `[]Tag` | Tags assigned to the block. 
| `emittedLight` | `u32` | Amount of light emitted by the block. 
| `absorption` | `u32` | Amount of light absorbed by the block. 
| `onInteract` | `ClientBlockCallback` | Callback executed when the block is interacted with. 
| `rotation` | `RotationMode` | Rotation mode used by the block. See [Rotation Modes](#rotation-modes). 
| `lodReplacement` | `u16` | Block used as a replacement in `LOD1` and higher. 
| `opaqueVariant` | `[]Tag` | Opaque variant used in `LOD0.5` and with the Leaves Quality option. 
| `friction` | `f32` | Surface friction of the block. 
| `bounciness` | `f32` | Bounce factor applied to entities. 
| `density` | `f32` | Physical density of the block. 
| `terminalVelocity` | `f32` | Maximum falling velocity through the block. 
| `mobility` | `f32` | Mobility value used by the physics system. 
| `allowOres` | `bool` | Whether ores can generate inside this block. 
| `ore` | `struct` | Ore generation settings. See table below. 
| `item` | `struct` | Item properties that can also be applied to blocks, such as textures and material values. 

### `Rotation Modes`


| Rotation Mode | Description |
|--------------|-------------|
| `no_rotation` | No rotation is applied. |
| `branch` | Branch-style rotation. |
| `carpet` | Rotation used for carpet-like blocks. |
| `direction` | Rotates to face a specific direction. |
| `fence` | Rotation used for fence connections. |
| `hanging` | Rotation used for hanging blocks. |
| `ore` | Rotation used for ore blocks. |
| `planar` | Rotation constrained to a plane. |
| `sign` | Rotation used for signs. |
| `stairs` | Rotation used for stairs. |
| `texture_pile` | Rotation used for texture pile blocks. |
| `torch` | Rotation used for torches. |

### `Ore Fields`

| Property | Type | Description |
|----------|------|-------------|
| `size` | `f32` | Average vein size in blocks. |
| `density` | `f32` | Average density of each vein. |
| `veins` | `f32` | Average number of veins per chunk. |
| `maxHeight` | `f32` | Highest point the ore can generate. |
| `minHeight` | `f32` | Lowest point the ore can generate. |

---

## Items
Every item has a `zig.zon` file containing all the properties of the item.

#### `texture: texturePath`

#### `tags: []Tag`

#### `stackSize: u16`
The maximum number of this item that can be held in one slot. Default is 120.

#### `material: u16`
These are the values used for procedural tool crafting.

* `durability: f32` - The amount of durability the material provides
* `massDamage: f32` - How much damage the material provides based on its mass
* `hardnessDamage: f32` - How much damage the material provides based on its hardness
* `swingSpeed: f32` - The speed of one swing
* `textureRoughness: f32` - A pass of roughness to the texture
* `colors:` - Palette of 5 colors from darkest to lightest
* `modifiers:` - [Modifiers](Modifiers)

## Models
Cubyz loads `.glb` files for block models, which you can make in your preferred 3D modelling software (i.e. [Blockbench](https://www.blockbench.net/) or [Blender](https://www.blender.org/).) However, there are some things to keep in mind when creating your model:

* Cubyz uses Z up
* Block model UVs are mapped to a 64x64 texture with 16 texture slots:

![Block uv template faces](../images/addons/Block_uv_template_faces.png)
![Block uv template numbers](../images/addons/Block_uv_template_numbers.png)

Once you're ready to use your model ingame, split the grid into the individual textures you need, and in your block's `zig.zon`, specify the file path of your textures in the following fields:

| List of Texture Fields |
| :--- |
| `texture` (Applied to all faces) |
| `texture_top` OR `texture0` |
| `texture_bottom` OR `texture1` |
| `texture_front` OR `texture2` |
| `texture_back` OR `texture3` |
| `texture_right` OR `texture4` |
| `texture_left` OR `texture5` |
| `texture6` |
| `texture7` |
| `texture8` |
| `texture9` |
| `texture10` |
| `texture11` |
| `texture12` |
| `texture13` |
| `texture14` |
| `texture15` |

To give a block your model, specify the file path of your model in the block's `zig.zon`'s `model` field.

## Particles

## Recipes

## Structure Building Blocks
