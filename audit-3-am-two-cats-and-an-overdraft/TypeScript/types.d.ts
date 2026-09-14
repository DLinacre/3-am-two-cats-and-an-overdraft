export interface Track {
  num: number;
  title: string;
  key: string;
  bpm: number;
  duration: string;
  art: string;
  src: string;
  ready: boolean;
}

export interface LyricItem {
  num: number;
  title: string;
  lyrics: string;
}

export interface AlbumMetadata {
  album_title: string;
  artist: string;
  year: number;
  edition: string;
  genre: string;
  total_tracks: number;
  streaming_url: string;
  github_repo: string;
  mastering_standard: string;
}
