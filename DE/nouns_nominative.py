from gtts import gTTS
from pydub import AudioSegment
import os
from datetime import datetime

# ===== CONFIGURATION =====
current_date = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = f"nouns_nominative_{current_date}.mp3"

# Non-verbs list: German → English
non_verbs = {


    # das
    # Each noun has only one example sentence, distributed: 20% das, 30% ein, 50% possessive (sein / dein / ihre )
    "das Handy, die Handys": "the mobile phone",
    "Das Handy ist neu.": "The mobile phone is new.",
    "das Buch, die Bücher": "the book",
    "Das Buch ist interessant.": "The book is interesting.",
    "das Bett, die Betten": "the bed",
    "Sein Bett ist groß.": "His bed is big.",
    "das Fenster, die Fenster": "the window",
    "Ein Fenster ist kaputt.": "A window is broken.",
    "das Klassenzimmer, die Klassenzimmer": "the classroom",
    "Mein Klassenzimmer ist hell.": "My classroom is bright.",
    "das Foto, die Fotos": "the photo",
    "Das Foto ist schön.": "The photo is beautiful.",
    "das Waschbecken, die Waschbecken": "the sink",
    "Ein Waschbecken ist neu.": "A sink is new.",
    "das Laub": "foliage",
    "Sein Laub ist bunt.": "His foliage is colorful.",
    "das Loch, die Löcher": "the hole",
    "Mein Loch ist klein.": "My hole is small.",
    "das Regal, die Regale": "the shelf",
    "Das Regal ist leer.": "The shelf is empty.",
    "das Radio, die Radios": "the radio",
    "Ihr Radio ist alt.": "Her radio is old.",
    "das Bild, die Bilder": "the picture",
    "Ein Bild ist bunt.": "A picture is colorful.",
    "das Telefon, die Telefone": "the telephone",
    "Mein Telefon ist neu.": "My telephone is new.",
    "das Auto, die Autos": "the car",
    "Das Auto ist schnell.": "The car is fast.",
    "das Wasser": "water",
    "Sein Wasser ist kalt.": "His water is cold.",
    "das Klavier, die Klaviere": "the piano",
    "Ein Klavier ist groß.": "A piano is big.",
    "das Geschenk, die Geschenke": "gift",
    "Ihr Geschenk ist teuer.": "Her gift is expensive.",
    "das Blumengeschäft, die Blumengeschäfte": "flower shop",
    "Ich gehe ins Blumengeschäft.": "I go to the flower shop.",
    "das Eiscafé, die Eiscafés": "ice cream café",
    "Das Eiscafé ist voll.": "The ice cream café is full.",
    "das Wörterbuch, die Wörterbücher": "dictionary",
    "Ein Wörterbuch ist nützlich.": "A dictionary is useful.",

    # der
    # Each noun has only one example sentence, distributed: 20% der, 30% ein, 50% possessive (sein/dein/sein)
    "der Tod": "death",
    "Der Tod ist traurig.": "Death is sad.",
    "der Mann, die Männer": "the man",
    "Ein Mann ist stark.": "A man is strong.",
    "der Computer, die Computer": "the computer",
    "Sein Computer ist schnell.": "His computer is fast.",
    "der Lehrer, die Lehrer": "the teacher",
    "Der Lehrer erklärt die Frage.": "The teacher explains the question.",
    "der Kollege, die Kollegen": "colleague (male)",
    "Mein Kollege ist freundlich.": "My colleague is friendly.",
    "der Boden, die Böden": "floor",
    "Ein Boden ist sauber.": "A floor is clean.",
    "der Fußboden, die Fußböden": "floor",
    "Mein Fußboden ist warm.": "My floor is warm.",
    "der Becher, die Becher": "the cup",
    "Sein Becher ist groß.": "His cup is big.",
    "der Herd, die Herde": "the stove",
    "Der Herd ist alt.": "The stove is old.",
    "der Gasherd, die Gasherde": "gas stove",
    "Sein Gasherd ist alt.": "His gas stove is old.",
    "der Bus, die Busse": "bus",
    "Mein Bus ist rot.": "My bus is red.",
    "der Reisebus, die Reisebusse": "coach / travel bus",
    "Ein Reisebus ist bequem.": "A coach is comfortable.",
    "der Elektroherd, die Elektroherde": "electric stove",
    "Mein Elektroherd ist neu.": "My electric stove is new.",
    "der Tisch, die Tische": "table",
    "Sein Tisch ist neu.": "His table is new.",
    "der Kugelschreiber, die Kugelschreiber": "pen",
    "Der Kugelschreiber liegt auf dem Tisch.": "The pen is on the table.",
    "der Taschenrechner, die Taschenrechner": "calculator",
    "Mein Taschenrechner ist alt.": "My calculator is old.",
    "der Stecker, die Stecker": "plug",
    "Sein Stecker ist neu.": "His plug is new.",
    "der Topf, die Töpfe": "pot",
    "Ein Topf ist heiß.": "A pot is hot.",
    "der Stuhl, die Stühle": "chair",
    "Mein Stuhl ist alt.": "My chair is old.",
    "der Wasserhahn, die Wasserhähne": "tap",
    "Der Wasserhahn ist neu.": "The tap is new.",
    "der Sommer, die Sommer": "summer",
    "Sein Sommer ist schön.": "His summer is beautiful.",
    "der Fernsehapparat, die Fernsehapparate": "television set",
    "Mein Fernsehapparat ist neu.": "My television set is new.",
    "der Abfalleimer, die Abfalleimer": "trash can",
    "Ein Abfalleimer ist voll.": "A trash can is full.",
    "der Geschirrspüler, die Geschirrspüler": "dishwasher",
    "Mein Geschirrspüler ist neu.": "My dishwasher is new.",
    "der Kühlschrank, die Kühlschränke": "refrigerator",
    "Sein Kühlschrank ist groß.": "His refrigerator is big.",
    "der Schrank, die Schränke": "cabinet / cupboard",
    "Mein Schrank ist alt.": "My cabinet is old.",
    "der Sohn, die Söhne": "son",
    "Ein Sohn ist nett.": "A son is nice.",
    "der Patient, die Patienten": "patient",
    "Mein Patient ist freundlich.": "My patient is friendly.",
    "der Rechner, die Rechner": "calculator",
    "Sein Rechner ist schnell.": "His calculator is fast.",
    "der Spüler, die Spüler": "rinsing device / washer",
    "Mein Spüler ist alt.": "My washer is old.",
    "der Geschäftsführer, die Geschäftsführer": "managing director",
    "Der Geschäftsführer spricht viel.": "The managing director speaks a lot.",
    "der Geschäftsmann, die Geschäftsleute": "businessman",
    "Der Geschäftsmann ist erfolgreich.": "The businessman is successful.",
    "der Chef, die Chefs": "boss / manager",
    "Sein Chef ist streng.": "His boss is strict.",
    "der Koch, die Köche": "cook / chef",
    "Mein Koch ist gut.": "My cook is good.",
    "der Regenschirm, die Regenschirme": "umbrella",
    "Der Regenschirm ist neu.": "The umbrella is new.",
    "der Radiergummi, die Radiergummis": "eraser",
    "Der Radiergummi ist klein.": "The eraser is small.",
    "der Geburtstag, die Geburtstage": "birthday",
    "Mein Geburtstag ist morgen.": "My birthday is tomorrow.",
    "der Handschuh, die Handschuhe": "glove",
    "Die Handschuhe sind warm.": "The gloves are warm.",
    "der Appetit": "appetite",
    "Ich habe guten Appetit.": "I have a good appetite.",
    "der Rock, die Röcke": "skirt",
    "Der Rock ist blau.": "The skirt is blue.",
    "der Bruder, die Brüder": "brother",
    "Mein Bruder ist klein.": "My brother is small.",
    "der Anzug, die Anzüge": "suit",
    "Sein Anzug ist elegant.": "His suit is elegant.",

    # die
    # Each noun has only one example sentence, distributed: 20% die, 30% eine, 50% possessive (meine/ihre/seine)
    "die Kantine, die Kantinen": "canteen",
    "Die Kantine ist groß.": "The canteen is big.",
    "die Kollegin, die Kolleginnen": "colleague (female)",
    "Die Kollegin ist nett.": "The colleague is nice.",
    "die Tür, die Türen": "door",
    "Ihre Tür ist neu.": "Her door is new.",
    "die Kommode, die Kommoden": "dresser",
    "Meine Kommode ist schön.": "My dresser is beautiful.",
    "die Wand, die Wände": "wall",
    "Die Wand ist weiß.": "The wall is white.",
    "die Hand, die Hände": "hand",
    "Seine Hand ist klein.": "His hand is small.",
    "die Tasse, die Tassen": "cup",
    "Die Tasse ist voll.": "The cup is full.",
    "die Klasse --- das Zimmer": "class --- room",
    "Meine Klasse ist groß.": "My class is big.",
    "die Mine, die Minen": "refill / pencil lead",
    "Die Mine ist neu.": "The refill is new.",
    "die Taschenlampe, die Taschenlampen": "flashlight",
    "Ihre Taschenlampe ist alt.": "Her flashlight is old.",
    "die Lampe, die Lampen": "lamp",
    "Ich habe eine Lampe.": "I have a lamp.",
    "die Glühbirne, die Glühbirnen": "light bulb",
    "Ihre Glühbirne ist neu.": "Her light bulb is new.",
    "die Mikrowelle, die Mikrowellen": "microwave",
    "Meine Mikrowelle ist laut.": "My microwave is loud.",
    "die Zahlen": "numbers",
    "Die Zahlen sind wichtig.": "The numbers are important.",
    "die Steckdose, die Steckdosen": "power socket",
    "Die Steckdose ist kaputt.": "The power socket is broken.",
    "die Batterien": "batteries",
    "Meine Batterie ist voll.": "My battery is full.",
    "die Batterie, die Batterien": "battery",
    "Ihre Batterie ist alt.": "Her battery is old.",
    "die Kamera, die Kameras": "camera",
    "Seine Kamera ist teuer.": "His camera is expensive.",
    "die Melodie, die Melodien": "melody",
    "Die Melodie ist schön.": "The melody is beautiful.",
    "die Spüle, die Spülen": "sink",
    "Ihre Spüle ist alt.": "Her sink is old.",
    "die Spülmaschine, die Spülmaschinen": "dishwasher",
    "Meine Spülmaschine ist neu.": "My dishwasher is new.",
    "die Waschmaschine, die Waschmaschinen": "washing machine",
    "Die Waschmaschine ist an.": "The washing machine is on.",
    "die Adresse, die Adressen": "address",
    "Meine Adresse ist lang.": "My address is long.",
    "die Uhr, die Uhren": "clock / watch",
    "Ihre Uhr ist teuer.": "Her clock is expensive.",
    "die Küche, die Küchen": "kitchen",
    "Die Küche ist groß.": "The kitchen is big.",
    "die Augen": "eyes",
    "Sein Auge ist verletzt.": "His eye is injured.",
    "die Reise, die Reisen": "trip / journey",
    "Die Reise ist schön.": "The trip is beautiful.",
    "die Geschäftsfrau, die Geschäftsfrauen": "businesswoman",
    "Ihre Geschäftsfrau ist erfolgreich.": "Her businesswoman is successful.",
     "die Damentasche, die Damentaschen": "ladies' handbag",
    "Die Damentasche ist schön.": "The ladies' handbag is beautiful.",
    "die Strumpfhose, die Strumpfhosen": "tights",
    "Die Strumpfhose ist schwarz.": "The tights are black.",
    "die Winterjacke, die Winterjacken": "winter jacket",
    "Die Winterjacke ist warm.": "The winter jacket is warm.",
    "die Schultasche, die Schultaschen": "school bag",
    "Meine Schultasche ist schwer.": "My school bag is heavy.",
    "die Verkäuferin, die Verkäuferinnen": "saleswoman",
    "Die Verkäuferin ist freundlich.": "The saleswoman is friendly.",
    "die Hauptstadt, die Hauptstädte": "capital city",
    "Berlin ist die Hauptstadt von Deutschland.": "Berlin is the capital city of Germany.",
    "die Schwester, die Schwestern": "sister",
    "Meine Schwester ist nett.": "My sister is nice.",
    "die Tube, die Tuben": "tube",
    "Die Tube ist leer.": "The tube is empty.",
    "die Mütze, die Mützen": "cap",
    "Die Mütze ist rot.": "The cap is red.",
    "die Sandalen": "sandals",
    "Meine Sandalen sind bequem.": "My sandals are comfortable.",

}

# ===== CREATE AUDIO =====
audio_segments = []

# Pauses
pause_1s = AudioSegment.silent(duration=3000)  # 3 seconds
pause_2s = AudioSegment.silent(duration=3000)  # 2 seconds

def generate_tts(text, lang, filename="temp.mp3"):
    """Generate speech for a given text and return as AudioSegment"""
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return AudioSegment.from_mp3(filename)

# 2. English → German for entire list
for german, english in non_verbs.items():
    english_audio = generate_tts(english, 'en')
    german_audio = generate_tts(german, 'de')

    # English word
    audio_segments.append(english_audio)
    audio_segments.append(pause_2s)

    # German translation repeated twice
    audio_segments.append(german_audio)
    audio_segments.append(pause_1s)
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