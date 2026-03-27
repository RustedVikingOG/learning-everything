# Model Download & Preparation Guide

## Overview

The `download-and-prep-model.py` script handles downloading TTS models from Hugging Face Hub to a local `downloads` folder for fast, offline use.

## Features

✅ **Download Models** - Fetch any TTS model from Hugging Face Hub  
✅ **Resume Downloads** - Automatically resume interrupted downloads  
✅ **List Downloaded** - See which models you have locally with sizes  
✅ **Get Model Path** - Programmatically access downloaded model paths  
✅ **Error Handling** - Graceful error messages and recovery  

## Usage

### Download a Model

```bash
# Command line
uv run python core/huggingface-stuff/download-and-prep-model.py hexgrad/Kokoro-82M

# Python code
from download_and_prep_model import download_model

result = download_model("hexgrad/Kokoro-82M")
if result["status"] == "success":
    print(f"Model at: {result['path']}")
```

### List Downloaded Models

```bash
uv run python core/huggingface-stuff/download-and-prep-model.py

# Output:
# Downloaded models:
#   Qwen_Qwen3-TTS-12Hz-0.6B-Base
#     Size: 4799.1 MB
#     Files: 2
#     Path: /path/to/downloads/Qwen_Qwen3-TTS-12Hz-0.6B-Base
```

### Get Model Path Programmatically

```python
from download_and_prep_model import get_model_path

path = get_model_path("hexgrad/Kokoro-82M")
if path:
    print(f"Model is at: {path}")
else:
    print("Model not downloaded yet")
```

## Currently Downloaded Models

✅ **Qwen/Qwen3-TTS-12Hz-0.6B-Base** (4.8 GB)
   - Lightweight, fast, Apache-2.0 license
   - Perfect for testing and development

## Recommended Models to Download

Based on our earlier discovery, here are the best options:

- **hexgrad/Kokoro-82M** - Most popular (9.2M downloads)
- **ResembleAI/chatterbox** - MIT licensed (2.2M downloads)
- **Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign** - Good quality (620K downloads)

## Next Steps

1. ✅ Model discovery complete
2. ✅ Download functionality added
3. ⏳ Create TTS inference wrapper
4. ⏳ Test audio generation  
5. ⏳ Integrate into podcast pipeline

## Examples

Download the most popular model:
```bash
uv run python core/huggingface-stuff/download-and-prep-model.py hexgrad/Kokoro-82M
```

Download the MIT-licensed option:
```bash
uv run python core/huggingface-stuff/download-and-prep-model.py ResembleAI/chatterbox
```

Download a lightweight option:
```bash
uv run python core/huggingface-stuff/download-and-prep-model.py Qwen/Qwen3-TTS-12Hz-0.6B-Base
```
