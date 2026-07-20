![{{ item.name }}]({{ item.image_url }}){ width="300" align=left }

| | |
|:-|-:|
|**ID**| {{ item.id }} |
{% if item.block -%}
|**Block**| [{{ item.id }}]({{ item.block.wiki_link }}) |
{%- endif %}


{% if item.material -%}
| | |
|:-|-:|
|**Durability**| {{ item.material.durability }} |
|**Mass Damage**| {{ item.material.massDamage }} |
|**Hardness Damage**| {{ item.material.hardnessDamage }} |
|**Swing Speed**| {{ item.material.swingSpeed }} |
{%- endif %}

{%  if item.tags %}
{% for tag in item.tags|sort %} <span class="md-tag md-tag-icon"> {{ tag }} </span> {% endfor %}
{%- endif %}