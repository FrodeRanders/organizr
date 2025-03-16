from os import path, makedirs

def generate_html(topic_dict, representatives, output_path="output/html/index.html"):
    html_content = """<html>
<meta charset="UTF-8">
<head>
    <title>PDF Topics</title>
</head>
<body>
"""

    # `topic_dict` is a dict with keys = cluster_id, values = list of doc paths
    # `representatives` is a list where representatives[c] is the path for cluster c
    for cluster_id, pdfs in topic_dict.items():
        rep_doc = representatives[cluster_id]
        if rep_doc is not None:
            rep_basename = path.basename(rep_doc)
            rep_html = f"<p>Representative for this cluster: <a href='{rep_doc}'>{rep_basename}</a></p>"
        else:
            rep_html = "<p><i>No representative</i></p>"

        html_content += f"<h2>Cluster {cluster_id}</h2>\n"
        html_content += rep_html + "\n<ul>\n"
        for pdf_file in pdfs:
            name = path.basename(pdf_file)
            html_content += f"  <li><a href='{pdf_file}'>{name}</a></li>\n"
        html_content += "</ul>\n"

    html_content += "</body>\n</html>"

    makedirs(path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)