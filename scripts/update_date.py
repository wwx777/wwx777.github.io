#!/usr/bin/env python3
"""Stamp the actual publishing commit date, using Europe/Paris."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

page = Path(__file__).resolve().parents[1] / 'index.html'
today = datetime.now(ZoneInfo('Europe/Paris'))
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
label = f'{months[today.month - 1]} {today.day}, {today.year}'
source = page.read_text()
updated, count = re.subn(r'<time id="last-updated" datetime="[^"]+">[^<]+</time>',
    f'<time id="last-updated" datetime="{today:%Y-%m-%d}">{label}</time>', source)
if count != 1:
    raise SystemExit('Expected exactly one last-updated date.')
if updated != source:
    page.write_text(updated)
