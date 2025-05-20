def render_template(template, context):
    tag = context.get("tag", "div")
    attrs = context.get("attrs", {})

    attrs_str = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    content = template.get("content", " ")
    for key, value in attrs.items():
        content = content.replace(f"{{{{ {key} }}}}", str(value))
    children = template.get("children", [])
    rendered_children = "".join(render_template(child, context) for child in children)
    return f"<{tag} {attrs_str}> {content}{rendered_children}</{tag}>"
