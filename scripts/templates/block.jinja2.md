---
icon: {{ block.icon }}
---

# {{ block.name }}

{% if block.item %}

!!! infobox "{{ block.item.name }} (item)"

{{ '{{ item_infobox(' -}}"{{ block.item.id }}"{{- ') }}' }}

{% endif %}

!!! infobox "{{ block.name }}"

{{ '{{ block_infobox(' -}}"{{ block.id }}"{{- ') }}' }}

## About

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## Obtaining

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## Usage

> This section is a stub. You can help the Cubyz Wiki by expanding it.

## History

> This section is a stub. You can help the Cubyz Wiki by expanding it.
