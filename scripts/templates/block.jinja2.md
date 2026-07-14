---
icon: {{ block.icon }}
---

{% if block.item %}

<script>
    window.location.replace("{{ block.item.wiki_link }}");
</script>

{% endif %}

# {{ block.name }}

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
