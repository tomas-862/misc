from datetime import datetime
import os

from gtts import gTTS
from pydub import AudioSegment


# ===== CONFIGURATION =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
current_date = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = os.path.join(BASE_DIR, f"partizip_ii_{current_date}.mp3")
TEMP_FILE = os.path.join(BASE_DIR, "temp_partizip_ii.mp3")


# ===== AUDIO HELPERS =====
audio_segments = []
pause_short = AudioSegment.silent(duration=1000)
pause_medium = AudioSegment.silent(duration=2200)
pause_long = AudioSegment.silent(duration=3500)


def generate_tts(text, lang):
    """Generate speech for a given text and return it as an AudioSegment."""
    tts = gTTS(text=text, lang=lang)
    tts.save(TEMP_FILE)
    return AudioSegment.from_mp3(TEMP_FILE)


def add_spoken(text, lang, pause=pause_short):
    audio_segments.append(generate_tts(text, lang))
    audio_segments.append(pause)


def add_english_to_german(english, german, repeats=2):
    add_spoken(english, "en", pause_medium)
    german_audio = generate_tts(german, "de")

    for _ in range(repeats):
        audio_segments.append(german_audio)
        audio_segments.append(pause_short)


def add_section(title):
    add_spoken(title, "en", pause_long)


# ===== PARTIZIP II SUMMARY =====
summary_rules = [
    (
        "Rule one. Regular verbs usually form Partizip zwei with ge, verb stem, and t.",
        "machen, gemacht. lernen, gelernt. kaufen, gekauft.",
    ),
    (
        "Rule two. Irregular verbs often use ge, a changed stem, and en.",
        "sehen, gesehen. schreiben, geschrieben. trinken, getrunken.",
    ),
    (
        "Rule three. Separable verbs put ge between the prefix and the verb.",
        "aufmachen, aufgemacht. einkaufen, eingekauft. anrufen, angerufen.",
    ),
    (
        "Rule four. Inseparable prefixes do not take ge.",
        "bezahlen, bezahlt. besuchen, besucht. erklären, erklärt. vergessen, vergessen.",
    ),
    (
        "Rule five. Verbs ending in ieren do not take ge and usually end with t.",
        "studieren, studiert. telefonieren, telefoniert. reparieren, repariert.",
    ),
    (
        "Rule six. Movement or change of state often uses sein in the Perfekt.",
        "Ich bin gegangen. Ich bin gekommen. Ich bin aufgestanden.",
    ),
    (
        "Rule seven. Most other verbs use haben in the Perfekt.",
        "Ich habe gelernt. Ich habe gekauft. Ich habe gearbeitet.",
    ),
]


regular_verbs = [
    ("to make or do. machen, gemacht.", "machen - gemacht"),
    ("I did it.", "Ich habe es gemacht."),
    ("to learn. lernen, gelernt.", "lernen - gelernt"),
    ("I learned German.", "Ich habe Deutsch gelernt."),
    ("to buy. kaufen, gekauft.", "kaufen - gekauft"),
    ("I bought bread.", "Ich habe Brot gekauft."),
    ("to play. spielen, gespielt.", "spielen - gespielt"),
    ("We played football.", "Wir haben Fußball gespielt."),
    ("to work. arbeiten, gearbeitet.", "arbeiten - gearbeitet"),
    ("He worked today.", "Er hat heute gearbeitet."),
    ("to ask. fragen, gefragt.", "fragen - gefragt"),
    ("She asked.", "Sie hat gefragt."),
    ("to say. sagen, gesagt.", "sagen - gesagt"),
    ("I said that.", "Ich habe das gesagt."),
    ("to live. wohnen, gewohnt.", "wohnen - gewohnt"),
    ("I lived in Berlin.", "Ich habe in Berlin gewohnt."),
]


