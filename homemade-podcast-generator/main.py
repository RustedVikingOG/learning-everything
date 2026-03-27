def main():
    """Show installed package versions."""
    import transformers
    import datasets
    import huggingface_hub
    import torch
    
    print("✅ Environment Ready")
    print(f"  transformers:    {transformers.__version__}")
    print(f"  datasets:        {datasets.__version__}")
    print(f"  huggingface_hub: {huggingface_hub.__version__}")
    print(f"  torch:           {torch.__version__}")

if __name__ == "__main__":
    main()
