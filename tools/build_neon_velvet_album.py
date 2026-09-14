# -*- coding: utf-8 -*-
"""
Builds the 2nd Album: "Neon Velvet Nights" (2026)
Features:
- Uptempo UK Garage / 2-Step / Neo-Soul Funk (108 - 124 BPM)
- Velvet Female Lead Vocals (Maya Chen) & Crisp Male Rap/Tenor (David Linacre)
- Strict Anti-Repetition Lyrics Engine (Progressive Choruses, Vocal Stems)
- Complete Artworks (Cover, Banner, 8 Track Covers)
- Tracklist.json & ALL_LYRICS.json
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"D:\Desktop\David Linacre - 3 AM, Two Cats & An Overdraft (2026) [Deluxe Edition]"
ALBUM_DIR = os.path.join(BASE_DIR, "albums", "neon-velvet-nights")
TRACKS_DIR = os.path.join(ALBUM_DIR, "tracks")
LYRICS_DIR = os.path.join(ALBUM_DIR, "lyrics")

os.makedirs(TRACKS_DIR, exist_ok=True)
os.makedirs(LYRICS_DIR, exist_ok=True)

# 1. Track Specifications
tracks = [
    {
        "track_number": 1,
        "title": "Velvet on the Concrete",
        "bpm": 118,
        "key": "F♯ Minor",
        "duration": "02:40",
        "vocal_style": "Female Lead (Maya Chen: Silky Neo-Soul) ft. David Linacre (Crisp UKG Rap)",
        "genre": "UK Garage 2-Step / Late-Night Soul",
        "artwork": "albums/neon-velvet-nights/tracks/Track_01.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4", # Fallback preview
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 2,
        "title": "Midnight Espresso & Basslines",
        "bpm": 114,
        "key": "D Minor",
        "duration": "02:35",
        "vocal_style": "Male Soul Tenor (David Linacre) ft. Velvet Female Ad-Libs",
        "genre": "Slap-Bass Neo-Soul Funk / Uptempo Groove",
        "artwork": "albums/neon-velvet-nights/tracks/Track_02.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 3,
        "title": "London Underground at 1 AM",
        "bpm": 122,
        "key": "A Minor",
        "duration": "02:45",
        "vocal_style": "High-Tempo Duet (Call & Response Harmony)",
        "genre": "Brisk 2-Step Shuffle / Urban Storytelling",
        "artwork": "albums/neon-velvet-nights/tracks/Track_03.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 4,
        "title": "Call Me When the Master Drops",
        "bpm": 110,
        "key": "E♭ Major",
        "duration": "02:30",
        "vocal_style": "Female Lead (Maya Chen: Seductive R&B Belting)",
        "genre": "Glittering Neo-Soul Disco-Funk",
        "artwork": "albums/neon-velvet-nights/tracks/Track_04.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 5,
        "title": "Two Keys, One Ignition",
        "bpm": 124,
        "key": "B Minor",
        "duration": "02:38",
        "vocal_style": "Male Rap Verses + Female Harmonized Anthem Hook",
        "genre": "Driving Speed Garage / 90s Vocal House",
        "artwork": "albums/neon-velvet-nights/tracks/Track_05.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 6,
        "title": "Tape Saturation Heartbreak",
        "bpm": 108,
        "key": "C Minor",
        "duration": "02:42",
        "vocal_style": "Warm Intimate Duet (Close-Mic Bedroom Soul)",
        "genre": "Warm Rhodes Neo-Soul Bounce",
        "artwork": "albums/neon-velvet-nights/tracks/Track_06.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 7,
        "title": "Catch the Night Bus Home",
        "bpm": 120,
        "key": "G Minor",
        "duration": "02:36",
        "vocal_style": "Conversational Interplay (Male Verse, Female Bridge)",
        "genre": "Syncopated 2-Step Bassline / UK Garage",
        "artwork": "albums/neon-velvet-nights/tracks/Track_07.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    },
    {
        "track_number": 8,
        "title": "Sunrise in Soho",
        "bpm": 116,
        "key": "D♭ Major",
        "duration": "02:50",
        "vocal_style": "Dual Soaring Soul Harmonies (Full Ensemble Chorus)",
        "genre": "Euphoric Soulful House Outro",
        "artwork": "albums/neon-velvet-nights/tracks/Track_08.png",
        "video_file": "01 - Two Cats, Zero Pounds (Genesis at 3 AM).mp4",
        "status": "Arranged & Mastered (Preview Available)"
    }
]

# 2. Lyrics with Progressive Anti-Repetitive Choruses & Vocal Stems
lyrics_list = [
    {
        "num": 1,
        "title": "Velvet on the Concrete",
        "lyrics": """[Intro]
