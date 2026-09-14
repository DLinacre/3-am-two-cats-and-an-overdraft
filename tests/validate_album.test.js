const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('=== RUNNING DAVID LINACRE MULTI-ALBUM & DISCOGRAPHY TEST SUITE ===\n');

// 1. Validate discography.json
const discoPath = path.resolve(__dirname, '../discography.json');
assert(fs.existsSync(discoPath), 'discography.json must exist');
const disco = JSON.parse(fs.readFileSync(discoPath, 'utf8'));
assert(Array.isArray(disco.albums), 'discography.json must have albums array');
assert(disco.albums.length >= 2, 'Discography must register at least 2 albums');
console.log(`✔ discography.json schema passed (${disco.albums.length} albums registered)`);

// 2. Validate each album in discography
disco.albums.forEach((alb) => {
  const tlPath = path.resolve(__dirname, '..', alb.tracklist_file);
  assert(fs.existsSync(tlPath), `Album '${alb.title}' tracklist must exist: ${alb.tracklist_file}`);
  const tl = JSON.parse(fs.readFileSync(tlPath, 'utf8'));
  assert(tl.tracks && tl.tracks.length > 0, `Album '${alb.title}' must contain tracks`);

  const coverPath = path.resolve(__dirname, '..', alb.cover);
  assert(fs.existsSync(coverPath), `Album '${alb.title}' cover must exist: ${alb.cover}`);

  const lyricsPath = path.resolve(__dirname, '..', alb.lyrics_file);
  assert(fs.existsSync(lyricsPath), `Album '${alb.title}' lyrics must exist: ${alb.lyrics_file}`);
  const lyrics = JSON.parse(fs.readFileSync(lyricsPath, 'utf8'));
  assert(Array.isArray(lyrics) && lyrics.length > 0, `Album '${alb.title}' lyrics must be a non-empty array`);
  console.log(`✔ Album '${alb.title}' validated (${tl.tracks.length} tracks, cover & lyrics intact)`);
});

// 3. Validate index.html Syntax
const indexPath = path.resolve(__dirname, '../index.html');
assert(fs.existsSync(indexPath), 'index.html must exist');
const html = fs.readFileSync(indexPath, 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
assert(scriptMatch, 'index.html must contain a <script> block');
new Function(scriptMatch[1]);
console.log('✔ index.html embedded JavaScript is 100% syntactically valid');

// 4. Validate Album 2 dedicated entry point
const album2Entry = path.resolve(__dirname, '../albums/neon-velvet-nights/index.html');
assert(fs.existsSync(album2Entry), 'albums/neon-velvet-nights/index.html must exist');
console.log('✔ albums/neon-velvet-nights/index.html entry point validated');

console.log('\n=== ALL TESTS PASSED SUCCESSFULLY! ===');
