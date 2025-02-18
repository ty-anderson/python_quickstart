# ffmpeg

ffmpeg is a video editing command tool. 

## How a Video Works

1. A video file consists of a container (like MP4, MKV) and encoded video/audio streams inside.
2. The codec is what encodes (compresses) the video/audio when saving it and decodes (decompresses) it when playing it.

## Converting a Video File (Transcoding)

If you want to convert a video file from one format to another (e.g., MKV to MP4 or H.264 to H.265), 
you use transcoding software (like HandBrake, FFmpeg, or VLC). The process involves:

1. Decoding (using the current codec).
2. Re-encoding (using a new codec or settings).
3. Packaging the video/audio into a new container format.

For example:

- MKV (H.264 + AAC) → MP4 (H.264 + AAC) → Just a container change (remuxing, no transcoding needed).
- MP4 (H.264) → MP4 (H.265) → A full re-encoding is required.

So while codecs are a part of the conversion process, they don't handle file conversion by themselves—you need transcoding software for that.

- Codec - software that compresses or decompresses media files (audio or video). Determines the encoding. 
Important for compression, compatability, and streaming efficiency.

- Video Codecs - These compress video data to reduce file size while maintaining visual quality.

- H.264 (AVC) – Most common, widely supported, good balance of quality and size.
- H.265 (HEVC) – More efficient than H.264 (better quality at smaller sizes), but requires more processing power.
- VP9 – Open-source alternative to H.265, widely used on YouTube.
- AV1 – Newer, even better compression than VP9 and H.265, but requires more CPU power to decode.
- MPEG-2 – Older, used in DVDs and some broadcast TV.

- Audio Codecs - These compress audio data for storage and streaming.

- AAC – Common in MP4 files, better quality than MP3 at the same bitrate.
- MP3 – Universal compatibility, but lower efficiency.
- Opus – High efficiency, used in VoIP and streaming.
- FLAC – Lossless, used for high-quality music storage.
- Dolby Digital (AC-3) / DTS – Used in surround sound systems.

## Codec vs. Container (MKV, MP4)

- Container formats (like MKV, MP4, AVI, MOV) hold video, audio, and subtitle tracks.
- Codecs determine how the actual video and audio inside the container are compressed and played.
  - Example: An MP4 file can contain H.264 video + AAC audio.

So, when choosing a video format, you need to consider both the container (MKV, MP4, etc.) and the codec (H.264, H.265, etc.).