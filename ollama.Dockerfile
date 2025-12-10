# Use the official Ollama image
FROM ollama/ollama

# Pull the gemma2:2b model.
# Note: gemma3 is not available in the Ollama library. Using gemma2:2b as a substitute.
RUN ollama pull mistral:latest 
