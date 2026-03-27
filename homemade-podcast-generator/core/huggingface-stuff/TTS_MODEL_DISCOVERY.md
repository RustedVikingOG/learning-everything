# TTS Model Discovery Results

## Summary

Successfully discovered **15 open-source, permissive-license TTS models** from Hugging Face Hub.

### Key Findings

✅ **MIT-Licensed Models Found:**
- `ResembleAI/chatterbox` - 2.2M downloads, 1.5K likes
- `ResembleAI/chatterbox-turbo` - 630 likes
- `microsoft/VibeVoice-1.5B` - 98K downloads, 2.2K likes
- `Aratako/Irodori-TTS-500M` - 68 likes
- `Aratako/Irodori-TTS-500M-v2` - 17 likes

✅ **Apache-2.0-Licensed Models Found:**
- `hexgrad/Kokoro-82M` - **9.2M downloads, 5.8K likes** ⭐ (Most Popular)
- `Qwen/Qwen3-TTS-12Hz-0.6B-Base` - 465K downloads (lightweight!)
- `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` - 620K downloads
- `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` - 968K downloads
- `sesame/csm-1b` - 135K downloads, 2.3K likes
- `OpenMOSS-Team/MOSS-TTS` - 88K downloads, 352 likes
- `FunAudioLLM/Fun-CosyVoice3-0.5B-2512` - 6K downloads
- `YatharthS/LuxTTS` - 7.2K downloads
- `silma-ai/silma-tts` - 26 downloads
- `onnx-community/Kokoro-82M-v1.0-ONNX` - 89K downloads (ONNX format)

## Top Recommendations

### 🥇 Best Overall: `hexgrad/Kokoro-82M`
- **License:** Apache-2.0 (permissive, suitable for open-source)
- **Downloads:** 9.2M (30 days)
- **Likes:** 5,845
- **Size Indicator:** 82M parameters (lightweight)
- **URL:** https://huggingface.co/hexgrad/Kokoro-82M
- **Why:** Most popular, well-maintained, proven in production

### 🥈 Best MIT: `ResembleAI/chatterbox`
- **License:** MIT (explicitly MIT)
- **Downloads:** 2.2M (30 days)
- **Likes:** 1,525
- **URL:** https://huggingface.co/ResembleAI/chatterbox
- **Why:** True MIT license, high community adoption

### 🥉 Best Lightweight: `Qwen/Qwen3-TTS-12Hz-0.6B-Base`
- **License:** Apache-2.0
- **Downloads:** 465K (30 days)
- **Size Indicator:** 0.6B parameters (very small)
- **URL:** https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base
- **Why:** Smallest model, fastest inference

## Implementation Strategy

### Option 1: Use Recommended Model (Kokoro)
```python
from transformers import pipeline

# Load TTS pipeline
tts_pipe = pipeline("text-to-speech", model="hexgrad/Kokoro-82M")

# Generate speech
wav = tts_pipe("This is a test of the text to speech system.", forward_params={"speaker": 0})
```

### Option 2: Lightweight Qwen Model
```python
from transformers import pipeline

tts_pipe = pipeline("text-to-speech", model="Qwen/Qwen3-TTS-12Hz-0.6B-Base")
```

### Option 3: MIT-Licensed Resemble Model
```python
from transformers import pipeline

tts_pipe = pipeline("text-to-speech", model="ResembleAI/chatterbox")
```

## Next Steps

1. ✅ Model discovery complete
2. ⏳ Create TTS inference wrapper with selected model
3. ⏳ Test with podcast script
4. ⏳ Integrate into pipeline: script → TTS → audio
5. ⏳ Build complete podcast generator

## Resources

- Hugging Face Model Hub: https://huggingface.co/models?pipeline_tag=text-to-speech
- Transformers Documentation: https://huggingface.co/docs/transformers/
- TTS Task Guide: https://huggingface.co/tasks/text-to-speech

