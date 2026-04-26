from datetime import datetime
import os

from gtts import gTTS
from pydub import AudioSegment


# ===== CONFIGURATION =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
current_date = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = os.path.join(BASE_DIR, f"flumserberg_story_{current_date}.mp3")
TEMP_FILE = os.path.join(BASE_DIR, "temp_flumserberg_story.mp3")


# ===== AUDIO HELPERS =====
audio_segments = []
pause_short = AudioSegment.silent(duration=1100)
pause_medium = AudioSegment.silent(duration=2500)
pause_long = AudioSegment.silent(duration=4200)


def generate_tts(text, lang):
    """Generate speech for a given text and return it as an AudioSegment."""
    tts = gTTS(text=text, lang=lang)
    tts.save(TEMP_FILE)
    return AudioSegment.from_mp3(TEMP_FILE)


def add_spoken(text, lang, pause=pause_short):
    audio_segments.append(generate_tts(text, lang))
    audio_segments.append(pause)


def add_learning_pair(lithuanian, german, repeats=3):
    add_spoken(lithuanian, "lt", pause_medium)
    german_audio = generate_tts(german, "de")

    for _ in range(repeats):
        audio_segments.append(german_audio)
        audio_segments.append(pause_short)


def add_section(title):
    add_spoken(title, "lt", pause_long)


def add_full_story(repeats=2):
    story_audio = generate_tts(full_story_german, "de")

    for _ in range(repeats):
        audio_segments.append(story_audio)
        audio_segments.append(pause_long)


# ===== STORY =====
full_story_german = """
Liebe Anna,
ich bin schon zwei Wochen im Flumserberg und morgen fahre ich nach Hause.
Die Zeit ist sehr schnell vergangen!
Der Urlaub war fantastisch.
Ich habe jeden Tag Ski gefahren und das Wetter war super.
Am Abend habe ich oft mit anderen Touristen gesprochen und wir haben zusammen gegessen.
Aber gestern habe ich einen Unglückstag gehabt.
Am Nachmittag bin ich Ski gefahren.
Ich bin nicht vorsichtig gewesen und bin gefallen.
Ich konnte nicht mehr laufen.
Ich bin zum Arzt gegangen.
Der Arzt hat gesagt, der Fuss ist nicht gebrochen.
Aber jetzt darf ich nicht mehr Ski fahren.
Das ist sehr schade!
Heute bleibe ich im Hotel und lese ein Buch.
Morgen fahre ich nach Hause.
Wie geht es dir?
Was hast du am Wochenende gemacht?
Liebe Grüsse,
Tomas
""".strip()


full_story_lithuanian = """
Miela Anna,
aš jau dvi savaites esu Flumserberge ir rytoj važiuoju namo.
Laikas prabėgo labai greitai!
Atostogos buvo fantastiškos.
Kiekvieną dieną slidinėjau, o oras buvo puikus.
Vakare dažnai kalbėjau su kitais turistais ir mes kartu valgėme.
Bet vakar man buvo nelaiminga diena.
Po pietų slidinėjau.
Nebuvau atsargus ir nukritau.
Nebegalėjau vaikščioti.
Nuėjau pas gydytoją.
Gydytojas pasakė, kad pėda nelūžusi.
Bet dabar nebegaliu slidinėti.
Labai gaila!
Šiandien lieku viešbutyje ir skaitau knygą.
Rytoj važiuoju namo.
Kaip tau sekasi?
Ką veikei savaitgalį?
Širdingi linkėjimai,
Tomas
""".strip()


