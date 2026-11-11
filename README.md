# Ghostty App Icons

<p align="center">
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-graphite-original.icns"><img src="./icons/modern/previews/ghostty-graphite-original.png" alt="Graphite Original" width="128" height="128"></a>
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-latte.icns"><img src="./icons/modern/previews/ghostty-catppuccin-latte.png" alt="Catppuccin Latte" width="128" height="128"></a>
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-mocha.icns"><img src="./icons/modern/previews/ghostty-catppuccin-mocha.png" alt="Catppuccin Mocha" width="128" height="128"></a>
</p>

Unofficial macOS app icons based on the [Ghostty logo](https://ghostty.org/ghostty-logo.svg). Choose a theme and click its preview in the [download gallery](#downloads).

| Collection | Appearance |
| --- | --- |
| [Borderless](./icons/borderless/) | The ghost silhouette on a transparent canvas. |
| [Rounded](./icons/rounded/) | The original artwork on a flat, light-grey tile. |
| [Modern](./icons/modern/) | Layered Icon Composer designs with a background gradient chosen for each theme. The Original theme is **Graphite Original**. |

## Installation

1. Download the `.icns` file for the theme and collection you want.
2. Copy it into `~/.config/ghostty/icons/`. For Graphite Original, run

   ```sh
   mkdir -p ~/.config/ghostty/icons
   cp ~/Downloads/ghostty-graphite-original.icns ~/.config/ghostty/icons/
   ```

3. Press `Cmd+,` in Ghostty to open its configuration. Set the filename to match your icon.

   ```ini
   macos-icon = custom
   macos-custom-icon = ~/.config/ghostty/icons/ghostty-graphite-original.icns
   ```

4. Save the configuration and press `Cmd+Shift+,` to reload it.

Several collections use the same filename for a given theme. To keep two styles of that theme installed, give each file a distinct name and use that name in your configuration.

Ghostty 1.4 supports custom icons in the Dock, app switcher, and Finder. Finder can take a view refresh to show the new icon. [Ghostty icon settings](https://ghostty.org/docs/config/reference#macos-custom-icon) · [Ghostty 1.4 release notes](https://ghostty.org/docs/install/release-notes/1-4-0)

### Switch icons with light and dark mode

Ghostty can select an icon through its light and dark terminal themes. For example, download the modern Latte and Mocha icons and place them in `~/.config/ghostty/icons/`. Copy your two terminal themes into `~/.config/ghostty/themes/` under distinct names, such as `Catppuccin Latte with Icon` and `Catppuccin Mocha with Icon`. The macOS app bundles its themes in `Ghostty.app/Contents/Resources/ghostty/themes/`.

In the Latte copy, add `macos-custom-icon = ~/.config/ghostty/icons/ghostty-catppuccin-latte.icns`. In the Mocha copy, add `macos-custom-icon = ~/.config/ghostty/icons/ghostty-catppuccin-mocha.icns`. Use these settings in the main configuration and comment out any global `macos-custom-icon` line, which would override both theme files.

```ini
macos-icon = custom
theme = light:Catppuccin Latte with Icon,dark:Catppuccin Mocha with Icon
```

Reload Ghostty to apply the changes. [Ghostty light and dark themes](https://ghostty.org/docs/features/theme#separate-light-and-dark-themes)

## Downloads

| Theme | Borderless | Rounded | Modern |
| --- | :---: | :---: | :---: |
| Original | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-original.icns"><img src="./icons/borderless/previews/ghostty-original.png" alt="Original — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-original.icns"><img src="./icons/rounded/previews/ghostty-original.png" alt="Original — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-graphite-original.icns"><img src="./icons/modern/previews/ghostty-graphite-original.png" alt="Graphite Original" width="128" height="128"></a> |
| Black | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-black.icns"><img src="./icons/borderless/previews/ghostty-black.png" alt="Black — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-black.icns"><img src="./icons/rounded/previews/ghostty-black.png" alt="Black — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-black.icns"><img src="./icons/modern/previews/ghostty-black.png" alt="Black — modern" width="128" height="128"></a> |
| White | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-white.icns"><img src="./icons/borderless/previews/ghostty-white.png" alt="White — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-white.icns"><img src="./icons/rounded/previews/ghostty-white.png" alt="White — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-white.icns"><img src="./icons/modern/previews/ghostty-white.png" alt="White — modern" width="128" height="128"></a> |
| Catppuccin Mocha | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-catppuccin-mocha.icns"><img src="./icons/borderless/previews/ghostty-catppuccin-mocha.png" alt="Catppuccin Mocha — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-catppuccin-mocha.icns"><img src="./icons/rounded/previews/ghostty-catppuccin-mocha.png" alt="Catppuccin Mocha — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-mocha.icns"><img src="./icons/modern/previews/ghostty-catppuccin-mocha.png" alt="Catppuccin Mocha — modern" width="128" height="128"></a> |
| Catppuccin Macchiato | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-catppuccin-macchiato.icns"><img src="./icons/borderless/previews/ghostty-catppuccin-macchiato.png" alt="Catppuccin Macchiato — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-catppuccin-macchiato.icns"><img src="./icons/rounded/previews/ghostty-catppuccin-macchiato.png" alt="Catppuccin Macchiato — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-macchiato.icns"><img src="./icons/modern/previews/ghostty-catppuccin-macchiato.png" alt="Catppuccin Macchiato — modern" width="128" height="128"></a> |
| Catppuccin Frappé | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-catppuccin-frappe.icns"><img src="./icons/borderless/previews/ghostty-catppuccin-frappe.png" alt="Catppuccin Frappé — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-catppuccin-frappe.icns"><img src="./icons/rounded/previews/ghostty-catppuccin-frappe.png" alt="Catppuccin Frappé — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-frappe.icns"><img src="./icons/modern/previews/ghostty-catppuccin-frappe.png" alt="Catppuccin Frappé — modern" width="128" height="128"></a> |
| Catppuccin Latte | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-catppuccin-latte.icns"><img src="./icons/borderless/previews/ghostty-catppuccin-latte.png" alt="Catppuccin Latte — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-catppuccin-latte.icns"><img src="./icons/rounded/previews/ghostty-catppuccin-latte.png" alt="Catppuccin Latte — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-catppuccin-latte.icns"><img src="./icons/modern/previews/ghostty-catppuccin-latte.png" alt="Catppuccin Latte — modern" width="128" height="128"></a> |
| Café Espresso | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-cafe-espresso.icns"><img src="./icons/borderless/previews/ghostty-cafe-espresso.png" alt="Café Espresso — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-cafe-espresso.icns"><img src="./icons/rounded/previews/ghostty-cafe-espresso.png" alt="Café Espresso — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-cafe-espresso.icns"><img src="./icons/modern/previews/ghostty-cafe-espresso.png" alt="Café Espresso — modern" width="128" height="128"></a> |
| Café Latte | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-cafe-latte.icns"><img src="./icons/borderless/previews/ghostty-cafe-latte.png" alt="Café Latte — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-cafe-latte.icns"><img src="./icons/rounded/previews/ghostty-cafe-latte.png" alt="Café Latte — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-cafe-latte.icns"><img src="./icons/modern/previews/ghostty-cafe-latte.png" alt="Café Latte — modern" width="128" height="128"></a> |
| Material Dark | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-material-dark.icns"><img src="./icons/borderless/previews/ghostty-material-dark.png" alt="Material Dark — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-material-dark.icns"><img src="./icons/rounded/previews/ghostty-material-dark.png" alt="Material Dark — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-material-dark.icns"><img src="./icons/modern/previews/ghostty-material-dark.png" alt="Material Dark — modern" width="128" height="128"></a> |
| Material Light | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-material-light.icns"><img src="./icons/borderless/previews/ghostty-material-light.png" alt="Material Light — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-material-light.icns"><img src="./icons/rounded/previews/ghostty-material-light.png" alt="Material Light — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-material-light.icns"><img src="./icons/modern/previews/ghostty-material-light.png" alt="Material Light — modern" width="128" height="128"></a> |
| Cute by Day | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-cute-by-day.icns"><img src="./icons/borderless/previews/ghostty-cute-by-day.png" alt="Cute by Day — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-cute-by-day.icns"><img src="./icons/rounded/previews/ghostty-cute-by-day.png" alt="Cute by Day — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-cute-by-day.icns"><img src="./icons/modern/previews/ghostty-cute-by-day.png" alt="Cute by Day — modern" width="128" height="128"></a> |
| Cute by Night | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/borderless/ghostty-cute-by-night.icns"><img src="./icons/borderless/previews/ghostty-cute-by-night.png" alt="Cute by Night — borderless" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-cute-by-night.icns"><img src="./icons/rounded/previews/ghostty-cute-by-night.png" alt="Cute by Night — rounded" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/modern/ghostty-cute-by-night.icns"><img src="./icons/modern/previews/ghostty-cute-by-night.png" alt="Cute by Night — modern" width="128" height="128"></a> |

### Moonrise

Moonrise is a separate layered design with a cobalt rim and a porcelain face on an indigo gradient. Click its preview to download the icon.

<a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/rounded/ghostty-moonrise.icns"><img src="./icons/rounded/previews/ghostty-moonrise.png" alt="Moonrise" width="128" height="128"></a>

## Source artwork

The [Affinity file](./ghostty-app-icons.af) and [root SVGs](./svg/) contain the original artwork. The [borderless SVGs](./icons/borderless/svg/) scale the ghost to the full canvas height. The rounded and modern collections include an editable `.icon` project beside each `.icns` export, with PNGs in the corresponding `previews/` folder. Open a project in [Icon Composer](https://developer.apple.com/icon-composer/) to edit its layers and appearance settings. The modern collection’s downloadable ICNS files use each project’s default appearance.
