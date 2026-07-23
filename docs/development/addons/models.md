---
icon: lucide/drafting-compass
---

# Models
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
