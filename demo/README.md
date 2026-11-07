# Demo video (not part of the skill package)

`video/` is a Remotion project: a chat scene where the user types only `/workdocs`, a slide to a browser frame playing a real recording of the six pages, and an end card, with an English voice-over (`video/public/vo-*.m4a`, generated locally with Kokoro-82M, Apache-2.0, voice `af_heart`; see `demo/tts.md`). No marketplace is named in the video.

Rebuild after changing the pages (the recording uses the documentation site of the workmap repo, `tracking/docs`, as a sample; any workdocs site works):

```bash
( cd ../../workmap/tracking && python3 -m http.server 4606 --bind 127.0.0.1 --directory docs & )
playwright-cli open && playwright-cli run-code --filename=demo/record-chrome.js && playwright-cli close
ffmpeg -y -i demo/video/public/chrome.webm -c:v libx264 -pix_fmt yuv420p -r 30 -an demo/video/public/chrome.mp4
cd demo/video && npm install && npx remotion render WorkdocsDemo ../../dist/listing/workdocs-demo.mp4
```

Listing screenshots in `../dist/listing/` come from headless Chrome over copies of the pages with `data-theme` forced on `<html>` (headless Chrome otherwise follows the system theme).
