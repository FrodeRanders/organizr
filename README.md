# organizr
Organise documents (currently PDF files) based on subject / theme

Embeddings of PDF files are generated, page by page, and then combined into a total embedding for that document.

Based on these embeddings, the documents are clustered -- currently using KMeans, with a configurable k -- and an HTML document is created as an categorized index of the PDF documents.

For each category, a single PDF document is picked as a representative for that category, by calculating the cosine similarity with the cluster centroid. The reason is that the categories are unnamed (unknown) and any document near the centroid should be a good approximation of the cluster topic.

This seems to work reasonably well, but it is possible to modify the setup:
* by picking different embedding models,
* by clustering by other algorithms than KMeans -- such as hierarchical clustering or density-based clustering

Short how-to setup for running:
```
➜  python3.12 -m venv env
➜  source env/bin/activate
➜  python3 -m pip install -r requirements.txt
```

How-to run this over PDF documents in ~/Documents. An index.html will be created in ~/Documents.
```
➜  python3 Main.py ~/Documents
```

Document embeddings are cached (based on path to PDF document) in a local sub-directory 'embedding-cache', so that a second run will load embeddings from the cache instead of re-running the embedding process.
I got some botched embeddings, possibly due to problems with the PDF files, which may result in "empty" cache-files. 
In order to remove these "empty" cached embeddings I can use (but this is not a necessity):
```
➜  find ./embedding-cache -maxdepth 1 -type f -size 136c -exec rm -f {} +
```