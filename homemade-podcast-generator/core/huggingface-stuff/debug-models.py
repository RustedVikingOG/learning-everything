"""Debug script to understand list_models() data structure"""

from huggingface_hub import list_models, HfApi

print("\n=== Checking what list_models() returns ===\n")

models = list(list_models(
    pipeline_tag="text-to-speech",
    full=True,
    limit=5
))

for i, model in enumerate(models[:3]):
    print(f"{i+1}. Model: {model.id}")
    print(f"   pipeline_tag: {model.pipeline_tag}")
    print(f"   card_data type: {type(model.card_data)}")
    print(f"   card_data: {model.card_data}")
    if model.card_data:
        print(f"   card_data.license: {getattr(model.card_data, 'license', 'N/A')}")
    print()

print("\n=== Checking HfApi.model_info() ===\n")

api = HfApi()
info = api.model_info("hexgrad/Kokoro-82M")

print(f"Model: {info.id}")
print(f"pipeline_tag: {info.pipeline_tag}")
print(f"card_data type: {type(info.card_data)}")
print(f"card_data: {info.card_data}")
if info.card_data:
    print(f"card_data.license: {getattr(info.card_data, 'license', 'N/A')}")
