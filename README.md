# organizr
Organise documents (currently PDF files) based on subject / theme

```
➜  python3.12 -m venv env
➜  source env/bin/activate

➜  python3 -m pip install -r requirements.txt
```

I got some botched embeddings, so in order to remove "empty" cached embeddings I use:
```
➜  cd embedding-cache
➜  find . -maxdepth 1 -type f -size 136c -exec rm -f {} +
```