"""Export the cutout PNG previews and ICNS files on macOS. Requires Pillow."""

import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image

CUTOUT_DIR = Path(__file__).resolve().parents[1] / "icons" / "cutout"
ICON_SIZES = (16, 32, 128, 256, 512)  # macOS icon sizes in points


def export_cutout(svg, staging):
    raster = staging / "master.png"
    subprocess.run(
        ["sips", "-s", "format", "png", "-z", "4096", "4096", svg, "--out", raster],
        check=True,
        stdout=subprocess.DEVNULL,
    )

    iconset = staging / f"{svg.stem}.iconset"
    iconset.mkdir()
    with Image.open(raster) as master:
        for points in ICON_SIZES:
            for scale, suffix in ((1, ""), (2, "@2x")):
                pixels = points * scale
                image = master.resize((pixels, pixels), Image.Resampling.LANCZOS)
                image.save(iconset / f"icon_{points}x{points}{suffix}.png")

    preview = staging / "previews" / f"{svg.stem}.png"
    shutil.copyfile(iconset / "icon_512x512@2x.png", preview)
    icon = staging / f"{svg.stem}.icns"
    subprocess.run(["iconutil", "-c", "icns", iconset, "-o", icon], check=True)
    return preview, icon


def main():
    svgs = sorted((CUTOUT_DIR / "svg").glob("ghostty-cutout-*.svg"))
    if not svgs:
        raise SystemExit(f"No cutout SVGs found in {CUTOUT_DIR / 'svg'}")

    with TemporaryDirectory(dir=CUTOUT_DIR) as temp:
        staging = Path(temp)
        (staging / "previews").mkdir()
        outputs = []
        for svg in svgs:
            outputs.extend(export_cutout(svg, staging))

        (CUTOUT_DIR / "previews").mkdir(exist_ok=True)
        updated = 0
        for output in outputs:
            destination = CUTOUT_DIR / output.relative_to(staging)
            if not destination.exists() or destination.read_bytes() != output.read_bytes():
                output.replace(destination)
                updated += 1

    print(f"Exported {len(svgs)} previews and {len(svgs)} ICNS files ({updated} files updated).")


if __name__ == "__main__":
    main()