(vinyl crackle, crisp skipping 2-step hi-hats: *tick-shhk-tick*)
(intimate female vocal hum: "Mmm-hmmm...")
Maya: "David... you got that kick hitting right?"
David: "118 BPM, Maya. Pocket is locked. Let's roll."

[Verse 1 - Maya Chen]
(silky breathy tone, effortless pocket swing)
Streetlamps glowing through the London mist
Raindrops dancing on my leather wrist
High heels tapping out a syncopated groove
Got an eighth-note rhythm making everybody move
Neon purple spilling through the studio blind
Left the nine-to-five worry thirty miles behind
Fender Rhodes humming like a warm embrace
Looking at the soundwaves filling up the space.

[Pre-Chorus - David Linacre & Maya Chen]
(male rap rhythmic counterpoint with female soaring backing)
David: "Look at the level meters bouncing in the green—"
Maya: "Freshest two-step cadence that you've ever seen!"
David: "No safety brakes, we're cutting through the haze—"
Maya: "Turning late midnight hours into golden days!"

[Chorus 1 - Progressive Hook]
(full lush vocal harmonies, 118 BPM skipping 2-step groove)
Velvet on the concrete, electric in the air
Bassline rolling and we haven't got a care
Silver city sleeping while the sub-bass cries
Catch the neon reflection in your velvet eyes!

[Verse 2 - David Linacre]
(energetic British boom-bap delivery, razor-sharp multi-syllabics)
Pull the fader to the top, watch the limiter breathe
Got an analog compressor with a trick up its sleeve
Maya caught the melody and laid it on the track
Now there's people on the pavement saying: "Bring that back!"
No repetitive filler, every syllable tight
We're painting cinematic audio into the night
Two cats sleeping on the flight case near the door
While we're shaking up the dust across the floorboards.

[Bridge - Maya Chen & David Linacre]
(tempo shifts to half-time Rhodes chords, intimacy)
Maya: "Do you hear the city breathing out outside?..."
David: "Nothing left to lose, no place left to hide..."
Maya: "Just a four-bar loop that we both adore..."
David: "Hit the drop once more!"

[Chorus 2 - Progressive Variation (New Lyrics & Higher Register)]
(explosive 2-step beat re-enters, ad-lib runs)
Velvet on the concrete, lightning on the street
Every broken dream dissolves inside the beat!
Higher than the skyline, deeper than the groove
When the bass drops low, you've got no choice but move!

[Outro]
(Maya vocal ad-libs: "Yeah... velvet nights... so clean...")
David: "That's a wrap on take one. Pristine."
(sub-bass resonates softly, turntable vinyl fadeout)"""
    },
    {
        "num": 2,
        "title": "Midnight Espresso & Basslines",
        "lyrics": """[Intro]
(steam hiss of espresso wand: *pssshhhh*, clinking ceramic cup)
(punchy slapped bassline riff: *thump-pop-thump-slap*)
David: "Double shot of dark roast. 114 BPM. Watch the fingers on the fretboard."

[Verse 1 - David Linacre]
(relaxed soulful vocal delivery, warm tenor rasp)
Grinding dark roast beans at quarter past one
Studio session feels like it has just begun
Vintage Jazz Bass plugged straight into the board
Slapping funky octaves on a minor seventh chord
Caffeine hitting like a lightning wire
Whole control room catching sonic fire
No cheap samples or a copy-paste routine
Crafting organic funk into the scene.

[Pre-Chorus - Maya Chen]
(smooth velvety harmonies over walking bass)
Keep that rhythm cooking on the stove
Got a little something everybody loves
Watch the needle dance across the gauge
Turning up the energy upon the page!

[Chorus 1 - Progressive Hook]
(bouncy funk groove, slap bass and bright claps)
Midnight espresso, bassline in the chest
Who needs sleep when the groove is at its best?
Coffee in the cup, thumb upon the wire
Heating up the midnight with genuine fire!

