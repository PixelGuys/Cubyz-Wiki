Every biome is defined by a `zig.zon` file that contains all the data the world generator needs to generate it.



## Basic Fields

| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `isCave` | `bool` | Whether the biome is a cave biome (`true`) or a surface biome (`false`). | `false` |
| `radius` | `f32` | Size of the biome. Use `minRadius` and `maxRadius` for variable sizes. | `256` |
| `minRadius` | `f32` | Minimum biome radius. | `256` |
| `maxRadius` | `f32` | Maximum biome radius. | `minRadius` |
| `minHeight` | `i32` | Lowest terrain height the biome can generate. | — |
| `maxHeight` | `i32` | Highest terrain height the biome can generate. | — |
| `minHeightLimit` | `i32` | Hard lower terrain limit, even after interpolation. | — |
| `maxHeightLimit` | `i32` | Hard upper terrain limit, even after interpolation. | — |
| `smoothBeaches` | `bool` | Enables smooth beach generation. | `false` |
| `interpolation` | `Interpolation` | Border interpolation method: `.none`, `.linear`, or `.square`. (`.smooth` resolves to `.square`.) | `.square` |
| `interpolationWeight` | `f32` | Strength of biome interpolation. Minimum is `std.math.floatMin(f32)`. | `1` |
| `roughness` | `f32` | Applies terrain roughness by scattering blocks. | `0` |
| `hills` | `f32` | Controls rolling hill generation. | `0` |
| `mountains` | `f32` | Controls spiky mountain generation. | `0` |
| `keepOriginalTerrain` | `f32` | Amount of the parent biome's terrain preserved in a sub-biome (`1` = all, `0.5` = 50%). | `0` |
| `caves` | `f32` | Cave generation factor. | — |
| `caveRadiusFactor` | `f32` | Multiplier for cave radius. | `1` |
| `caveNoiseStrength` | `f32` | Multiplier for cave radius. | `8` |
| `crystals` | `u32` | Average number of randomly placed Glow Crystals. | `0` |
| `soilCreep` | `f32` | Controls erosion of surface blocks based on terrain slope. | `0.5` |
| `stoneBlock` | `String` | Base block the biome is constructed from. | `cubyz:slate/smooth` |
| `fogLower` | `f32` | Lower fog boundary. | `100` |
| `fogHigher` | `f32` | Upper fog boundary. | `1000` |
| `fogDensity` | `f32` | Density of biome fog. | `1` |
| `fogColor` | — | Fog color in hexidecimal. | `0xffbfe2ff` |
| `skyColor` | — | Sky color in hexidecimal. | `.{0.46, 0.7, 1.0}` |
| `maxSubBiomeCount` | `f32` | Maximum number of sub-biomes allowed per biome instance. | — |
| `music` | `String` | Music file that loops while the player is in the biome. | — |
| `isValidPlayerSpawn` | `bool` | Whether players can spawn in this biome. Used to ensure the player starts in a biome with trees. | — |
| `chance` | `f32` | Generation chance or weight. | `1` |

## Nested Fields

### `climate`
Basic information about the biome that helps the game decide where it should be generated.

Example usage, showing default values:
```zig
.climate = .{
	.temperate,
	.land,
	.neitherWetNorDry,
	.balanced,
	.lowTerrain,
},
```

List of valid fields:

`.hot` / `.temperate` / `.cold`

`.inland` / `.land` / `.ocean`

`.wet` / `.neitherWetNorDry` / `.dry`

`.barren` / `.balanced` / `.overgrown`

`.mountain` / `.lowTerrain` / `.antiMountain`

### `ground_structure`

Ground structure definitions.

Example usage:
```zig
.ground_structure = .{
	"1 to 2 mod:block"
	"mod:block",
},
```

### `stripes`

Stripes that replace the biome's `stoneBlock`.

Example usage:
```zig
.stripes = .{
	.{
		.direction = .{0, 0, 0},
		.block = "mod:block",
		.distance = 0,
		.offset = 0,
		.width = 0,
	},
},
```

### `structures`
Structures that can generate in the biome.

Example usage with an SBB structure:
```zig
.structures = .{
	.{
		.id = "cubyz:sbb",
		.structure = "mod:sbb",
		.placeMode = .degradable,
		.chance = 1,
	},
},
```


### `parentBiomes`

Parent biomes this biome can generate within. `chance` defaults to `1` if omitted.

Example usage:
```zig
.parentBiomes = .{
	.{
		.id = "mod:biome",
		.chance = 1,
	},
},
```

### `transitionBiomes`

Transition biome definitions.

Example usage:
```zig
.transitionBiomes = .{
	.{
		.id = "mod:biome",
		.chance = 1,
		.width = 1,
		.climate = .{.land},
	},
},
```

