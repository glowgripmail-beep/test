---
name: video-production
description: "Video production: watching/understanding any video and editing or animating videos. Use to watch a video (URL or local file) and answer questions about it — downloads with yt-dlp, extracts frames with ffmpeg, pulls the transcript (captions, local WhisperX or cloud Whisper), or lets Gemini watch it; and to work as a pro video editor for Reels/TikTok — edit footage in CapCut (cuts, zooms, word-synced captions, color, music, SFX) and build motion graphics or fully animated videos. Triggers: /watch, \"watch this video\", \"what's in this video\", \"edit my video\", \"edit this in CapCut\", \"make this a reel\", \"motion graphics\", \"animate this\", \"animated video\", \"תערוך לי סרטון\", \"תערוך בקאפקאט\", \"ערוך את הסרטון הפתוח\", \"תכין לי את זה לריל\", \"תיצור לי אנימציה\", \"סרטון אנימציה\", \"מושן גרפיקס\", \"תצפה בסרטון\"."
---

# Video production

This skill merges two former skills into one topic skill. Each keeps its full original instructions in its own folder; supporting files keep their original relative paths.

| Part | Folder | What it does |
|---|---|---|
| watch | `watch/GUIDE.md` (+ `watch/scripts/`) | Watch a video from a URL or local path and answer questions about it: frames + transcript (local engine) or Google Gemini watching the whole video (gemini engine). MIT-licensed. |
| capcut-video-studio-by-amit-chen | `capcut-video-studio-by-amit-chen/GUIDE.md` | Professional editor / motion designer / sound designer for vertical video: Mode A CapCut edit, Mode B footage + motion graphics inserts, Mode C 100% animated video. |

## Which file to read when

| Task | Read |
|---|---|
| "What's in this video?", summarize / answer questions about a YouTube link or local video, pull a transcript, grab frames at given times | `watch/GUIDE.md` (sections "First run and setup", "Watch and answer") |
| First run of watch in a session, choosing engine (gemini / local), detail level, transcription backend | `watch/GUIDE.md` → "First run and setup" |
| Download failures, missing captions, WhisperX / Groq / OpenAI fallback, security of uploads | `watch/GUIDE.md` → "Transcription and failure handling", "Security and runtime access" |
| Edit footage open in CapCut, cut dead air, punch-ins, captions, color, voice cleanup | `capcut-video-studio-by-amit-chen/GUIDE.md` sections 0-4 |
| CapCut project JSON (bulk/precise edits, timing, transforms) | `capcut-video-studio-by-amit-chen/GUIDE.md` → "CapCut project JSON" |
| Motion graphics, kinetic typography, HyperFrames, custom Playwright render pipeline, RTL/Hebrew text in animation, safe zones | `capcut-video-studio-by-amit-chen/GUIDE.md` sections 5, 6, 7 |
| Music choice, phone-speaker rule, levels, music search terms by video type | `capcut-video-studio-by-amit-chen/GUIDE.md` sections 5a, 5b |
| Sound design (SFX) | `capcut-video-studio-by-amit-chen/GUIDE.md` section 5c |
| Fully animated video from scratch | `capcut-video-studio-by-amit-chen/GUIDE.md` section 8 |
| TikTok version, export, loudness, verification, final report | `capcut-video-studio-by-amit-chen/GUIDE.md` sections 9-12 |
| Analyze a reference/competitor video before editing or writing an ad | `watch/GUIDE.md` first, then the editing guide or the skills listed under "חיבור לסקילים אחרים" in `watch/GUIDE.md` |

Typical combined flow: use **watch** to get the word-level material of a reference video or of the user's own footage (transcript, timestamps, key frames), then **capcut-video-studio-by-amit-chen** to plan and execute the edit.

## Invocation notes

- `watch` was invoked as `/watch` (its body is titled `# /watch`). Its commands use `SKILL_DIR`, which now means the `watch/` folder of this skill (`<video-production>/watch/`); the bundled scripts are at `watch/scripts/`.
- The editing part's original trigger phrases are listed at the top of its GUIDE.md.

## Conflicts between sources

These are places where the two parts give different guidance. They are listed, not resolved; follow the part you are executing.

1. **Installing software.** capcut-video-studio-by-amit-chen: "Check what exists at the start and install missing pieces (npm, pip) where allowed." watch: "Do not use sudo automatically" and "Do not treat silence as permission to install local models or upload audio; the no-key/no-install path remains available."
2. **Asking the user questions.** capcut-video-studio-by-amit-chen: one check-in before executing, then "finish through export without more stops", and "Never hand the user a list of options to pick from." watch: on first run asks the engine question and (local engine) the detail and transcription questions, presenting numbered options.
3. **Source of word timestamps.** capcut-video-studio-by-amit-chen needs word-level timestamps (CapCut auto captions read from the project JSON, or "a transcription tool"). watch's WhisperX fallback runs with "No alignment or diarization", and its transcripts are timestamped segments, so watch output may not give word-level times on its own.
4. **Where the video goes.** watch's gemini engine uploads local or downloaded videos to Google ("Likewise use `--engine local` when the user says the video is private or must not leave the machine"). capcut-video-studio-by-amit-chen keeps everything in the project folder ("Before reporting, confirm nothing was written outside the project folder") but allows connected AI generators and cloud transfers.
