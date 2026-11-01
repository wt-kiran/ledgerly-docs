"""Documentation build hook. Single source of truth: release.json. No app dependency."""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parents[1]

def on_config(config):
    release = json.loads((ROOT / 'release.json').read_text())
    config.extra['version_label'] = 'v' + release['version']
    return config

def on_page_markdown(markdown, page, config, files):
    release = json.loads((ROOT / 'release.json').read_text())
    anchor = lambda url, label, css='': f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer" class="{css}">{label}</a>'
    cards=[]
    for key, label in [('macos','macOS'),('windows','Windows')]:
        a=release['assets'][key]
        cards.append(f'''<section class="download-card"><span class="eyebrow">{label}</span><h2>{label} installer</h2><p>{escape(a['requirements'])}</p><p><strong>{escape(a['filename'])}</strong><br>{a['bytes']:,} bytes · {a['bytes']/1024/1024:.2f} MiB</p>{anchor(a['url'], 'Download for '+label, 'md-button md-button--primary')}<p class="checksum-label">SHA-256 · verified {release['verified_on']}</p><code class="checksum">{a['sha256']}</code></section>''')
    values={'version':release['version'],'release_link':anchor(release['release_url'],'GitHub release v'+release['version']), 'download_button':anchor(release['release_url'],'Download Ledgerly', 'md-button md-button--primary'),'download_cards':'<div class="download-grid">'+''.join(cards)+'</div>', 'verification_date':release['verified_on']}
    for key,value in values.items(): markdown=markdown.replace('{{ '+key+' }}',value)
    return markdown

def on_post_page(output, page, config):
    # The application has no separate favicon asset: do not substitute a theme logo.
    import re
    return re.sub(r'<link[^>]+rel="(?:shortcut )?icon"[^>]*>', '', output)
