#!/usr/bin/env python3
"""Count observed phrase and token-pair support from cleaned local UTF-8 texts."""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

TOKEN = re.compile(r"[^\W_]+(?:[-'’][^\W_]+)*", re.UNICODE)
BOUNDARY = re.compile(r"[.!?。！？]+|[\r\n]+")


def count_file(path, max_gap):
    ngrams = Counter()
    skipgrams = Counter()
    normalized = path.read_text(encoding="utf-8-sig").casefold()
    for sentence in BOUNDARY.split(normalized):
        tokens = TOKEN.findall(sentence)
        for start, token in enumerate(tokens):
            for width in (2, 3, 4):
                if start + width <= len(tokens):
                    phrase = " ".join(tokens[start:start + width])
                    ngrams[phrase] += 1
            for gap in range(1, max_gap + 1):
                end = start + gap + 1
                if end < len(tokens):
                    skipgrams[(token, tokens[end], gap)] += 1
    return ngrams, skipgrams


def support_rows(occurrences, documents, minimum, limit, render):
    candidates = [key for key, count in documents.items() if count >= minimum]
    candidates.sort(key=lambda key: (-documents[key], -occurrences[key], key))
    return [
        {
            **render(key),
            "documents": documents[key],
            "occurrences": occurrences[key],
        }
        for key in candidates[:limit]
    ]


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("files", type=Path, nargs="+", help="One clean text file per comparable source URL")
    cli.add_argument("--min-docs", type=int, default=2, help="Minimum distinct source files")
    cli.add_argument("--limit", type=int, default=40, help="Maximum rows per result group")
    cli.add_argument("--max-gap", type=int, choices=(1, 2), default=2, help="Maximum intervening tokens")
    options = cli.parse_args()

    paths = list(dict.fromkeys(path.resolve() for path in options.files))
    if not 1 <= options.min_docs <= len(paths):
        cli.error("--min-docs must be between 1 and the number of distinct paths")
    if options.limit < 1:
        cli.error("--limit must be positive")

    ngrams = Counter()
    ngram_docs = Counter()
    skips = Counter()
    skip_docs = Counter()
    try:
        for path in paths:
            phrases, pairs = count_file(path, options.max_gap)
            ngrams.update(phrases)
            ngram_docs.update(phrases.keys())
            skips.update(pairs)
            skip_docs.update(pairs.keys())
    except (OSError, UnicodeError) as error:
        cli.error(str(error))

    output = {
        "method": "Casefolded Unicode word tokens within approximate sentence or line boundaries.",
        "document_count": len(paths),
        "minimum_document_support": options.min_docs,
        "max_intervening_tokens": options.max_gap,
        "ngrams": support_rows(
            ngrams, ngram_docs, options.min_docs, options.limit, lambda key: {"phrase": key}
        ),
        "skipgrams": support_rows(
            skips,
            skip_docs,
            options.min_docs,
            options.limit,
            lambda key: {"first": key[0], "second": key[1], "gap": key[2]},
        ),
    }
    sys.stdout.write(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
