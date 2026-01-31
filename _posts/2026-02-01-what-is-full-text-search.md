---
layout: post
title: "What is Full-Text Search?"
date: 2026-02-01
tags: [programming, search, full-text-search]
---

# What is Full-Text Search?

Full-text search is a technique used by databases and search engines to find and retrieve documents based on their textual content. Unlike simple substring or exact-match searches (e.g., SQL LIKE), full-text search analyzes the text and supports linguistic processing, ranking, and advanced query types.

## Example

Document: “The aircraft engines are inspected regularly.”

``sql
SELECT * FROM documents WHERE content LIKE '%engine%';
```

``full-text
SELECT * FROM documents WHERE MATCH(content) AGAINST('engine' IN NATURAL LANGUAGE MODE);
```

| Query     | LIKE | Full-text |
|-----------|:----:|:---------:|
| aircraft  | ✅   | ✅        |
| engine    | ❌   | ✅        |
| engines   | ✅   | ✅        |
| inspect   | ❌   | ✅        |
| inspection| ❌   | ✅        |

Reason: full-text search applies techniques such as stemming or lemmatization to reduce words to a common root (e.g., "inspected" → "inspect"), so a search for "inspect" matches "inspected". A LIKE query matches substrings exactly and does not perform linguistic normalization.

## How Full-Text Search Works

1. Indexing: The system builds an inverted index mapping terms to documents for fast lookup.  
2. Tokenization: Text is split into tokens (words, phrases) according to language rules.  
3. Normalization: Lowercasing, removing punctuation, and applying stemming/lemmatization.  
4. Stop-word removal: Common words (e.g., "the", "is") may be omitted to reduce noise.  
5. Ranking and retrieval: Matches are scored (e.g., TF-IDF, BM25) and results are ranked by relevance.

## Advantages

- Relevance ranking (term frequency, document length, etc.).  
- Support for complex queries: boolean, phrase, proximity, fuzzy matches.  
- Optimized for large text corpora and fast retrieval.

## Common Use Cases

- Search engines (web or site search)  
- Document management and knowledge bases  
- E-commerce product search  
- Content management systems (CMS)

## Notes & Considerations

- Language and tokenizer choice affect accuracy.  
- Stop-word lists and stemming rules can alter results — tune for your use case.  
- Some systems support synonyms, language detection, and highlight snippets.
what is full-text-search ?

