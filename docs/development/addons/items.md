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
