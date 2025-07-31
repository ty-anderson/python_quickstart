def get_top_level_keys(data):
    """
    Given a list of dicts with 'Parent > Child' keys, return unique top-level keys.
    """
    top_levels = set()
    for item in data:
        for key in item.keys():
            top = key.split(" > ")[0]
            top_levels.add(top)
    return sorted(top_levels)


def flatten_to_rows(d, parent_key=""):
    """
    Flatten nested dicts/lists into a flat list of dicts.
    Each resulting dict has only one key-value pair, where the key includes its parent(s).
    """
    rows = []

    if isinstance(d, dict):
        for k, v in d.items():
            full_key = f"{parent_key} > {k}" if parent_key else k
            if isinstance(v, dict):
                rows.extend(flatten_to_rows(v, full_key))
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        rows.extend(flatten_to_rows(item, full_key))
                    else:
                        rows.append({full_key: item})
            else:
                rows.append({full_key: v})

    elif isinstance(d, list):
        for item in d:
            rows.extend(flatten_to_rows(item, parent_key))

    return rows


def add_to_nav(nav, title, path, folder=None):
    """
    Adds a new page to nav structure.
    - If folder is provided, add under that group.
    - If folder not found, create new top-level group.
    """
    entry = {title: path}

    if folder:
        # Try to find the folder group
        for i, item in enumerate(nav):
            if isinstance(item, dict) and folder in item:
                # Found folder group
                if isinstance(item[folder], list):
                    item[folder].append(entry)
                else:
                    item[folder] = [entry]
                return
        # If folder not found, create it
        nav.append({folder: [entry]})
    else:
        # No folder specified, add to top
        nav.append(entry)

