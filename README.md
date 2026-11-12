# Ghostty App Icons

<p align="center">
  <a href="./icons/tile/ghostty-tile-original-dark.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-original-dark.png" alt="Original Dark" width="128" height="128"></a>
  <a href="./icons/tile/ghostty-tile-original-light.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-original-light.png" alt="Original Light" width="128" height="128"></a>
</p>

Unofficial macOS app icons based on the [Ghostty logo](https://ghostty.org/ghostty-logo.svg).

## Installation

1. Download an `.icns` file and copy it to `~/.config/ghostty/icons/`. This example uses the Graphite Dark tile.

   ```sh
   mkdir -p ~/.config/ghostty/icons
   cp ~/Downloads/ghostty-tile-graphite-dark.icns ~/.config/ghostty/icons/
   ```

2. Edit your Ghostty config file (typically `~/.config/ghostty/config.ghostty`) to select the installed icon.

   ```ini
   macos-icon = custom
   macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-graphite-dark.icns
   ```

3. Reload Ghostty’s configuration.

Ghostty 1.4 supports custom icons in the Dock, app switcher, and Finder. Finder may need a view refresh to show the new icon. See [Ghostty icon settings](https://ghostty.org/docs/config/reference#macos-custom-icon) and [Ghostty 1.4 release notes](https://ghostty.org/docs/install/release-notes/1-4-0).

### Switch icons with light and dark mode

Download the **Original Light** and **Original Dark** Tile icons from [Downloads](#downloads) and copy both files to `~/.config/ghostty/icons/`. This example pairs Original Light with the Catppuccin Latte terminal theme in Light Mode and Original Dark with Catppuccin Mocha in Dark Mode.

Make local copies of the bundled [Catppuccin Latte theme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/ghostty/Catppuccin%20Latte) and [Catppuccin Mocha theme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/ghostty/Catppuccin%20Mocha).

```sh
mkdir -p ~/.config/ghostty/themes
cp -n "/Applications/Ghostty.app/Contents/Resources/ghostty/themes/Catppuccin Latte" ~/.config/ghostty/themes/"Catppuccin Latte with Icon"
cp -n "/Applications/Ghostty.app/Contents/Resources/ghostty/themes/Catppuccin Mocha" ~/.config/ghostty/themes/"Catppuccin Mocha with Icon"
```

Set `macos-custom-icon` in each local theme file.

**Light Mode** — `~/.config/ghostty/themes/Catppuccin Latte with Icon`

```ini
macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-original-light.icns
```

**Dark Mode** — `~/.config/ghostty/themes/Catppuccin Mocha with Icon`

```ini
macos-custom-icon = ~/.config/ghostty/icons/ghostty-tile-original-dark.icns
```

In `~/.config/ghostty/config.ghostty`, select the two themes and remove or comment out any global `macos-custom-icon` setting, which takes precedence over the theme files.

```ini
macos-icon = custom
theme = light:Catppuccin Latte with Icon,dark:Catppuccin Mocha with Icon
```

Reload Ghostty to apply the changes. See [Ghostty light and dark themes](https://ghostty.org/docs/features/theme#separate-light-and-dark-themes).

## Downloads

### Cutouts

<table>
  <thead>
    <tr><th scope="col">Theme</th><th colspan="4" scope="colgroup">Downloads</th></tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Original</th>
      <td colspan="4" align="center"><a href="./icons/cutout/ghostty-cutout-original.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-original.png" alt="Original Cutout" width="128" height="128"><br>Original Cutout</a></td>
    </tr>
    <tr>
      <th scope="row">Graphite</th>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-graphite-light.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-graphite-light.png" alt="Graphite Light Cutout" width="128" height="128"><br>Light</a></td>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-graphite-dark.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-graphite-dark.png" alt="Graphite Dark Cutout" width="128" height="128"><br>Dark</a></td>
    </tr>
    <tr>
      <th scope="row">Black &amp; White</th>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-white.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-white.png" alt="White Cutout" width="128" height="128"><br>White</a></td>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-black.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-black.png" alt="Black Cutout" width="128" height="128"><br>Black</a></td>
    </tr>
    <tr>
      <th scope="row">Catppuccin</th>
      <td align="center"><a href="./icons/cutout/ghostty-cutout-catppuccin-latte.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-latte.png" alt="Catppuccin Latte Cutout" width="128" height="128"><br>Latte</a></td>
      <td align="center"><a href="./icons/cutout/ghostty-cutout-catppuccin-frappe.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-frappe.png" alt="Catppuccin Frappé Cutout" width="128" height="128"><br>Frappé</a></td>
      <td align="center"><a href="./icons/cutout/ghostty-cutout-catppuccin-macchiato.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-macchiato.png" alt="Catppuccin Macchiato Cutout" width="128" height="128"><br>Macchiato</a></td>
      <td align="center"><a href="./icons/cutout/ghostty-cutout-catppuccin-mocha.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-catppuccin-mocha.png" alt="Catppuccin Mocha Cutout" width="128" height="128"><br>Mocha</a></td>
    </tr>
    <tr>
      <th scope="row">Café</th>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-cafe-latte.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-cafe-latte.png" alt="Café Latte Cutout" width="128" height="128"><br>Latte</a></td>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-cafe-espresso.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-cafe-espresso.png" alt="Café Espresso Cutout" width="128" height="128"><br>Espresso</a></td>
    </tr>
    <tr>
      <th scope="row">Material</th>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-material-light.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-material-light.png" alt="Material Light Cutout" width="128" height="128"><br>Light</a></td>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-material-dark.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-material-dark.png" alt="Material Dark Cutout" width="128" height="128"><br>Dark</a></td>
    </tr>
    <tr>
      <th scope="row">Cute</th>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-cute-by-day.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-cute-by-day.png" alt="Cute by Day Cutout" width="128" height="128"><br>Cute by Day</a></td>
      <td colspan="2" align="center"><a href="./icons/cutout/ghostty-cutout-cute-by-night.icns?raw=true"><img src="./icons/cutout/previews/ghostty-cutout-cute-by-night.png" alt="Cute by Night Cutout" width="128" height="128"><br>Cute by Night</a></td>
    </tr>
  </tbody>
</table>

### Tiles

<table>
  <thead>
    <tr><th scope="col">Theme</th><th colspan="4" scope="colgroup">Downloads</th></tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Original</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-original-light.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-original-light.png" alt="Original Light Tile" width="128" height="128"><br>Light</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-original-dark.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-original-dark.png" alt="Original Dark Tile" width="128" height="128"><br>Dark</a></td>
    </tr>
    <tr>
      <th scope="row">Graphite</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-graphite-light.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-graphite-light.png" alt="Graphite Light Tile" width="128" height="128"><br>Light</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-graphite-dark.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-graphite-dark.png" alt="Graphite Dark Tile" width="128" height="128"><br>Dark</a></td>
    </tr>
    <tr>
      <th scope="row">Black &amp; White</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-white.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-white.png" alt="White Tile" width="128" height="128"><br>White</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-black.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-black.png" alt="Black Tile" width="128" height="128"><br>Black</a></td>
    </tr>
    <tr>
      <th scope="row">Catppuccin</th>
      <td align="center"><a href="./icons/tile/ghostty-tile-catppuccin-latte.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-catppuccin-latte.png" alt="Catppuccin Latte Tile" width="128" height="128"><br>Latte</a></td>
      <td align="center"><a href="./icons/tile/ghostty-tile-catppuccin-frappe.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-catppuccin-frappe.png" alt="Catppuccin Frappé Tile" width="128" height="128"><br>Frappé</a></td>
      <td align="center"><a href="./icons/tile/ghostty-tile-catppuccin-macchiato.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-catppuccin-macchiato.png" alt="Catppuccin Macchiato Tile" width="128" height="128"><br>Macchiato</a></td>
      <td align="center"><a href="./icons/tile/ghostty-tile-catppuccin-mocha.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-catppuccin-mocha.png" alt="Catppuccin Mocha Tile" width="128" height="128"><br>Mocha</a></td>
    </tr>
    <tr>
      <th scope="row">Café</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-cafe-latte.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-cafe-latte.png" alt="Café Latte Tile" width="128" height="128"><br>Latte</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-cafe-espresso.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-cafe-espresso.png" alt="Café Espresso Tile" width="128" height="128"><br>Espresso</a></td>
    </tr>
    <tr>
      <th scope="row">Material</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-material-light.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-material-light.png" alt="Material Light Tile" width="128" height="128"><br>Light</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-material-dark.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-material-dark.png" alt="Material Dark Tile" width="128" height="128"><br>Dark</a></td>
    </tr>
    <tr>
      <th scope="row">Cute</th>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-cute-by-day.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-cute-by-day.png" alt="Cute by Day Tile" width="128" height="128"><br>Cute by Day</a></td>
      <td colspan="2" align="center"><a href="./icons/tile/ghostty-tile-cute-by-night.icns?raw=true"><img src="./icons/tile/previews/ghostty-tile-cute-by-night.png" alt="Cute by Night Tile" width="128" height="128"><br>Cute by Night</a></td>
    </tr>
  </tbody>
</table>
