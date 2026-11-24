# Recipes

Recipe files are what the game uses to define the inventory crafting menu's recipes.

| Property | Type | Description |
|----------|------|-------------|
| `inputs` | `.{String}` | List of inputs needed to craft the output. Amount can be specified. |
| `output` | `String` | The output of the recipe. Amount can be specified. |
| `reversible` | `bool` | Whether or not the output can be crafted back into the input. |

Example usage:
```zig
.{
	.{
		.inputs = .{"mod:item"},
		.output = "mod:item_2",
		.reversible = true,
	},
	.{
		.inputs = .{"4 mod:item", "mod:item_2"},
		.output = "mod:item_3",
	},
}
```

## Key Matching

To reduce the amount of duplicate recipes, `{keys}` can be used. For example, the following recipe can be used to turn any item in `{mod}:log/` into its matching `{mod}:planks/`:

```zig
.{
	.inputs = .{"{mod}:log/{type}"},
	.output = "4 {mod}:planks/{type}",
},
```

### Default Key Matches

It is important to note that the default `cubyz:` assets have key matches that will affect addons. They are as listed below (irrelevant recipes have been removed):

#### `special_recipes`

```zig
.{
	.inputs = .{"cubyz:coal_ore", "{mod}:{type}_ore"},
	.output = "{mod}:{type}_ingot",
},
...
.{
	.inputs = .{"{mod}:{type}_ingot"},
	.output = "4 {mod}:bars/{type}",
},
```

#### `wood_recipes`

```zig
.{
	.inputs = .{"4 {mod}:planks/{type}"},
	.output = "cubyz:workbench",
},
...
.{
	.inputs = .{"{mod}:planks/{type}", "cubyz:coal_ore"},
	.output = "8 cubyz:torch",
},
.{
	.inputs = .{"{mod}:planks/{type}", "cubyz:sulfur_ore"},
	.output = "8 cubyz:sulfur_torch",
},
.{
	.inputs = .{"{mod}:planks/{type}", "cubyz:lumiflora"},
	.output = "8 cubyz:torch/lumi",
},
```