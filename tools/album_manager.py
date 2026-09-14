# -*- coding: utf-8 -*-
"""
David Linacre Album Manager & Studio Orchestrator CLI
Allows seamless creation, management, lyric generation, and validation of multi-album discographies.

Usage:
  python tools/album_manager.py list
  python tools/album_manager.py create --slug "sunset-drive" --title "Sunset Drive" --genre "Synthwave / 80s Funk" --bpm 115 --vocals "male_tenor"
  python tools/album_manager.py validate
"""

import os
import sys
import json
import argparse
from PIL import Image, ImageDraw

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ALBUM_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISCOGRAPHY_PATH = os.path.join(ALBUM_ROOT, "discography.json")

def load_discography():
    if not os.path.exists(DISCOGRAPHY_PATH):
        return {"artist": "David Linacre", "default_album": "", "albums": []}
    with open(DISCOGRAPHY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_discography(data):
    with open(DISCOGRAPHY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def list_albums():
    disco = load_discography()
    print("=" * 70)
    print(f"DAVID LINACRE DISCOGRAPHY CATALOG ({len(disco.get('albums', []))} ALBUMS)")
    print("=" * 70)
    for idx, alb in enumerate(disco.get("albums", []), 1):
        is_def = " (DEFAULT)" if alb.get("id") == disco.get("default_album") else ""
        print(f"[{idx}] {alb.get('title')} ({alb.get('year')}) [{alb.get('edition')}]{is_def}")
        print(f"    ID: {alb.get('id')}")
        print(f"    Genre: {alb.get('genre')} | Tempo: {alb.get('bpm_range')}")
        print(f"    Vocals: {alb.get('vocals')}")
        print(f"    Tracks: {alb.get('total_tracks')}")
        print()

def create_album(slug, title, genre, bpm, vocals, edition="Studio Edition", num_tracks=8):
    disco = load_discography()
    # Check if slug exists
    if any(a["id"] == slug for a in disco["albums"]):
        print(f"Error: Album slug '{slug}' already exists in discography!")
        return

    album_dir = os.path.join(ALBUM_ROOT, "albums", slug)
    tracks_dir = os.path.join(album_dir, "tracks")
    lyrics_dir = os.path.join(album_dir, "lyrics")
    os.makedirs(tracks_dir, exist_ok=True)
    os.makedirs(lyrics_dir, exist_ok=True)

    # Generate placeholder cover
    cover_path = os.path.join(album_dir, "Cover.png")
    img = Image.new("RGB", (1080, 1080), color="#120c1f")
    draw = ImageDraw.Draw(img)
    draw.rectangle([60, 60, 1020, 1020], outline="#a855f7", width=4)
    draw.text((100, 450), title.upper(), fill="#ffffff")
    draw.text((100, 550), f"David Linacre • {genre}", fill="#ec4899")
    draw.text((100, 620), f"{bpm} BPM • {edition}", fill="#38bdf8")
    img.save(cover_path, "PNG")

    # Generate initial Tracklist.json
    tracklist_data = {
        "album_title": title,
        "artist": "David Linacre",
        "year": 2026,
        "edition": edition,
        "genre": genre,
        "bpm_range": f"{bpm} BPM",
        "vocals": vocals,
        "total_tracks": num_tracks,
        "tracks": []
    }
    for i in range(1, num_tracks + 1):
        tracklist_data["tracks"].append({
            "track_number": i,
            "title": f"Track {i:02d}",
            "bpm": bpm,
            "key": "C Minor",
            "duration": "02:30",
            "artwork": f"albums/{slug}/tracks/Track_{i:02d}.png",
            "video_file": None,
            "status": "Scaffolded / Ready for Neural Synthesis"
        })

    with open(os.path.join(album_dir, "Tracklist.json"), "w", encoding="utf-8") as f:
        json.dump(tracklist_data, f, indent=2)

    # Register in discography
    new_entry = {
        "id": slug,
        "title": title,
        "edition": edition,
        "year": 2026,
        "genre": genre,
        "bpm_range": f"{bpm} BPM",
        "vocals": vocals,
        "total_tracks": num_tracks,
        "cover": f"albums/{slug}/Cover.png",
        "banner": f"albums/{slug}/Cover.png",
        "tracklist_file": f"albums/{slug}/Tracklist.json",
        "lyrics_file": f"albums/{slug}/lyrics/ALL_LYRICS.json",
        "media_root": f"albums/{slug}/",
        "description": f"A brand-new {genre} album produced at {bpm} BPM with {vocals} vocal styling."
    }
    disco["albums"].append(new_entry)
    disco["total_albums"] = len(disco["albums"])
    save_discography(disco)
    print(f"Successfully created and registered new album: '{title}' ({slug})!")

def validate_all():
    disco = load_discography()
    print("Validating all albums in discography...")
    all_ok = True
    for alb in disco.get("albums", []):
        tl_path = os.path.join(ALBUM_ROOT, alb.get("tracklist_file", ""))
        cov_path = os.path.join(ALBUM_ROOT, alb.get("cover", ""))
        tl_ok = os.path.exists(tl_path)
        cov_ok = os.path.exists(cov_path)
        status_str = "✔ PASS" if (tl_ok and cov_ok) else "❌ FAIL"
        if not (tl_ok and cov_ok):
            all_ok = False
        print(f"  [{status_str}] {alb.get('title')} -> Tracklist: {tl_ok}, Cover: {cov_ok}")
    return all_ok

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="David Linacre Album Manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all albums in discography")
    subparsers.add_parser("validate", help="Validate all discography albums")

    create_p = subparsers.add_parser("create", help="Create a new album scaffold")
    create_p.add_argument("--slug", required=True, help="Album slug (e.g. neon-dreams)")
    create_p.add_argument("--title", required=True, help="Album title")
    create_p.add_argument("--genre", default="Uptempo Soul / UK Garage", help="Genre description")
    create_p.add_argument("--bpm", type=int, default=118, help="Target BPM")
    create_p.add_argument("--vocals", default="Velvet Female & Crisp Male Duet", help="Vocal description")
    create_p.add_argument("--tracks", type=int, default=8, help="Number of tracks")

    args = parser.parse_args()
    if args.command == "list" or not args.command:
        list_albums()
    elif args.command == "validate":
        validate_all()
    elif args.command == "create":
        create_album(args.slug, args.title, args.genre, args.bpm, args.vocals, num_tracks=args.tracks)