irregular_verbs = [
    ("to be. sein, gewesen.", "sein - gewesen"),
    ("I was at home.", "Ich bin zu Hause gewesen."),
    ("to have. haben, gehabt.", "haben - gehabt"),
    ("I had time.", "Ich habe Zeit gehabt."),
    ("to go. gehen, gegangen.", "gehen - gegangen"),
    ("I went home.", "Ich bin nach Hause gegangen."),
    ("to come. kommen, gekommen.", "kommen - gekommen"),
    ("She came late.", "Sie ist spät gekommen."),
    ("to drink. trinken, getrunken.", "trinken - getrunken"),
    ("I drank water.", "Ich habe Wasser getrunken."),
    ("to eat. essen, gegessen.", "essen - gegessen"),
    ("We ate soup.", "Wir haben Suppe gegessen."),
    ("to read. lesen, gelesen.", "lesen - gelesen"),
    ("He read the book.", "Er hat das Buch gelesen."),
    ("to write. schreiben, geschrieben.", "schreiben - geschrieben"),
    ("I wrote an email.", "Ich habe eine E-Mail geschrieben."),
    ("to see. sehen, gesehen.", "sehen - gesehen"),
    ("I saw the film.", "Ich habe den Film gesehen."),
    ("to speak. sprechen, gesprochen.", "sprechen - gesprochen"),
    ("We spoke German.", "Wir haben Deutsch gesprochen."),
    ("to take. nehmen, genommen.", "nehmen - genommen"),
    ("I took the bus.", "Ich habe den Bus genommen."),
    ("to find. finden, gefunden.", "finden - gefunden"),
    ("I found my keys.", "Ich habe meine Schlüssel gefunden."),
]


separable_verbs = [
    ("to open. aufmachen, aufgemacht.", "aufmachen - aufgemacht"),
    ("I opened the door.", "Ich habe die Tür aufgemacht."),
    ("to close. zumachen, zugemacht.", "zumachen - zugemacht"),
    ("I closed the window.", "Ich habe das Fenster zugemacht."),
    ("to call. anrufen, angerufen.", "anrufen - angerufen"),
    ("I called my mother.", "Ich habe meine Mutter angerufen."),
    ("to shop. einkaufen, eingekauft.", "einkaufen - eingekauft"),
    ("We went shopping.", "Wir haben eingekauft."),
    ("to get up. aufstehen, aufgestanden.", "aufstehen - aufgestanden"),
    ("I got up early.", "Ich bin früh aufgestanden."),
]


inseparable_and_ieren_verbs = [
    ("to visit. besuchen, besucht. No ge.", "besuchen - besucht"),
    ("I visited my friend.", "Ich habe meinen Freund besucht."),
    ("to pay. bezahlen, bezahlt. No ge.", "bezahlen - bezahlt"),
    ("I paid the bill.", "Ich habe die Rechnung bezahlt."),
    ("to explain. erklären, erklärt. No ge.", "erklären - erklärt"),
    ("The teacher explained the grammar.", "Der Lehrer hat die Grammatik erklärt."),
    ("to forget. vergessen, vergessen. No ge.", "vergessen - vergessen"),
    ("I forgot the word.", "Ich habe das Wort vergessen."),
    ("to study. studieren, studiert. No ge.", "studieren - studiert"),
    ("She studied medicine.", "Sie hat Medizin studiert."),
    ("to telephone. telefonieren, telefoniert. No ge.", "telefonieren - telefoniert"),
    ("I telephoned today.", "Ich habe heute telefoniert."),
]


haben_vs_sein = [
    ("I learned.", "Ich habe gelernt."),
    ("I worked.", "Ich habe gearbeitet."),
    ("I bought something.", "Ich habe etwas gekauft."),
    ("I ate.", "Ich habe gegessen."),
    ("I drank.", "Ich habe getrunken."),
    ("I went.", "Ich bin gegangen."),
    ("I came.", "Ich bin gekommen."),
    ("I got up.", "Ich bin aufgestanden."),
    ("I drove to Berlin.", "Ich bin nach Berlin gefahren."),
    ("I stayed at home.", "Ich bin zu Hause geblieben."),
]


# ===== CREATE AUDIO =====
add_section("Partizip zwei summary. Listen to the rule, then repeat the German examples.")
for english, german in summary_rules:
    add_english_to_german(english, german)

add_section("Regular verbs. The pattern is ge plus stem plus t.")
for english, german in regular_verbs:
    add_english_to_german(english, german)

add_section("Irregular verbs. Learn these as fixed forms.")
for english, german in irregular_verbs:
    add_english_to_german(english, german)

add_section("Separable verbs. Ge goes between the prefix and the verb.")
for english, german in separable_verbs:
    add_english_to_german(english, german)

add_section("Inseparable prefixes and verbs ending in ieren. These forms do not use ge.")
for english, german in inseparable_and_ieren_verbs:
    add_english_to_german(english, german)

add_section("Haben or sein in the Perfekt. Repeat the full sentence.")
for english, german in haben_vs_sein:
    add_english_to_german(english, german)


# Combine all segments and export final file
final_audio = sum(audio_segments)
final_audio.export(OUTPUT_FILE, format="mp3")


# Cleanup
if os.path.exists(TEMP_FILE):
    os.remove(TEMP_FILE)

print(f"Audio file created: {OUTPUT_FILE}")
