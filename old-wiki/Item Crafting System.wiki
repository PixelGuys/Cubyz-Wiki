This page is about the inventory crafting system that allows direct crafting of materials into non-tool items and blocks. For the tool crafting system, see [[Workbench]]. {{Stub|section}}
[[File:Crafting system.png|thumb|Inventory crafting window with button in inventory.]]In order to craft, the player inventory needs to be opened via <code>openInventory</code>. Then, clicking the center button with the tools icon will open up the crafting window. In the crafting window, the game will check the players inventory and will display the available crafts accordingly.

Recipes are stored in the .zon files in the <code>Cubyz/assets/cubyz/recipes/</code> folder. 

For each entry, <code>.inputs</code> specifies the items to be used up in the craft while <code>.outputs</code> specifies what items are given to the player on craft. An additional <code>.reversible</code> variable can also be utilized to indicate to also generate a recipe with the <code>.input</code> and <code>.output</code> fields reversed. 

Currently as of 0.2.0, a max of 5 inputs and only a single output can be set. Reversible recipes require a single input to be set or will throw an error otherwise.

''Note: Recipes are saved to memory on startup and require a game restart for any changes made to take effect.
''