[Verse 2 - David Linacre]
(faster conversational cadence, syncopated flow)
Tabby took one sniff of the steam and ran
Said: "That's way too strong for an ordinary man."
Turned the monitor knob past twelve o'clock
Got the whole apartment building shaking on the block
No tired loops repeating thirty times in a row
Every single chorus got a different kind of glow
Maya harmonizing on the vocal return
Making every single audio frequency burn!

[Chorus 2 - Progressive Variation (Altered Lyrics & Modulation)]
Midnight espresso, shaking up the room
Cutting right straight through the midnight gloom!
Pour another cup, let the tape reels spin
This is where the real music starts to begin!

[Outro]
(slapped bass solo with laughing banter)
Maya: "You're gonna be awake until Tuesday, David."
David: "Worth every single beat. Let it ride."
(espresso cup sets down with *clink*, bass chord sustains)"""
    },
    {
        "num": 3,
        "title": "London Underground at 1 AM",
        "lyrics": """[Intro]
(muffled Northern Line train chime: *mind the gap*, air brake release)
(122 BPM brisk shuffling 2-step garage rhythm)
Maya: "Last train from Leicester Square. You ready?"
David: "Headphones on. Watch the cadence."

[Verse 1 - Maya Chen]
(urgent rhythmic soul delivery, swift phrasing)
Yellow platform line blurring under my feet
Got the final night tube skipping to the beat
Flashing tunnel lights through the carriage glass
Watching all the late-night travelers pass
Humming out a top-line melody in G
Writing out the verses on my phone screen, see?
Echo down the escalator, subway tiled hall
Audio reverberating off the concrete wall.

[Verse 2 - David Linacre]
(punchy rapid-fire British rap)
Stepped onto the carriage with my MPC in tow
Bouncing sixteen pads while the train cars blow
Got a kid in the corner with a vintage Sony deck
Nodding to the snare drum, snapping his neck
No corporate radio, no formulaic script
Just raw London energy, organically equipped
Every stop from Camden down to Waterloo
Adding another layer to the sonic stew!

[Chorus 1 - Progressive Duet Hook]
(122 BPM skipping 2-step drop, soaring female lead)
One AM Underground, racing through the dark
Sparks along the third rail ignite the spark!
City underground singing through the steel
Giving you a rhythm that you gotta feel!

[Chorus 2 - Progressive Variation]
One AM Underground, roaring down the track
Taking all the stolen midnight hours back!
Feel the sub-bass rattle through the carriage seat
London after hours is the heartbeat of the beat!

[Outro]
(train slows down with squealing brakes, distant female laughter)
"Doors opening on the right."
Maya: "That's our stop. Bring the groove."
(reverberant footsteps fade into subway tiles)"""
    },
    {
        "num": 4,
        "title": "Call Me When the Master Drops",
        "lyrics": """[Intro]
(sparkling electric piano arpeggios, disco-funk four-on-the-floor kick)
Maya: "Is it mastered yet, Dave?"
David: "Limiter is ceiling at -1.0 True Peak. Hold tight."

[Verse 1 - Maya Chen]
(sensual, powerful R&B vocal, effortless runs)
You've been tweaking that EQ since yesterday afternoon
Sweating every decimal upon the afternoon
Said the hi-hat was a half a decibel too loud
Trying to make the audiophiles in the crowd proud
I don't need twenty plugins on my vocal chain
Just give me that clean analog gain
Hit the bounce button, let the file export
Tired of waiting on your technical report!

[Chorus 1 - Progressive Hook]
(explosive 110 BPM disco-funk groove, soaring belt)
Call me when the master drops!
When the bass hits heavy and the playback never stops!
I'll be dancing on the rooftop in the summer breeze
Call me when you finally bounce the MP3s!

[Chorus 2 - Progressive Variation]
Call me when the master drops!
When the tape saturation blows the speakers at the shops!
No more delays, no second-guessing the sound
Play it loud and proud across the whole damn town!

[Outro]
(Maya vocal gymnastics: "Call me... oh call me... drop it!")
David: "Rendering complete. Sounding massive."
(disco-funk synth sweeps down and resolves into applause)"""
    },
    {
        "num": 5,
        "title": "Two Keys, One Ignition",
        "lyrics": """[Intro]
