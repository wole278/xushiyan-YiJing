#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公开阅读站构建入口（由私有研究库发布闸门生成，请勿在公开库手工修改）。

复用 tools/core/build_site.py 引擎（研究分支自动发现），并自动完成：
  - 站点标题替换为 PUBLISH_INFO.json 中的 site_title
  - 「核心专论」分类标签按实际发布的分支自动生成（新增分支自动出现）
  - 页脚注入授权声明（年份由闸门自动计算）
  - 版权 meta 标记

用法：python content/tools/build_public_site.py [输出目录，默认 ../_site]
"""
import html as htmllib
import json
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CONTENT / "tools" / "core"))

import build_site as bs  # noqa: E402

info_path = CONTENT.parent / "PUBLISH_INFO.json"
info = json.loads(info_path.read_text(encoding="utf-8")) if info_path.exists() else {}

out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (CONTENT.parent / "_site")
bs.build_site(out)

manifest = json.loads((out / "data" / "manifest.json").read_text(encoding="utf-8"))
modules = manifest.get("modules", [])

# 1) 站点标题
title = info.get("site_title")
if title:
    for name in ("manifest.json", "manifest.js"):
        p = out / "data" / name
        txt = p.read_text(encoding="utf-8")
        txt = re.sub(r'"siteTitle": "[^"]*"', f'"siteTitle": "{title}"', txt, count=1)
        p.write_text(txt, encoding="utf-8")

idx = out / "index.html"
page = idx.read_text(encoding="utf-8")
if title:
    page = re.sub(r"<title>[^<]*</title>", f"<title>{htmllib.escape(title)}</title>", page, count=1)

# 2) 核心专论分类标签：按实际有专论的分支自动生成
featured_mods = {d["module"] for d in manifest.get("featuredPapers", [])}
tabs = ['<button class="feat-tab active" data-cat="all">全部精选成果</button>']
if any(d.get("tier") == 1 for d in manifest.get("featuredPapers", [])):
    tabs.append('<button class="feat-tab" data-cat="tier1">💎 1 级基石 (因子 0.4)</button>')
for m in modules:
    if m["code"] in featured_mods:
        tabs.append(f'<button class="feat-tab" data-cat="{m["code"]}">{m.get("icon", "📚")} {htmllib.escape(m["title"])}</button>')
page = re.sub(
    r'(<div[^>]*id="featuredTabs"[^>]*>)(.*?)(</div>)',
    lambda mo: mo.group(1) + "\n" + "\n".join("        " + t for t in tabs) + "\n      " + mo.group(3),
    page, count=1, flags=re.S,
)

# 3) 版权 meta（公开内容用于分享，不设反爬标记）
years = info.get("copyright_years", "")
author = info.get("author", "")
if 'name="copyright"' not in page:
    page = page.replace(
        "<head>",
        f'<head>\n  <meta name="copyright" content="© {years} {author} · CC BY-NC-ND 4.0">',
        1,
    )

# 4) 页脚授权声明
notice = info.get("footer_notice")
if notice and "footer-license" not in page:
    page = page.replace(
        '<div class="footer-meta">',
        '<div class="footer-license" style="font-size:12px;opacity:.85;margin:6px 0;line-height:1.7">'
        f"{notice}</div>\n        " + '<div class="footer-meta">',
        1,
    )
idx.write_text(page, encoding="utf-8")

print(f"[public-site] 完成：{out}（分支 {len(modules)} 个：{'、'.join(m['title'] for m in modules)}；"
      f"版权 {years}；来源提交 {info.get('source_commit', '?')}）")
