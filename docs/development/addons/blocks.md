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