story_pairs = [
    ("Miela Anna.", "Liebe Anna,"),
    (
        "Aš jau dvi savaites esu Flumserberge ir rytoj važiuoju namo.",
        "Ich bin schon zwei Wochen im Flumserberg und morgen fahre ich nach Hause.",
    ),
    ("Laikas prabėgo labai greitai.", "Die Zeit ist sehr schnell vergangen!"),
    ("Atostogos buvo fantastiškos.", "Der Urlaub war fantastisch."),
    (
        "Kiekvieną dieną slidinėjau, o oras buvo puikus.",
        "Ich habe jeden Tag Ski gefahren und das Wetter war super.",
    ),
    (
        "Vakare dažnai kalbėjau su kitais turistais ir mes kartu valgėme.",
        "Am Abend habe ich oft mit anderen Touristen gesprochen und wir haben zusammen gegessen.",
    ),
    ("Bet vakar man buvo nelaiminga diena.", "Aber gestern habe ich einen Unglückstag gehabt."),
    ("Po pietų slidinėjau.", "Am Nachmittag bin ich Ski gefahren."),
    (
        "Nebuvau atsargus ir nukritau.",
        "Ich bin nicht vorsichtig gewesen und bin gefallen.",
    ),
    ("Nebegalėjau vaikščioti.", "Ich konnte nicht mehr laufen."),
    ("Nuėjau pas gydytoją.", "Ich bin zum Arzt gegangen."),
    (
        "Gydytojas pasakė, kad pėda nelūžusi.",
        "Der Arzt hat gesagt, der Fuss ist nicht gebrochen.",
    ),
    ("Bet dabar nebegaliu slidinėti.", "Aber jetzt darf ich nicht mehr Ski fahren."),
    ("Labai gaila.", "Das ist sehr schade!"),
    (
        "Šiandien lieku viešbutyje ir skaitau knygą.",
        "Heute bleibe ich im Hotel und lese ein Buch.",
    ),
    ("Rytoj važiuoju namo.", "Morgen fahre ich nach Hause."),
    ("Kaip tau sekasi?", "Wie geht es dir?"),
    ("Ką veikei savaitgalį?", "Was hast du am Wochenende gemacht?"),
    ("Širdingi linkėjimai.", "Liebe Grüsse,"),
    ("Tomas.", "Tomas"),
]


partizip_notes = [
    ("Praėjo. Veiksmažodis: vergehen. Partizip zwei: vergangen.", "Die Zeit ist vergangen."),
    ("Slidinėjau. Veiksmažodis: Ski fahren. Perfekt su haben.", "Ich habe Ski gefahren."),
    ("Kalbėjau. Veiksmažodis: sprechen. Partizip zwei: gesprochen.", "Ich habe gesprochen."),
    ("Valgėme. Veiksmažodis: essen. Partizip zwei: gegessen.", "Wir haben gegessen."),
    ("Buvau. Veiksmažodis: sein. Partizip zwei: gewesen.", "Ich bin gewesen."),
    ("Nukritau. Veiksmažodis: fallen. Perfekt su sein.", "Ich bin gefallen."),
    ("Nuėjau. Veiksmažodis: gehen. Perfekt su sein.", "Ich bin gegangen."),
    ("Pasakė. Veiksmažodis: sagen. Partizip zwei: gesagt.", "Der Arzt hat gesagt."),
    ("Sulūžęs. Veiksmažodis: brechen. Partizip zwei: gebrochen.", "Der Fuss ist gebrochen."),
    ("Veikei. Veiksmažodis: machen. Partizip zwei: gemacht.", "Was hast du gemacht?"),
]


# ===== CREATE AUDIO =====
add_section("Pirmiausia visas pasakojimas vokiškai. Klausykis bendros prasmės.")
add_full_story(repeats=1)

add_section("Dabar visas vertimas į lietuvių kalbą.")
add_spoken(full_story_lithuanian, "lt", pause_long)

add_section("Dabar mokomės sakiniais. Išgirsi lietuviškai, tada vokiškai tris kartus.")
for lithuanian, german in story_pairs:
    add_learning_pair(lithuanian, german, repeats=3)

add_section("Svarbiausios Partizip zwei formos iš šio pasakojimo.")
for lithuanian, german in partizip_notes:
    add_learning_pair(lithuanian, german, repeats=2)

add_section("Pabaigai visas pasakojimas vokiškai du kartus. Bandyk kalbėti kartu.")
add_full_story(repeats=2)


# Combine all segments and export final file
final_audio = sum(audio_segments)
final_audio.export(OUTPUT_FILE, format="mp3")


# Cleanup
if os.path.exists(TEMP_FILE):
    os.remove(TEMP_FILE)

print(f"Audio file created: {OUTPUT_FILE}")
