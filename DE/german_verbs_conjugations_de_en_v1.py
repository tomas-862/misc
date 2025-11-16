from gtts import gTTS
from pydub import AudioSegment
from datetime import datetime

# === German Verb Conjugations with English Translations ===
verbs_conjugations = {
    # Regular verbs
    "wandern (to hike)": [
        ("ich wandere", "I hike"),
        ("du wanderst", "you hike"),
        ("er/sie/es wandert", ""),
        ("wir wandern", ""),
        ("ihr wandert", ""),
        ("sie/Sie wandern", "")
    ],

    "fragen (to ask)": [
        ("ich frage", "I ask"),
        ("du fragst", "you ask"),
        ("er/sie/es fragt", ""),
        ("wir fragen", ""),
        ("ihr fragt", ""),
        ("sie/Sie fragen", "")
    ],

    "kommen (to come)": [
        ("ich komme", "I come"),
        ("du kommst", "you come"),
        ("er/sie/es kommt", ""),
        ("wir kommen", ""),
        ("ihr kommt", ""),
        ("sie/Sie kommen", "")
    ],

    "gehen (to go)": [
        ("ich gehe", "I go"),
        ("du gehst", "you go"),
        ("er/sie/es geht", ""),
        ("wir gehen", ""),
        ("ihr geht", ""),
        ("sie/Sie gehen", "")
    ],

    "trinken (to drink)": [
        ("ich trinke", "I drink"),
        ("du trinkst", "you drink"),
        ("er/sie/es trinkt", ""),
        ("wir trinken", ""),
        ("ihr trinkt", ""),
        ("sie/Sie trinken", "")
    ],

    # Stem-changing verbs (e → i)
    "sprechen (to speak)": [
        ("ich spreche", "I speak"),
        ("du sprichst", "you speak"),
        ("er/sie/es spricht", ""),
        ("wir sprechen", ""),
        ("ihr sprecht", ""),
        ("sie/Sie sprechen", "")
    ],

    "nehmen (to take)": [
        ("ich nehme", "I take"),
        ("du nimmst", "you take"),
        ("er/sie/es nimmt", ""),
        ("wir nehmen", ""),
        ("ihr nehmt", ""),
        ("sie/Sie nehmen", "")
    ],

    "essen (to eat)": [
        ("ich esse", "I eat"),
        ("du isst", "you eat"),
        ("er/sie/es isst", ""),
        ("wir essen", ""),
        ("ihr esst", ""),
        ("sie/Sie essen", "")
    ],

    "vergessen (to forget)": [
        ("ich vergesse", "I forget"),
        ("du vergisst", "you forget"),
        ("er/sie/es vergisst", ""),
        ("wir vergessen", ""),
        ("ihr vergesst", ""),
        ("sie/Sie vergessen", "")
    ],

    "geben (to give)": [
        ("ich gebe", "I give"),
        ("du gibst", "you give"),
        ("er/sie/es gibt", ""),
        ("wir geben", ""),
        ("ihr gebt", ""),
        ("sie/Sie geben", "")
    ],

    # Stem-changing verbs (a → ä)
    "tragen (to wear / to carry)": [
        ("ich trage", "I wear"),
        ("du trägst", "you wear"),
        ("er/sie/es trägt", ""),
        ("wir tragen", ""),
        ("ihr tragt", ""),
        ("sie/Sie tragen", "")
    ],

    "schlagen (to hit)": [
        ("ich schlage", "I hit"),
        ("du schlägst", "you hit"),
        ("er/sie/es schlägt", ""),
        ("wir schlagen", ""),
        ("ihr schlagt", ""),
        ("sie/Sie schlagen", "")
    ],

    "fahren (to drive / to go by vehicle)": [
        ("ich fahre", "I drive"),
        ("du fährst", "you drive"),
        ("er/sie/es fährt", ""),
        ("wir fahren", ""),
        ("ihr fahrt", ""),
        ("sie/Sie fahren", "")
    ],

    "laufen (to run)": [
        ("ich laufe", "I run"),
        ("du läufst", "you run"),
        ("er/sie/es läuft", ""),
        ("wir laufen", ""),
        ("ihr lauft", ""),
        ("sie/Sie laufen", "")
    ],

    "halten (to hold / to stop)": [
        ("ich halte", "I hold"),
        ("du hältst", "you hold"),
        ("er/sie/es hält", ""),
        ("wir halten", ""),
        ("ihr haltet", ""),
        ("sie/Sie halten", "")
    ],

    "treten (to kick)": [
        ("ich trete", "I kick"),
        ("du trittst", "you kick"),
        ("er/sie/es tritt", ""),
        ("wir treten", ""),
        ("ihr tretet", ""),
        ("sie/Sie treten", "")
    ],

    "raten (to guess / to advise)": [
        ("ich rate", "I guess"),
        ("du rätst", "you guess"),
        ("er/sie/es rät", ""),
        ("wir raten", ""),
        ("ihr ratet", ""),
        ("sie/Sie raten", "")
    ],

    "sterben (to die)": [
        ("ich sterbe", "I die"),
        ("du stirbst", "you die"),
        ("er/sie/es stirbt", ""),
        ("wir sterben", ""),
        ("ihr sterbt", ""),
        ("sie/Sie sterben", "")
    ],

    # Special verbs (like mögen, sehen, sein, etc.)
    "mögen (to like)": [
        ("ich mag", "I like"),
        ("du magst", "you like"),
        ("er/sie/es mag", ""),
        ("wir mögen", ""),
        ("ihr mögt", ""),
        ("sie/Sie mögen", "")
    ],

    "sehen (to see)": [
        ("ich sehe", "I see"),
        ("du siehst", "you see"),
        ("er/sie/es sieht", ""),
        ("wir sehen", ""),
        ("ihr seht", ""),
        ("sie/Sie sehen", "")
    ],

    "töten (to kill)": [
        ("ich töte", "I kill"),
        ("du tötest", "you kill"),
        ("er/sie/es tötet", ""),
        ("wir töten", ""),
        ("ihr tötet", ""),
        ("sie/Sie töten", "")
    ],

    "beschreiben (to describe)": [
        ("ich beschreibe", "I describe"),
        ("du beschreibst", "you describe"),
        ("er/sie/es beschreibt", ""),
        ("wir beschreiben", ""),
        ("ihr beschreibt", ""),
        ("sie/Sie beschreiben", "")
    ],

    "erziehen (to raise/educate)": [
        ("ich erziehe", "I raise"),
        ("du erziehst", "you raise"),
        ("er/sie/es erzieht", ""),
        ("wir erziehen", ""),
        ("ihr erzieht", ""),
        ("sie/Sie erziehen", "")
    ],

    "lesen (to read)": [
        ("ich lese", "I read"),
        ("du liest", "you read"),
        ("er/sie/es liest", ""),
        ("wir lesen", ""),
        ("ihr lest", ""),
        ("sie/Sie lesen", "")
    ],

    "sein (to be)": [
        ("ich bin", "I am"),
        ("du bist", "you are"),
        ("er/sie/es ist", ""),
        ("wir sind", ""),
        ("ihr seid", ""),
        ("sie/Sie sind", "")
    ],

    "kaufen (to buy)": [
        ("ich kaufe", "I buy"),
        ("du kaufst", "you buy"),
        ("er/sie/es kauft", ""),
        ("wir kaufen", ""),
        ("ihr kauft", ""),
        ("sie/Sie kaufen", "")
    ],

    "verkaufen (to sell)": [
        ("ich verkaufe", "I sell"),
        ("du verkaufst", "you sell"),
        ("er/sie/es verkauft", ""),
        ("wir verkaufen", ""),
        ("ihr verkauft", ""),
        ("sie/Sie verkaufen", "")
    ],

    "spielen (to play)": [
        ("ich spiele", "I play"),
        ("du spielst", "you play"),
        ("er/sie/es spielt", ""),
        ("wir spielen", ""),
        ("ihr spielt", ""),
        ("sie/Sie spielen", "")
    ],

    "lernen (to learn)": [
        ("ich lerne", "I learn"),
        ("du lernst", "you learn"),
        ("er/sie/es lernt", ""),
        ("wir lernen", ""),
        ("ihr lernt", ""),
        ("sie/Sie lernen", "")
    ],

    "arbeiten (to work)": [
        ("ich arbeite", "I work"),
        ("du arbeitest", "you work"),
        ("er/sie/es arbeitet", ""),
        ("wir arbeiten", ""),
        ("ihr arbeitet", ""),
        ("sie/Sie arbeiten", "")
    ],

    "anfangen (to begin)": [
        ("ich fange an", "I begin"),
        ("du fängst an", "you begin"),
        ("er/sie/es fängt an", ""),
        ("wir fangen an", ""),
        ("ihr fangt an", ""),
        ("sie/Sie fangen an", "")
    ],

    "fangen (to catch)": [
        ("ich fange", "I catch"),
        ("du fängst", "you catch"),
        ("er/sie/es fängt", ""),
        ("wir fangen", ""),
        ("ihr fangt", ""),
        ("sie/Sie fangen", "")
    ],

    "treiben (to do/to practice)": [
        ("ich treibe", "I do/practice"),
        ("du treibst", "you do/practice"),
        ("er/sie/es treibt", ""),
        ("wir treiben", ""),
        ("ihr treibt", ""),
        ("sie/Sie treiben", "")
    ],

    "führen (to lead/to guide)": [
        ("ich führe", "I lead"),
        ("du führst", "you lead"),
        ("er/sie/es führt", ""),
        ("wir führen", ""),
        ("ihr führt", ""),
        ("sie/Sie führen", "")
    ],

    "kochen (to cook)": [
        ("ich koche", "I cook"),
        ("du kochst", "you cook"),
        ("er/sie/es kocht", ""),
        ("wir kochen", ""),
        ("ihr kocht", ""),
        ("sie/Sie kochen", "")
    ],

    "schreiben (to write)": [
        ("ich schreibe", "I write"),
        ("du schreibst", "you write"),
        ("er/sie/es schreibt", ""),
        ("wir schreiben", ""),
        ("ihr schreibt", ""),
        ("sie/Sie schreiben", "")
    ],

    "machen (to do / to make)": [
        ("ich mache", "I do"),
        ("du machst", "you do"),
        ("er/sie/es macht", ""),
        ("wir machen", ""),
        ("ihr macht", ""),
        ("sie/Sie machen", "")
    ],

    "zumachen (to close)": [
        ("ich mache zu", "I close"),
        ("du machst zu", "you close"),
        ("er/sie/es macht zu", ""),
        ("wir machen zu", ""),
        ("ihr macht zu", ""),
        ("sie/Sie machen zu", "")
    ],

    "aufmachen (to open)": [
        ("ich mache auf", "I open"),
        ("du machst auf", "you open"),
        ("er/sie/es macht auf", ""),
        ("wir machen auf", ""),
        ("ihr macht auf", ""),
        ("sie/Sie machen auf", "")
    ],

    "schließen (to close / to shut)": [
        ("ich schließe", "I close"),
        ("du schließt", "you close"),
        ("er/sie/es schließt", ""),
        ("wir schließen", ""),
        ("ihr schließt", ""),
        ("sie/Sie schließen", "")
    ],

    "rechnen (to calculate)": [
        ("ich rechne", "I calculate"),
        ("du rechnest", "you calculate"),
        ("er/sie/es rechnet", ""),
        ("wir rechnen", ""),
        ("ihr rechnet", ""),
        ("sie/Sie rechnen", "")
    ],
}

