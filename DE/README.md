

# German Language Learning Scripts

This directory contains Python scripts that generate **audio files for learning German**.

---

## 1. `verbs_conjugations.py`

- Generates audio for **German verb conjugations** with English translations.  
- Supports **regular, stem-changing, and special verbs**.  
- Produces a single MP3 file using **gTTS** and **pydub**, with pauses and optional repetition.  
- English translations are included for most forms, except some third-person singular/plural forms.  
- Usage:

```bash
python verbs_conjugations.py
```

- Output: `german_verbs_conjugations_de_en_YYYY-MM-DD.mp3`

---

## 2. `nouns_accusative.py`

- Generates audio for **German nouns in the accusative case** with English translations.  
- Includes definite, indefinite, and negation examples.  
- Produces a single MP3 file with pauses and repetition.  
- Usage:

```bash
python nouns_accusative.py
```

- Output: `nouns_accusative_YYYYMMDD.mp3`

---

## 3. `nouns_nominative.py`

- Generates audio for **German nouns in the nominative case** with English translations.  
- Includes example sentences and articles (der, die, das).  
- Produces a single MP3 file with pauses and repeated pronunciations.  
- Usage:

```bash
python nouns_nominative.py
```

- Output: `nouns_nominative_YYYYMMDD.mp3`

---

## 4. `partizip_ii.py`

- Generates audio for learning **Partizip II / Perfekt** forms.
- Includes a short summary of the rules, regular verbs, irregular verbs, separable verbs, inseparable prefixes, `-ieren` verbs, and `haben` vs. `sein` examples.
- Uses English prompts followed by German examples repeated twice.
- Usage:

```bash
python partizip_ii.py
```

- Output: `partizip_ii_YYYYMMDD.mp3`

---

## Requirements

```bash
pip install gtts pydub
```

- **ffmpeg** is required by `pydub` to export MP3 files.

---

## Notes

- All scripts create **German → English audio files** for language learning.  
- Dictionaries can be expanded with additional verbs or nouns.  
- Generated audio files can be used for **repetition-based practice**.
