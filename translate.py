import json
import os

import requests

EMOJIBASE_VERSION = "15.3.0"


def load_emojibase(locale):
    print(f"Loading {locale}...")
    url = f"https://cdn.jsdelivr.net/npm/emojibase-data@{EMOJIBASE_VERSION}/{locale}/data.json"
    return requests.get(url).json()


def load_emojimart():
    print("Loading emojimart...")
    url = "https://cdn.jsdelivr.net/npm/@emoji-mart/data"
    return requests.get(url).json()


emojimart = load_emojimart()


def translate(locale):
    emojibase = load_emojibase(locale)

    emojis = {}
    translated = 0
    for k, v in emojimart["emojis"].items():
        emoji = emojimart["emojis"][k]
        skin = emoji["skins"][0]
        hexcode = skin["unified"].upper()
        hexcode2 = hexcode.split("-")[0]

        if skin:
            base = [
                x
                for x in emojibase
                if x["hexcode"] == hexcode or x["hexcode"] == hexcode2
            ]

            if base:
                base = base[0]
                emoji["keywords"] = base.get("tags") or emoji["keywords"]
                emoji["name"] = base["label"].capitalize()
                translated += 1

        emojis[k] = emoji

    emojimart["emojis"] = emojis
    if not os.path.exists(f"./data/{locale}"):
        os.makedirs(f"./data/{locale}")

    print(f"Translated {translated} emojis")
    open(f"./locales/{locale}/data.json", "w").write(
        json.dumps(emojimart, ensure_ascii=False)
    )


locale = input("Enter locale: ")
translate(locale)
