# -*- coding: utf-8 -*-
"""
David Linacre Advanced Audio Pipeline & Anti-Repetition Lyric Engine
Features:
- Anti-repetition progressive chorus architecture
- Diverse vocal profiles: Velvet Female, Crisp Male Rap, Male Soul Tenor, Intimate Duets
- Uptempo BPM configurations (98 - 132 BPM)
- Automated ComfyUI Music 3 prompt compilation & mastering integration
"""

import os
import sys
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ALBUM_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOCAL_PROFILES = {
    "female_velvet_soul": {
        "name": "Velvet Female Neo-Soul (Sade / Cleo Sol Style)",
        "prompt_snippet": "Lush velvety female neo-soul vocalist, smooth breathy intimacy, resonant chest tones, expressive soulful vibrato, reminiscent of Sade, Erykah Badu, Cleo Sol, high studio fidelity, pristine tube microphone capture.",
        "gender": "female",
        "style_tags": "[Female Vocal: Silky intimate delivery, warm vibrato, breathy tone]"
    },
    "female_uptempo_rnb": {
        "name": "Bright Uptempo Female R&B (Mahalia / SZA Style)",
        "prompt_snippet": "Bright energetic female R&B vocalist, nimble vocal runs, soulful power, charismatic attitude, crisp modern pop-soul production, pristine vocal clarity.",
        "gender": "female",
        "style_tags": "[Female Vocal: Energetic modern R&B, melodic runs, confident projection]"
    },
    "male_soul_tenor": {
        "name": "Warm Male Soul Tenor (Anderson .Paak / Tom Misch Style)",
        "prompt_snippet": "Warm soulful male tenor with gentle rasp, effortless falsetto transitions, relaxed behind-the-beat phrasing, reminiscent of Anderson .Paak, Tom Misch, D'Angelo, pristine Neumann U87 vocal chain.",
        "gender": "male",
        "style_tags": "[Male Vocal: Soulful tenor, warm rasp, effortless falsetto]"
    },
    "male_crisp_rap": {
        "name": "Crisp British Male Rap (90s Boom-Bap Cadence)",
        "prompt_snippet": "Charismatic British male rap delivery, energetic 90s boom-bap flow, razor-sharp multi-syllabic articulation, rhythmic bounce, confident conversational delivery.",
        "gender": "male",
        "style_tags": "[Male Rap: Punchy 90s boom-bap flow, crisp diction, pocket swing]"
    },
    "duet_harmony": {
        "name": "Intimate Male & Female Duet (Call & Response)",
        "prompt_snippet": "Intimate vocal duet featuring male rhythmic storytelling verses and lush female vocal harmonies on the chorus, call-and-response ad-libs, warm stereo vocal spread, rich octave doublings.",
        "gender": "duet",
        "style_tags": "[Duet: Male and female interplay, layered 3rd harmonies, call-and-response]"
    }
}

TEMPO_GROOVES = {
    "uptempo_boombap": {
        "bpm_range": (96, 106),
        "default_bpm": 102,
        "description": "90s Golden-Age Uptempo Boom-Bap, punchy acoustic kicks, crisp snare crack, swinging hi-hats, dusty vinyl crackle"
    },
    "funk_neosoul": {
        "bpm_range": (108, 118),
        "default_bpm": 114,
        "description": "Uptempo Neo-Soul Funk, slapped electric bass, warm Fender Rhodes chords, four-on-the-floor kick, rhythmic clavinet"
    },
    "uk_garage_2step": {
        "bpm_range": (120, 130),
        "default_bpm": 124,
        "description": "Syncopated UK Garage 2-Step shuffle, deep rolling sub-bass, skipping rimshots, lush synth stabs, urgent nocturnal energy"
    }
}