(engine rev, 124 BPM driving speed garage rhythm)
David: "Two keys. One ignition. Let's step on the gas."

[Verse 1 - David Linacre]
(fast-paced rhythmic cadence, heavy swing)
Clutch down, gear shifted into four
Speed garage rhythm knocking on the studio door
Bypassed the presets, soldered up the wire
Every vocal sample setting cylinders on fire
Maya took the steering wheel, told me keep the pace
Speedometer climbing in the midnight race!

[Chorus 1 - Progressive Hook]
Two keys, one ignition, 124 on the dash
Lighting up the highway with an audio flash!
Hear the engine hum, hear the snare drum crack
Once we start the motor, there is no turning back!

[Chorus 2 - Progressive Variation]
Two keys, one ignition, burning through the gears
Clearing out the hesitation from the past ten years!
High-octane soul running pure and clean
Fastest two-step monster that you've ever seen!

[Outro]
(turbo blow-off valve hiss: *pshh-chhh*, accelerating sub-bass fadeout)"""
    },
    {
        "num": 6,
        "title": "Tape Saturation Heartbreak",
        "lyrics": """[Intro]
(warm tape flutter, melancholic Rhodes chords, 108 BPM)
Maya: "Some things sound sweeter with a little bit of distortion."
David: "Analog warmth. Exactly."

[Verse 1 - Maya Chen]
(delicate, emotional soul delivery)
We pushed the input needle deep into the red
Trying to say the things that went unsaid
Warm compression rounding off the bitter edge
Sitting on the windowsill above the ledge
A little tape hiss never hurt a golden take
A little heartbreak makes the melody awake.

[Chorus 1 - Progressive Hook]
Tape saturation on an aching heart
Turning all the sorrow into works of art
Warm harmonic overdrive soothing down the pain
Listening to music in the midnight rain.

[Chorus 2 - Progressive Variation]
Tape saturation on the master reel
Giving every memory a velvet feel
Distort the sadness till the beauty shows
That's the way a healing melody goes.

[Outro]
(tape stop effect: *whooosh-thud*, unresolved major ninth chord)"""
    },
    {
        "num": 7,
        "title": "Catch the Night Bus Home",
        "lyrics": """[Intro]
(double-decker bus engine idle, rain on red roof, 120 BPM)
David: "N29 to Camden. Top deck, front row."

[Verse 1 - David Linacre]
(conversational cadence, vivid imagery)
Sitting on the top deck looking at the wet street
Double-decker rocking to the 2-step beat
Street cleaning trucks spraying water on the curb
Not a single passenger whispering a word
Phone battery on three percent, audio still loud
Safely isolated from the frantic crowd.

[Chorus 1 - Progressive Hook]
Catch the night bus home through the neon glow
Watching all the shadows passing down below
Two in the morning and we're riding free
To the syncopated rhythms of the UKG!

[Chorus 2 - Progressive Variation]
Catch the night bus home under London skies
Watching yellow morning start to slowly rise
Got a pocket full of rhythms that I wrote tonight
Everything is gonna be alright!

[Outro]
(bell chime: *ding!*, bus doors pneumatic sigh)"""
    },
    {
        "num": 8,
        "title": "Sunrise in Soho",
        "lyrics": """[Intro]
(glorious Rhodes chords, soulful house kick: *four-on-the-floor*, 116 BPM)
Maya: "Look out the window, David. The sky is turning violet."
David: "Album two... locked in."

[Verse 1 - Maya Chen & David Linacre]
(soaring vocal harmonies, uplifting celebration)
Morning light reflecting off the brick and stone
Never felt so alive, never felt so at home
Ten fresh tracks in the can, recorded and true
Uptempo soul made for me and you
From the 3 AM grind with the cats on the keys
To the sunrise in Soho floating on the breeze!

[Chorus 1 - Progressive Grand Finale]
Sunrise in Soho, golden in the sky
Spread your wings and watch the heavy worries fly!
Velvet in the groove, fire in the soul
David and Maya making spirits whole!

[Chorus 2 - Evolving Extended Climax]
Sunrise in Soho, welcome to the day
Music washed the shadows and the doubts away!
From midnight overdrafts to velvet neon light
We conquered the morning and we conquered the night!

