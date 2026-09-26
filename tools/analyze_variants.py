"""Mesure reproductible du texte des deux maquettes HTML locales."""

from html.parser import HTMLParser
from pathlib import Path
import re

FILES = ("index.html", "experimental.html")
PHRASES = (
    "Smart IPTV",
    "abonnement IPTV",
    "abonnement IPTV France",
    "IPTV premium",
    "abonnement IPTV Smart TV",
    "IPTV multi-écrans",
)
CATEGORIES = ("title", "description", "h1", "headings", "body", "alt")
WORD_PATTERN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[’'-][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*")


class ContentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.all_body = []
        self.content = {category: [] for category in CATEGORIES}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.stack.append(tag)
        if tag == "meta" and attributes.get("name") == "description":
            self.content["description"].append(attributes.get("content", ""))
        if attributes.get("alt") is not None:
            self.content["alt"].append(attributes["alt"])

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index] == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        if not data.strip() or any(tag in self.stack for tag in ("script", "style")):
            return
        if "title" in self.stack:
            self.content["title"].append(data)
        if "h1" in self.stack:
            self.content["h1"].append(data)
        if any(tag in self.stack for tag in ("h2", "h3")):
            self.content["headings"].append(data)
        if "body" in self.stack:
            self.all_body.append(data)
            if not any(tag in self.stack for tag in ("h1", "h2", "h3")):
                self.content["body"].append(data)


for filename in FILES:
    parser = ContentParser()
    parser.feed(Path(filename).read_text(encoding="utf-8"))
    text = {key: " ".join(value) for key, value in parser.content.items()}
    words = WORD_PATTERN.findall(" ".join(parser.all_body))
    print(f"\n{filename}: {len(words)} mots visibles")
    for phrase in PHRASES:
        counts = [len(re.findall(re.escape(phrase), text[key], re.IGNORECASE)) for key in CATEGORIES]
        print(f"{phrase}: {dict(zip(CATEGORIES, counts))}")
