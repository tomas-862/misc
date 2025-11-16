from gtts import gTTS
from pydub import AudioSegment
import os
from datetime import datetime

# ===== CONFIGURATION =====
current_date = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = f"nouns_accusativ_{current_date}.mp3"

#
# =======================
#      FOOD SECTOR
# =======================
#
# ===== FOOD SECTOR: German → English =====
das_nouns = {
    "das Essen": "the food / meal",
    "das Öl": "the oil",
    "das Bier, die Biere": "the beer, the beers",
    "das Brot, die Brote": "the bread, the breads",
    "das Brötchen, die Brötchen": "the bread roll, the bread rolls",
    "das Ei, die Eier": "the egg, the eggs",
    "das Salz": "the salt",
    "das Fleisch": "the meat",
    "das Hähnchen, die Hähnchen": "the chicken, the chickens",
    "das Obst": "the fruit",
    "das Wasser": "the water",
    "das Glas, die Gläser": "the glass, the glasses",
    "das Messer, die Messer": "the knife, the knives",
}

der_nouns = {
    "der Apfel, die Äpfel": "the apple, the apples",
    "der Saft, die Säfte": "the juice, the juices",
    "der Fisch, die Fische": "the fish, the fishes",
    "der Schinken, die Schinken": "the ham, the hams",
    "der Tee, die Tees": "the tea, the teas",
    "der Kaffee, die Kaffees": "the coffee, the coffees",
    "der Wein, die Weine": "the wine, the wines",
    "der Käse": "the cheese",
    "der Salat, die Salate": "the salad, the salads",
    "der Löffel, die Löffel": "the spoon, the spoons",
    "der Teller, die Teller": "the plate, the plates",
    "der Zucker": "the sugar",
    "der Kuchen, die Kuchen": "the cake, the cakes",
}

die_nouns = {
    "die Birne, die Birnen": "the pear, the pears",
    "die Nudeln": "the noodles / pasta",
    "die Banane, die Bananen": "the banana, the bananas",
    "die Pommes": "the fries",
    "die Sahne": "the cream",
    "die Butter": "the butter",
    "die Suppe, die Suppen": "the soup, the soups",
    "die Tomate, die Tomaten": "the tomato, the tomatoes",
    "die Kartoffel, die Kartoffeln": "the potato, the potatoes",
    "die Wurst, die Würste": "the sausage, the sausages",
    "die Zigarette, die Zigaretten": "the cigarette, the cigarettes",
    "die Milch": "the milk",
    "die Gabel, die Gabeln": "the fork, the forks",
}

# Accusative case example sentences with negation forms kein/keine/keinen
accusative_examples = {
    "das Essen": "Ich esse kein Essen.",
    "das Öl": "Ich kaufe kein Öl.",
    "das Bier, die Biere": "Ich trinke kein Bier.",
    "das Brot, die Brote": "Ich backe kein Brot.",
    "das Brötchen, die Brötchen": "Ich nehme kein Brötchen.",
    "das Ei, die Eier": "Ich mag kein Ei.",
    "das Salz": "Ich brauche kein Salz.",
    "das Fleisch": "Ich esse kein Fleisch.",
    "das Hähnchen, die Hähnchen": "Ich bestelle kein Hähnchen.",
    "das Obst": "Ich habe kein Obst.",
    "das Wasser": "Ich trinke kein Wasser.",
    "das Glas, die Gläser": "Ich nehme kein Glas.",
    "das Messer, die Messer": "Ich benutze kein Messer.",
    "der Apfel, die Äpfel": "Ich kaufe keinen Apfel.",
    "der Saft, die Säfte": "Ich trinke keinen Saft.",
    "der Fisch, die Fische": "Ich esse keinen Fisch.",
    "der Schinken, die Schinken": "Ich möchte keinen Schinken.",
    "der Tee, die Tees": "Ich trinke keinen Tee.",
    "der Kaffee, die Kaffees": "Ich trinke keinen Kaffee.",
    "der Wein, die Weine": "Ich trinke keinen Wein.",
    "der Käse": "Ich esse keinen Käse.",
    "der Salat, die Salate": "Ich nehme keinen Salat.",
    "der Löffel, die Löffel": "Ich brauche keinen Löffel.",
    "der Teller, die Teller": "Ich wasche keinen Teller.",
    "der Zucker": "Ich nehme keinen Zucker.",
    "der Kuchen, die Kuchen": "Ich backe keinen Kuchen.",
    "die Birne, die Birnen": "Ich kaufe keine Birne.",
    "die Nudeln": "Ich esse keine Nudeln.",
    "die Banane, die Bananen": "Ich esse keine Banane.",
    "die Pommes": "Ich esse keine Pommes.",
    "die Sahne": "Ich nehme keine Sahne.",
    "die Butter": "Ich kaufe keine Butter.",
    "die Suppe, die Suppen": "Ich esse keine Suppe.",
    "die Tomate, die Tomaten": "Ich schneide keine Tomate.",
    "die Kartoffel, die Kartoffeln": "Ich koche keine Kartoffel.",
    "die Wurst, die Würste": "Ich esse keine Wurst.",
    "die Zigarette, die Zigaretten": "Ich rauche keine Zigarette.",
    "die Milch": "Ich trinke keine Milch.",
    "die Gabel, die Gabeln": "Ich nehme keine Gabel.",
}

