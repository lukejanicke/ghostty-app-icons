# Ghostty App Icons

<p align="center">
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-graphite-original.icns"><img src="./icons/tile/previews/ghostty-tile-graphite-original.png" alt="Graphite Original" width="128" height="128"></a>
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-latte.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-latte.png" alt="Catppuccin Latte" width="128" height="128"></a>
  <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-mocha.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-mocha.png" alt="Catppuccin Mocha" width="128" height="128"></a>
</p>

Unofficial macOS app icons based on the [Ghostty logo](https://ghostty.org/ghostty-logo.svg).

## Installation

1. Download an `.icns` file and copy it to `~/.config/ghostty/icons/`. This example uses Graphite Original.

   ```sh
   mkdir -p ~/.config/ghostty/icons
   cp ~/Downloads/ghostty-tile-graphite-original.icns ~/.config/ghostty/icons/
   ```

2. Edit your Ghostty config file (typically `~/.config/ghostty/config.ghostty`) to select the installed icon.

   ```ini
   macos-icon = custom
   macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-graphite-original.icns
   ```

3. Reload Ghostty’s configuration.

Ghostty 1.4 supports custom icons in the Dock, app switcher, and Finder. Finder may need a view refresh to show the new icon. See [Ghostty icon settings](https://ghostty.org/docs/config/reference#macos-custom-icon) and [Ghostty 1.4 release notes](https://ghostty.org/docs/install/release-notes/1-4-0).

### Switch icons with light and dark mode

Install (for example) the Tile **Catppuccin Latte** and **Catppuccin Mocha** icons in `~/.config/ghostty/icons/`. Make local copies of the bundled [Catppuccin Latte theme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/ghostty/Catppuccin%20Latte) and [Catppuccin Mocha theme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/ghostty/Catppuccin%20Mocha).

```sh
mkdir -p ~/.config/ghostty/themes
cp -n "/Applications/Ghostty.app/Contents/Resources/ghostty/themes/Catppuccin Latte" ~/.config/ghostty/themes/"Catppuccin Latte with Icon"
cp -n "/Applications/Ghostty.app/Contents/Resources/ghostty/themes/Catppuccin Mocha" ~/.config/ghostty/themes/"Catppuccin Mocha with Icon"
```

Add the corresponding icon setting to each local theme file.

In `~/.config/ghostty/themes/Catppuccin Latte with Icon` add:
```
macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-catppuccin-latte.icns
```

In `~/.config/ghostty/themes/Catppuccin Mocha with Icon` add:
```
macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-catppuccin-mocha.icns
```

In `~/.config/ghostty/config.ghostty`, select the two themes and remove or comment out any global `macos-custom-icon` setting, which takes precedence over the theme files.

```ini
macos-icon = custom
theme = light:Catppuccin Latte with Icon,dark:Catppuccin Mocha with Icon
```

Reload Ghostty to apply the changes. See [Ghostty light and dark themes](https://ghostty.org/docs/features/theme#separate-light-and-dark-themes).

## Downloads

| Theme | Cutout | Tile |
| --- | :---: | :---: |
| Original | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-original.icns"><img src="./icons/cutout/previews/ghostty-cutout-original.png" alt="Original — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-graphite-original.icns"><img src="./icons/tile/previews/ghostty-tile-graphite-original.png" alt="Graphite Original" width="128" height="128"></a> |
| Black | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-black.icns"><img src="./icons/cutout/previews/ghostty-cutout-black.png" alt="Black — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-black.icns"><img src="./icons/tile/previews/ghostty-tile-black.png" alt="Black — tile" width="128" height="128"></a> |
| White | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-white.icns"><img src="./icons/cutout/previews/ghostty-cutout-white.png" alt="White — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-white.icns"><img src="./icons/tile/previews/ghostty-tile-white.png" alt="White — tile" width="128" height="128"></a> |
| Catppuccin Mocha | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-catppuccin-mocha.icns"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-mocha.png" alt="Catppuccin Mocha — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-mocha.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-mocha.png" alt="Catppuccin Mocha — tile" width="128" height="128"></a> |
| Catppuccin Macchiato | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-catppuccin-macchiato.icns"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-macchiato.png" alt="Catppuccin Macchiato — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-macchiato.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-macchiato.png" alt="Catppuccin Macchiato — tile" width="128" height="128"></a> |
| Catppuccin Frappé | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-catppuccin-frappe.icns"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-frappe.png" alt="Catppuccin Frappé — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-frappe.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-frappe.png" alt="Catppuccin Frappé — tile" width="128" height="128"></a> |
| Catppuccin Latte | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-catppuccin-latte.icns"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-latte.png" alt="Catppuccin Latte — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-catppuccin-latte.icns"><img src="./icons/tile/previews/ghostty-tile-catppuccin-latte.png" alt="Catppuccin Latte — tile" width="128" height="128"></a> |
| Café Espresso | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-cafe-espresso.icns"><img src="./icons/cutout/previews/ghostty-cutout-cafe-espresso.png" alt="Café Espresso — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-cafe-espresso.icns"><img src="./icons/tile/previews/ghostty-tile-cafe-espresso.png" alt="Café Espresso — tile" width="128" height="128"></a> |
| Café Latte | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-cafe-latte.icns"><img src="./icons/cutout/previews/ghostty-cutout-cafe-latte.png" alt="Café Latte — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-cafe-latte.icns"><img src="./icons/tile/previews/ghostty-tile-cafe-latte.png" alt="Café Latte — tile" width="128" height="128"></a> |
| Material Dark | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-material-dark.icns"><img src="./icons/cutout/previews/ghostty-cutout-material-dark.png" alt="Material Dark — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-material-dark.icns"><img src="./icons/tile/previews/ghostty-tile-material-dark.png" alt="Material Dark — tile" width="128" height="128"></a> |
| Material Light | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-material-light.icns"><img src="./icons/cutout/previews/ghostty-cutout-material-light.png" alt="Material Light — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-material-light.icns"><img src="./icons/tile/previews/ghostty-tile-material-light.png" alt="Material Light — tile" width="128" height="128"></a> |
| Cute by Day | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-cute-by-day.icns"><img src="./icons/cutout/previews/ghostty-cutout-cute-by-day.png" alt="Cute by Day — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-cute-by-day.icns"><img src="./icons/tile/previews/ghostty-tile-cute-by-day.png" alt="Cute by Day — tile" width="128" height="128"></a> |
| Cute by Night | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/cutout/ghostty-cutout-cute-by-night.icns"><img src="./icons/cutout/previews/ghostty-cutout-cute-by-night.png" alt="Cute by Night — cutout" width="128" height="128"></a> | <a href="https://raw.githubusercontent.com/lukejanicke/ghostty-app-icons/refs/heads/main/icons/tile/ghostty-tile-cute-by-night.icns"><img src="./icons/tile/previews/ghostty-tile-cute-by-night.png" alt="Cute by Night — tile" width="128" height="128"></a> |

## Source artwork

The [Affinity file](./ghostty-app-icons.af) and [root SVGs](./svg/) contain the original artwork. The [Cutout SVGs](./icons/cutout/svg/) scale the ghost to the full canvas height. The [Tile collection](./icons/tile/) includes an editable [Icon Composer](https://developer.apple.com/icon-composer/) project beside each `.icns` export. Both collections store their PNG previews in a `previews/` folder.
