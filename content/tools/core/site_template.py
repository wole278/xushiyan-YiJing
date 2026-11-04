#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZhouYi-Research 东方雅致学术门户前端模板 (site_template.py)
包含完整的 HTML 骨架、宣纸/玄墨双主题 CSS 样式与 VitePress 风格三栏交互逻辑。
"""

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>易经研究、笺注与审议体系 — 东方唯物学术门户</title>
  <meta name="description" content="以历史唯物辩证法为方法、以生生为唯一价值标尺、以四重证据法与384爻实证回测为基准的现代学术级《周易》研究门户。" />
  <!-- Google Fonts: Noto Serif SC & Noto Sans SC -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700;900&display=swap" rel="stylesheet">
  <!-- KaTeX CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <!-- Portal Custom CSS -->
  <link rel="stylesheet" href="assets/portal.css" />
</head>
<body>
  <!-- 顶部导航栏 (VitePress 风格毛玻璃顶栏) -->
  <header class="top-navbar">
    <div class="navbar-inner">
      <div class="navbar-left">
        <button class="mobile-menu-btn" id="mobileMenuBtn" title="展开目录" aria-label="展开目录">☰</button>
        <a href="#/" class="brand-link">
          <span class="brand-seal">易</span>
          <div class="brand-text">
            <span class="brand-title">徐时言-易经研究</span>
            <span class="brand-sub">ZhouYi Research &amp; Review System</span>
          </div>
        </a>
      </div>

      <div class="navbar-search">
        <button class="search-trigger-btn" id="openSearchBtn">
          <span class="search-icon">🔍</span>
          <span class="search-placeholder">检索全库 01–07 文献、卦爻、词义...</span>
          <kbd class="search-kbd">Ctrl K</kbd>
        </button>
      </div>

      <nav class="navbar-links">
        <a href="#/" class="nav-item" data-nav="home">🏛️ 首页</a>
        <a href="#/hexagrams" class="nav-item" data-nav="hexagrams">☯️ 六十四卦方阵</a>
        <a href="#/featured" class="nav-item" data-nav="featured">📜 1/2级核心专论</a>
        <a href="#/doc/03%20%E5%91%A8%E6%98%93%E7%AC%BA%E6%B3%A8/01_%E4%B9%BE%E5%8D%A6.md" class="nav-item" data-nav="reader">📖 知识库阅读</a>
        <button class="theme-toggle-btn" id="themeToggleBtn" title="切换宣纸浅色 / 玄墨深色模式">
          <span id="themeIcon">☾ 玄墨</span>
        </button>
        <a href="https://github.com/wole278/xushiyan-YiJing" target="_blank" rel="noopener" class="github-link" title="GitHub 仓库">GitHub ↗</a>
      </nav>
    </div>
  </header>

  <!-- 视图一：学术门户首页 (Landing Page) -->
  <main id="homeView" class="home-view">
    <!-- 1. 顶部学术门户 Hero 区 -->
    <section class="hero-section">
      <div class="hero-bg-pattern"></div>
      <div class="hero-container">
        <div class="hero-badge-row">
          <span class="seal-pill">生生之谓易</span>
          <span class="meta-pill">审议标准 v3.5</span>
          <span class="meta-pill">四重证据法</span>
          <span class="meta-pill">384爻全样本回测 η²=0.131</span>
        </div>
        <h1 class="hero-title">周易笺注、元研究与四级审议体系</h1>
        <p class="hero-subtitle">
          以<strong>历史唯物主义与《矛盾论》</strong>为方法底座，以<strong>“生生”</strong>为唯一价值标尺，<br class="desktop-br"/>
          深融<strong>商周考古实物、出土甲骨金文简帛与先秦古经传注</strong>的现代学术级《周易》研究文库
        </p>

        <div class="hero-search-bar">
          <button class="hero-search-box" id="heroSearchBtn">
            <span class="hero-search-icon">🔍</span>
            <span class="hero-search-text">点击搜索全库 251 篇研究论文、64 卦母本笺注、核心词义训诂或历史人物...</span>
            <span class="hero-search-shortcut">Ctrl + K</span>
          </button>
        </div>

        <div class="hero-actions">
          <a href="#/doc/03%20%E5%91%A8%E6%98%93%E7%AC%BA%E6%B3%A8/01_%E4%B9%BE%E5%8D%A6.md" class="btn-primary">📖 进入 64 卦权威主母本</a>
          <a href="#/doc/01%20%E5%AE%A1%E8%AE%AE%E4%BD%93%E7%B3%BB/01_%E6%A0%87%E5%87%86%E4%B8%8E%E8%A7%84%E8%8C%83/%E5%91%A8%E6%98%93%E7%AC%BA%E6%B3%A8%E5%AE%A1%E8%AE%AE%E4%B8%8E%E5%AE%8C%E5%96%84%E7%B3%BB%E7%BB%9F_%E6%A0%87%E5%87%86v3.5.md" class="btn-secondary">⚖️ 查阅《审议标准 v3.5》</a>
          <a href="#/doc/01%20%E5%AE%A1%E8%AE%AE%E4%BD%93%E7%B3%BB/01_%E6%A0%87%E5%87%86%E4%B8%8E%E8%A7%84%E8%8C%83/%E5%AD%A6%E6%9C%AF%E7%A0%94%E7%A9%B6%E8%AE%BA%E6%96%87%E6%92%B0%E5%86%99%E6%A0%BC%E5%BC%8F%E4%B8%8E%E6%9C%9F%E5%88%8A%E7%BA%A7%E6%A8%A1%E6%9D%BF%E8%A7%84%E8%8C%83.md" class="btn-outline">📝 期刊论文格式规范</a>
        </div>

        <!-- 核心实证指标仪表盘 -->
        <div class="hero-stats-grid" id="heroStatsGrid">
          <div class="stat-card">
            <div class="stat-value">64 卦 · 384 爻</div>
            <div class="stat-label">四部丛刊本影印校准底本</div>
            <div class="stat-note">100% 终审定稿 · SHA-256 锁定</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">η² = 0.131</div>
            <div class="stat-label">时位主矛盾实证解释力</div>
            <div class="stat-note">当位零解释力 (η²=0.000, p&lt;0.001)</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" id="statTier1">16 部</div>
            <div class="stat-label">1 级本体公理与实证基石</div>
            <div class="stat-note">核心依赖因子 0.4 · 向下单向覆盖</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" id="statTotalDocs">251 篇</div>
            <div class="stat-label">01–07 全库学术研究文档</div>
            <div class="stat-note">原典 verify.cmd 逐字核验闭环</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. 01-07 七大研究模块卡片导航 -->
    <section class="home-section" id="modulesSection">
      <div class="section-container">
        <div class="section-header">
          <div>
            <span class="section-eyebrow">SEVEN RESEARCH MODULES</span>
            <h2 class="section-title">01–07 七大核心研究模块导航</h2>
          </div>
          <p class="section-desc">从顶层审议法典、1级元哲学公理、64卦权威母本到单卦档案、词义训诂、跨界融合与历史人物全周期研判</p>
        </div>
        <div class="modules-grid" id="modulesGrid"></div>
      </div>
    </section>

    <!-- 3. 六十四卦交互式速查方阵 -->
    <section class="home-section alt-bg" id="hexagramsSection">
      <div class="section-container">
        <div class="section-header">
          <div>
            <span class="section-eyebrow">INTERACTIVE 64 HEXAGRAMS MATRIX</span>
            <h2 class="section-title">《周易》六十四卦与十翼交互式速查方阵</h2>
          </div>
          <p class="section-desc">点击任意卦象卡片直达《03 周易笺注史鉴》权威主母本，或一键切换至该卦的《04 单卦研究总结》与《01 四级审议报告》</p>
        </div>

        <div class="hex-toolbar">
          <div class="hex-tabs" id="hexFilterTabs">
            <button class="hex-tab active" data-filter="all">全部六十四卦 (01–64)</button>
            <button class="hex-tab" data-filter="upper">周易上经 (01 乾 – 30 离)</button>
            <button class="hex-tab" data-filter="lower">周易下经 (31 咸 – 64 未济)</button>
            <button class="hex-tab" data-filter="wings">十翼传文底本 (65–72)</button>
          </div>
          <div class="hex-search-wrap">
            <input type="text" id="hexSearchInput" class="hex-search-input" placeholder="筛选卦名、卦序或卦辞（如：16、豫、履虎尾、大过）..." />
          </div>
        </div>

        <div class="hexagrams-grid" id="hexagramsGrid"></div>
      </div>
    </section>

    <!-- 4. 1级(0.4)与2级(0.3)核心学术成果精选展台 -->
    <section class="home-section" id="featuredSection">
      <div class="section-container">
        <div class="section-header">
          <div>
            <span class="section-eyebrow">FEATURED MONOGRAPHS &amp; AXIOMS</span>
            <h2 class="section-title">1 级公理基石（0.4）与 2 级专题论文（0.3）精选展台</h2>
          </div>
          <p class="section-desc">遵循《文档价值基准应用分级体系》与《期刊级论文撰写格式规范》，汇集元研究、词义通考、融合研究与人物研判代表作</p>
        </div>

        <div class="featured-tabs" id="featuredTabs">
          <button class="feat-tab active" data-cat="all">全部精选成果</button>
          <button class="feat-tab" data-cat="tier1">🟢 1 级公理基石 (因子 0.4)</button>
          <button class="feat-tab" data-cat="02">🌌 02 元研究专论</button>
          <button class="feat-tab" data-cat="05">🔤 05 词义研究论文</button>
          <button class="feat-tab" data-cat="06">⚔️ 06 融合研究论文</button>
          <button class="feat-tab" data-cat="07">👤 07 历史人物分析</button>
        </div>

        <div class="featured-grid" id="featuredGrid"></div>
      </div>
    </section>

    <footer class="site-footer">
      <div class="footer-inner">
        <div class="footer-brand">
          <span class="brand-seal small">易</span>
          <span>周易笺注、元研究与审议体系（xushiyan-YiJing）</span>
        </div>
        <div class="footer-meta">
          基于唯物辩证法 · 生生价值标尺 · 四重证据法 · 384 爻实证回测构建 ｜ <a href="#/doc/README.md">查看项目总览 README</a>
        </div>
      </div>
    </footer>
  </main>

  <!-- 视图二：VitePress 风格三栏学术阅读器视图 (Reader View) -->
  <div id="readerView" class="reader-layout hidden">
    <!-- 左侧可折叠目录树 (Sidebar) -->
    <aside class="reader-sidebar" id="readerSidebar">
      <div class="sidebar-header">
        <div class="sidebar-mod-pills" id="sidebarModPills"></div>
        <div class="sidebar-filter-wrap">
          <input type="text" id="sidebarFilterInput" class="sidebar-filter-input" placeholder="过滤左侧目录文档..." />
        </div>
      </div>
      <div class="sidebar-tree" id="sidebarTree"></div>
    </aside>

    <!-- 居中期刊级文章阅读区 (Main Content) -->
    <div class="reader-main-wrap">
      <article class="reader-article-container">
        <!-- 顶部文章元数据栏 -->
        <div class="article-topbar" id="articleTopbar"></div>

        <!-- 单卦三维联动工作台（当阅读 01~64 卦相关文档时自动显现） -->
        <div class="hex-workbench hidden" id="hexWorkbench"></div>

        <!-- Markdown 渲染正文 -->
        <div class="markdown-body" id="markdownBody"></div>

        <!-- 底部上一篇 / 下一篇翻页导航 -->
        <nav class="article-pager" id="articlePager"></nav>
      </article>
    </div>

    <!-- 右侧浮动章节大纲 (Right TOC Outline) -->
    <aside class="reader-outline" id="readerOutline">
      <div class="outline-inner">
        <div class="outline-title">📑 本页章节大纲</div>
        <nav class="outline-nav" id="outlineNav"></nav>
      </div>
    </aside>
  </div>

  <!-- 全局全文搜索模态框 (Ctrl+K) -->
  <div class="search-modal-backdrop hidden" id="searchModal">
    <div class="search-modal-dialog">
      <div class="search-modal-header">
        <span class="search-modal-icon">🔍</span>
        <input type="text" id="globalSearchInput" class="search-modal-input" placeholder="输入关键词搜索全库 251 篇文档（如：藏礼于器、二簋、元亨利贞、周公、豫卦、曹操）..." autocomplete="off" />
        <button class="search-close-btn" id="closeSearchBtn">ESC</button>
      </div>
      <div class="search-modal-results" id="globalSearchResults"></div>
    </div>
  </div>

  <!-- 文物图片与图表点击放大灯箱 (Lightbox) -->
  <div class="lightbox-backdrop hidden" id="lightboxModal">
    <img id="lightboxImg" src="" alt="预览大图" />
    <div class="lightbox-caption" id="lightboxCaption"></div>
  </div>

  <!-- 预加载 Manifest 数据 (兼容 file:// 与 HTTP) -->
  <script src="data/manifest.js"></script>
  <!-- Marked.js / KaTeX / Mermaid CDN -->
  <script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
  <script src="assets/portal.js"></script>
</body>
</html>
"""

