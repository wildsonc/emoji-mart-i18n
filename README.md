# Emoji Translation Utility

This utility script translates emoji metadata using the `emojibase` library, leveraging the extensive emoji data provided by `emojibase-data` and `@emoji-mart/data`. It's designed to help developers integrate multi-language support for emojis into their applications, making emojis more accessible and understandable across different languages.

## Features

- Loads emoji data from `emojibase` based on the specified locale.
- Translates emojis from `emoji-mart` using `emojibase` data, matching them by their hexcodes.
- Creates a locale-specific directory and saves the translated emoji data in a JSON file.
- Supports dynamic locale input for translation into different languages.

## Usage

```
https://cdn.jsdelivr.net/gh/wildsonc/emoji-mart-i18n@latest/locales/{locale}/data.json
```

## Development

1. Ensure you have Python 3 installed on your system.
2. Install the `requests` library using pip:

```bash
pip install requests
```

3. When prompted, enter the locale code for the language you wish to translate the emojis into (e.g., `pt`, `es`, `fr`).
