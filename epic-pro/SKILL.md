---
name: epic-pro
description: Pro video-editing toolkit (Epic Pro). Use for any video/montage/reel/short-form editing request (مونتاج، انتقالات، مؤثرات صوتية، خطوط، فيديو سينمائي): editing instructions, ready-made CC0 sound effects and whooshes, GL/FFmpeg transitions, OFL fonts incl. Arabic, 3D/VFX asset sources, a voice/sound generation tool, and an internet-connected dev environment. Use ready assets from this skill first; do not synthesize assets by hand.
---

# Epic Pro

Rule #1: **use the ready assets in this skill. Never invent, synthesize or fake a sound/transition/font by hand.**
If an asset you need is not here, say so and point to the sources in `references/3d/` or `SOURCES.md`. Do not substitute a made-up one.
Respect licences: everything bundled is CC0 / MIT / OFL (see `licenses/` and `SOURCES.md`).

## 1) Editing instructions -> `references/editing/`
- `master-edit/` : cut/caption/dead-space tools (`tools/*.py`) and the editing workflow.
- `master-virality/`, `master-build/` : hooks, retention, QA/design checklists.
- `take-one/` : studio-style pipeline (brief, storyboard, timing, captions, audio, vertical formats, quality checklist). Start with `SKILL.md`, then `references/timing.md`, `captions.md`, `audio.md`, `vertical.md`, `quality-checklist.md`.
- `remotion-motion-graphics/` : Remotion motion patterns and design rules.
- `video-shotcraft/` : cinematic shot language.
Workflow: read the relevant file(s) first, plan cuts/beats, then build with the assets below.

## 2) Ready assets -> `assets/`
- **Sound effects (CC0):** `assets/sfx/adbertiser-cc0/` (408 wav: whoosh, swish, transition, impact, riser, stinger, glitch, cinematic, UI...). Look up files in its `catalog.json` (name, tags, duration, description). `assets/sfx/freesound-cc0/` (52 mp3 by edit beat: Hooks, Tension, Climax, Reactions, Outro; sources in `SOURCES.md`).
- **Transitions:** `assets/transitions/gl-transitions/*.glsl` (300 MIT GLSL transitions) and `assets/transitions/xfade-easing/` (ready FFmpeg `xfade` expression files: eased/uneased, rgb24/yuv420p, script/inline). Usage: see its README; e.g. `ffmpeg -i a.mp4 -i b.mp4 -filter_complex "xfade=transition=custom:duration=1:offset=4:expr=..."`.
- **Fonts (OFL):** `assets/fonts/<family>/` Bebas Neue, Anton, Oswald, Montserrat, Poppins, Orbitron, Cinzel, Bangers, Bungee, Russo One, Teko, Righteous, Archivo Black, Black Ops One, Permanent Marker and Arabic: Cairo, Tajawal, Almarai, Changa, Lalezar, Reem Kufi, El Messiri, Amiri.
Pick by mood: whoosh/swish for cuts, impact/stinger for hits, riser before drops, glitch for tech.

## 3) 3D / legendary footage -> `references/3d/`
`3d-resources-index_CC0.md` is a curated CC0 index of free 3D models, HDRIs, textures and stock sources (Poly Haven, Sketchfab CC0, Blender assets). No openly-licensed 3D video clips are bundled; download from those sources, check the licence on each page, and keep a credit line.

## 4) Voice / sound generation tool -> `tools/audio_gen.py`
CLI wrapper around open models (Kokoro TTS, Bark, AudioCraft AudioGen/MusicGen). Run `python tools/audio_gen.py --help`. Needs a GPU runtime (e.g. Colab). Note: AudioCraft model weights are CC-BY-NC (non-commercial).

## 5) Internet-connected dev environment -> `tools/devenv/`
`setup_codeserver.sh` installs code-server (VS Code in the browser) and exposes it through a Cloudflare quick tunnel; works on Colab/VPS. See `tools/devenv/README.md`.
