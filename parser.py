def extract_text(soup):
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text_blocks = []

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        content = tag.get_text(strip=True)
        if len(content) > 40:
            text_blocks.append({
                "tag": tag.name,
                "text": content
            })

    return text_blocks