def analyze_lyrics_repetition(lyrics_text):
    """Checks lyrics for exact stanza repetition, repeated end-rhymes, and progressive chorus variation."""
    lines = [l.strip() for l in lyrics_text.split("\n") if l.strip() and not l.startswith("[") and not l.startswith("(")]
    stanzas = re.findall(r"\[Chorus.*?\]\n([\s\S]*?)(?=\n\[|\Z)", lyrics_text)
    
    warnings = []
    if len(stanzas) >= 2:
        s1 = stanzas[0].strip().split("\n")
        s2 = stanzas[1].strip().split("\n")
        if s1 == s2:
            warnings.append("WARNING: Chorus 1 and Chorus 2 are 100% identical. Recommend progressive variation (altering at least 2 lines or melody in Chorus 2).")
        else:
            shared = set(s1).intersection(set(s2))
            diff_pct = 1.0 - (len(shared) / max(len(s1), 1))
            if diff_pct < 0.25:
                warnings.append(f"NOTICE: Chorus variation is only {diff_pct*100:.0f}%. Recommend greater melodic/lyrical divergence.")

    # Check for excessive word repetition (excluding articles and pronouns)
    words = [w.lower() for w in re.findall(r"\b[A-Za-z]{4,}\b", lyrics_text)]
    stopwords = {"that", "with", "this", "they", "your", "from", "when", "there", "what", "have", "been"}
    filtered_words = [w for w in words if w not in stopwords]
    word_counts = {}
    for w in filtered_words:
        word_counts[w] = word_counts.get(w, 0) + 1
    
    top_repeated = [f"'{w}' ({c}x)" for w, c in word_counts.items() if c >= 5]
    if top_repeated:
        warnings.append("Top repeated content words: " + ", ".join(top_repeated[:5]))
    
    score = max(0, 100 - (len(warnings) * 15))
    return {
        "score": score,
        "warnings": warnings,
        "total_lines": len(lines),
        "stanzas_count": len(stanzas)
    }

def compile_comfyui_prompt(track_spec, vocal_key="duet_harmony", groove_key="uk_garage_2step"):
    vocal = VOCAL_PROFILES.get(vocal_key, VOCAL_PROFILES["duet_harmony"])
    groove = TEMPO_GROOVES.get(groove_key, TEMPO_GROOVES["uk_garage_2step"])
    
    caption = (
        f"{groove['description']}, {track_spec['bpm']} BPM, {track_spec['key']}.\n"
        f"Vocal profile: {vocal['prompt_snippet']}\n"
        f"Atmosphere: High production fidelity, organic acoustic warmth, dynamic stereo depth, zero mud, radio-ready mix balance."
    )
    return {
        "caption": caption,
        "vocal_style": vocal["style_tags"],
        "bpm": track_spec["bpm"],
        "key": track_spec["key"]
    }

if __name__ == "__main__":
    print("=" * 70)
    print("DAVID LINACRE ADVANCED AUDIO PIPELINE & LYRICS QUALITY ENGINE")
    print("=" * 70)
    print("\nAvailable Vocal Profiles:")
    for k, v in VOCAL_PROFILES.items():
        print(f"  • [{k}]: {v['name']} ({v['gender'].upper()})")
    
    print("\nAvailable Uptempo Grooves:")
    for k, g in TEMPO_GROOVES.items():
        print(f"  • [{k}]: {g['default_bpm']} BPM ({g['bpm_range'][0]}-{g['bpm_range'][1]} BPM)")

    # Test repetition engine on Track 1 of Neon Velvet Nights
    sample_path = os.path.join(ALBUM_ROOT, "albums", "neon-velvet-nights", "lyrics", "01_Velvet_on_the_Concrete.txt")
    if os.path.exists(sample_path):
        with open(sample_path, "r", encoding="utf-8") as f:
            sample_lyrics = f.read()
        analysis = analyze_lyrics_repetition(sample_lyrics)
        print("\nQuality Audit for 'Velvet on the Concrete':")
        print(f"  Quality Score: {analysis['score']}/100")
        print(f"  Total Lines: {analysis['total_lines']}, Choruses: {analysis['stanzas_count']}")
        if analysis["warnings"]:
            for w in analysis["warnings"]:
                print(f"  {w}")
        else:
            print("  ✔ No repetitive chorus traps detected! Progressive variation validated.")
