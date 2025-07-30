import yaml

with open("../mkdocs.yml", "r") as f:
    config = yaml.safe_load(f)

new_title = "My New Page"
new_slug = "my_new_page.md"

config["nav"].append({new_title: new_slug})

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f)