# Accusative case example sentences with indefinite articles ein/eine/einen
accusative_indefinite_examples = {
    "das Essen": "Ich esse ein Essen.",
    "das Öl": "Ich kaufe ein Öl.",
    "das Bier, die Biere": "Ich trinke ein Bier.",
    "das Brot, die Brote": "Ich backe ein Brot.",
    "das Brötchen, die Brötchen": "Ich nehme ein Brötchen.",
    "das Ei, die Eier": "Ich mag ein Ei.",
    "das Salz": "Ich brauche ein Salz.",
    "das Fleisch": "Ich esse ein Fleisch.",
    "das Hähnchen, die Hähnchen": "Ich bestelle ein Hähnchen.",
    "das Obst": "Ich habe ein Obst.",
    "das Wasser": "Ich trinke ein Wasser.",
    "das Glas, die Gläser": "Ich nehme ein Glas.",
    "das Messer, die Messer": "Ich benutze ein Messer.",
    "der Apfel, die Äpfel": "Ich kaufe einen Apfel.",
    "der Saft, die Säfte": "Ich trinke einen Saft.",
    "der Fisch, die Fische": "Ich esse einen Fisch.",
    "der Schinken, die Schinken": "Ich möchte einen Schinken.",
    "der Tee, die Tees": "Ich trinke einen Tee.",
    "der Kaffee, die Kaffees": "Ich trinke einen Kaffee.",
    "der Wein, die Weine": "Ich trinke einen Wein.",
    "der Käse": "Ich esse einen Käse.",
    "der Salat, die Salate": "Ich nehme einen Salat.",
    "der Löffel, die Löffel": "Ich brauche einen Löffel.",
    "der Teller, die Teller": "Ich wasche einen Teller.",
    "der Zucker": "Ich nehme einen Zucker.",
    "der Kuchen, die Kuchen": "Ich backe einen Kuchen.",
    "die Birne, die Birnen": "Ich kaufe eine Birne.",
    "die Nudeln": "Ich esse eine Nudel.",
    "die Banane, die Bananen": "Ich esse eine Banane.",
    "die Pommes": "Ich esse eine Pommes.",
    "die Sahne": "Ich nehme eine Sahne.",
    "die Butter": "Ich kaufe eine Butter.",
    "die Suppe, die Suppen": "Ich esse eine Suppe.",
    "die Tomate, die Tomaten": "Ich schneide eine Tomate.",
    "die Kartoffel, die Kartoffeln": "Ich koche eine Kartoffel.",
    "die Wurst, die Würste": "Ich esse eine Wurst.",
    "die Zigarette, die Zigaretten": "Ich rauche eine Zigarette.",
    "die Milch": "Ich trinke eine Milch.",
    "die Gabel, die Gabeln": "Ich nehme eine Gabel.",
}