PORTAL_CSS = r"""/* ==========================================================================
   ZhouYi-Research 东方雅致学术门户样式表 (portal.css)
   配色体系：宣纸米白 (#FAF7F0) · 松烟墨黑 (#1C242B) · 朱砂印红 (#B2382A) · 青铜古绿 (#266859)
   ========================================================================== */

:root {
  --bg-page: #FAF7F0;
  --bg-surface: #FFFFFF;
  --bg-subtle: #F3EFE4;
  --bg-elevated: rgba(250, 247, 240, 0.90);
  --border-color: #E2DAC7;
  --border-strong: #CEBFA3;
  --text-primary: #1C242B;
  --text-secondary: #4E5A65;
  --text-muted: #7B858E;
  --accent-cinnabar: #B2382A;
  --accent-cinnabar-soft: rgba(178, 56, 42, 0.10);
  --accent-bronze: #266859;
  --accent-bronze-soft: rgba(38, 104, 89, 0.10);
  --accent-gold: #8F6824;
  --accent-gold-soft: rgba(143, 104, 36, 0.12);
  --shadow-sm: 0 2px 8px rgba(28, 36, 43, 0.05);
  --shadow-md: 0 8px 24px rgba(28, 36, 43, 0.08);
  --shadow-lg: 0 16px 40px rgba(28, 36, 43, 0.14);
  --font-serif: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", serif;
  --font-sans: "Noto Sans SC", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  --font-mono: "JetBrains Mono", Consolas, Monaco, monospace;
  --navbar-h: 64px;
}

html[data-theme="dark"] {
  --bg-page: #111519;
  --bg-surface: #181E24;
  --bg-subtle: #1E262E;
  --bg-elevated: rgba(17, 21, 25, 0.90);
  --border-color: #2A343E;
  --border-strong: #3B4856;
  --text-primary: #E7E2D8;
  --text-secondary: #A9B2BC;
  --text-muted: #707B86;
  --accent-cinnabar: #DF6253;
  --accent-cinnabar-soft: rgba(223, 98, 83, 0.16);
  --accent-bronze: #46A58F;
  --accent-bronze-soft: rgba(70, 165, 143, 0.16);
  --accent-gold: #D4A857;
  --accent-gold-soft: rgba(212, 168, 87, 0.16);
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.35);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.50);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-page);
  color: var(--text-primary);
  font-family: var(--font-sans);
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

a {
  color: var(--accent-cinnabar);
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: var(--accent-bronze);
}

.hidden {
  display: none !important;
}

/* ==========================================================================
   顶部导航栏 (Top Navbar)
   ========================================================================== */
.top-navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  height: var(--navbar-h);
  background: var(--bg-elevated);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
}

.navbar-inner {
  max-width: 1600px;
  height: 100%;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mobile-menu-btn {
  display: none;
  background: none;
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 18px;
  cursor: pointer;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-primary);
}

.brand-seal {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: var(--accent-cinnabar);
  color: #FAF7F0;
  font-family: var(--font-serif);
  font-weight: 900;
  font-size: 20px;
  border-radius: 6px;
  box-shadow: inset 0 0 0 2px rgba(250, 247, 240, 0.25);
  flex-shrink: 0;
}

.brand-seal.small {
  width: 26px;
  height: 26px;
  font-size: 14px;
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.brand-title {
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 17px;
  letter-spacing: 0.5px;
}

.brand-sub {
  font-size: 11px;
  color: var(--text-muted);
}

.navbar-search {
  flex: 1;
  max-width: 380px;
}

.search-trigger-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 7px 14px;
  background: var(--bg-subtle);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-secondary);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.search-trigger-btn:hover {
  border-color: var(--accent-cinnabar);
  background: var(--bg-surface);
}

.search-kbd {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--text-muted);
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-item {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  transition: all 0.2s;
}

.nav-item:hover,
.nav-item.active {
  color: var(--accent-cinnabar);
  background: var(--accent-cinnabar-soft);
}

.theme-toggle-btn {
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-subtle);
  color: var(--text-primary);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}

.theme-toggle-btn:hover {
  border-color: var(--accent-gold);
}

.github-link {
  padding: 6px 10px;
  font-size: 13px;
  color: var(--text-muted);
}

/* ==========================================================================
   首页门户 (Home Landing Page)
   ========================================================================== */
.hero-section {
  position: relative;
  padding: 64px 24px 56px;
  border-bottom: 1px solid var(--border-color);
  background: radial-gradient(circle at 50% 0%, var(--accent-cinnabar-soft), transparent 70%);
}

.hero-container {
  max-width: 1180px;
  margin: 0 auto;
  text-align: center;
}

.hero-badge-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 22px;
}

.seal-pill {
  background: var(--accent-cinnabar);
  color: #FAF7F0;
  padding: 4px 14px;
  border-radius: 999px;
  font-family: var(--font-serif);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
}

.meta-pill {
  background: var(--bg-surface);
  border: 1px solid var(--border-strong);
  color: var(--text-secondary);
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 12.5px;
  font-weight: 500;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: clamp(28px, 4.2vw, 48px);
  font-weight: 900;
  letter-spacing: 1.5px;
  color: var(--text-primary);
  margin-bottom: 18px;
  line-height: 1.25;
}

.hero-subtitle {
  max-width: 820px;
  margin: 0 auto 28px;
  font-size: clamp(15px, 1.8vw, 17.5px);
  color: var(--text-secondary);
  line-height: 1.8;
}

.hero-search-bar {
  max-width: 680px;
  margin: 0 auto 26px;
}

.hero-search-box {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  background: var(--bg-surface);
  border: 2px solid var(--border-strong);
  border-radius: 12px;
  box-shadow: var(--shadow-md);
  color: var(--text-secondary);
  font-size: 15px;
  cursor: pointer;
  transition: all 0.2s;
}

.hero-search-box:hover {
  border-color: var(--accent-cinnabar);
  transform: translateY(-1px);
}

.hero-search-shortcut {
  background: var(--bg-subtle);
  border: 1px solid var(--border-color);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 12px;
  font-family: var(--font-mono);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 14px;
  margin-bottom: 44px;
}

.btn-primary,
.btn-secondary,
.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: 8px;
  font-size: 14.5px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.btn-primary {
  background: var(--accent-cinnabar);
  color: #FAF7F0 !important;
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  opacity: 0.92;
  transform: translateY(-1px);
}

.btn-secondary {
  background: var(--accent-bronze);
  color: #FAF7F0 !important;
}

.btn-secondary:hover {
  opacity: 0.92;
  transform: translateY(-1px);
}

.btn-outline {
  background: var(--bg-surface);
  border: 1px solid var(--border-strong);
  color: var(--text-primary) !important;
}

.btn-outline:hover {
  border-color: var(--accent-cinnabar);
  color: var(--accent-cinnabar) !important;
}

.hero-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  text-align: left;
}

.stat-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-top: 3px solid var(--accent-cinnabar);
  border-radius: 10px;
  padding: 18px 20px;
  box-shadow: var(--shadow-sm);
}

.stat-card:nth-child(2) { border-top-color: var(--accent-bronze); }
.stat-card:nth-child(3) { border-top-color: var(--accent-gold); }
.stat-card:nth-child(4) { border-top-color: var(--accent-cinnabar); }

.stat-value {
  font-family: var(--font-serif);
  font-size: 23px;
  font-weight: 900;
  color: var(--text-primary);
  margin-bottom: 4px;
}

.stat-label {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 4px;
}

.stat-note {
  font-size: 12px;
  color: var(--text-muted);
}

/* ==========================================================================
   通用章节与 01-07 模块卡片
   ========================================================================== */
.home-section {
  padding: 56px 24px;
  border-bottom: 1px solid var(--border-color);
}

.home-section.alt-bg {
  background: var(--bg-subtle);
}

.section-container {
  max-width: 1280px;
  margin: 0 auto;
}

.section-header {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 32px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-color);
}

.section-eyebrow {
  display: block;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 2px;
  color: var(--accent-cinnabar);
  margin-bottom: 6px;
}

.section-title {
  font-family: var(--font-serif);
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
}

.section-desc {
  max-width: 540px;
  font-size: 14px;
  color: var(--text-secondary);
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 20px;
}

.mod-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
  transition: all 0.22s ease;
}

.mod-card:hover {
  transform: translateY(-3px);
  border-color: var(--accent-cinnabar);
  box-shadow: var(--shadow-md);
}

.mod-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.mod-code-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 800;
  color: var(--text-primary);
}

.mod-count-pill {
  background: var(--bg-subtle);
  border: 1px solid var(--border-color);
  padding: 2px 10px;
  border-radius: 999px;
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 600;
}

.mod-subtitle {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--accent-bronze);
  margin-bottom: 10px;
}

.mod-desc {
  font-size: 13.8px;
  color: var(--text-secondary);
  margin-bottom: 18px;
  line-height: 1.65;
}

.mod-sample-links {
  border-top: 1px dashed var(--border-color);
  padding-top: 12px;
  margin-bottom: 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.mod-sample-item {
  font-size: 13px;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mod-sample-item:hover {
  color: var(--accent-cinnabar);
}

.mod-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mod-enter-btn {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--accent-cinnabar);
}

/* ==========================================================================
   六十四卦交互式速查方阵 (64 Hexagrams Matrix)
   ========================================================================== */
.hex-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}

.hex-tabs,
.featured-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.hex-tab,
.feat-tab {
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-secondary);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.hex-tab.active,
.feat-tab.active {
  background: var(--accent-cinnabar);
  border-color: var(--accent-cinnabar);
  color: #FAF7F0;
}

.hex-search-wrap {
  flex: 1;
  max-width: 360px;
}

.hex-search-input {
  width: 100%;
  padding: 9px 14px;
  border-radius: 8px;
  border: 1px solid var(--border-strong);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 13.5px;
}

.hexagrams-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 14px;
}

.hex-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.2s ease;
  cursor: pointer;
}

.hex-card:hover {
  border-color: var(--accent-cinnabar);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.hex-card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.hex-no-badge {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 700;
  color: var(--accent-gold);
  background: var(--accent-gold-soft);
  padding: 2px 7px;
  border-radius: 4px;
}

.hex-struct-tag {
  font-size: 11.5px;
  color: var(--text-muted);
}

.hex-visual-row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 10px;
}

/* 六爻卦画精细绘制 (自下而上：初爻 -> 上爻) */
.hex-bars {
  width: 38px;
  display: flex;
  flex-direction: column-reverse;
  gap: 3.5px;
  flex-shrink: 0;
}

.hex-bar {
  height: 4px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.hex-bar.yang::before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  background: var(--accent-cinnabar);
  border-radius: 1px;
}

.hex-bar.yin::before,
.hex-bar.yin::after {
  content: "";
  display: block;
  width: 44%;
  height: 100%;
  background: var(--text-primary);
  border-radius: 1px;
}

.hex-name-main {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 800;
  color: var(--text-primary);
}

.hex-guaci-text {
  font-size: 12px;
  color: var(--text-secondary);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 10px;
  min-height: 36px;
}

.hex-quick-links {
  display: flex;
  gap: 6px;
  border-top: 1px solid var(--border-color);
  padding-top: 8px;
}

.hex-qlink {
  flex: 1;
  text-align: center;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 4px;
  border-radius: 4px;
  background: var(--bg-subtle);
  color: var(--text-secondary);
}

.hex-qlink:hover {
  background: var(--accent-cinnabar);
  color: #FAF7F0;
}

/* ==========================================================================
   1级/2级精选成果展台 (Featured Monographs)
   ========================================================================== */
.featured-tabs {
  margin-bottom: 24px;
}

.featured-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 18px;
}

.paper-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.2s;
  cursor: pointer;
}

.paper-card:hover {
  border-color: var(--accent-cinnabar);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.paper-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 10px;
}

.tier-badge {
  display: inline-flex;
  align-items: center;
  padding: 2px 9px;
  border-radius: 4px;
  font-size: 11.5px;
  font-weight: 700;
}

.tier-1 {
  background: var(--accent-cinnabar-soft);
  color: var(--accent-cinnabar);
  border: 1px solid var(--accent-cinnabar);
}

.tier-2 {
  background: var(--accent-bronze-soft);
  color: var(--accent-bronze);
  border: 1px solid var(--accent-bronze);
}

.tier-3 {
  background: var(--accent-gold-soft);
  color: var(--accent-gold);
}

.paper-title {
  font-family: var(--font-serif);
  font-size: 17.5px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 10px;
  line-height: 1.4;
}

.paper-snippet {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.paper-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  color: var(--text-muted);
  border-top: 1px dashed var(--border-color);
  padding-top: 10px;
}

/* ==========================================================================
   VitePress 风格三栏阅读器布局 (Reader View)
   ========================================================================== */
.reader-layout {
  display: grid;
  grid-template-columns: 300px minmax(0, 1fr) 250px;
  max-width: 1600px;
  margin: 0 auto;
  min-height: calc(100vh - var(--navbar-h));
}

.reader-sidebar {
  position: sticky;
  top: var(--navbar-h);
  height: calc(100vh - var(--navbar-h));
  overflow-y: auto;
  border-right: 1px solid var(--border-color);
  background: var(--bg-subtle);
  padding: 16px 14px 40px;
}

.sidebar-mod-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 10px;
}

.smod-pill {
  padding: 4px 8px;
  border-radius: 5px;
  font-size: 11.5px;
  font-weight: 600;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-secondary);
  cursor: pointer;
}

.smod-pill.active {
  background: var(--accent-cinnabar);
  border-color: var(--accent-cinnabar);
  color: #FAF7F0;
}

.sidebar-filter-input {
  width: 100%;
  padding: 7px 10px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 12.5px;
  margin-bottom: 12px;
}

.tree-mod-block {
  margin-bottom: 14px;
}

.tree-mod-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 8px;
  font-family: var(--font-serif);
  font-size: 14px;
  font-weight: 800;
  color: var(--text-primary);
  cursor: pointer;
  border-radius: 6px;
}

.tree-mod-header:hover {
  background: var(--bg-surface);
}

.tree-group {
  margin: 4px 0 8px 6px;
  padding-left: 8px;
  border-left: 1px solid var(--border-color);
}

.tree-group-title {
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  padding: 4px 6px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
}

.tree-doc-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding: 5px 8px;
  border-radius: 5px;
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.35;
  margin: 2px 0;
}

.tree-doc-link:hover {
  background: var(--bg-surface);
  color: var(--accent-cinnabar);
}

.tree-doc-link.active {
  background: var(--accent-cinnabar-soft);
  color: var(--accent-cinnabar);
  font-weight: 700;
}

.tree-doc-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.tree-tier-dot {
  font-size: 10px;
  padding: 0 4px;
  border-radius: 3px;
  flex-shrink: 0;
}

/* 居中正文阅读区 */
.reader-main-wrap {
  padding: 32px 44px 72px;
  min-width: 0;
}

.reader-article-container {
  max-width: 880px;
  margin: 0 auto;
}

.article-topbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 14px;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
  font-size: 13px;
  color: var(--text-muted);
}

/* 单卦三维联动工作台 */
.hex-workbench {
  background: var(--bg-subtle);
  border: 1px solid var(--border-strong);
  border-left: 4px solid var(--accent-cinnabar);
  border-radius: 10px;
  padding: 16px 20px;
  margin-bottom: 28px;
}

.wb-top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}

.wb-title-wrap {
  display: flex;
  align-items: center;
  gap: 14px;
}

.wb-gua-name {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 900;
}

.wb-guaci {
  font-size: 13px;
  color: var(--text-secondary);
}

.wb-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.wb-tab {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12.5px;
  font-weight: 600;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
}

.wb-tab.active {
  background: var(--accent-cinnabar);
  border-color: var(--accent-cinnabar);
  color: #FAF7F0;
}

/* ==========================================================================
   期刊级 Markdown 正文排版 (markdown-body)
   ========================================================================== */
.markdown-body {
  font-size: 16px;
  line-height: 1.85;
  color: var(--text-primary);
}

.markdown-body h1 {
  font-family: var(--font-serif);
  font-size: 30px;
  font-weight: 900;
  line-height: 1.3;
  margin: 0 0 22px;
  padding-bottom: 14px;
  border-bottom: 2px solid var(--border-strong);
}

.markdown-body h2 {
  font-family: var(--font-serif);
  font-size: 22px;
  font-weight: 800;
  margin: 40px 0 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-color);
  scroll-margin-top: 84px;
}

.markdown-body h3 {
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 700;
  margin: 28px 0 12px;
  scroll-margin-top: 84px;
}

.markdown-body h4 {
  font-size: 16px;
  font-weight: 700;
  margin: 20px 0 10px;
}

.markdown-body p {
  margin: 0 0 16px;
}

.markdown-body ul,
.markdown-body ol {
  margin: 0 0 16px;
  padding-left: 24px;
}

.markdown-body li {
  margin-bottom: 6px;
}

.markdown-body blockquote {
  margin: 18px 0;
  padding: 14px 20px;
  background: var(--bg-subtle);
  border-left: 4px solid var(--accent-gold);
  border-radius: 0 8px 8px 0;
  color: var(--text-secondary);
}

.markdown-body blockquote p:last-child {
  margin-bottom: 0;
}

/* GitHub 风格 Alerts */
.md-alert {
  margin: 18px 0;
  padding: 14px 18px;
  border-radius: 8px;
  border-left: 4px solid var(--accent-bronze);
  background: var(--accent-bronze-soft);
}

.md-alert-title {
  font-weight: 700;
  font-size: 14px;
  margin-bottom: 6px;
}

.md-alert.alert-important,
.md-alert.alert-warning,
.md-alert.alert-caution {
  border-left-color: var(--accent-cinnabar);
  background: var(--accent-cinnabar-soft);
}

.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 14px;
  background: var(--bg-surface);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.markdown-body th,
.markdown-body td {
  border: 1px solid var(--border-color);
  padding: 10px 14px;
  text-align: left;
  vertical-align: top;
}

.markdown-body th {
  background: var(--bg-subtle);
  font-family: var(--font-serif);
  font-weight: 700;
}

.markdown-body tr:nth-child(even) td {
  background: rgba(143, 104, 36, 0.02);
}

.markdown-body img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 20px auto;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
  cursor: zoom-in;
}

.markdown-body code {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: var(--bg-subtle);
  border: 1px solid var(--border-color);
  padding: 2px 6px;
  border-radius: 4px;
}

.markdown-body pre {
  background: #1A2026;
  color: #E6E1D6;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 18px 0;
}

.markdown-body pre code {
  background: none;
  border: none;
  color: inherit;
  padding: 0;
}

.mermaid-box {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  margin: 22px 0;
  text-align: center;
  overflow-x: auto;
}

.markdown-body hr {
  border: none;
  border-top: 1px solid var(--border-color);
  margin: 32px 0;
}

/* 底部翻页器 */
.article-pager {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--border-color);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.pager-card {
  display: flex;
  flex-direction: column;
  padding: 14px 18px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  background: var(--bg-surface);
  transition: all 0.2s;
}

.pager-card:hover {
  border-color: var(--accent-cinnabar);
}

.pager-card.next {
  text-align: right;
}

.pager-label {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 4px;
}

.pager-title {
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 700;
  color: var(--accent-cinnabar);
}

/* 右侧大纲 (Right Outline) */
.reader-outline {
  position: sticky;
  top: var(--navbar-h);
  height: calc(100vh - var(--navbar-h));
  overflow-y: auto;
  padding: 28px 18px;
  border-left: 1px solid var(--border-color);
}

.outline-title {
  font-family: var(--font-serif);
  font-size: 13px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-color);
}

.outline-link {
  display: block;
  padding: 4px 0 4px 10px;
  font-size: 12.5px;
  color: var(--text-secondary);
  border-left: 2px solid transparent;
  line-height: 1.4;
}

.outline-link.level-3 {
  padding-left: 22px;
  font-size: 12px;
  color: var(--text-muted);
}

.outline-link:hover,
.outline-link.active {
  color: var(--accent-cinnabar);
  border-left-color: var(--accent-cinnabar);
  font-weight: 600;
}

/* ==========================================================================
   全文搜索弹窗与图片灯箱 (Modals)
   ========================================================================== */
.search-modal-backdrop,
.lightbox-backdrop {
  position: fixed;
  inset: 0;
  z-index: 200;
  background: rgba(17, 21, 25, 0.65);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 8vh 16px;
}

.search-modal-dialog {
  width: 100%;
  max-width: 720px;
  background: var(--bg-surface);
  border: 1px solid var(--border-strong);
  border-radius: 12px;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
}

.search-modal-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--border-color);
}

.search-modal-input {
  flex: 1;
  border: none;
  background: none;
  font-size: 16px;
  color: var(--text-primary);
  outline: none;
}

.search-close-btn {
  padding: 3px 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-subtle);
  border-radius: 4px;
  font-size: 11px;
  color: var(--text-muted);
  cursor: pointer;
}

.search-modal-results {
  max-height: 65vh;
  overflow-y: auto;
  padding: 12px;
}

.search-res-item {
  display: block;
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px solid transparent;
  margin-bottom: 6px;
}

.search-res-item:hover {
  background: var(--bg-subtle);
  border-color: var(--border-color);
}

.search-res-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}

.search-res-title {
  font-family: var(--font-serif);
  font-size: 15.5px;
  font-weight: 700;
  color: var(--text-primary);
}

.search-res-snippet {
  font-size: 12.5px;
  color: var(--text-secondary);
}

mark {
  background: var(--accent-cinnabar-soft);
  color: var(--accent-cinnabar);
  font-weight: 700;
  padding: 0 2px;
  border-radius: 2px;
}

.lightbox-backdrop {
  align-items: center;
  flex-direction: column;
  cursor: zoom-out;
}

.lightbox-backdrop img {
  max-width: 92vw;
  max-height: 82vh;
  border-radius: 8px;
  box-shadow: var(--shadow-lg);
}

.lightbox-caption {
  margin-top: 12px;
  color: #FAF7F0;
  font-size: 14px;
}

.site-footer {
  padding: 32px 24px;
  background: var(--bg-surface);
}

.footer-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 13px;
  color: var(--text-muted);
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-serif);
  font-weight: 700;
  color: var(--text-primary);
}

/* 响应式适配 */
@media (max-width: 1180px) {
  .reader-layout {
    grid-template-columns: 270px minmax(0, 1fr);
  }
  .reader-outline {
    display: none;
  }
  .hero-stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 820px) {
  .mobile-menu-btn {
    display: inline-block;
  }
  .navbar-links .nav-item {
    display: none;
  }
  .reader-layout {
    grid-template-columns: 1fr;
  }
  .reader-sidebar {
    position: fixed;
    left: -310px;
    top: var(--navbar-h);
    width: 290px;
    z-index: 150;
    transition: left 0.25s ease;
    box-shadow: var(--shadow-lg);
  }
  .reader-sidebar.open {
    left: 0;
  }
  .reader-main-wrap {
    padding: 20px 16px 56px;
  }
  .markdown-body table {
    display: block;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  .article-pager {
    grid-template-columns: 1fr;
  }
  .brand-sub, .search-kbd, .github-link {
    display: none;
  }
  .search-placeholder {
    max-width: 96px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .hexagrams-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  }
  .hero-stats-grid {
    grid-template-columns: 1fr;
  }
}
"""

