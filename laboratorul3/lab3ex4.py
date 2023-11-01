def build_xml_element(tag, content, **things):
     xmlElement = f"<{tag}"
     for key, value in things.items():
         xmlElement += f' {key}="{value}"'
     xmlElement += f'>{content}</{tag}>'
     return xmlElement

exemplu = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(exemplu)