# === German Nouns with English Translations ===
nouns = {
    "der Sohn": "son",
}

# === Audio Creation ===
audio_segments = []
pause = AudioSegment.silent(duration=1000)  # 1-second pause

def speak_text(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("temp.mp3")
    return AudioSegment.from_mp3("temp.mp3") + pause


# === Group definitions for clarity and consistency ===
groups = [
    {
        "name": "Regular verbs",
        "verbs": [
            "wandern (to hike)",
            "fragen (to ask)",
            "kommen (to come)",
            "gehen (to go)",
            "trinken (to drink)",
            "arbeiten (to work)",
            "lernen (to learn)",
            "spielen (to play)",
            "schreiben (to write)",
            "machen (to do / to make)",
            "zumachen (to close)",
            "aufmachen (to open)",
            "schließen (to close / to shut)",
            "rechnen (to calculate)",
            "kaufen (to buy)",
            "verkaufen (to sell)",
            "kochen (to cook)",
            "führen (to lead/to guide)",
            "treiben (to do/to practice)"
        ]
    },
    {
        "name": "Stem-changing verbs (e→i)",
        "verbs": [
            "sprechen (to speak)",
            "nehmen (to take)",
            "essen (to eat)",
            "vergessen (to forget)",
            "geben (to give)"
        ]
    },
    {
        "name": "Stem-changing verbs (a→ä)",
        "verbs": [
            "tragen (to wear / to carry)",
            "schlagen (to hit)",
            "fahren (to drive / to go by vehicle)",
            "laufen (to run)",
            "halten (to hold / to stop)",
            "treten (to kick)",
            "raten (to guess / to advise)",
            "sterben (to die)"
        ]
    },
    {
        "name": "Special verbs",
        "verbs": [
            "mögen (to like)",
            "sehen (to see)",
            "lesen (to read)",
            "sein (to be)",
            "töten (to kill)",
            "beschreiben (to describe)",
            "erziehen (to raise/educate)",
            "anfangen (to begin)",
            "fangen (to catch)"
        ]
    }
]

# Set of third-person tokens to avoid English translation for those forms
third_person_tokens = {"er", "sie", "es", "er/sie/es"}

# === Iterate through each group, clearly label and speak the group header ===
for group in groups:
    group_name = group["name"]
    verb_list = group["verbs"]
    # Speak the group header clearly
    audio_segments.append(speak_text(f"Now, {group_name}", 'en'))

    for verb in verb_list:
        # Speak any special comments before the verb
        if verb == "arbeiten (to work)":
            comment_text = "arbeiten means to work, for example as a chef or in an office."
            audio_segments.append(speak_text(comment_text, 'en'))
        elif verb == "anfangen (to begin)":
            comment_text = "anfangen means to begin or to start. It is separable, for example, Ich fange an means I begin."
            audio_segments.append(speak_text(comment_text, 'en'))
        elif verb == "fangen (to catch)":
            comment_text = "fangen means to catch, for example, to catch fish."
            audio_segments.append(speak_text(comment_text, 'en'))
        elif verb == "treiben (to do/to practice)":
            comment_text = "treiben means to do or to practice, often used for sports or business."
            audio_segments.append(speak_text(comment_text, 'en'))
        elif verb == "führen (to lead/to guide)":
            comment_text = "führen means to lead or to guide, for example, to run a company."
            audio_segments.append(speak_text(comment_text, 'en'))
        elif verb == "kochen (to cook)":
            comment_text = "kochen means to cook. For example, Ich koche gern means I like to cook."
            audio_segments.append(speak_text(comment_text, 'en'))

        # Announce the verb infinitive in German
        audio_segments.append(speak_text(verb, 'de'))

        forms = verbs_conjugations.get(verb, [])
        for german, english in forms:
            # Speak the German conjugated form
            audio_segments.append(speak_text(german, 'de'))

            # Only speak the English if not third-person and translation is present
            first_token = german.split()[0].strip().lower() if german.strip() else ""
            if english and first_token not in third_person_tokens:
                audio_segments.append(speak_text(english, 'en'))

for noun_de, noun_en in nouns.items():
    # Announce the noun in German
    audio_segments.append(speak_text(noun_de, 'de'))

    # Announce the noun in English
    audio_segments.append(speak_text(noun_en, 'en'))

# Combine everything into one file
final_audio = sum(audio_segments)
pause_10s = AudioSegment.silent(duration=10000)
repeat_count = 2
final_audio_with_repeats = AudioSegment.empty()

for i in range(repeat_count):
    final_audio_with_repeats += final_audio
    if i < repeat_count - 1:
        final_audio_with_repeats += pause_10s

current_date = datetime.now().strftime("%Y-%m-%d")
output_file = f"german_verbs_conjugations_de_en_{current_date}.mp3"
final_audio_with_repeats.export(output_file, format="mp3")

print(f"✅ Audio file created: {output_file}")
