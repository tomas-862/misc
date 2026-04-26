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
pause_recall = AudioSegment.silent(duration=3000)


def generate_tts(text, lang, slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(TEMP_FILE)
    return AudioSegment.from_mp3(TEMP_FILE)


def add_spoken(text, lang, pause=pause_short):
    audio_segments.append(generate_tts(text, lang))
    audio_segments.append(pause)


def add_learning_pair(lithuanian, german, repeats=2, partizip_form=None):
    if partizip_form:
        add_spoken(f"Partizip zwei: {partizip_form}", "lt", pause_short)
        for form in partizip_form.split(", "):
            form_audio = generate_tts(form.strip(), "de", slow=True)
            audio_segments.append(form_audio)
            audio_segments.append(pause_short)
    add_spoken(lithuanian, "lt", pause_recall)
    german_audio = generate_tts(german, "de")
    for _ in range(repeats):
        audio_segments.append(german_audio)
        audio_segments.append(pause_medium)


def add_partizip_note(lithuanian, german, form):
    for f in form.split(", "):
        form_audio = generate_tts(f.strip(), "de", slow=True)
        audio_segments.append(form_audio)
        audio_segments.append(pause_short)
    add_spoken(lithuanian, "lt", pause_short)
    german_audio = generate_tts(german, "de")
    audio_segments.append(german_audio)
    audio_segments.append(pause_medium)
    audio_segments.append(german_audio)
    audio_segments.append(pause_medium)


def add_section(title):
    add_spoken(title, "lt", pause_long)


def add_full_story(repeats=2):
    story_audio = generate_tts(full_story_german, "de")
    for _ in range(repeats):
        audio_segments.append(story_audio)
        audio_segments.append(pause_long)


def add_annotated_story():
    for sentence, partizip in story_sentences_annotated:
        add_spoken(sentence, "de", pause_short)
        if partizip:
            add_spoken(f"Partizip zwei: {partizip}", "lt", pause_short)
            for form in partizip.split(", "):
                form_audio = generate_tts(form.strip(), "de", slow=True)
                audio_segments.append(form_audio)
                audio_segments.append(pause_short)
            audio_segments.append(pause_medium)


def add_comprehension_test():
    for lithuanian, german in story_pairs:
        add_spoken(german, "de", AudioSegment.silent(duration=4000))
        add_spoken(lithuanian, "lt", pause_medium)


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

sentence_partizip_map = {
    "Die Zeit ist sehr schnell vergangen!": "vergangen",
    "Ich habe jeden Tag Ski gefahren und das Wetter war super.": "gefahren",
    "Am Abend habe ich oft mit anderen Touristen gesprochen und wir haben zusammen gegessen.": "gesprochen, gegessen",
    "Aber gestern habe ich einen Unglückstag gehabt.": "gehabt",
    "Am Nachmittag bin ich Ski gefahren.": "gefahren",
    "Ich bin nicht vorsichtig gewesen und bin gefallen.": "gewesen, gefallen",
    "Ich bin zum Arzt gegangen.": "gegangen",
    "Der Arzt hat gesagt, der Fuss ist nicht gebrochen.": "gesagt, gebrochen",
    "Was hast du am Wochenende gemacht?": "gemacht",
}

partizip_haben = [
    (
        "Slidinėjau. Veiksmažodis: Ski fahren. Partizip zwei: gefahren. Vartojamas su haben.",
        "Ich habe Ski gefahren.",
        "gefahren",
    ),
    (
        "Kalbėjau. Veiksmažodis: sprechen. Partizip zwei: gesprochen. Vartojamas su haben.",
        "Ich habe gesprochen.",
        "gesprochen",
    ),
    (
        "Valgėme. Veiksmažodis: essen. Partizip zwei: gegessen. Vartojamas su haben.",
        "Wir haben gegessen.",
        "gegessen",
    ),
    (
        "Pasakė. Veiksmažodis: sagen. Partizip zwei: gesagt. Vartojamas su haben.",
        "Der Arzt hat gesagt.",
        "gesagt",
    ),
    (
        "Sulūžęs. Veiksmažodis: brechen. Partizip zwei: gebrochen.",
        "Der Fuss ist gebrochen.",
        "gebrochen",
    ),
    (
        "Veikei. Veiksmažodis: machen. Partizip zwei: gemacht. Vartojamas su haben.",
        "Was hast du gemacht?",
        "gemacht",
    ),
]

partizip_sein = [
    (
        "Praėjo. Veiksmažodis: vergehen. Partizip zwei: vergangen. Vartojamas su sein.",
        "Die Zeit ist vergangen.",
        "vergangen",
    ),
    (
        "Buvau. Veiksmažodis: sein. Partizip zwei: gewesen. Vartojamas su sein.",
        "Ich bin gewesen.",
        "gewesen",
    ),
    (
        "Nukritau. Veiksmažodis: fallen. Partizip zwei: gefallen. Vartojamas su sein.",
        "Ich bin gefallen.",
        "gefallen",
    ),
    (
        "Nuėjau. Veiksmažodis: gehen. Partizip zwei: gegangen. Vartojamas su sein.",
        "Ich bin gegangen.",
        "gegangen",
    ),
]

story_sentences_annotated = [
    ("Liebe Anna,", None),
    ("ich bin schon zwei Wochen im Flumserberg und morgen fahre ich nach Hause.", None),
    ("Die Zeit ist sehr schnell vergangen!", "vergangen"),
    ("Der Urlaub war fantastisch.", None),
    ("Ich habe jeden Tag Ski gefahren und das Wetter war super.", "gefahren"),
    ("Am Abend habe ich oft mit anderen Touristen gesprochen und wir haben zusammen gegessen.", "gesprochen, gegessen"),
    ("Aber gestern habe ich einen Unglückstag gehabt.", "gehabt"),
    ("Am Nachmittag bin ich Ski gefahren.", "gefahren"),
    ("Ich bin nicht vorsichtig gewesen und bin gefallen.", "gewesen, gefallen"),
    ("Ich konnte nicht mehr laufen.", None),
    ("Ich bin zum Arzt gegangen.", "gegangen"),
    ("Der Arzt hat gesagt, der Fuss ist nicht gebrochen.", "gesagt, gebrochen"),
    ("Aber jetzt darf ich nicht mehr Ski fahren.", None),
    ("Das ist sehr schade!", None),
    ("Heute bleibe ich im Hotel und lese ein Buch.", None),
    ("Morgen fahre ich nach Hause.", None),
    ("Wie geht es dir?", None),
    ("Was hast du am Wochenende gemacht?", "gemacht"),
    ("Liebe Grüsse, Tomas", None),
]


# ===== CREATE AUDIO =====

# 1. Full story in German — listen for general meaning
add_section("Pirmiausia visas pasakojimas vokiškai. Klausykis bendros prasmės.")
add_full_story(repeats=1)

# 2. Full Lithuanian translation
add_section("Dabar visas vertimas į lietuvių kalbą.")
add_spoken(full_story_lithuanian, "lt", pause_long)

# 3. Sentence pairs with active recall pause and Partizip II highlighting
add_section(
    "Dabar mokomės sakiniais. Išgirsi lietuviškai, tyla trims sekundėms — pabandyk atkurti vokiškai, tada išgirsi du kartus."
)
for lithuanian, german in story_pairs:
    partizip = sentence_partizip_map.get(german)
    add_learning_pair(lithuanian, german, repeats=2, partizip_form=partizip)

# 4a. Partizip II structured section — haben group
add_section("Svarbiausios Partizip zwei formos. Pirma veiksmažodžiai su haben.")
for lithuanian, german, form in partizip_haben:
    add_partizip_note(lithuanian, german, form)

# 4b. Partizip II structured section — sein group
add_section("Dabar veiksmažodžiai su sein.")
for lithuanian, german, form in partizip_sein:
    add_partizip_note(lithuanian, german, form)

# 5. Annotated story reading with Partizip II callouts per sentence
add_section("Dabar pasakojimas sakinys po sakinio. Po kiekvieno sakinio su Partizip zwei išgirsi formą lėtai.")
add_annotated_story()

# 6. Comprehension test — German then pause then Lithuanian
add_section("Supratimo testas. Išgirsi vokiškai. Pabandyk suprasti. Tada išgirsi lietuviškai.")
add_comprehension_test()

# 7. Final full story twice — speak along
add_section("Pabaigai visas pasakojimas vokiškai du kartus. Bandyk kalbėti kartu.")
add_full_story(repeats=2)


# Combine all segments and export final file
final_audio = sum(audio_segments)
final_audio.export(OUTPUT_FILE, format="mp3")

if os.path.exists(TEMP_FILE):
    os.remove(TEMP_FILE)

print(f"Audio file created: {OUTPUT_FILE}")
