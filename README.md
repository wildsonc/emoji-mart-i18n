# Emoji Translation Utility

This utility script translates emoji metadata using the `emojibase` library, leveraging the extensive emoji data provided by `emojibase-data` and `@emoji-mart/data`. It's designed to help developers integrate multi-language support for emojis into their applications, making emojis more accessible and understandable across different languages.

## Usage

```
https://cdn.jsdelivr.net/gh/wildsonc/emoji-mart-i18n@latest/locales/{locale}/data.json
```
> Replace {locale} to desired locale


```javascript
<Picker
  data={async () => {
    const response = await fetch(
      "https://cdn.jsdelivr.net/gh/wildsonc/emoji-mart-i18n@latest/locales/pt/data.json",
    );

    return response.json();
  }}
  locale="pt"
/>
```

## Suported locales

- Bengali (bu)
- Chinese (zh)
- Chinese, Traditional (zh-hant)
- Danish (da)
- Dutch (nl)
- Estonian (et)
- Finnish (fi)
- French (fr)
- German (de)
- Hindu (hi)
- Hungarian (hu)
- Italian (it)
- Japanese (ja)
- Korean (ko)
- Lithuanian (lt)
- Malay (ms)
- Norwegian (nb)
- Polish (pl)
- Portuguese (pt)
- Russian (ru)
- Spanish (es)
- Spanish, Mexico (es-mx)
- Swedish (sv)
- Thai (th)
- Ukrainian (uk)

## Development

1. Ensure you have Python 3 installed on your system.
2. Install the `requests` library using pip:

```bash
pip install requests
```

3. When prompted, enter the locale code for the language you wish to translate the emojis into (e.g., `pt`, `es`, `fr`).