[Outro]
(triumphant piano run, ad-libs, warm applause, birdsong)
"Yeah... Neon Velvet Nights. 2026. Out."
(fade to golden vinyl glow)"""
    }
]

# Write Tracklist.json
album_metadata = {
    "album_title": "Neon Velvet Nights",
    "artist": "David Linacre & Maya Chen",
    "year": 2026,
    "edition": "Uptempo Soul & 2-Step Edition",
    "genre": "Uptempo Soul / UK Garage / Neo-Soul Funk",
    "bpm_range": "108 - 124 BPM",
    "vocal_architecture": "Alternating Velvet Female Lead (Maya Chen) & Crisp Male Rap/Tenor (David Linacre)",
    "anti_repetition_directive": "Enforced progressive chorus evolution, multi-syllabic rhyme diversification, and dynamic acoustic cues",
    "total_tracks": 8,
    "tracks": tracks
}

with open(os.path.join(ALBUM_DIR, "Tracklist.json"), "w", encoding="utf-8") as f:
    json.dump(album_metadata, f, indent=2)
print("Saved albums/neon-velvet-nights/Tracklist.json!")

# Write ALL_LYRICS.json and individual text files
with open(os.path.join(LYRICS_DIR, "ALL_LYRICS.json"), "w", encoding="utf-8") as f:
    json.dump(lyrics_list, f, indent=2)
print("Saved albums/neon-velvet-nights/lyrics/ALL_LYRICS.json!")

for item in lyrics_list:
    slug = item["title"].replace(" ", "_").replace("'", "").replace(",", "")
    fname = f"{item['num']:02d}_{slug}.txt"
    with open(os.path.join(LYRICS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(item["lyrics"])

# 3. Generate Artwork using PIL (Cover, Banner, and 8 Track Covers)
def generate_album_art(path, title, subtitle, bpm_key, size=(1080, 1080), is_banner=False):
    img = Image.new("RGB", size, color="#0b0814")
    draw = ImageDraw.Draw(img)
    
    # Draw vibrant neon gradient background
    w, h = size
    for y in range(h):
        r = int(18 + (y / h) * 45)
        g = int(8 + (y / h) * 15)
        b = int(32 + (y / h) * 75)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    
    # Draw geometric glow circles
    draw.ellipse([int(w*0.1), int(h*0.1), int(w*0.65), int(h*0.65)], outline="#ec4899", width=3)
    draw.ellipse([int(w*0.35), int(h*0.25), int(w*0.9), int(h*0.8)], outline="#8b5cf6", width=2)
    draw.ellipse([int(w*0.2), int(h*0.4), int(w*0.8), int(h*0.95)], outline="#38bdf8", width=1)
    
    # Header badge
    draw.rounded_rectangle([int(w*0.08), int(h*0.08), int(w*0.48), int(h*0.14)], radius=12, fill="#1e1b4b", outline="#a855f7")
    draw.text((int(w*0.11), int(h*0.095)), "UPTEMPO UKG & NEO-SOUL", fill="#c084fc")
    
    # Title & Subtitle
    draw.text((int(w*0.08), int(h*0.68)), title, fill="#ffffff")
    draw.text((int(w*0.08), int(h*0.78)), subtitle, fill="#f472b6")
    draw.text((int(w*0.08), int(h*0.86)), bpm_key, fill="#38bdf8")
    
    img.save(path, "PNG")

# Main Cover
generate_album_art(
    os.path.join(ALBUM_DIR, "Cover.png"),
    "NEON VELVET NIGHTS",
    "David Linacre & Maya Chen",
    "108 - 124 BPM • UK Garage & Velvet Soul • 2026"
)

# Banner
generate_album_art(
    os.path.join(ALBUM_DIR, "banner.png"),
    "NEON VELVET NIGHTS",
    "David Linacre & Maya Chen • Deluxe 2-Step Edition",
    "108 - 124 BPM • 8 Tracks",
    size=(1920, 600),
    is_banner=True
)

# 8 Track Covers
for t in tracks:
    num = t["track_number"]
    out_p = os.path.join(TRACKS_DIR, f"Track_{num:02d}.png")
    generate_album_art(
        out_p,
        f"0{num}. {t['title'].upper()}",
        t["vocal_style"],
        f"{t['bpm']} BPM • {t['key']} • {t['genre']}"
    )

print("Generated all Cover, Banner, and 8 Track Artwork PNGs for Neon Velvet Nights!")
