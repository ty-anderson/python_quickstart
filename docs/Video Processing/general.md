# Basics of Video Files

## How Video Files Work

```text
===============================================================
 VIDEO FILE BASICS
===============================================================

• A video file contains:
  - A CONTAINER (MP4, MKV, MOV)
  - VIDEO + AUDIO STREAMS encoded with codecs

• CODEC = software that compresses/decompresses video/audio
• CONTAINER = the wrapper that holds streams + metadata


===============================================================
 TRANSCODING (CONVERTING VIDEO)
===============================================================

• Converting formats involves:
  1. Decode old codec
  2. Re-encode into new codec
  3. Repackage into container

• REMUX = container change only (no re-encode)
  Example: MKV (H.264) → MP4 (H.264)  

• RE-ENCODE = codec change
  Example: H.264 → H.265


===============================================================
 COMMON VIDEO CODECS
===============================================================

• H.264 (AVC)
  - Most common, highly compatible

• H.265 (HEVC)
  - Better compression than H.264
  - Requires more processing power

• VP9
  - Open-source alternative to HEVC
  - Widely used by YouTube

• AV1
  - Newer, best compression efficiency
  - CPU-heavy decoding

• MPEG-2
  - Older, used in DVDs/broadcast


===============================================================
 COMMON AUDIO CODECS
===============================================================

• AAC
  - Standard in MP4, good quality

• MP3
  - Universal support, older format

• Opus
  - Very efficient, great for streaming/VoIP

• FLAC
  - Lossless, larger files

• AC-3 / DTS
  - Surround sound codecs


===============================================================
 CONTAINER vs CODEC
===============================================================

• Container = file type:
  - MP4, MKV, MOV, AVI

• Codec = how streams are compressed:
  - H.264, H.265, VP9, AV1 (video)
  - AAC, MP3, Opus, FLAC (audio)

• Example:
  MP4 container can include:
    • H.264 video + AAC audio
    • H.265 video + AAC audio

===============================================================

```

## Best Formats

```text
###############################################################
#  BEST VIDEO CODECS
###############################################################

# AV1 — BEST OVERALL QUALITY + COMPRESSION
# - Most efficient modern codec
# - Smallest file size, best quality
# - Royalty-free
# - Used by YouTube, Netflix, Twitch
# - Poor support on older devices (QuickTime can't play on M1)
# Best for: streaming, archival, future-proofing

# H.264 / AVC — BEST COMPATIBILITY (UNIVERSAL)
# - Works everywhere: iPhone, Android, browsers, TVs
# - Hardware acceleration everywhere
# - Smooth editing
# Best for: sharing, editing, MP4 outputs

# H.265 / HEVC — HIGH EFFICIENCY (Apple-favored)
# - Better compression than H.264
# - Works great on iPhone/iPad/Apple TV
# - Slow encoding on CPU
# Best for: 4K distribution, Apple workflows

# VP9 — GOOD COMPRESSION, WIDELY SUPPORTED IN BROWSERS
# - Used by YouTube (older 4K formats)
# - Better than H.264
# Best for: web playback


###############################################################
#  BEST AUDIO CODECS
###############################################################

# OPUS — BEST MODERN LOSSY AUDIO
# - Highest quality at any bitrate
# - Amazing for speech + music
# - Not supported inside MP4
# Best for: WEBM, MKV, streaming

# AAC — MOST COMPATIBLE AUDIO
# - Universal on mobile/desktop
# - Native to MP4
# Best for: H.264/H.265 MP4 outputs

# FLAC — BEST LOSSLESS AUDIO
# - Perfect compression, no quality loss
# Best for: archival, MKV

# PCM WAV — RAW, UNCOMPRESSED
# Best for: editing timelines (ProRes workflows)


###############################################################
#  BEST PAIRINGS (Most Common)
###############################################################

# 1. Best Overall Modern (Web/Streaming)
#    AV1 + Opus (WEBM or MKV)

# 2. Best Universal Compatibility
#    H.264 + AAC (MP4)

# 3. Best Apple Ecosystem
#    HEVC (H.265) + AAC (MP4/MOV)

# 4. Best Editing Workflow
#    Apple ProRes + PCM WAV (MOV)

# 5. Best Archival (Lossless)
#    FFV1 + FLAC (MKV)

###############################################################
#  QUICK RULES
###############################################################

# - If you care about compatibility → Use H.264 + AAC
# - If you care about smallest size + best quality → Use AV1 + Opus
# - If you are archiving media → Use MKV (supports everything)
# - If you edit video → Use ProRes
# - If you’re on macOS (QuickTime) → Convert AV1 to H.264 or HEVC
# - MP4 is strict → MKV is flexible

###############################################################
#  BEST CONTAINER CHOICES
###############################################################

# MKV  → Best for AV1, VP9, FLAC, Opus, multi-tracks, archival
# MP4  → Best for compatibility (H.264/AAC)
# MOV  → Best for editing (ProRes)
# WEBM → Best for browser streaming (AV1/VP9 + Opus)
```

## Chose a Container

```text
===============================================================
             VIDEO CONTAINER DECISION FLOWCHART
===============================================================

START
 │
 ├── Do you need MAXIMUM compatibility across ALL devices?
 │        (iPhone, Android, TV, browser, Windows, macOS, apps)
 │
 └──► YES → Use **MP4**
          - Best universal playback
          - Requires H.264/H.265 + AAC
          - Works everywhere

 └──► NO → Continue
            │
            ├── Are you editing video (Final Cut, Premiere, DaVinci)?
            │
            └──► YES → Use **MOV**
                     - Use ProRes for editing
                     - Intra-frame codec = smooth timeline

            └──► NO → Continue
                       │
                       ├── Do you want BEST quality + flexibility?
                       │   (AV1, VP9, Opus, FLAC, multi-audio, subtitles)
                       │
                       └──► YES → Use **MKV**
                                - Supports all modern codecs
                                - Best for archival + high quality

                       └──► NO → Use **MP4**
                                - Good for small files, wide support

===============================================================

```

## Choose a Codec

```text
===============================================================
                 VIDEO / AUDIO CODEC DECISION GUIDE
===============================================================

VIDEO CODECS
---------------------------------------------------------------

● Want best compression + quality?
    → **AV1**
    (Smallest files, best quality, future standard)

● Want best compatibility?
    → **H.264**
    (Works everywhere)

● Want smaller files but still high compatibility?
    → **H.265 / HEVC**
    (Great for 4K on Apple devices)

● Need YouTube-like web performance?
    → **VP9**
    (Widely supported in browsers)

● Editing in Final Cut / Premiere?
    → **ProRes**
    (Smoothest editing workflow)

● True archival / lossless?
    → **FFV1**
    (Used for film preservation)


AUDIO CODECS
---------------------------------------------------------------

● Best general-purpose quality?
    → **AAC**

● Universal compatibility?
    → **MP3**

● Best modern efficiency?
    → **Opus**
    (Great for streaming, voice, web media)

● Best lossless audio storage?
    → **FLAC**

● Surround sound?
    → **AC-3 (Dolby Digital)** or **DTS**

---------------------------------------------------------------
SUMMARY PAIRS
---------------------------------------------------------------
● Streaming / Future-proof → AV1 + Opus
● Universal playback → H.264 + AAC (MP4)
● Apple ecosystem / 4K → HEVC + AAC (MP4/MOV)
● Editing workflow → ProRes + WAV (MOV)
● Archival → FFV1 + FLAC (MKV)
===============================================================

```

