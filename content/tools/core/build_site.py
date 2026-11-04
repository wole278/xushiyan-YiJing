#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZhouYi-Research 东方雅致学术门户构建器 (build_site.py)
自动扫描 01~07 全部研究目录、zhouyi.json 权威底本与 assets 图版资产，
生成兼具 VitePress 三栏学术阅读体验、六十四卦交互方阵、1/2级成果展台、
Mermaid 流程图、KaTeX 公式与全文检索的静态学术个人主页。

用法:
  python tools/core/build_site.py                 # 构建静态站点至 _site/
  python tools/core/build_site.py --serve         # 构建并启动本地预览服务器 (http://127.0.0.1:8000)
  python tools/core/build_site.py --out _site     # 指定输出目录
"""

import argparse
import hashlib
import http.server
import json
import os
import re
import shutil
import socketserver
import sys
import urllib.parse
import webbrowser
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

MODULES_META = [
    {
        "code": "01",
        "dir": "01 审议体系",
        "title": "01 审议体系",
        "short": "审议体系",
        "icon": "⚖️",
        "subtitle": "学术标准法典 · 384爻实证回测 · 进度台账 · 唯一底本",
        "desc": "全库唯一学术真源：收录《标准 v3.5》、《期刊论文撰写规范》、《文档价值分级体系》、《384爻断辞回测报告》及 64 卦四级审议报告。",
        "default_doc": "01 审议体系/README.md",
    },
    {
        "code": "02",
        "dir": "02 元研究",
        "title": "02 元研究",
        "short": "元研究",
        "icon": "🌌",
        "subtitle": "本体论公理 · 依赖因子 0.4 · 最高理论基石",
        "desc": "关于太极、恒道、三易归源、立业、殷商制度、文物实证、乾坤生息与互卦化生的 8 部元哲学专论，享有向下单向覆盖公理效力。",
        "default_doc": "02 元研究/README.md",
    },
    {
        "code": "03",
        "dir": "03 周易笺注史鉴",
        "title": "03 周易笺注史鉴",
        "short": "周易笺注史鉴",
        "icon": "📖",
        "subtitle": "64 卦权威主母本 · 十翼传文底本 · 一卦一档",
        "desc": "通行本《周易》01 乾卦至 64 未济卦最终权威笺注主文档（含卦解、爻解、典论核验、1644信史史鉴）及 65~72 十翼传文底本。",
        "default_doc": "03 周易笺注史鉴/README.md",
    },
    {
        "code": "04",
        "dir": "04 单卦研究记录",
        "title": "04 单卦研究记录",
        "short": "单卦研究",
        "icon": "🔬",
        "subtitle": "64 卦独立分支档案 · 阶段性深度通考总结",
        "desc": "按一卦一子目录归档 64 卦各阶段的专题研判总结、名家训诂比对与历史唯物主义推演记录。",
        "default_doc": "04 单卦研究记录/2026-10-15_周易分卦解通考备忘.md",
    },
    {
        "code": "05",
        "dir": "05 词义研究记录",
        "title": "05 词义研究记录",
        "short": "词义研究",
        "icon": "🔤",
        "subtitle": "甲骨金文字源 · 全经穷尽式矩阵 · 四重证据训诂",
        "desc": "针对匪寇婚媾、用与勿用、利与不利、贞、帝乙归妹、元亨利贞、包、朋与友、豫等核心范畴的博士/教授级训诂专论。",
        "default_doc": "05 词义研究记录/README.md",
    },
    {
        "code": "06",
        "dir": "06 融合研究记录",
        "title": "06 融合研究记录",
        "short": "融合研究",
        "icon": "⚔️",
        "subtitle": "文明演进法则 · 考古礼器实证 · 历史战略博弈",
        "desc": "融汇历史唯物主义、商周考古实物与古经传注，收录《天泽履文明演进》《四渡赤水》《大过洪灾应对》《藏礼于器》《周公制礼作乐》等专论。",
        "default_doc": "06 融合研究记录/README.md",
    },
    {
        "code": "07",
        "dir": "07 易经模型人事分析",
        "title": "07 易经模型人事分析",
        "short": "易经模型人事分析",
        "icon": "👤",
        "subtitle": "六位时位矩阵 · 全生命周期战略研判专栏",
        "desc": "依托 384 爻时位实证矩阵与生生四判据，对曹操、秦始皇、刘邦、毛泽东、王猛、周恩来等历史人物开展去脸谱化的唯物战略解构。",
        "default_doc": "07 易经模型人事分析/README.md",
    },
]

TIER_1_CIYI = {
    "01_基于唯物辩证原则的易经匪寇与婚媾原意辨析.md",
    "02_周易中用和勿用的词义研究.md",
    "03_周易中利与不利的词义研究.md",
    "04_周易中贞的词义训诂与战略哲学研究.md",
    "06_周易中元亨利贞的词义通考与系统演进哲学研究.md",
}

TIER_1_RONGHE = {
    "01_天泽履从荒泽拓荒秩序丛林到大国破局的文明演进法则.md",
    "03_从大过卦看上古洪水时期的先民应对过程.md",
    "04_藏礼于器_周易中的用器研究.md",
}


MODULE_DIR_RE = re.compile(r"^(\d{2})[ _](.+)$")
DEFAULT_ICON = "📚"


def _readme_positioning(mod_dir: Path) -> str:
    """从分支 README 的「模块定位」行或首段提取一句话简介"""
    readme = mod_dir / "README.md"
    if not readme.exists():
        return ""
    text = readme.read_text(encoding="utf-8")
    m = re.search(r"模块定位\**\s*[:：]\**\s*(.+)", text)
    if m:
        line = m.group(1)
    else:
        line = next((l for l in text.splitlines() if l.strip() and not l.lstrip().startswith(("#", ">", "-", "|", "!"))), "")
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
    return re.sub(r"[*`>_#]", "", line).strip()


def discover_modules(root: Path = None):
    """自动发现研究分支：根目录下「两位编号 + 名称」且含 Markdown 的目录。
    已在 MODULES_META 中登记的沿用其元数据；新分支自动生成默认元数据。"""
    root = root or ROOT_DIR
    known = {m["dir"]: m for m in MODULES_META}
    mods = []
    for p in sorted(root.iterdir()):
        if not p.is_dir():
            continue
        mm = MODULE_DIR_RE.match(p.name)
        if not mm or not any(p.rglob("*.md")):
            continue
        if p.name in known:
            mods.append(known[p.name])
            continue
        code, name = mm.group(1), mm.group(2)
        desc = _readme_positioning(p)
        mods.append({
            "code": code,
            "dir": p.name,
            "title": p.name,
            "short": name,
            "icon": DEFAULT_ICON,
            "subtitle": desc[:40],
            "desc": desc or f"{name}研究分支",
            "default_doc": f"{p.name}/README.md" if (p / "README.md").exists() else "",
        })
    return mods


def get_doc_tier(rel_path: str):
    """根据文档路径判定价值等级 (1~3级) 与核心依赖因子"""
    parts = rel_path.split("/")
    top = parts[0]
    fname = parts[-1]
    if fname == "README.md":
        return 0, 0.0, "模块导览"
    if top == "02 元研究":
        return 1, 0.4, "1级 · 0.4"
    if top == "05 词义研究记录":
        if fname in TIER_1_CIYI:
            return 1, 0.4, "1级 · 0.4"
        return 2, 0.3, "2级 · 0.3"
    if top == "06 融合研究记录":
        if fname in TIER_1_RONGHE:
            return 1, 0.4, "1级 · 0.4"
        return 2, 0.3, "2级 · 0.3"
    if top == "01 审议体系":
        if len(parts) > 1 and parts[1] in ("01_标准与规范", "02_回测与实证"):
            return 2, 0.3, "2级 · 0.3"
        return 3, 0.2, "3级 · 0.2"
    return 3, 0.2, "3级 · 0.2"


def extract_title_and_snippet(md_text: str, fallback_name: str):
    """提取文章主标题与纯文本摘要片段"""
    lines = md_text.splitlines()
    title = fallback_name.replace(".md", "")
    for line in lines[:15]:
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            title = m.group(1).strip()
            break

    # 优先提取【摘要】或 ## 摘要 或核心结论
    abstract_match = re.search(r"(?:【摘要】|##\s*摘要\s*\n+)(.+?)(?:\n\n|\n##|\n---)", md_text, re.S)
    if abstract_match:
        raw = abstract_match.group(1)
    else:
        # 去除代码块、Mermaid、标题、表格分隔线
        body = re.sub(r"```[\s\S]*?```", "", md_text)
        body_lines = []
        for l in body.splitlines():
            s = l.strip()
            if not s or s.startswith("#") or s.startswith("!") or s.startswith("|---") or s.startswith(":---"):
                continue
            if "Notion Page ID" in s or "本地化同步时间" in s:
                continue
            body_lines.append(s)
            if len(" ".join(body_lines)) > 260:
                break
        raw = " ".join(body_lines)

    # 清理 Markdown 标记
    clean = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", raw)
    clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", clean)
    clean = re.sub(r"[>*_`#|~]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return title, clean[:180] + ("…" if len(clean) > 180 else "")


def detect_hexagram_no(rel_path: str):
    """检测文档是否关联特定单卦 (1~64)"""
    parts = rel_path.split("/")
    if parts[0] == "03 周易笺注史鉴":
        m = re.match(r"^(\d{2})_", parts[-1])
        if m:
            no = int(m.group(1))
            if 1 <= no <= 64:
                return no
    elif parts[0] == "04 单卦研究记录" and len(parts) >= 2:
        m = re.match(r"^(\d{2})_", parts[1])
        if m:
            no = int(m.group(1))
            if 1 <= no <= 64:
                return no
    elif parts[0] == "01 审议体系" and "03_审议台账与进展" in rel_path:
        m = re.match(r"^(\d{2})_", parts[-1])
        if m:
            no = int(m.group(1))
            if 1 <= no <= 64:
                return no
    return None


def normalize_markdown_content(md_text: str, current_rel_path: str, all_known_paths: set):
    """
    标准化 Markdown 内部的图片路径与文档跳转链接：
    1. 将 ../assets/xxx 统一重写为 assets/xxx
    2. 将内部 .md 链接统一解析为 #/doc/<rel_path>
    """
    curr_dir = Path(current_rel_path).parent

    # 1. 处理图片 ![alt](url)
    def repl_img(match):
        alt = match.group(1)
        url = match.group(2).strip()
        decoded = urllib.parse.unquote(url)
        if "assets/" in decoded:
            idx = decoded.find("assets/")
            clean_asset = decoded[idx:]
            return f"![{alt}]({clean_asset})"
        return match.group(0)

    md_text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl_img, md_text)

    # 2. 处理普通链接 [text](url)（排除图片）
    def repl_link(match):
        prefix = match.group(1)  # 可能是空或非 '!' 字符
        text = match.group(2)
        url = match.group(3).strip()

        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        decoded = urllib.parse.unquote(url).replace("\\", "/")
        # 剥离锚点
        anchor = ""
        if "#" in decoded:
            decoded, anchor = decoded.split("#", 1)

        # 处理历史遗留 file:/// 链接
        if decoded.startswith("file:///"):
            for mod in MODULES_META:
                mdir = mod["dir"]
                if mdir in decoded:
                    idx = decoded.find(mdir)
                    target_rel = decoded[idx:]
                    if target_rel in all_known_paths:
                        encoded_id = urllib.parse.quote(target_rel)
                        return f"{prefix}[{text}](#/doc/{encoded_id})"
            return f"{prefix}{text}"

        if not decoded.endswith(".md") and not decoded.endswith("/"):
            return match.group(0)

        # 计算相对于仓库根目录的路径
        raw_target = (curr_dir / decoded).as_posix()
        # 规范化 ../ 与 ./
        norm_parts = []
        for part in raw_target.split("/"):
            if part in ("", "."):
                continue
            if part == "..":
                if norm_parts:
                    norm_parts.pop()
            else:
                norm_parts.append(part)
        resolved = "/".join(norm_parts)

        if not resolved.endswith(".md"):
            candidate_readme = f"{resolved}/README.md" if resolved else "README.md"
            if candidate_readme in all_known_paths:
                resolved = candidate_readme

        if resolved in all_known_paths:
            encoded_id = urllib.parse.quote(resolved)
            return f"{prefix}[{text}](#/doc/{encoded_id})"

        return match.group(0)

    md_text = re.sub(r"(^|[^!])\[([^\]]+)\]\(([^)]+)\)", repl_link, md_text)
    return md_text


def build_site(out_dir: Path):
    print(f"[build_site] 正在扫描仓库 01~07 目录并构建静态学术门户 -> {out_dir} ...")
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "data").mkdir(parents=True, exist_ok=True)

    # 1. 复制 assets/ 目录
    src_assets = ROOT_DIR / "assets"
    dst_assets = out_dir / "assets"
    if src_assets.exists():
        shutil.copytree(src_assets, dst_assets)

    # 2. 收集全部 Markdown 文档路径
    all_md_files = []
    root_readme = ROOT_DIR / "README.md"
    if root_readme.exists():
        all_md_files.append(("00", root_readme))

    modules = discover_modules()
    for mod in modules:
        mdir = ROOT_DIR / mod["dir"]
        if mdir.exists():
            for p in sorted(mdir.rglob("*.md")):
                all_md_files.append((mod["code"], p))

    all_known_paths = {p.relative_to(ROOT_DIR).as_posix() for _, p in all_md_files}

    # 3. 解析全部文档并按模块分片存储
    docs_by_mod = {"00": {}, **{m["code"]: {} for m in modules}}
    manifest_docs = []
    hexagram_links = {i: {"master": None, "reviews": [], "records": []} for i in range(1, 65)}

    for mod_code, path in all_md_files:
        rel_path = path.relative_to(ROOT_DIR).as_posix()
        raw_md = path.read_text(encoding="utf-8")
        norm_md = normalize_markdown_content(raw_md, rel_path, all_known_paths)
        title, snippet = extract_title_and_snippet(raw_md, path.name)
        tier, factor, tier_label = get_doc_tier(rel_path)
        hex_no = detect_hexagram_no(rel_path)
        word_count = len(re.sub(r"\s+", "", raw_md))

        docs_by_mod[mod_code][rel_path] = {
            "id": rel_path,
            "title": title,
            "module": mod_code,
            "tier": tier,
            "factor": factor,
            "tierLabel": tier_label,
            "hexNo": hex_no,
            "wordCount": word_count,
            "content": norm_md,
        }

        manifest_docs.append({
            "id": rel_path,
            "name": path.name,
            "title": title,
            "module": mod_code,
            "tier": tier,
            "factor": factor,
            "tierLabel": tier_label,
            "hexNo": hex_no,
            "wordCount": word_count,
            "snippet": snippet,
        })

        if hex_no:
            if mod_code == "03":
                hexagram_links[hex_no]["master"] = rel_path
            elif mod_code == "01":
                hexagram_links[hex_no]["reviews"].append({"id": rel_path, "title": title})
            elif mod_code == "04":
                hexagram_links[hex_no]["records"].append({"id": rel_path, "title": title})

    # 4. 读取 zhouyi.json 构建 64 卦交互式方阵数据
    zhouyi_json_path = ROOT_DIR / "01 审议体系" / "04_核心数据库" / "zhouyi.json"
    hexagrams_data = []
    if zhouyi_json_path.exists():
        raw_zy = json.loads(zhouyi_json_path.read_text(encoding="utf-8"))
        for g in raw_zy:
            no = g["no"]
            lines_bin = []
            for y in g.get("yao", [])[:6]:
                lbl = y.get("label", "")
                lines_bin.append(1 if "九" in lbl else 0)
            struct_clean = g.get("struct", "").replace("-{", "").replace("}-", "")
            unicode_char = chr(0x4DC0 + no - 1)
            hexagrams_data.append({
                "no": no,
                "noStr": f"{no:02d}",
                "name": g["name"],
                "unicode": unicode_char,
                "struct": struct_clean,
                "guaci": g.get("guaci", ""),
                "daxiang": g.get("daxiang", ""),
                "lines": lines_bin,  # [初爻..上爻], 1=阳, 0=阴
                "links": hexagram_links.get(no, {}),
            })

    # 十翼传文 (65~72)
    ten_wings = []
    for item in manifest_docs:
        if item["module"] == "03":
            m = re.match(r"^(6[5-9]|7[0-2])_(.+)\.md$", item["name"])
            if m:
                ten_wings.append({
                    "no": int(m.group(1)),
                    "noStr": m.group(1),
                    "name": m.group(2),
                    "id": item["id"],
                    "title": item["title"],
                    "snippet": item["snippet"],
                })

    # 5. 构建左侧目录树结构 (Sidebar Tree)
    sidebar_tree = []
    for mod in modules:
        mcode = mod["code"]
        mdir = mod["dir"]
        mod_items = [d for d in manifest_docs if d["module"] == mcode]

        if mcode == "01":
            groups = [
                {"title": "📌 体系总览", "items": [d for d in mod_items if d["id"] == f"{mdir}/README.md"]},
                {"title": "📜 01_标准与规范", "items": [d for d in mod_items if "/01_标准与规范/" in d["id"]]},
                {"title": "📊 02_回测与实证", "items": [d for d in mod_items if "/02_回测与实证/" in d["id"]]},
                {
                    "title": "📋 03_看板与价值台账",
                    "items": [
                        d for d in mod_items
                        if "/03_审议台账与进展/" in d["id"] and not re.match(r"^\d{2}_", d["name"]) and not d["name"].startswith("06融合")
                    ],
                },
                {
                    "title": "🗄️ 04_核心数据库校勘",
                    "items": [d for d in mod_items if "/04_核心数据库/" in d["id"]],
                },
                {
                    "title": "📑 64卦与专题四级审议报告",
                    "collapsed": True,
                    "items": [
                        d for d in mod_items
                        if "/03_审议台账与进展/" in d["id"] and (re.match(r"^\d{2}_", d["name"]) or d["name"].startswith("06融合"))
                    ],
                },
            ]
        elif mcode == "03":
            groups = [
                {"title": "📌 主母本库导览", "items": [d for d in mod_items if d["name"] == "README.md"]},
                {
                    "title": "☯️ 周易上经 (01 乾 ~ 30 离)",
                    "items": [d for d in mod_items if d["hexNo"] and 1 <= d["hexNo"] <= 30],
                },
                {
                    "title": "☯️ 周易下经 (31 咸 ~ 64 未济)",
                    "items": [d for d in mod_items if d["hexNo"] and 31 <= d["hexNo"] <= 64],
                },
                {
                    "title": "📜 十翼传文底本 (65 彖 ~ 72 杂卦)",
                    "items": [d for d in mod_items if re.match(r"^(6[5-9]|7[0-2])_", d["name"])],
                },
            ]
        elif mcode == "04":
            groups = [
                {"title": "📌 全书分卦通考备忘", "items": [d for d in mod_items if d["id"].count("/") == 1]},
                {
                    "title": "🔬 上经单卦研究 (01~30卦)",
                    "collapsed": False,
                    "items": [d for d in mod_items if d["hexNo"] and 1 <= d["hexNo"] <= 30],
                },
                {
                    "title": "🔬 下经单卦研究 (31~64卦)",
                    "collapsed": True,
                    "items": [d for d in mod_items if d["hexNo"] and 31 <= d["hexNo"] <= 64],
                },
            ]
        else:
            readme_items = [d for d in mod_items if d["name"] == "README.md"]
            other_items = [d for d in mod_items if d["name"] != "README.md"]
            groups = []
            if readme_items:
                groups.append({"title": "📌 专栏导览与规约", "items": readme_items})
            groups.append({"title": f"{mod['icon']} 专题研究成果 ({len(other_items)}篇)", "items": other_items})

        sidebar_tree.append({
            **mod,
            "count": len(mod_items),
            "groups": groups,
        })

    # 6. 精选 1 级 (0.4) 与 2 级 (0.3) 学术成果展台
    featured_papers = [
        d for d in manifest_docs
        if d["name"] != "README.md" and d["module"] in ("01", "02", "05", "06", "07") and (d["tier"] in (1, 2) or d["module"] == "07")
    ]
    featured_papers.sort(key=lambda x: (x["tier"], x["module"], x["id"]))

    manifest_payload = {
        "siteTitle": "周易笺注、元研究与审议体系",
        "siteSubtitle": "历史唯物主义 · 考古实物研究 · 古经传注研究 三维交叉融合学术门户",
        "stats": {
            "totalDocs": len(manifest_docs),
            "hexagrams": 64,
            "yaos": 384,
            "tier1Count": sum(1 for d in manifest_docs if d["tier"] == 1),
            "tier2Count": sum(1 for d in manifest_docs if d["tier"] == 2),
        },
        "modules": sidebar_tree,
        "hexagrams": hexagrams_data,
        "tenWings": ten_wings,
        "featuredPapers": featured_papers,
        "searchIndex": manifest_docs,
    }

    # 写入 JSON 与 JS 数据分片（兼顾 HTTP fetch 与本地 file:// 直接双击打开）
    manifest_json = json.dumps(manifest_payload, ensure_ascii=False)
    (out_dir / "data" / "manifest.json").write_text(manifest_json, encoding="utf-8")
    (out_dir / "data" / "manifest.js").write_text(f"window.__ZHOUYI_MANIFEST__ = {manifest_json};\n", encoding="utf-8")

    for mod_code, mod_dict in docs_by_mod.items():
        chunk_json = json.dumps(mod_dict, ensure_ascii=False)
        (out_dir / "data" / f"docs_{mod_code}.json").write_text(chunk_json, encoding="utf-8")
        (out_dir / "data" / f"docs_{mod_code}.js").write_text(
            f"window.__ZHOUYI_DOCS_CHUNKS__ = window.__ZHOUYI_DOCS_CHUNKS__ || {{}};\n"
            f"window.__ZHOUYI_DOCS_CHUNKS__['{mod_code}'] = {chunk_json};\n",
            encoding="utf-8",
        )

    # 写入 .nojekyll 确保 GitHub Pages 原样托管静态资源
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    # 生成前端页面与样式脚本
    write_frontend_files(out_dir)
    print(f"[build_site] 构建完成！共索引 {len(manifest_docs)} 篇学术文档、64 卦全息方阵与 {len(featured_papers)} 篇核心专论。")


def write_frontend_files(out_dir: Path):
    """写入东方雅致学术风 HTML / CSS / JS 前端文件"""
    from site_template import INDEX_HTML, PORTAL_CSS, PORTAL_JS
    (out_dir / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    (out_dir / "assets").mkdir(parents=True, exist_ok=True)
    (out_dir / "assets" / "portal.css").write_text(PORTAL_CSS, encoding="utf-8")
    (out_dir / "assets" / "portal.js").write_text(PORTAL_JS, encoding="utf-8")


def serve_site(out_dir: Path, port: int = 8000):
    os.chdir(out_dir)
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://127.0.0.1:{port}"
        print(f"\n======================================================================")
        print(f" 🏛️ 周易研究个人主页本地预览已启动: {url}")
        print(f" 按 Ctrl+C 停止服务")
        print(f"======================================================================\n")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[build_site] 已停止本地预览服务。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="构建周易研究静态个人主页")
    parser.add_argument("--out", default=str(ROOT_DIR / "_site"), help="输出目录路径 (默认: _site)")
    parser.add_argument("--serve", action="store_true", help="构建完成后启动本地预览服务器")
    parser.add_argument("--port", type=int, default=8000, help="本地预览端口 (默认: 8000)")
    args = parser.parse_args()

    target_out = Path(args.out).resolve()
    build_site(target_out)
    if args.serve:
        serve_site(target_out, args.port)
