import os

def generate_html(topic_dict, output_path="output/html/index.html"):
    # Since PDFs are relative cwd
    current_dir = os.getcwd()

    html_content = "<html>\n<meta charset=\"UTF-8\">\n<head><title>PDF Topics</title></head>\n<body>\n"

    for topic, pdfs in topic_dict.items():
        html_content += f"<h2>{topic}</h2>\n<ul>\n"
        for pdf_file in pdfs:
            html_content += f"  <li><a href='{current_dir}/data/pdfs/{pdf_file}'>{pdf_file}</a></li>\n"
        html_content += "</ul>\n"

    html_content += "</body>\n</html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

