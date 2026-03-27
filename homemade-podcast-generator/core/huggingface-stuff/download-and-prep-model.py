"""
Download and prepare TTS models from Hugging Face Hub.
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
from huggingface_hub import snapshot_download, HfApi, hf_hub_download


# Get the downloads folder (same directory as this script)
DOWNLOADS_DIR = Path(__file__).parent / "downloads"
DOWNLOADS_DIR.mkdir(exist_ok=True)


def download_model(
    model_id: str,
    cache_dir: Optional[str] = None,
    token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Download a Hugging Face model to the downloads folder.
    
    Args:
        model_id: Model ID (e.g., "hexgrad/Kokoro-82M")
        cache_dir: Optional custom cache directory (defaults to downloads folder)
        token: Optional Hugging Face API token for gated models
    
    Returns:
        Dictionary with download status and model path
    """
    if cache_dir is None:
        cache_dir = str(DOWNLOADS_DIR / model_id.replace("/", "_"))
    
    try:
        print(f"\n{'='*80}")
        print(f"Downloading model: {model_id}")
        print(f"Cache directory: {cache_dir}")
        print(f"{'='*80}\n")
        
        # Use snapshot_download to get all model files
        model_path = snapshot_download(
            repo_id=model_id,
            cache_dir=cache_dir,
            token=token,
            resume_download=True,  # Resume if interrupted
            force_download=False,  # Don't re-download if already cached
        )
        
        print(f"\n{'='*80}")
        print(f"✅ Model downloaded successfully!")
        print(f"   Location: {model_path}")
        print(f"{'='*80}\n")
        
        # Get model info
        api = HfApi()
        info = api.model_info(model_id)
        
        return {
            "status": "success",
            "model_id": model_id,
            "path": model_path,
            "size_bytes": sum(
                f.size for f in info.siblings if f.blob_id
            ) if hasattr(info, "siblings") else "unknown",
            "license": getattr(info.card_data, "license", "unknown") if info.card_data else "unknown",
        }
        
    except Exception as e:
        print(f"\n❌ Error downloading model: {e}")
        return {
            "status": "error",
            "model_id": model_id,
            "error": str(e),
            "path": None,
        }


def list_downloaded_models() -> list:
    """
    List all models currently downloaded in the downloads folder.
    
    Returns:
        List of downloaded model directories
    """
    if not DOWNLOADS_DIR.exists():
        return []
    
    models = []
    
    # HuggingFace stores models in: DOWNLOADS_DIR/ModelName_ModelVersion/models--Author--Repo/snapshots/hash/
    for model_dir in DOWNLOADS_DIR.iterdir():
        if not model_dir.is_dir():
            continue
        
        # Look for model files in the nested structure
        model_files = list(model_dir.glob("**/*.safetensors")) + list(model_dir.glob("**/*.bin")) + list(model_dir.glob("**/*.pt"))
        
        if model_files:
            # Calculate total size
            total_size = sum(f.stat().st_size for f in model_dir.rglob("*") if f.is_file())
            
            models.append({
                "name": model_dir.name,
                "path": str(model_dir),
                "size_mb": total_size / (1024*1024),
                "files": len(model_files),
            })
    
    return models


def get_model_path(model_id: str) -> Optional[str]:
    """
    Get the path to a downloaded model if it exists.
    
    Args:
        model_id: Model ID (e.g., "hexgrad/Kokoro-82M")
    
    Returns:
        Path to model directory, or None if not found
    """
    model_dir_name = model_id.replace("/", "_")
    potential_paths = [
        DOWNLOADS_DIR / model_dir_name,
        DOWNLOADS_DIR / model_id,
    ]
    
    for path in potential_paths:
        if path.exists():
            return str(path)
    
    return None


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python download-and-prep-model.py <model_id>")
        print("Example: python download-and-prep-model.py hexgrad/Kokoro-82M")
        print()
        print("Downloaded models:")
        downloaded = list_downloaded_models()
        if downloaded:
            for model in downloaded:
                print(f"  {model['name']}")
                print(f"    Size: {model['size_mb']:.1f} MB")
                print(f"    Files: {model['files']}")
                print(f"    Path: {model['path']}")
                print()
        else:
            print("  (none yet)")
        sys.exit(0)
    
    model_id = sys.argv[1]
    result = download_model(model_id)
    
    if result["status"] == "success":
        print(f"Model ready at: {result['path']}")
    else:
        print(f"Download failed: {result.get('error', 'unknown error')}")
        sys.exit(1)
