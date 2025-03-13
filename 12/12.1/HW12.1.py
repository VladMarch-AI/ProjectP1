import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ""
    in_tag = False

    for el in html:
        if el == "<":
            in_tag = True
        elif el == ">":
            in_tag = False
        elif not in_tag:
            cleaned_text += el

    cleaned_text = [el.strip() for el in cleaned_text.splitlines() if el.strip()]
    cleaned_text = '\n'.join(cleaned_text)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)
    print(f"{result_file} is ready!")
