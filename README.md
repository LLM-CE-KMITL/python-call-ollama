# Python calling ollama API

## Install ollama
*  Go to https://ollama.com/download
*  Download and Install

## At Terminal
*   Install a model e.g.
```
ollama run llama3.2
```

## Install ollama for python
```
pip install ollama
```

## Run Python Code
*  Run the file local-ollama.py

## CORS
* Read https://atlassc.net/2024/09/14/how-to-enable-api-for-ollama
* E.g. For MAC, run this command and restart ollama for solving the issue of CORS
```
launchctl setenv OLLAMA_ORIGINS "*"
```

## Reference
*  https://github.com/ollama/ollama/blob/main/docs/api.md
*  https://github.com/ollama/ollama-python
*  https://pypi.org/project/ollama/
