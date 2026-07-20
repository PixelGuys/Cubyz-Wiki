---
icon: {{ item.icon }}
---

# {{ item.name }}

!!! infobox "{{ item.name }}"

{{ '{{ item_infobox(' -}}"{{ item.id }}"{{- ') }}' }}

{% if item.block %}

!!! infobox "{{ item.block.name }} (block)"

{{ '{{ block_infobox(' -}}"{{ item.block.id }}"{{- ') }}' }}

{% endif %}


## About

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## Obtaining

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## Usage

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## History

> This section is a stub. You can help the Cubyz Wiki by expanding it.
