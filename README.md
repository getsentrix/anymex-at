# AltStore Source for AnymeX

Custom AltStore / SideStore repository for [AnymeX](https://github.com/RyanYuuki/AnymeX), an open-source anime, manga, and light novel tracking client with multi-service support (AniList, MyAnimeList, SIMKL).

<p align="center">
  <img src="logo.png" alt="AnymeX Logo" width="120" style="border-radius: 24px;" />
</p>

---

## 🔗 Repository URL

Copy and paste this URL into your sideloading app:

```text
https://getsentrix.github.io/anymex-at/apps.json
```

*(Raw fallback URL: `https://raw.githubusercontent.com/getsentrix/anymex-at/main/apps.json`)*

---

## 📲 How to Add

### SideStore / AltStore
1. Open **SideStore** or **AltStore**.
2. Navigate to the **Sources** tab.
3. Tap the **+** (Add) button in the top corner.
4. Paste the URL: `https://getsentrix.github.io/anymex-at/apps.json`
5. Tap **Add**. AnymeX will now appear in your browse/source list with automatic update notifications!

### Feather / ESign / Scarlet
1. Open the app and go to **Sources / Repositories**.
2. Tap **Add Source**.
3. Paste `https://getsentrix.github.io/anymex-at/apps.json` and confirm.

---

## ⚙️ How It Works

This repository automatically stays up to date with official releases:
- A GitHub Actions workflow runs every 12 hours (and can be triggered manually).
- It queries the official upstream repository ([RyanYuuki/AnymeX](https://github.com/RyanYuuki/AnymeX)) via GitHub API for new releases.
- When a new version with an iOS `.ipa` is published, it updates `apps.json` with the new version number, download link, release notes, and file size.

---

## 📜 Credits

- [RyanYuuki/AnymeX](https://github.com/RyanYuuki/AnymeX) - Developer of AnymeX
- [AltStore](https://altstore.io/) - Sideloading platform & source specifications
