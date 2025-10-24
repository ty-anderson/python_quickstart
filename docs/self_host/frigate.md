# Frigate

Open source video security feed.

There are several ways to handle streams. Different protocols exist to 
handle this.

- RTSP - Realtime streaming protocol
- RTMP - not as common
- HTTP/MJPEG - video over HTTP, slower.

If a camera can expose a URI to connect to, then Frigate can probably connect.
It uses ffmpeg under the hood. Here's an example of how you can try to see if
a camera is working over a stream:

```bash
# ffplay is a ffmpeg module
ffplay rtsp://user:password@CAMERA_IP:554/stream_path

# basic view stream over http if no auth required
ffplay http://192.168.1.205:8081/video

# connect with username and password
ffplay http://admin:admin@192.168.1.205:8081/video

# use rtsp
ffplay rtsp://user:password@192.168.1.50:554/stream1


```

## Docker Compose Setup

Lets setup Frigate.

Create the directory:

```bash
mkdir /srv/frigate
mkdir /srv/frigate/config
touch /srv/frigate/config/config.yaml
touch /srv/frigate/docker-compose.yaml
```


Docker Compose file:
```yaml
services:
  frigate:
    container_name: frigate
    image: ghcr.io/blakeblackshear/frigate:stable
    restart: unless-stopped
    privileged: true
    shm_size: "64mb"  # needed for ffmpeg buffer
    ports:
      - "5000:5000"    # Web UI
      - "1935:1935"    # RTMP streaming (optional)
    environment:
      - FRIGATE_RTSP_PASSWORD=KineWind88
      - NVIDIA_VISIBLE_DEVICES=all
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ./config:/config
      - ./media:/media/frigate
      - type: tmpfs
        target: /tmp/cache
        tmpfs:
          size: 1000000000
    runtime: nvidia  # enable gpu acceleration with nvidia gpu
```

Once the docker compose is working, the config file is how you add 
cameras and adjust settings.

config.yaml
```yaml
mqtt:
  enabled: False

cameras:
  iphone_camera:
    ffmpeg:
      hwaccel_args: []
      inputs:
        - path: http://username:password@192.168.1.205:8081/video
          input_args: -avoid_negative_ts make_zero -fflags nobuffer -flags low_delay -analyzeduration 1000000 -probesize 1000000 -rw_timeout 5000000 -use_wallclock_as_timestamps 1
          roles:
            - detect
            - record
    detect:
      width: 1280
      height: 720
      fps: 5

    record:
      enabled: true
      retain:
        days: 2
        mode: motion
      events:
        pre_capture: 5   # seconds before motion
        post_capture: 5  # seconds after motion

    snapshots:
      enabled: true
      timestamp: true
      bounding_box: true
      retain:
        default: 2     # keep snapshots for 2 days
```

This config is used for testing an http stream with an iphone running 
ip camera lite. The additional input args are used to turn off gpu 
accleration since its not supported by http protocol.

Here is a config that uses RTSP instead of HTTP. This is
preferred if the camera supports it.

config.yaml with RTSP:
```yaml
mqtt:
  enabled: false

cameras:
  iphone_camera:
    ffmpeg:
      hwaccel_args: preset-nvidia-h264
      inputs:
        - path: rtsp://admin:admin@192.168.1.205:8554/live
          input_args: preset-rtsp-restream
          roles:
            - detect
            - record

    detect:
      width: 1280
      height: 720
      fps: 5

    record:
      enabled: true
      retain:
        days: 2
        mode: motion
      events:
        pre_capture: 5   # seconds before motion
        post_capture: 5  # seconds after motion

    snapshots:
      enabled: true
      timestamp: true
      bounding_box: true
      retain:
        default: 2     # keep snapshots for 2 days
```