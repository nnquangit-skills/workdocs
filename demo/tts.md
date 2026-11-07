# Voice-over (Kokoro-82M, Apache-2.0)

The narration clips in `video/public/vo-*.m4a` are generated locally with [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (hexgrad, Apache License 2.0), voice `af_heart`, 24 kHz, then encoded to AAC with ffmpeg. macOS system voices are not used: Apple's licence allows them only for personal, non-commercial content.

```bash
brew install espeak-ng
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python "kokoro>=0.9.2" soundfile
.venv/bin/python - <<'PY'
import soundfile as sf, numpy as np
from kokoro import KPipeline
pipe = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
text = "Where are we on the project? ..."              # the narration of one scene
audio = np.concatenate([a for _, _, a in pipe(text, voice="af_heart")])
sf.write("vo-chat.wav", audio, 24000)
PY
ffmpeg -y -i vo-chat.wav -c:a aac -b:a 128k video/public/vo-chat.m4a
```

The narration texts are the subtitle cues in `../dist/listing/*.en.srt`.