# English translations of example sentences (full sentences)
accusative_examples_english = {
    "Ich esse kein Essen.": "I do not eat any food.",
    "Ich kaufe kein Öl.": "I do not buy any oil.",
    "Ich trinke kein Bier.": "I do not drink any beer.",
    "Ich backe kein Brot.": "I do not bake any bread.",
    "Ich nehme kein Brötchen.": "I do not take any bread roll.",
    "Ich mag kein Ei.": "I do not like any egg.",
    "Ich brauche kein Salz.": "I do not need any salt.",
    "Ich esse kein Fleisch.": "I do not eat any meat.",
    "Ich bestelle kein Hähnchen.": "I do not order any chicken.",
    "Ich habe kein Obst.": "I do not have any fruit.",
    "Ich trinke kein Wasser.": "I do not drink any water.",
    "Ich nehme kein Glas.": "I do not take any glass.",
    "Ich benutze kein Messer.": "I do not use any knife.",
    "Ich kaufe keinen Apfel.": "I do not buy any apple.",
    "Ich trinke keinen Saft.": "I do not drink any juice.",
    "Ich esse keinen Fisch.": "I do not eat any fish.",
    "Ich möchte keinen Schinken.": "I do not want any ham.",
    "Ich trinke keinen Tee.": "I do not drink any tea.",
    "Ich trinke keinen Kaffee.": "I do not drink any coffee.",
    "Ich trinke keinen Wein.": "I do not drink any wine.",
    "Ich esse keinen Käse.": "I do not eat any cheese.",
    "Ich nehme keinen Salat.": "I do not take any salad.",
    "Ich brauche keinen Löffel.": "I do not need any spoon.",
    "Ich wasche keinen Teller.": "I do not wash any plate.",
    "Ich nehme keinen Zucker.": "I do not take any sugar.",
    "Ich backe keinen Kuchen.": "I do not bake any cake.",
    "Ich kaufe keine Birne.": "I do not buy any pear.",
    "Ich esse keine Nudeln.": "I do not eat any noodles.",
    "Ich esse keine Banane.": "I do not eat any banana.",
    "Ich esse keine Pommes.": "I do not eat any fries.",
    "Ich nehme keine Sahne.": "I do not take any cream.",
    "Ich kaufe keine Butter.": "I do not buy any butter.",
    "Ich esse keine Suppe.": "I do not eat any soup.",
    "Ich schneide keine Tomate.": "I do not cut any tomato.",
    "Ich koche keine Kartoffel.": "I do not cook any potato.",
    "Ich esse keine Wurst.": "I do not eat any sausage.",
    "Ich rauche keine Zigarette.": "I do not smoke any cigarette.",
    "Ich trinke keine Milch.": "I do not drink any milk.",
    "Ich nehme keine Gabel.": "I do not take any fork.",
}

accusative_indefinite_examples_english = {
    "Ich esse ein Essen.": "I eat a meal.",
    "Ich kaufe ein Öl.": "I buy an oil.",
    "Ich trinke ein Bier.": "I drink a beer.",
    "Ich backe ein Brot.": "I bake a bread.",
    "Ich nehme ein Brötchen.": "I take a bread roll.",
    "Ich mag ein Ei.": "I like an egg.",
    "Ich brauche ein Salz.": "I need a salt.",
    "Ich esse ein Fleisch.": "I eat a meat.",
    "Ich bestelle ein Hähnchen.": "I order a chicken.",
    "Ich habe ein Obst.": "I have a fruit.",
    "Ich trinke ein Wasser.": "I drink a water.",
    "Ich nehme ein Glas.": "I take a glass.",
    "Ich benutze ein Messer.": "I use a knife.",
    "Ich kaufe einen Apfel.": "I buy an apple.",
    "Ich trinke einen Saft.": "I drink a juice.",
    "Ich esse einen Fisch.": "I eat a fish.",
    "Ich möchte einen Schinken.": "I want a ham.",
    "Ich trinke einen Tee.": "I drink a tea.",
    "Ich trinke einen Kaffee.": "I drink a coffee.",
    "Ich trinke einen Wein.": "I drink a wine.",
    "Ich esse einen Käse.": "I eat a cheese.",
    "Ich nehme einen Salat.": "I take a salad.",
    "Ich brauche einen Löffel.": "I need a spoon.",
    "Ich wasche einen Teller.": "I wash a plate.",
    "Ich nehme einen Zucker.": "I take a sugar.",
    "Ich backe einen Kuchen.": "I bake a cake.",
    "Ich kaufe eine Birne.": "I buy a pear.",
    "Ich esse eine Nudel.": "I eat a noodle.",
    "Ich esse eine Banane.": "I eat a banana.",
    "Ich esse eine Pommes.": "I eat fries.",
    "Ich nehme eine Sahne.": "I take cream.",
    "Ich kaufe eine Butter.": "I buy butter.",
    "Ich esse eine Suppe.": "I eat a soup.",
    "Ich schneide eine Tomate.": "I cut a tomato.",
    "Ich koche eine Kartoffel.": "I cook a potato.",
    "Ich esse eine Wurst.": "I eat a sausage.",
    "Ich rauche eine Zigarette.": "I smoke a cigarette.",
    "Ich trinke eine Milch.": "I drink milk.",
    "Ich nehme eine Gabel.": "I take a fork.",
}

