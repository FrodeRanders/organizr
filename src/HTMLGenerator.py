from os import path

def generate_html(topic_dict, output_path="output/html/index.html"):
    html_content = "<html>\n<meta charset=\"UTF-8\">\n<head><title>PDF Topics</title></head>\n<body>\n"

    for topic, pdfs in topic_dict.items():
        html_content += f"<h2>{topic}</h2>\n<ul>\n"
        for pdf_file in pdfs:
            name = path.basename(pdf_file)
            html_content += f"  <li><a href='{pdf_file}'>{name}</a></li>\n"
        html_content += "</ul>\n"

    html_content += "</body>\n</html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

