"""Generate the flat cutout SVGs from the Original Dark artwork and palettes.json."""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "icons" / "cutout" / "svg"
TEMPLATE_THEME = "original-dark"
SVG_NS = "http://www.w3.org/2000/svg"
ROLES = ("background", "middle", "face", "chevron", "eye")


def named_paths(svg):
    paths = {}
    for role in ROLES:
        layers = svg.findall(f".//*[@id='{role}']")
        if len(layers) != 1:
            raise ValueError(f"Expected one layer named '{role}' in the template SVG")
        shapes = list(layers[0].iter(f"{{{SVG_NS}}}path"))
        if len(shapes) != 1:
            raise ValueError(f"Expected one path in the '{role}' layer")
        paths[role] = shapes[0]
    return paths


def set_fill(path, colour):
    # Affinity puts some fills in inline styles, which override SVG attributes.
    styles = []
    for declaration in path.get("style", "").split(";"):
        if declaration.strip() and declaration.partition(":")[0].strip() != "fill":
            styles.append(declaration)
    if styles:
        path.set("style", ";".join(styles) + ";")
    else:
        path.attrib.pop("style", None)
    path.set("fill", colour)


def main():
    ET.register_namespace("", SVG_NS)
    svg = ET.parse(SVG_DIR / f"ghostty-cutout-{TEMPLATE_THEME}.svg").getroot()
    paths = named_paths(svg)
    svg.set("width", "1024")
    svg.set("height", "1024")
    palettes = json.loads((ROOT / "palettes.json").read_text(encoding="utf-8"))

    with TemporaryDirectory(dir=SVG_DIR) as staging:
        outputs = []
        for theme, palette in palettes.items():
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", theme):
                raise ValueError(f"Invalid theme filename: {theme!r}")
            if palette.keys() != paths.keys():
                raise ValueError(f"Expected these colours for {theme}: {', '.join(ROLES)}")
            if theme == TEMPLATE_THEME:
                continue
            for role, colour in palette.items():
                if not re.fullmatch(r"#[0-9a-fA-F]{6}", colour):
                    raise ValueError(f"Expected a six-digit hex colour for {theme}.{role}")
                set_fill(paths[role], colour)

            output = Path(staging) / f"ghostty-cutout-{theme}.svg"
            output.write_bytes(ET.tostring(svg, encoding="utf-8", xml_declaration=True) + b"\n")
            outputs.append(output)

        for output in outputs:
            output.replace(SVG_DIR / output.name)

    print(f"Generated {len(outputs)} themed cutout SVGs.")


if __name__ == "__main__":
    main()
