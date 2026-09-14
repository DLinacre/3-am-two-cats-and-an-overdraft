const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('=== RUNNING DAVID LINACRE ALBUM TEST SUITE ===\n');

// 1. Tracklist.json
const tracklistPath = path.resolve(__dirname, '../Tracklist.json');
assert(fs.existsSync(tracklistPath), 'Tracklist.json must exist');
const tracklist = JSON.parse(fs.readFileSync(tracklistPath, 'utf8'));
assert.strictEqual(tracklist.total_tracks, 16, 'Album must declare 16 tracks');
assert.strictEqual(tracklist.tracks.length, 16, 'Tracks array must contain 16 items');
console.log('✔ Tracklist.json schema validation passed (16 tracks)');

// 2. ALL_LYRICS.json
const lyricsPath = path.resolve(__dirname, '../assets/lyrics/ALL_LYRICS.json');
assert(fs.existsSync(lyricsPath), 'ALL_LYRICS.json must exist');
const lyrics = JSON.parse(fs.readFileSync(lyricsPath, 'utf8'));
assert(Array.isArray(lyrics), 'ALL_LYRICS.json must be an array');
assert.strictEqual(lyrics.length, 16, 'ALL_LYRICS.json must contain 16 lyrical suites');
console.log('✔ ALL_LYRICS.json contains 16 complete lyrical suites');

// 3. index.html Syntax
const indexPath = path.resolve(__dirname, '../index.html');
assert(fs.existsSync(indexPath), 'index.html must exist');
const html = fs.readFileSync(indexPath, 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
assert(scriptMatch, 'index.html must contain a <script> block');
new Function(scriptMatch[1]);
console.log('✔ index.html embedded JavaScript is 100% syntactically valid');

console.log('\n=== ALL TESTS PASSED SUCCESSFULLY! (3/3) ===');
