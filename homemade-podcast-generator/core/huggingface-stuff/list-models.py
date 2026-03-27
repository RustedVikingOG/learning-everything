"""
Utility to find and list Hugging Face models with specific filters.

Filters include:
- Task (e.g., text-to-speech, text-generation)
- License (e.g., MIT, Apache-2.0)
- Open source requirement
- Downloadable requirement
"""

from typing import Optional, List, Dict, Any
from huggingface_hub import list_models, HfApi


def find_tts_models(
    permissive_licenses_only: bool = True,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Find text-to-speech models from Hugging Face Hub with license filtering.
    
    Note: This fetches detailed info for each model to get license data, which is slower
    but necessary since list_models() doesn't populate card_data.
    
    Args:
        permissive_licenses_only: If True, filter to MIT, Apache, BSD, etc.
        limit: Maximum number of models to return
    
    Returns:
        List of TTS models with metadata, filtered by permissive licenses if requested
    """
    # Permissive licenses we consider appropriate for open-source projects
    permissive_patterns = ["mit", "apache", "bsd", "isc", "unlicense", "mpl"]
    api = HfApi()
    
    try:
        # Get a list of TTS models - fetch more since we'll filter some out
        all_models = list(list_models(
            pipeline_tag="text-to-speech",
            limit=limit * 3  # Fetch more to filter by license
        ))
        
        results = []
        for model in all_models:
            try:
                # Get detailed info including card_data
                info = api.model_info(model.id)
                
                # Extract license info
                license_info = "unknown"
                if info.card_data and hasattr(info.card_data, "license"):
                    license_info = info.card_data.license or "unknown"
                
                # Filter by license if requested
                if permissive_licenses_only:
                    license_lower = str(license_info).lower()
                    is_permissive = any(pattern in license_lower for pattern in permissive_patterns)
                    if not is_permissive:
                        continue
                
                result = {
                    "id": info.id,
                    "author": info.author,
                    "license": license_info,
                    "downloads": info.downloads,
                    "likes": info.likes,
                    "gated": info.gated,
                    "url": f"https://huggingface.co/{info.id}",
                }
                results.append(result)
                
                if len(results) >= limit:
                    break
                    
            except Exception as e:
                # Skip models that error out
                continue
        
        return results
    
    except Exception as e:
        print(f"Error querying Hugging Face Hub: {e}")
        return []


def get_model_info(model_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific model.
    
    Args:
        model_id: Model ID (e.g., "hexgrad/Kokoro-82M")
    
    Returns:
        Dictionary with model details
    """
    try:
        api = HfApi()
        info = api.model_info(model_id)
        
        # Extract license  
        license_info = "unknown"
        if info.card_data and hasattr(info.card_data, "license"):
            license_info = info.card_data.license or "unknown"
        
        return {
            "id": info.id,
            "author": info.author,
            "task": info.pipeline_tag,
            "license": license_info,
            "downloads": info.downloads,
            "likes": info.likes,
            "gated": info.gated,
            "private": info.private,
            "url": f"https://huggingface.co/{info.id}",
        }
    except Exception as e:
        print(f"Error getting model info: {e}")
        return {}


# Example usage
if __name__ == "__main__":
    print("\n" + "="*100)
    print("FINDING PERMISSIVE-LICENSE TTS MODELS")
    print("="*100)
    
    # Find TTS models with permissive licenses
    tts_models = find_tts_models(permissive_licenses_only=True, limit=15)
    
    if tts_models:
        print(f"\nFound {len(tts_models)} TTS models with permissive licenses (MIT, Apache-2.0, BSD, etc.):")
        print("-" * 100)
        for i, model in enumerate(tts_models, 1):
            print(f"\n{i}. {model['id']}")
            print(f"   License: {model['license']}")
            print(f"   Downloads (30d): {model['downloads']:,}")
            print(f"   Likes: {model['likes']:,}")
            print(f"   URL: {model['url']}")
    else:
        print("\nNo permissive-license TTS models found.")
    
    # Get detailed info on recommended models
    print("\n" + "="*100)
    print("DETAILED MODEL INFORMATION")
    print("="*100)
    
    recommended = [
        "hexgrad/Kokoro-82M",
        "ResembleAI/chatterbox",
    ]
    
    for model_id in recommended:
        print(f"\n{model_id}:")
        info = get_model_info(model_id)
        if info:
            for key, value in info.items():
                if key != "url":
                    print(f"  {key}: {value}")
                else:
                    print(f"  {key}: {value}")
        else:
            print(f"  Could not retrieve information")