#
# =======================
#      QUESTION SECTOR
# =======================
#
question_words = {
    "wer?": "who?",
    "was?": "what?",
    "wann?": "when?",
    "wo?": "where?",
    "warum?": "why?",
    "wohin?": "where to?",
    "wie ...?": "how ...?",
    "wie alt ...?": "how old ...?",
    "wie lange ...?": "how long ...?",
    "wie oft ...?": "how often ...?",
    "wie weit ...?": "how far ...?",
}

# ===== CREATE AUDIO =====
audio_segments = []

# Pauses
pause_1s = AudioSegment.silent(duration=3000)  # 3 seconds
pause_2s = AudioSegment.silent(duration=3000)  # 3 seconds

def generate_tts(text, lang, filename="temp.mp3"):
    """Generate speech for a given text and return as AudioSegment"""
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return AudioSegment.from_mp3(filename)

def process_nouns(nouns_dict):
    for german, english in nouns_dict.items():
        english_audio = generate_tts(english, 'en')
        german_audio = generate_tts(german, 'de')

        # English word
        audio_segments.append(english_audio)
        audio_segments.append(pause_2s)

        # German translation once
        audio_segments.append(german_audio)
        audio_segments.append(pause_1s)

        # German translation repeated second time
        audio_segments.append(german_audio)
        audio_segments.append(pause_1s)

        # Add accusative negation example sentence if available
        example_sentence_neg = accusative_examples.get(german)
        if example_sentence_neg:
            # Generate English translation of example sentence from the English dictionary
            example_english_text = accusative_examples_english.get(example_sentence_neg, english)
            example_english_audio = generate_tts(example_english_text, 'en')
            example_german_audio = generate_tts(example_sentence_neg, 'de')

            # English example sentence
            audio_segments.append(example_english_audio)
            audio_segments.append(pause_2s)

            # German example sentence once
            audio_segments.append(example_german_audio)
            audio_segments.append(pause_1s)

            # German example sentence repeated second time
            audio_segments.append(example_german_audio)
            audio_segments.append(pause_1s)

        # Add accusative indefinite article example sentence if available
        example_sentence_indef = accusative_indefinite_examples.get(german)
        if example_sentence_indef:
            # Generate English translation of example sentence from the English dictionary
            example_english_text = accusative_indefinite_examples_english.get(example_sentence_indef, english)
            example_english_audio = generate_tts(example_english_text, 'en')
            example_german_audio = generate_tts(example_sentence_indef, 'de')

            # English example sentence
            audio_segments.append(example_english_audio)
            audio_segments.append(pause_2s)

            # German example sentence once
            audio_segments.append(example_german_audio)
            audio_segments.append(pause_1s)

            # German example sentence repeated second time
            audio_segments.append(example_german_audio)
            audio_segments.append(pause_1s)

# 2. English → German for das nouns
process_nouns(das_nouns)

# 2. English → German for der nouns
process_nouns(der_nouns)

# 2. English → German for die nouns
process_nouns(die_nouns)

# English → German for question words with German repeated twice
for german, english in question_words.items():
    english_audio = generate_tts(english, 'en')
    german_audio = generate_tts(german, 'de')

    # English word
    audio_segments.append(english_audio)
    audio_segments.append(pause_2s)

    # German translation once
    audio_segments.append(german_audio)
    audio_segments.append(pause_1s)

    # German translation repeated second time
    audio_segments.append(german_audio)
    audio_segments.append(pause_1s)

# Combine all segments
final_audio = sum(audio_segments)

# Export final file
final_audio.export(OUTPUT_FILE, format="mp3")

# Cleanup
if os.path.exists("temp.mp3"):
    os.remove("temp.mp3")

print(f"Audio file created: {OUTPUT_FILE}")