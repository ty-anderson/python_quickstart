# Video Tools

## FFmpeg

ffmpeg is an open source video editing command tool. Very powerful, other 
video editing programs are built on top of this software.

```bash
###############################################################
#  BASIC INFO
###############################################################

# Show file info
ffprobe -hide_banner input.mp4

# Show all streams
ffmpeg -i input.mp4


###############################################################
#  REMUX (NO RE-ENCODE) — Lossless, Fast
###############################################################

# MP4 → MKV
ffmpeg -i input.mp4 -c copy output.mkv

# MKV → MP4 (only works if codecs are MP4-compatible)
ffmpeg -i input.mkv -c copy output.mp4

# WEBM → MKV (AV1/VP9 safe)
ffmpeg -i input.webm -c copy output.mkv


###############################################################
#  VIDEO CONVERSION (RE-ENCODE)
###############################################################

# Convert to H.264 (good quality)
ffmpeg -i input.mkv -c:v libx264 -crf 18 -preset medium -c:a aac output.mp4

# Convert to HEVC (H.265)
ffmpeg -i input.mp4 -c:v libx265 -crf 20 -preset medium -c:a copy output_hevc.mp4

# Convert AV1 to H.264 (for QuickTime, iPhone)
ffmpeg -i input.webm -c:v libx264 -crf 18 -preset medium -c:a aac output.mp4

# re-encode the audio and video
ffmpeg -i 'Video file.webm' \
-c:v libx264 -crf 18 -preset medium \
-c:a aac -b:a 192k \
'Video file.mp4'

# to mkv
ffmpeg -i 'Video file.webm' \
-c:v copy \
-c:a aac -b:a 192k \
'Video file.mkv'

###############################################################
#  HARDWARE ACCELERATION (Apple M1/M2/M3)
###############################################################

# H.264 hardware encode (fast)
ffmpeg -i input.mov -c:v h264_videotoolbox -c:a aac output.mp4

# HEVC hardware encode
ffmpeg -i input.mov -c:v hevc_videotoolbox -c:a aac output_hevc.mp4


###############################################################
#  AUDIO ONLY
###############################################################

# Extract audio (no re-encode)
ffmpeg -i input.mp4 -vn -c:a copy audio.m4a

# Convert audio to AAC
ffmpeg -i input.opus -c:a aac -b:a 192k output.m4a

# Convert audio to MP3
ffmpeg -i input.wav -c:a libmp3lame -b:a 320k output.mp3


###############################################################
#  TRIM / CUT VIDEO (NO RE-ENCODE)
###############################################################

# Cut between timestamps (fast, no re-encode)
ffmpeg -ss 00:00:30 -to 00:01:00 -i input.mp4 -c copy clip.mp4

# Cut and re-encode (more accurate)
ffmpeg -ss 00:00:30 -to 00:01:00 -i input.mp4 -c:v libx264 -c:a copy clip.mp4


###############################################################
#  SCALE / RESIZE
###############################################################

# Resize to 1080p
ffmpeg -i input.mp4 -vf scale=1920:1080 -c:v libx264 -crf 18 output_1080p.mp4

# Resize with hardware acceleration
ffmpeg -i input.mp4 -vf scale=1280:720 -c:v h264_videotoolbox output_720p.mp4


###############################################################
#  CONCATENATION (JOIN VIDEOS)
###############################################################

# Method 1: Same codec (fast)
# Create list.txt containing:
# file 'a.mp4'
# file 'b.mp4'
ffmpeg -f concat -safe 0 -i list.txt -c copy merged.mp4

# Method 2: Different codecs (re-encode)
ffmpeg -i "concat:a.mp4|b.mp4" -c:v libx264 -c:a aac output.mp4


###############################################################
#  EXTRA USEFUL COMMANDS
###############################################################

# Extract JPG thumbnail at 10 seconds
ffmpeg -ss 00:00:10 -i input.mp4 -vframes 1 thumb.jpg

# Increase brightness
ffmpeg -i input.mp4 -vf "eq=brightness=0.1" output.mp4

# Remove audio
ffmpeg -i input.mp4 -an no_audio.mp4

# Remove video (audio only)
ffmpeg -i input.mp4 -vn audio_only.m4a

# Change playback speed (2x faster)
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" -filter:a "atempo=2.0" output_fast.mp4


###############################################################
#  CREATE GIF (HIGH QUALITY)
###############################################################

# Generate palette (better colors)
ffmpeg -i input.mp4 -vf palettegen palette.png

# Create GIF using palette
ffmpeg -i input.mp4 -i palette.png -filter_complex "paletteuse" output.gif

```

## yt-dlp

yt-dlp is a fork of youtube-dl. It is a command-line program to download videos from YouTube and many other sites.

```bash
# basic download
yt-dlp "https://www.youtube.com/watch?v=VIDEO_ID"

# download best video and audio
yt-dlp -f "bestvideo+bestaudio/best" "URL"

# download playlist
yt-dlp --yes-playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# download audio only
yt-dlp -x --audio-format mp3 "URL"

# Download with custom filename
yt-dlp -o "%(title)s.%(ext)s" "URL"

# combine best quality, location, and make sure it's not a playlist
yt-dlp -f "bestvideo+bestaudio/best" -o "downloads/%(title)s.%(ext)s" --no-playlist "URL"

```
