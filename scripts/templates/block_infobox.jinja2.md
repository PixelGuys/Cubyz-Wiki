![{{ block.name }}]({{ block.image_url }}){ width="300" align=left }

| | |
|:-|-:|
|**ID**| {{ block.id }} |
{% if block.item -%}
|**Item**| [{{ block.id }}]({{ block.item.wiki_link }}) |
{%- endif %}
{%- if block.ore %}
|**Max Height**| {{ block.ore.max_height }} |
|**Min Height**| {{ block.ore.min_height }} |
{%- endif %}

{% if block.item and block.item.material -%}
| | |
|:-|-:|
|**Durability**| {{ block.item.material.durability }} |
|**Mass Damage**| {{ block.item.material.massDamage }} |
|**Hardness Damage**| {{ block.item.material.hardnessDamage }} |
|**Swing Speed**| {{ block.item.material.swingSpeed }} |
{%- endif %}

{%  if block.tags %}
{% for tag in block.tags|sort %} <span class="md-tag md-tag-icon"> {{ tag }} </span> {% endfor %}
{%- endif %}