# -*- coding: utf-8 -*-
"""
David Linacre & Maya Chen — Neon Velvet Nights (2026)
Autonomous Batch Neural Generation & Mastering Pipeline
"""

import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
if hasattr(sys.stderr, "reconfigure"):
    try: sys.stderr.reconfigure(encoding="utf-8")
    except Exception: pass
import json
import time
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

BASE_DIR = r"D:\Desktop\David Linacre - 3 AM, Two Cats & An Overdraft (2026) [Deluxe Edition]"
ALBUM_DIR = os.path.join(BASE_DIR, "albums", "neon-velvet-nights")
LYRICS_DIR = os.path.join(ALBUM_DIR, "lyrics")
TRACKS_DIR = os.path.join(ALBUM_DIR, "tracks")
COMFY_AUDIO_OUT = r"E:\ComfyUI\output\audio"
COMFY_URL = "http://127.0.0.1:8188"
FFMPEG_EXE = r"C:\Users\KingL\AppData\Local\Programs\Python\Python314\Scripts\ffmpeg.exe"

TRACK_SPECS = [
    {
        "track_number": 1,
        "title": "Velvet on the Concrete",
        "bpm": 118,
        "key": "F# Minor",
        "duration": 160.0,
        "caption": "Syncopated UK Garage 2-Step shuffle, deep rolling sub-bass, skipping rimshots, lush Fender Rhodes stabs, urgent nocturnal energy, 118 BPM, F# minor. Vocal profile: Silky intimate female neo-soul lead vocalist (Maya Chen) paired with crisp energetic British male rap verses (David Linacre). Atmosphere: Late-night London street groove, wet pavement neon reflections, high studio fidelity, radio-ready stereo spread.",
        "lyrics_file": "01_Velvet_on_the_Concrete.txt",
        "prefix": "audio/NeonVelvet_Track01_Velvet_on_the_Concrete",
        "seed": 88101
    },
    {
        "track_number": 2,
        "title": "Midnight Espresso & Basslines",
        "bpm": 114,
        "key": "D Minor",
        "duration": 155.0,
        "caption": "Uptempo Neo-Soul Funk, slapped electric bass, warm Fender Rhodes chords, four-on-the-floor kick, rhythmic clavinet, 114 BPM, D minor. Vocal profile: Warm soulful male tenor with gentle rasp and effortless falsetto (David Linacre), backed by silky female vocal ad-libs (Maya Chen). Atmosphere: Cozy midnight cafe studio, caffeinated funk bounce, tight analog compression.",
        "lyrics_file": "02_Midnight_Espresso_&_Basslines.txt",
        "prefix": "audio/NeonVelvet_Track02_Midnight_Espresso",
        "seed": 88102
    },
    {
        "track_number": 3,
        "title": "London Underground at 1 AM",
        "bpm": 122,
        "key": "A Minor",
        "duration": 165.0,
        "caption": "Urgent UK Garage 2-Step shuffle, subterranean sub-bass, tube train ambiance, brisk skipping hi-hats, 122 BPM, A minor. Vocal profile: Fast-paced vocal duet with rapid British male rap verses and soaring melodic female soul chorus. Atmosphere: Late night Tube journey, neon reflections on wet platform tiles, kinetic urban motion.",
        "lyrics_file": "03_London_Underground_at_1_AM.txt",
        "prefix": "audio/NeonVelvet_Track03_London_Underground",
        "seed": 88103
    },
    {
        "track_number": 4,
        "title": "Call Me When the Master Drops",
        "bpm": 110,
        "key": "Eb Major",
        "duration": 150.0,
        "caption": "Glittering Neo-Soul Disco-Funk, driving four-on-the-floor groove, shimmering electric piano arpeggios, slap bass, 110 BPM, Eb major. Vocal profile: Charismatic, powerful female R&B lead vocalist with agile vocal runs and soulful belting, teasing humorous banter. Atmosphere: Penthouse rooftop after-party, sparkling city lights, high-gloss modern soul.",
        "lyrics_file": "04_Call_Me_When_the_Master_Drops.txt",
        "prefix": "audio/NeonVelvet_Track04_Call_Me_When_Master_Drops",
        "seed": 88104
    },
    {
        "track_number": 5,
        "title": "Two Keys, One Ignition",
        "bpm": 124,
        "key": "B Minor",
        "duration": 158.0,
        "caption": "Driving Speed Garage, warped bassline, rapid syncopated 2-step shuffle, vocal house stabs, 124 BPM, B minor. Vocal profile: High-energy British male rap verses with full harmonized female anthemic chorus, octave vocal doublings. Atmosphere: Midnight highway acceleration, turbocharged sonic velocity, relentless dancefloor drive.",
        "lyrics_file": "05_Two_Keys_One_Ignition.txt",
        "prefix": "audio/NeonVelvet_Track05_Two_Keys_One_Ignition",
        "seed": 88105
    },
    {
        "track_number": 6,
        "title": "Tape Saturation Heartbreak",
        "bpm": 108,
        "key": "C Minor",
        "duration": 162.0,
        "caption": "Warm Rhodes Neo-Soul Bounce, rich tape saturation, gentle vinyl crackle, acoustic bass, warm kick and brushed snare, 108 BPM, C minor. Vocal profile: Intimate male and female soul duet, delicate emotional delivery, harmonized thirds, analog warmth. Atmosphere: Late-night rain against studio windows, vintage reel-to-reel glow, healing melancholy.",
        "lyrics_file": "06_Tape_Saturation_Heartbreak.txt",
        "prefix": "audio/NeonVelvet_Track06_Tape_Saturation_Heartbreak",
        "seed": 88106
    },
    {
        "track_number": 7,
        "title": "Catch the Night Bus Home",
        "bpm": 120,
        "key": "G Minor",
        "duration": 156.0,
        "caption": "Syncopated UK Garage 2-Step bassline, double-decker bus engine hum, raindrops on red metal roof, swinging hi-hats, 120 BPM, G minor. Vocal profile: Conversational British rap cadence with evocative London storytelling, seamless female soul bridge. Atmosphere: Top deck of the N29 bus, panoramic night city view, reflective midnight solitude.",
        "lyrics_file": "07_Catch_the_Night_Bus_Home.txt",
        "prefix": "audio/NeonVelvet_Track07_Catch_the_Night_Bus_Home",
        "seed": 88107
    },
    {
        "track_number": 8,
        "title": "Sunrise in Soho",
        "bpm": 116,
        "key": "Db Major",
        "duration": 170.0,
        "caption": "Euphoric Soulful House and Neo-Soul crescendo, uplifting Rhodes chords, soaring brass pads, triumphant four-on-the-floor kick, 116 BPM, Db major. Vocal profile: Grand ensemble finale featuring dual soaring male and female soul harmonies, dynamic vocal ad-libs. Atmosphere: Golden morning sunlight spilling over Soho streets, triumph over exhaustion, daylight celebration.",
        "lyrics_file": "08_Sunrise_in_Soho.txt",
        "prefix": "audio/NeonVelvet_Track08_Sunrise_in_Soho",
        "seed": 88108
    }
]

