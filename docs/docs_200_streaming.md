# Streaming

The **"best" streaming protocol** depends on the use case. Here’s a breakdown of what’s ideal for different scenarios:

### **Best Streaming Protocols by Use Case**

**On-Demand Video Streaming (e.g., Netflix, YouTube)**

- **Best:** **DASH (MPEG-DASH) or HLS**
- **Why?** Adaptive bitrate streaming (ABR) ensures smooth playback across different devices and network conditions.
- **Used By:** Netflix, YouTube (DASH), Apple (HLS), Amazon Prime Video (DASH + HLS)

**Live Streaming (e.g., Twitch, YouTube Live)**

- **Best:** **HLS (Low-Latency), DASH (LL-DASH), or WebRTC for real-time interactivity**
- **Why?** HLS and DASH offer scalability, while WebRTC provides ultra-low latency for live interaction.
- **Used By:** Twitch (RTMP for ingest, HLS for playback), YouTube Live (DASH + HLS)

**Real-Time Communication (e.g., Zoom, Google Meet)**

- **Best:** **WebRTC**
- **Why?** Peer-to-peer, ultra-low latency, no need for external servers.
- **Used By:** Google Meet, Zoom, Microsoft Teams

**Professional Broadcast / Contribution (e.g., TV Networks, Sports)**

- **Best:** **SRT or RTMP (for ingest)**
- **Why?** SRT provides reliable, high-quality, low-latency transmission, while RTMP is still widely supported for ingestion.
- **Used By:** ESPN, news networks, live sports broadcasting

---

### **What Does Netflix Use?**

Netflix uses **MPEG-DASH** for most of its streaming, alongside **HLS for Apple devices**. Their stack includes:

- **DASH (MPEG-DASH)** – Adaptive bitrate streaming for optimal playback across devices.
- **HLS (HTTP Live Streaming)** – For Apple devices, since Apple mandates HLS.
- **CDN Optimization** – Uses its own **Open Connect CDN** to reduce latency and improve video delivery.
- **Per-Title Encoding** – Dynamically adjusts compression based on the content to optimize quality vs. bandwidth.

So HLS can be used to stream an mp4 file to another device?

Yes, **HLS (HTTP Live Streaming)** can be used to stream an **MP4 file** to another device, but it requires some processing first. 

### **How HLS Streams an MP4 File**

**Segment the MP4 File**  

   - HLS requires the video to be split into small chunks (typically `.ts` files, though newer versions support fragmented MP4 `.m4s`).
   - A tool like **FFmpeg** can do this.

**Create an M3U8 Playlist**  

   - HLS uses a `.m3u8` file (a playlist) that lists the segmented video files.
   - The player downloads and plays the segments in order.

**Host the Segments & Playlist on a Server**  

   - You need an **HTTP server (e.g., Nginx, Apache, or a cloud service like S3)** to serve the files.

**Play the Stream on Another Device**  

   - Open the `.m3u8` URL in a compatible player (e.g., **Safari, VLC, ExoPlayer, or hls.js in a browser**).

---

### **Example: Convert MP4 to HLS Using FFmpeg**
```sh
ffmpeg -i input.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8
```
- `-hls_time 10` → Splits video into **10-second** segments.
- `-hls_list_size 0` → Keeps all segments in the playlist.
- `output.m3u8` → The playlist file.

### **How to Serve the Stream**

1. Move the `output.m3u8` and `.ts` files to a web server.
2. Access the stream via:  
   ```
   http://yourserver.com/path/output.m3u8
   ```
   
3. Play it in:

   **Web browser** with `hls.js` OR
   **VLC media player** (Open Network Stream) OR
   **iOS Safari (built-in HLS support)**

---

## **🎯 DASH Command with FFmpeg**

Run:
```sh
ffmpeg -i vid_file.mp4 -codec: copy -map 0 -f dash output.mpd
```

### **🔍 Explanation of Flags:**

- `-i vid_file.mp4` → Input video file.
- `-codec: copy` → Copies the streams without re-encoding.
- `-map 0` → Ensures all streams (audio & video) are included.
- `-f dash` → Specifies DASH output format.
- `output.mpd` → The DASH manifest file.

---

## **📂 DASH Output Files**

This will generate:

- **`output.mpd`** → The DASH manifest (index) file.
- **Segmented `.m4s` video/audio chunks**.

---

## **🖥️ Serving DASH with Python HTTP Server**

Just like HLS, you can serve DASH using:

```sh
python3 -m http.server 9000
```

Then play in VLC:
```
http://localhost:9000/output.mpd
```
✔️ **VLC supports DASH**, so this should work without additional configuration.

---

## **🌐 Play DASH in a Browser**

Browsers don’t natively support DASH, so you need a **DASH player** like [dash.js](https://reference.dashif.org/dash.js/latest/samples/getting-started/basic-example.html).

To embed DASH in HTML, use:
```html
<video id="dashPlayer" controls>
    <source src="http://localhost:9000/output.mpd" type="application/dash+xml">
</video>
<script src="https://cdn.dashjs.org/latest/dash.all.min.js"></script>
<script>
    var player = dashjs.MediaPlayer().create();
    player.initialize(document.querySelector("#dashPlayer"), "http://localhost:9000/output.mpd", true);
</script>
```

---

## **📌 Advanced DASH: Multi-Bitrate Encoding**

To **support adaptive streaming**, generate multiple bitrates:

```sh
ffmpeg -i vid_file.mp4 \
  -map 0:v -map 0:a \
  -b:v:0 2000k -b:v:1 1000k \
  -s:v:0 1920x1080 -s:v:1 1280x720 \
  -c:v libx264 -c:a aac \
  -f dash -seg_duration 4 -use_timeline 1 -use_template 1 \
  output.mpd
```

✔️ **This creates multiple video quality options** that DASH players can switch between dynamically.

---

### **🚀 Summary**
- **Basic DASH:** `ffmpeg -i vid_file.mp4 -codec: copy -map 0 -f dash output.mpd`
- **Serve DASH:** `python3 -m http.server 9000`
- **Play in VLC:** `http://localhost:9000/output.mpd`
- **Play in Browser:** Use `dash.js`
- **Adaptive Streaming:** Encode multiple bitrates with `-b:v` and `-s:v`

