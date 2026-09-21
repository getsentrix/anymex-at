import json
import os
import urllib.request
from datetime import datetime, timezone

REPO = "RyanYuuki/AnymeX"
SOURCE_NAME = "AnymeX Community Source"
SOURCE_ID = "com.community.anymex-source"
APP_NAME = "AnymeX"
BUNDLE_ID = "com.ryan.anymex"
DEVELOPER_NAME = "RyanYuuki"
SUBTITLE = "An Open Source Multiservice Tracking Client"
LOCALIZED_DESCRIPTION = (
    "AnymeX is an open-source app for tracking anime, manga, and light novels "
    "across multiple services (AniList, MyAnimeList, SIMKL) with integrated "
    "media streaming and reading support."
)
ICON_URL = "https://raw.githubusercontent.com/getsentrix/anymex-at/main/logo.png"
TINT_COLOR = "FF3B30"

url = f"https://api.github.com/repos/{REPO}/releases/latest"
headers = {"User-Agent": "AltStore-Updater"}
github_token = os.environ.get("GITHUB_TOKEN")
if github_token:
    headers["Authorization"] = f"token {github_token}"

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

version = data.get("tag_name", "").lstrip("v")
release_date = data.get("published_at", datetime.now(timezone.utc).isoformat())
body = data.get("body", "Latest release of AnymeX.")

# Find the iOS .ipa asset
ipa_asset = next(
    (
        a for a in data.get("assets", [])
        if a["name"].lower().endswith(".ipa")
    ),
    None,
)

if not ipa_asset:
    raise SystemExit("No iOS IPA asset found in latest release.")

ipa_url = ipa_asset["browser_download_url"]
size = ipa_asset["size"]

source_data = {
    "name": SOURCE_NAME,
    "identifier": SOURCE_ID,
    "apps": [
        {
            "name": APP_NAME,
            "bundleIdentifier": BUNDLE_ID,
            "developerName": DEVELOPER_NAME,
            "subtitle": SUBTITLE,
            "localizedDescription": LOCALIZED_DESCRIPTION,
            "iconURL": ICON_URL,
            "tintColor": TINT_COLOR,
            "version": version,
            "versionDate": release_date,
            "versionDescription": body,
            "downloadURL": ipa_url,
            "size": size,
        }
    ],
}

with open("apps.json", "w", encoding="utf-8") as f:
    json.dump(source_data, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Successfully generated apps.json for {APP_NAME} v{version}")