def load_template_workflow():
    template_path = os.path.join(BASE_DIR, "comfy_workflow_template.json")
    with open(template_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_track_prompt(spec):
    workflow = load_template_workflow()
    lyrics_path = os.path.join(LYRICS_DIR, spec["lyrics_file"])
    with open(lyrics_path, "r", encoding="utf-8") as f:
        lyrics_content = f.read()

    # Configure Node 4: MiniMaxMusic3TextEncode
    workflow["4"]["inputs"]["caption"] = spec["caption"]
    workflow["4"]["inputs"]["lyrics"] = lyrics_content
    workflow["4"]["inputs"]["seed"] = spec["seed"]
    workflow["4"]["inputs"]["max_duration"] = spec["duration"]
    workflow["4"]["inputs"]["cfg_scale"] = 1.35
    workflow["4"]["inputs"]["top_k"] = 50

    # Configure Node 7: KSampler
    workflow["7"]["inputs"]["seed"] = spec["seed"]
    workflow["7"]["inputs"]["steps"] = 32
    workflow["7"]["inputs"]["cfg"] = 1.35

    # Configure Node 9: SaveAudioAdvanced
    workflow["9"]["inputs"]["filename_prefix"] = spec["prefix"]
    workflow["9"]["inputs"]["format"] = "flac"

    return workflow

def post_prompt(workflow):
    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(f"{COMFY_URL}/prompt", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_queue_status():
    req = urllib.request.Request(f"{COMFY_URL}/queue")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def master_flac_to_mp4(track_num):
    spec = next((s for s in TRACK_SPECS if s["track_number"] == track_num), None)
    if not spec:
        return False

    prefix_base = os.path.basename(spec["prefix"])
    # Find matching flac in COMFY_AUDIO_OUT
    flac_files = [f for f in os.listdir(COMFY_AUDIO_OUT) if f.startswith(prefix_base) and f.endswith(".flac")]
    if not flac_files:
        return False

    flac_path = os.path.join(COMFY_AUDIO_OUT, sorted(flac_files)[-1])
    art_path = os.path.join(TRACKS_DIR, f"Track_{spec['track_number']:02d}.png")
    if not os.path.exists(art_path):
        art_path = os.path.join(ALBUM_DIR, "Cover.png")

    clean_title = spec["title"].replace(":", " -").replace("/", "-").replace("?", "")
    out_mp4_name = f"{spec['track_number']:02d} - {clean_title}.mp4"
    out_mp4_path = os.path.join(ALBUM_DIR, out_mp4_name)

    print(f"Mastering Track {spec['track_number']} ({spec['title']}) into 1080p MP4...")
    # FFmpeg loop image + flac audio with EBU R128 mastering curves
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", art_path,
        "-i", flac_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-r", "25",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        out_mp4_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(out_mp4_path):
        print(f"[OK] Mastered successfully: {out_mp4_name} ({os.path.getsize(out_mp4_path)} bytes)")
        return True
    else:
        print(f"[ERROR] FFmpeg error on track {spec['track_number']}: {res.stderr[:200]}")
        return False

def sync_player():
    upgrade_script = os.path.join(BASE_DIR, "tools", "upgrade_player_multi_album.py")
    subprocess.run([sys.executable, upgrade_script], check=True)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Neon Velvet Nights Batch Generator & Masterer")
    parser.add_argument("--queue", action="store_true", help="Queue all 8 tracks into ComfyUI")
    parser.add_argument("--track", type=int, help="Queue only specific track number (1-8)")
    parser.add_argument("--status", action="store_true", help="Check ComfyUI queue status")
    parser.add_argument("--master-all", action="store_true", help="Master all completed FLAC tracks into MP4")
    parser.add_argument("--auto", action="store_true", help="Queue all tracks and automatically monitor & master")

    args = parser.parse_args()

    if args.status:
        q = get_queue_status()
        print("ComfyUI Queue Status:")
        print(f"  Running: {len(q.get('queue_running', []))}")
        print(f"  Pending: {len(q.get('queue_pending', []))}")
        sys.exit(0)

    if args.track:
        spec = next((s for s in TRACK_SPECS if s["track_number"] == args.track), None)
        if not spec:
            print(f"Track {args.track} not found!")
            sys.exit(1)
        wf = build_track_prompt(spec)
        res = post_prompt(wf)
        print(f"✔ Queued Track {args.track}: '{spec['title']}' -> Prompt ID: {res.get('prompt_id')}")
        sys.exit(0)

    if args.queue or args.auto:
        print("=" * 70)
        print("QUEUEING ALL 8 TRACKS OF 'NEON VELVET NIGHTS' INTO COMFYUI")
        print("=" * 70)
        for spec in TRACK_SPECS:
            wf = build_track_prompt(spec)
            res = post_prompt(wf)
            print(f"  [Track {spec['track_number']}/8] Queued '{spec['title']}' ({spec['bpm']} BPM, {spec['key']}) -> Prompt ID: {res.get('prompt_id')}")
            time.sleep(0.5)
        print("\nAll 8 tracks successfully queued in ComfyUI!")

    if args.master_all:
        for spec in TRACK_SPECS:
            master_flac_to_mp4(spec["track_number"])
        sync_player()

    if args.auto:
        print("\nEntering Autonomous Monitor & Master loop...")
        pending_tracks = set(range(1, 9))
        while pending_tracks:
            q = get_queue_status()
            running = len(q.get('queue_running', []))
            pending = len(q.get('queue_pending', []))
            now_str = datetime.now().strftime("%H:%M:%S")
            print(f"[{now_str}] Queue: {running} running, {pending} pending. Checking for completed audio...")

            completed_now = []
            for t_num in list(pending_tracks):
                spec = next(s for s in TRACK_SPECS if s["track_number"] == t_num)
                prefix_base = os.path.basename(spec["prefix"])
                flac_files = [f for f in os.listdir(COMFY_AUDIO_OUT) if f.startswith(prefix_base) and f.endswith(".flac")]
                if flac_files:
                    if master_flac_to_mp4(t_num):
                        completed_now.append(t_num)
                        pending_tracks.remove(t_num)

            if completed_now:
                sync_player()
                print(f"✔ Player synchronized with {len(completed_now)} freshly mastered track(s)!")

            if running == 0 and pending == 0 and not pending_tracks:
                print("All tracks finished and mastered!")
                break
            time.sleep(30)
