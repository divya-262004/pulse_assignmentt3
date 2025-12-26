from parser import extract_text

def extract_modules(pages):
    modules = []
    current_module = None

    for page in pages:
        blocks = extract_text(page["content"])

        for block in blocks:
            if block["tag"] == "h2":
                current_module = {
                    "module": block["text"],
                    "Description": "",
                    "Submodules": {}
                }
                modules.append(current_module)

            elif block["tag"] == "h3" and current_module:
                current_module["Submodules"][block["text"]] = ""

            elif block["tag"] == "p" and current_module:
                if current_module["Description"] == "":
                    current_module["Description"] = block["text"]
                elif current_module["Submodules"]:
                    last_sub = list(current_module["Submodules"].keys())[-1]
                    current_module["Submodules"][last_sub] += " " + block["text"]

    return modules
