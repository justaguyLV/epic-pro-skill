#!/usr/bin/env python3
"""Epic Pro audio generator: thin CLI over open-source models.
  tts   : Kokoro-82M (Apache-2.0)      pip install kokoro soundfile
  sfx   : AudioCraft AudioGen (MIT code, CC-BY-NC weights)  pip install audiocraft
  music : AudioCraft MusicGen          pip install audiocraft
  bark  : Suno Bark (MIT)              pip install git+https://github.com/suno-ai/bark.git
Examples:
  python audio_gen.py tts  "Hello world" out.wav --voice af_heart
  python audio_gen.py sfx  "thunder and heavy rain" out.wav --seconds 6
  python audio_gen.py music "epic orchestral trailer" out.wav --seconds 15
  python audio_gen.py bark "[laughs] this is epic" out.wav
"""
import argparse, sys

def tts(a):
    from kokoro import KPipeline; import soundfile as sf, numpy as np
    p = KPipeline(lang_code=a.lang)
    audio = np.concatenate([x[2] for x in p(a.text, voice=a.voice)])
    sf.write(a.out, audio, 24000)

def audiocraft(a, kind):
    from audiocraft.models import AudioGen, MusicGen
    from audiocraft.data.audio import audio_write
    m = AudioGen.get_pretrained("facebook/audiogen-medium") if kind == "sfx" else MusicGen.get_pretrained("facebook/musicgen-small")
    m.set_generation_params(duration=a.seconds)
    wav = m.generate([a.text])
    audio_write(a.out.rsplit(".", 1)[0], wav[0].cpu(), m.sample_rate, strategy="loudness")

def bark(a):
    from bark import SAMPLE_RATE, generate_audio, preload_models
    from scipy.io.wavfile import write
    preload_models(); write(a.out, SAMPLE_RATE, generate_audio(a.text))

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("mode", choices=["tts", "sfx", "music", "bark"])
ap.add_argument("text"); ap.add_argument("out")
ap.add_argument("--voice", default="af_heart"); ap.add_argument("--lang", default="a")
ap.add_argument("--seconds", type=float, default=5)
a = ap.parse_args()
{"tts": tts, "bark": bark}.get(a.mode, lambda x: audiocraft(x, a.mode))(a)
print("saved", a.out)