PORTAL_JS = r"""/* ==========================================================================
   ZhouYi-Research 东方雅致学术门户交互引擎 (portal.js)
   ========================================================================== */
(function () {
  "use strict";

  const state = {
    manifest: window.__ZHOUYI_MANIFEST__ || null,
    chunks: window.__ZHOUYI_DOCS_CHUNKS__ || {},
    activeModFilter: "all",
    activeHexFilter: "all",
    hexSearchQuery: "",
    activeFeaturedCat: "all",
    currentDocId: null,
    theme: localStorage.getItem("zhouyi_theme") || "light",
  };

  // 1. 初始化主题与 Mermaid
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("zhouyi_theme", theme);
    const iconEl = document.getElementById("themeIcon");
    if (iconEl) {
      iconEl.textContent = theme === "dark" ? "☀ 宣纸" : "☾ 玄墨";
    }
    if (window.mermaid) {
      window.mermaid.initialize({
        startOnLoad: false,
        theme: theme === "dark" ? "dark" : "neutral",
        securityLevel: "loose",
      });
    }
  }

  // 2. 按需加载模块文档数据分片 (兼容 HTTP fetch 与 file:// script 标签动态加载)
  function ensureChunkLoaded(modCode) {
    if (state.chunks[modCode]) {
      return Promise.resolve(state.chunks[modCode]);
    }
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = `data/docs_${modCode}.js`;
      script.onload = () => {
        state.chunks = window.__ZHOUYI_DOCS_CHUNKS__ || {};
        resolve(state.chunks[modCode] || {});
      };
      script.onerror = () => {
        fetch(`data/docs_${modCode}.json`)
          .then((r) => r.json())
          .then((data) => {
            state.chunks[modCode] = data;
            resolve(data);
          })
          .catch(reject);
      };
      document.head.appendChild(script);
    });
  }

  // 3. 渲染六爻阴阳卦画 HTML
  function renderHexBarsHtml(lines) {
    if (!lines || !lines.length) return "";
    return `<div class="hex-bars">${lines
      .map((b) => `<div class="hex-bar ${b === 1 ? "yang" : "yin"}"></div>`)
      .join("")}</div>`;
  }

  // 4. 渲染首页：01–07 七大模块卡片
  function renderModulesGrid() {
    const grid = document.getElementById("modulesGrid");
    if (!grid || !state.manifest) return;

    grid.innerHTML = state.manifest.modules
      .map((mod) => {
        const allItems = mod.groups
          .flatMap((g) => g.items)
          .filter((d) => d.name !== "README.md")
          .slice(0, 3);
        const samplesHtml = allItems
          .map(
            (item) =>
              `<a href="#/doc/${encodeURIComponent(item.id)}" class="mod-sample-item">📄 ${escapeHtml(
                item.title
              )}</a>`
          )
          .join("");

        return `
        <div class="mod-card">
          <div>
            <div class="mod-card-top">
              <span class="mod-code-badge">${mod.icon} ${escapeHtml(mod.title)}</span>
              <span class="mod-count-pill">${mod.count} 篇文献</span>
            </div>
            <div class="mod-subtitle">${escapeHtml(mod.subtitle)}</div>
            <p class="mod-desc">${escapeHtml(mod.desc)}</p>
            <div class="mod-sample-links">${samplesHtml}</div>
          </div>
          <div class="mod-card-footer">
            <a href="#/doc/${encodeURIComponent(mod.default_doc)}" class="mod-enter-btn">进入 ${escapeHtml(
          mod.short
        )} 专栏 →</a>
          </div>
        </div>`;
      })
      .join("");
  }

  // 5. 渲染首页：六十四卦与十翼交互式速查方阵
  function renderHexagramsGrid() {
    const grid = document.getElementById("hexagramsGrid");
    if (!grid || !state.manifest) return;

    const q = state.hexSearchQuery.trim().toLowerCase();

    if (state.activeHexFilter === "wings") {
      const wings = state.manifest.tenWings.filter(
        (w) => !q || w.name.toLowerCase().includes(q) || w.title.toLowerCase().includes(q)
      );
      grid.innerHTML = wings
        .map(
          (w) => `
        <div class="hex-card" onclick="location.hash='#/doc/${encodeURIComponent(w.id)}'">
          <div>
            <div class="hex-card-head">
              <span class="hex-no-badge">十翼 · ${w.noStr}</span>
              <span class="hex-struct-tag">易传底本</span>
            </div>
            <div class="hex-visual-row">
              <div class="hex-name-main">《${escapeHtml(w.name)}》</div>
            </div>
            <div class="hex-guaci-text">${escapeHtml(w.snippet)}</div>
          </div>
          <div class="hex-quick-links">
            <a href="#/doc/${encodeURIComponent(w.id)}" class="hex-qlink" onclick="event.stopPropagation()">阅读传文底本 →</a>
          </div>
        </div>`
        )
        .join("");
      return;
    }

    const list = state.manifest.hexagrams.filter((h) => {
      if (state.activeHexFilter === "upper" && h.no > 30) return false;
      if (state.activeHexFilter === "lower" && h.no <= 30) return false;
      if (q) {
        const hay = `${h.noStr} ${h.name} ${h.struct} ${h.guaci} ${h.daxiang}`.toLowerCase();
        return hay.includes(q);
      }
      return true;
    });

    grid.innerHTML = list
      .map((h) => {
        const masterUrl = h.links && h.links.master ? `#/doc/${encodeURIComponent(h.links.master)}` : "#/";
        const recUrl =
          h.links && h.links.records && h.links.records.length
            ? `#/doc/${encodeURIComponent(h.links.records[0].id)}`
            : masterUrl;
        const revUrl =
          h.links && h.links.reviews && h.links.reviews.length
            ? `#/doc/${encodeURIComponent(h.links.reviews[0].id)}`
            : masterUrl;

        return `
        <div class="hex-card" onclick="location.hash='${masterUrl}'">
          <div>
            <div class="hex-card-head">
              <span class="hex-no-badge">第 ${h.noStr} 卦</span>
              <span class="hex-struct-tag">${escapeHtml(h.struct)}</span>
            </div>
            <div class="hex-visual-row">
              ${renderHexBarsHtml(h.lines)}
              <div>
                <div class="hex-name-main">${escapeHtml(h.name)}卦 <span style="font-weight:400;font-size:16px;color:var(--text-muted)">${h.unicode}</span></div>
              </div>
            </div>
            <div class="hex-guaci-text" title="${escapeHtml(h.guaci)}">${escapeHtml(h.guaci)}</div>
          </div>
          <div class="hex-quick-links" onclick="event.stopPropagation()">
            <a href="${masterUrl}" class="hex-qlink" title="03 周易笺注史鉴主母本">主母本</a>
            <a href="${recUrl}" class="hex-qlink" title="04 单卦研究总结">单卦研究</a>
            <a href="${revUrl}" class="hex-qlink" title="01 四级审议报告">审议报告</a>
          </div>
        </div>`;
      })
      .join("");
  }

  // 6. 渲染首页：1级(0.4)与2级(0.3)核心学术专论展台
  function renderFeaturedGrid() {
    const grid = document.getElementById("featuredGrid");
    if (!grid || !state.manifest) return;

    const list = state.manifest.featuredPapers.filter((d) => {
      if (state.activeFeaturedCat === "all") return true;
      if (state.activeFeaturedCat === "tier1") return d.tier === 1;
      return d.module === state.activeFeaturedCat;
    });

    grid.innerHTML = list
      .map((d) => {
        const tierClass = d.tier === 1 ? "tier-1" : d.tier === 2 ? "tier-2" : "tier-3";
        const modObj = state.manifest.modules.find((m) => m.code === d.module);
        const modName = modObj ? modObj.title : d.module;
        return `
        <div class="paper-card" onclick="location.hash='#/doc/${encodeURIComponent(d.id)}'">
          <div>
            <div class="paper-meta-row">
              <span class="tier-badge ${tierClass}">${escapeHtml(d.tierLabel)}</span>
              <span style="font-size:12px;color:var(--text-muted)">${escapeHtml(modName)}</span>
            </div>
            <h3 class="paper-title">${escapeHtml(d.title)}</h3>
            <p class="paper-snippet">${escapeHtml(d.snippet)}</p>
          </div>
          <div class="paper-footer">
            <span>约 ${d.wordCount.toLocaleString()} 字</span>
            <span style="color:var(--accent-cinnabar);font-weight:700">阅读全文 →</span>
          </div>
        </div>`;
      })
      .join("");
  }

  // 7. 渲染阅读器左侧目录树 (Sidebar Tree)
  function renderSidebar(filterText = "") {
    const pillsEl = document.getElementById("sidebarModPills");
    const treeEl = document.getElementById("sidebarTree");
    if (!treeEl || !state.manifest) return;

    if (pillsEl && !pillsEl.innerHTML) {
      const pills = [{ code: "all", short: "全部" }, ...state.manifest.modules];
      pillsEl.innerHTML = pills
        .map(
          (m) =>
            `<button class="smod-pill ${state.activeModFilter === m.code ? "active" : ""}" data-mod="${
              m.code
            }">${escapeHtml(m.code === "all" ? "全部" : m.code)}</button>`
        )
        .join("");

      pillsEl.querySelectorAll(".smod-pill").forEach((btn) => {
        btn.addEventListener("click", () => {
          state.activeModFilter = btn.getAttribute("data-mod");
          pillsEl.querySelectorAll(".smod-pill").forEach((b) => b.classList.remove("active"));
          btn.classList.add("active");
          renderSidebar(document.getElementById("sidebarFilterInput").value);
        });
      });
    }

    const q = filterText.trim().toLowerCase();
    const mods = state.manifest.modules.filter(
      (m) => state.activeModFilter === "all" || m.code === state.activeModFilter
    );

    treeEl.innerHTML = mods
      .map((mod) => {
        const groupsHtml = mod.groups
          .map((grp) => {
            const items = grp.items.filter(
              (item) => !q || item.title.toLowerCase().includes(q) || item.id.toLowerCase().includes(q)
            );
            if (!items.length) return "";

            const linksHtml = items
              .map((item) => {
                const isActive = state.currentDocId === item.id;
                const badge =
                  item.tier === 1
                    ? `<span class="tree-tier-dot tier-1">1级</span>`
                    : item.tier === 2
                    ? `<span class="tree-tier-dot tier-2">2级</span>`
                    : "";
                return `<a href="#/doc/${encodeURIComponent(item.id)}" class="tree-doc-link ${
                  isActive ? "active" : ""
                }" data-docid="${escapeHtml(item.id)}">
                  <span class="tree-doc-text" title="${escapeHtml(item.title)}">${escapeHtml(item.title)}</span>
                  ${badge}
                </a>`;
              })
              .join("");

            return `
            <div class="tree-group">
              <div class="tree-group-title">${escapeHtml(grp.title)} <span>(${items.length})</span></div>
              <div class="tree-group-items">${linksHtml}</div>
            </div>`;
          })
          .join("");

        if (!groupsHtml) return "";
        return `
        <div class="tree-mod-block">
          <div class="tree-mod-header">${mod.icon} ${escapeHtml(mod.title)}</div>
          ${groupsHtml}
        </div>`;
      })
      .join("");
  }

  // 8. 渲染 Markdown 文本（支持 KaTeX 数学公式、GitHub Alerts、Mermaid 流程图）
  function renderMarkdownWithExtensions(mdText) {
    // 保护代码块与 Mermaid 块
    const mathBlocks = [];
    let processed = mdText;

    // 提取块级公式 $$...$$
    processed = processed.replace(/\$\$([\s\S]+?)\$\$/g, (_, tex) => {
      const idx = mathBlocks.length;
      mathBlocks.push({ display: true, tex: tex.trim() });
      return `@@MATH_BLOCK_${idx}@@`;
    });

    // 提取行内公式 $...$ (不跨行)
    processed = processed.replace(/(?<!\\)\$([^\$\n]+?)\$/g, (_, tex) => {
      const idx = mathBlocks.length;
      mathBlocks.push({ display: false, tex: tex.trim() });
      return `@@MATH_BLOCK_${idx}@@`;
    });

    // 使用 marked 解析
    const renderer = new marked.Renderer();
    const origCode = renderer.code.bind(renderer);
    renderer.code = function (code, infostring, escaped) {
      const lang = (infostring || "").trim().toLowerCase();
      if (lang === "mermaid") {
        return `<div class="mermaid-box"><pre class="mermaid">${escapeHtml(code)}</pre></div>`;
      }
      return origCode(code, infostring, escaped);
    };

    let html = marked.parse(processed, { renderer, gfm: true, breaks: false });

    // 还原 KaTeX 公式
    html = html.replace(/@@MATH_BLOCK_(\d+)@@/g, (_, idxStr) => {
      const item = mathBlocks[Number(idxStr)];
      if (!item || !window.katex) return item ? item.tex : "";
      try {
        return window.katex.renderToString(item.tex, {
          displayMode: item.display,
          throwOnError: false,
        });
      } catch (e) {
        return `<code>${escapeHtml(item.tex)}</code>`;
      }
    });

    // 转换 GitHub 风格 Alerts: <blockquote><p>[!NOTE] ...
    html = html.replace(
      /<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*([^\n<]*)\n?([\s\S]*?)<\/blockquote>/gi,
      (_, type, titleLine, rest) => {
        const t = type.toLowerCase();
        const labels = {
          note: "📌 说明 (NOTE)",
          tip: "💡 提示 (TIP)",
          important: "🏛️ 核心要义 (IMPORTANT)",
          warning: "⚠️ 注意 (WARNING)",
          caution: "🚨 红线警示 (CAUTION)",
        };
        const title = titleLine.trim() || labels[t] || type;
        return `<div class="md-alert alert-${t}"><div class="md-alert-title">${title}</div><p>${rest}</div>`;
      }
    );

    return html;
  }

  // 9. 打开并渲染指定文档 (#/doc/<id>)
  async function openDocument(docId) {
    if (!state.manifest) return;
    let meta = state.manifest.searchIndex.find((d) => d.id === docId);
    if (!meta) {
      // 尝试回退匹配
      meta = state.manifest.searchIndex.find((d) => d.id.endsWith(docId)) || state.manifest.searchIndex[0];
    }
    if (!meta) return;

    state.currentDocId = meta.id;
    document.getElementById("homeView").classList.add("hidden");
    document.getElementById("readerView").classList.remove("hidden");
    document.getElementById("readerSidebar").classList.remove("open");

    // 加载对应模块数据分片
    const chunk = await ensureChunkLoaded(meta.module);
    const docData = chunk[meta.id];
    if (!docData) return;

    // 更新顶部面包屑与价值评级栏
    const tierClass = meta.tier === 1 ? "tier-1" : meta.tier === 2 ? "tier-2" : "tier-3";
    const readMins = Math.max(1, Math.round(meta.wordCount / 450));
    const topbar = document.getElementById("articleTopbar");
    topbar.innerHTML = `
      <div>
        <a href="#/">🏠 首页</a> / <span>${escapeHtml(meta.id)}</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px">
        ${meta.tier > 0 ? `<span class="tier-badge ${tierClass}">${escapeHtml(meta.tierLabel)}</span>` : ""}
        <span>约 ${meta.wordCount.toLocaleString()} 字 · 预计阅读 ${readMins} 分钟</span>
      </div>
    `;

    // 若关联单卦 (1~64)，渲染「本卦三维联动工作台」
    const wbEl = document.getElementById("hexWorkbench");
    if (meta.hexNo) {
      const hex = state.manifest.hexagrams.find((h) => h.no === meta.hexNo);
      if (hex) {
        const masterId = hex.links && hex.links.master;
        const recs = (hex.links && hex.links.records) || [];
        const revs = (hex.links && hex.links.reviews) || [];

        wbEl.classList.remove("hidden");
        wbEl.innerHTML = `
          <div class="wb-top">
            <div class="wb-title-wrap">
              ${renderHexBarsHtml(hex.lines)}
              <div>
                <div class="wb-gua-name">第 ${hex.noStr} 卦 · ${escapeHtml(hex.name)}卦 ${hex.unicode} <span style="font-size:13px;font-weight:500;color:var(--text-muted)">(${escapeHtml(hex.struct)})</span></div>
                <div class="wb-guaci">${escapeHtml(hex.guaci)} ｜ 《大象》：${escapeHtml(hex.daxiang)}</div>
              </div>
            </div>
          </div>
          <div class="wb-tabs">
            ${
              masterId
                ? `<a href="#/doc/${encodeURIComponent(masterId)}" class="wb-tab ${
                    meta.id === masterId ? "active" : ""
                  }">📖 03 周易笺注史鉴主母本</a>`
                : ""
            }
            ${recs
              .map(
                (r, idx) =>
                  `<a href="#/doc/${encodeURIComponent(r.id)}" class="wb-tab ${
                    meta.id === r.id ? "active" : ""
                  }">🔬 04 单卦研究总结${recs.length > 1 ? " (" + (idx + 1) + ")" : ""}</a>`
              )
              .join("")}
            ${revs
              .map(
                (r) =>
                  `<a href="#/doc/${encodeURIComponent(r.id)}" class="wb-tab ${
                    meta.id === r.id ? "active" : ""
                  }">⚖️ 01 四级审议报告</a>`
              )
              .join("")}
          </div>
        `;
      } else {
        wbEl.classList.add("hidden");
      }
    } else {
      wbEl.classList.add("hidden");
    }

    // 渲染正文
    const bodyEl = document.getElementById("markdownBody");
    bodyEl.innerHTML = renderMarkdownWithExtensions(docData.content);

    // 为标题生成锚点 ID 并构建右侧大纲 (TOC)
    buildOutlineAndHeadingIds(bodyEl);

    // 渲染 Mermaid 图表
    if (window.mermaid) {
      const mermaidNodes = bodyEl.querySelectorAll(".mermaid");
      if (mermaidNodes.length) {
        try {
          await window.mermaid.run({ nodes: mermaidNodes });
        } catch (err) {
          console.warn("Mermaid render notice:", err);
        }
      }
    }

    // 绑定图片点击灯箱放大
    bodyEl.querySelectorAll("img").forEach((img) => {
      img.addEventListener("click", () => {
        const modal = document.getElementById("lightboxModal");
        document.getElementById("lightboxImg").src = img.src;
        document.getElementById("lightboxCaption").textContent = img.alt || "";
        modal.classList.remove("hidden");
      });
    });

    // 构建底部上一篇 / 下一篇导航
    renderArticlePager(meta.id);

    // 刷新左侧目录高亮并滚动到顶部
    renderSidebar(document.getElementById("sidebarFilterInput").value);
    window.scrollTo({ top: 0, behavior: "instant" });
    document.title = `${meta.title} — 周易研究学术门户`;
  }

  // 10. 构建右侧章节大纲 (Right Outline)
  function buildOutlineAndHeadingIds(container) {
    const outlineNav = document.getElementById("outlineNav");
    if (!outlineNav) return;

    const headings = Array.from(container.querySelectorAll("h2, h3"));
    if (!headings.length) {
      outlineNav.innerHTML = `<div style="font-size:12px;color:var(--text-muted)">本文无二级子章节</div>`;
      return;
    }

    outlineNav.innerHTML = headings
      .map((h, i) => {
        const id = `sec-heading-${i}`;
        h.id = id;
        const level = h.tagName === "H3" ? "level-3" : "level-2";
        return `<a href="javascript:void(0)" class="outline-link ${level}" data-target="${id}">${escapeHtml(
          h.textContent
        )}</a>`;
      })
      .join("");

    outlineNav.querySelectorAll(".outline-link").forEach((link) => {
      link.addEventListener("click", () => {
        const targetEl = document.getElementById(link.getAttribute("data-target"));
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      });
    });
  }

  // 11. 构建底部上一篇 / 下一篇卡片
  function renderArticlePager(currentId) {
    const pagerEl = document.getElementById("articlePager");
    if (!pagerEl || !state.manifest) return;

    const list = state.manifest.searchIndex;
    const idx = list.findIndex((d) => d.id === currentId);
    const prev = idx > 0 ? list[idx - 1] : null;
    const next = idx >= 0 && idx < list.length - 1 ? list[idx + 1] : null;

    pagerEl.innerHTML = `
      <div>
        ${
          prev
            ? `<a href="#/doc/${encodeURIComponent(prev.id)}" class="pager-card prev">
                <span class="pager-label">← 上一篇文献</span>
                <span class="pager-title">${escapeHtml(prev.title)}</span>
              </a>`
            : ""
        }
      </div>
      <div>
        ${
          next
            ? `<a href="#/doc/${encodeURIComponent(next.id)}" class="pager-card next">
                <span class="pager-label">下一篇文献 →</span>
                <span class="pager-title">${escapeHtml(next.title)}</span>
              </a>`
            : ""
        }
      </div>
    `;
  }

  // 12. 全局全文搜索 (Ctrl+K)
  function runGlobalSearch(query) {
    const resEl = document.getElementById("globalSearchResults");
    if (!resEl || !state.manifest) return;

    const q = query.trim().toLowerCase();
    const list = state.manifest.searchIndex
      .filter((d) => {
        if (!q) return d.tier === 1 || d.tier === 2;
        return (
          d.title.toLowerCase().includes(q) ||
          d.id.toLowerCase().includes(q) ||
          d.snippet.toLowerCase().includes(q)
        );
      })
      .slice(0, 30);

    if (!list.length) {
      resEl.innerHTML = `<div style="padding:24px;text-align:center;color:var(--text-muted)">未找到匹配的文献，请尝试其他关键词（如卦名、词义、人物名）</div>`;
      return;
    }

    resEl.innerHTML = list
      .map((d) => {
        const tierClass = d.tier === 1 ? "tier-1" : d.tier === 2 ? "tier-2" : "tier-3";
        return `
        <a href="#/doc/${encodeURIComponent(d.id)}" class="search-res-item" onclick="document.getElementById('searchModal').classList.add('hidden')">
          <div class="search-res-top">
            <span class="search-res-title">${highlightText(d.title, q)}</span>
            ${d.tier > 0 ? `<span class="tier-badge ${tierClass}">${escapeHtml(d.tierLabel)}</span>` : ""}
          </div>
          <div style="font-size:11.5px;color:var(--accent-bronze);margin-bottom:4px">${escapeHtml(d.id)}</div>
          <div class="search-res-snippet">${highlightText(d.snippet, q)}</div>
        </a>`;
      })
      .join("");
  }

  function highlightText(text, q) {
    const safe = escapeHtml(text || "");
    if (!q) return safe;
    const escapedQ = q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    return safe.replace(new RegExp(`(${escapedQ})`, "gi"), "<mark>$1</mark>");
  }

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // 13. 路由调度 (Hash Router)
  function handleRoute() {
    const hash = window.location.hash || "#/";
    document.querySelectorAll(".navbar-links .nav-item").forEach((el) => el.classList.remove("active"));

    if (hash.startsWith("#/doc/")) {
      const docId = decodeURIComponent(hash.slice("#/doc/".length));
      document.querySelector('.nav-item[data-nav="reader"]')?.classList.add("active");
      openDocument(docId);
      return;
    }

    // 显示首页门户
    document.getElementById("readerView").classList.add("hidden");
    document.getElementById("homeView").classList.remove("hidden");
    document.title = "周易笺注、元研究与审议体系 — 东方唯物学术门户";

    if (hash === "#/hexagrams") {
      document.querySelector('.nav-item[data-nav="hexagrams"]')?.classList.add("active");
      document.getElementById("hexagramsSection")?.scrollIntoView({ behavior: "smooth" });
    } else if (hash === "#/featured") {
      document.querySelector('.nav-item[data-nav="featured"]')?.classList.add("active");
      document.getElementById("featuredSection")?.scrollIntoView({ behavior: "smooth" });
    } else {
      document.querySelector('.nav-item[data-nav="home"]')?.classList.add("active");
      window.scrollTo({ top: 0, behavior: "instant" });
    }
  }

  // 14. 启动初始化
  function init() {
    applyTheme(state.theme);

    if (state.manifest) {
      document.getElementById("statTotalDocs").textContent = `${state.manifest.stats.totalDocs} 篇`;
      document.getElementById("statTier1").textContent = `${state.manifest.stats.tier1Count} 部`;
      renderModulesGrid();
      renderHexagramsGrid();
      renderFeaturedGrid();
      renderSidebar();
    }

    // 绑定主题切换
    document.getElementById("themeToggleBtn")?.addEventListener("click", () => {
      applyTheme(state.theme === "dark" ? "light" : "dark");
    });

    // 绑定移动端菜单
    document.getElementById("mobileMenuBtn")?.addEventListener("click", () => {
      const rv = document.getElementById("readerView");
      if (rv && rv.classList.contains("hidden")) {
        window.location.hash = "#/doc/03%20%E5%91%A8%E6%98%93%E7%AC%BA%E6%B3%A8/01_%E4%B9%BE%E5%8D%A6.md";
        setTimeout(() => document.getElementById("readerSidebar")?.classList.add("open"), 60);
      } else {
        document.getElementById("readerSidebar")?.classList.toggle("open");
      }
    });

    // 绑定六十四卦筛选与搜索
    document.querySelectorAll("#hexFilterTabs .hex-tab").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll("#hexFilterTabs .hex-tab").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        state.activeHexFilter = btn.getAttribute("data-filter");
        renderHexagramsGrid();
      });
    });

    document.getElementById("hexSearchInput")?.addEventListener("input", (e) => {
      state.hexSearchQuery = e.target.value;
      renderHexagramsGrid();
    });

    // 绑定精选成果分类切换
    document.querySelectorAll("#featuredTabs .feat-tab").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll("#featuredTabs .feat-tab").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        state.activeFeaturedCat = btn.getAttribute("data-cat");
        renderFeaturedGrid();
      });
    });

    // 绑定左侧目录过滤
    document.getElementById("sidebarFilterInput")?.addEventListener("input", (e) => {
      renderSidebar(e.target.value);
    });

    // 绑定全局搜索弹窗 (Ctrl+K)
    const openSearch = () => {
      const modal = document.getElementById("searchModal");
      const input = document.getElementById("globalSearchInput");
      modal.classList.remove("hidden");
      input.focus();
      runGlobalSearch(input.value);
    };

    document.getElementById("openSearchBtn")?.addEventListener("click", openSearch);
    document.getElementById("heroSearchBtn")?.addEventListener("click", openSearch);
    document.getElementById("closeSearchBtn")?.addEventListener("click", () => {
      document.getElementById("searchModal").classList.add("hidden");
    });
    document.getElementById("searchModal")?.addEventListener("click", (e) => {
      if (e.target.id === "searchModal") {
        document.getElementById("searchModal").classList.add("hidden");
      }
    });
    document.getElementById("globalSearchInput")?.addEventListener("input", (e) => {
      runGlobalSearch(e.target.value);
    });

    // 绑定灯箱关闭
    document.getElementById("lightboxModal")?.addEventListener("click", () => {
      document.getElementById("lightboxModal").classList.add("hidden");
    });

    window.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        openSearch();
      } else if (e.key === "Escape") {
        document.getElementById("searchModal")?.classList.add("hidden");
        document.getElementById("lightboxModal")?.classList.add("hidden");
      }
    });

    window.addEventListener("hashchange", handleRoute);
    handleRoute();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
"""
