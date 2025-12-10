# EthicLab 

This project scope is being change. Now it is evolved to be an ethics experimentation over the texts (tweets in previous scope)

### Large Language Model (LLM)

Offline LLM models using Ollama will be experimented


## Dependency Management 
uv is the new dependency management systems 

## Poetry with uvicorn
poetry run uvicorn autotweet.app:app --reload

## Dockerization

## Deployment
Kubernetes will be used for deployment

## API Interface
http://0.0.0.0:8000/docs

## How to execute

uv run uvicorn src.ethicslab.main:app --reload
## Other API Interface
1. http://0.0.0.0:8000
2. http://0.0.0.0:8000/docs
2. http://0.0.0.0:8000/tweet
3. http://0.0.0.0:8000/health
4. http://0.0.0.0:8000/docs



### Verify Loading
git config --get pull.rebase

(It must print true / false whatever is inside .gitconfig)