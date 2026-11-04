#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公开阅读站构建入口（由私有研究库发布闸门生成，请勿在公开库手工修改）。
复用 tools/core/build_site.py 引擎，只展示实际发布的模块，并替换站点标题。

用法：python content/tools/build_public_site.py [输出目录，默认 ../_site]
"""
import json
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CONTENT / "tools" / "core"))

import build_site as bs  # noqa: E402

info_path = CONTENT.parent / "PUBLISH_INFO.json"
info = json.loads(info_path.read_text(encoding="utf-8")) if info_path.exists() else {}

# 只保留实际包含文章的模块
bs.MODULES_META = [m for m in bs.MODULES_META if any((CONTENT / m["dir"]).rglob("*.md"))]

out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (CONTENT.parent / "_site")
bs.build_site(out)

title = info.get("site_title")
idx = out / "index.html"
html = idx.read_text(encoding="utf-8")
if title:
    for name in ("manifest.json", "manifest.js"):
        p = out / "data" / name
        txt = p.read_text(encoding="utf-8")
        txt = re.sub(r'"siteTitle": "[^"]*"', f'"siteTitle": "{title}"', txt, count=1)
        p.write_text(txt, encoding="utf-8")
    html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)

# 版权与反 AI 训练声明（meta），以及页脚授权声明
meta = (
    '\n  <meta name="robots" content="index, follow, noai, noimageai">'
    '\n  <meta name="copyright" content="© 徐时言 · CC BY-NC-ND 4.0 · 禁止商用与 AI 训练">'
)
if 'name="copyright"' not in html:
    html = html.replace("<head>", "<head>" + meta, 1)
notice = info.get("footer_notice")
if notice and "footer-license" not in html:
    html = html.replace(
        '<div class="footer-meta">',
        '<div class="footer-license" style="font-size:12px;opacity:.85;margin:6px 0;line-height:1.7">'
        f"{notice}</div>\n        " + '<div class="footer-meta">',
        1,
    )
idx.write_text(html, encoding="utf-8")

print(f"[public-site] 完成：{out}（模块 {len(bs.MODULES_META)} 个，来源提交 {info.get('source_commit', '?')}）")
