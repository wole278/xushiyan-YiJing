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
          <span class="search-placeholder">检索全库 01–09 文献、卦爻、词义...</span>
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
            <div class="stat-label">01–09 全库学术研究文档</div>
            <div class="stat-note">原典 verify.cmd 逐字核验闭环</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. 01-09 九大研究模块卡片导航 -->
    <section class="home-section" id="modulesSection">
      <div class="section-container">
        <div class="section-header">
          <div>
            <span class="section-eyebrow">NINE RESEARCH MODULES</span>
            <h2 class="section-title">01–09 九大核心研究模块导航</h2>
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
          <button class="feat-tab" data-cat="08">📜 08 源流与哲学史</button>
          <button class="feat-tab" data-cat="09">🧭 09 周易数术纲目</button>
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
   通用章节与 01-09 模块卡片
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
  padding: 14px 14px 40px;
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
  gap: 6px;
  padding: 7px 8px;
  font-family: var(--font-serif);
  font-size: 14px;
  font-weight: 800;
  color: var(--text-primary);
  cursor: pointer;
  border-radius: 6px;
  user-select: none;
}

.tree-mod-header:hover {
  background: var(--bg-surface);
}

.tree-chevron {
  font-size: 12px;
  color: var(--text-muted);
  transition: transform 0.18s ease;
  flex-shrink: 0;
}

.tree-mod-block.collapsed .tree-mod-groups {
  display: none;
}

.tree-group.collapsed .tree-group-items {
  display: none;
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
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  user-select: none;
}

.tree-group-title:hover {
  background: var(--bg-surface);
  color: var(--text-primary);
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

/* ==========================================================================
   数术六维联动工作台 & 8大数术交互式动画沙盘 (.shushu-anim-*)
   ========================================================================== */
.wb-shushu-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 2px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  background: var(--accent-bronze-soft);
  color: var(--accent-bronze);
  border: 1px solid var(--accent-bronze);
}

.shushu-anim-card {
  margin: 26px 0;
  background: var(--bg-surface);
  border: 1px solid var(--border-strong);
  border-top: 4px solid var(--accent-cinnabar);
  border-radius: 12px;
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.shushu-anim-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 18px;
  background: var(--bg-subtle);
  border-bottom: 1px solid var(--border-color);
}

.shushu-anim-title-wrap {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.shushu-anim-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  width: fit-content;
  font-size: 11.5px;
  font-weight: 700;
  padding: 2px 9px;
  border-radius: 4px;
  background: var(--accent-cinnabar-soft);
  color: var(--accent-cinnabar);
}

.shushu-anim-title {
  font-family: var(--font-serif);
  font-size: 17px;
  font-weight: 800;
  color: var(--text-primary);
}

.shushu-anim-controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
}

.shushu-ctrl-btn {
  padding: 6px 11px;
  border-radius: 6px;
  border: 1px solid var(--border-strong);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s ease;
}

.shushu-ctrl-btn:hover:not(:disabled) {
  border-color: var(--accent-cinnabar);
  color: var(--accent-cinnabar);
}

.shushu-ctrl-btn.primary {
  background: var(--accent-cinnabar);
  border-color: var(--accent-cinnabar);
  color: #FAF7F0;
}

.shushu-ctrl-btn.primary:hover {
  opacity: 0.9;
  color: #FAF7F0;
}

.shushu-ctrl-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.shushu-step-track {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 4px;
  padding: 10px 14px;
  background: var(--bg-page);
  border-bottom: 1px solid var(--border-color);
}

.shushu-step-pill {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 6px 4px;
  border-radius: 6px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-muted);
  font-size: 11px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.shushu-step-pill:hover {
  background: var(--bg-subtle);
  color: var(--text-primary);
}

.shushu-step-pill.done {
  color: var(--accent-bronze);
  border-color: rgba(38, 104, 89, 0.25);
}

.shushu-step-pill.active {
  background: var(--accent-cinnabar-soft);
  border-color: var(--accent-cinnabar);
  color: var(--accent-cinnabar);
  font-weight: 700;
}

.shushu-step-num {
  font-family: var(--font-mono);
  font-size: 10.5px;
  font-weight: 700;
}

.shushu-step-lbl {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}

.shushu-anim-body {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.95fr);
  gap: 0;
}

.shushu-anim-stage {
  padding: 18px;
  background: var(--bg-page);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 360px;
}

.shushu-anim-detail {
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: var(--bg-surface);
}

.shushu-detail-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-bottom: 8px;
  border-bottom: 1px dashed var(--border-color);
}

.shushu-detail-title {
  font-family: var(--font-serif);
  font-size: 16px;
  font-weight: 800;
  color: var(--text-primary);
}

.shushu-detail-step-tag {
  font-family: var(--font-mono);
  font-size: 11.5px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  background: var(--accent-gold-soft);
  color: var(--accent-gold);
  flex-shrink: 0;
}

.shushu-detail-block {
  padding: 9px 12px;
  border-radius: 7px;
  background: var(--bg-subtle);
  border-left: 3px solid var(--border-strong);
  font-size: 13px;
  line-height: 1.65;
  color: var(--text-secondary);
}

.shushu-detail-block.mantra { border-left-color: var(--accent-gold); }
.shushu-detail-block.formula { border-left-color: var(--accent-bronze); font-family: var(--font-mono); font-size: 12.2px; }
.shushu-detail-block.board { border-left-color: var(--accent-cinnabar); }
.shushu-detail-block.dialectics { border-left-color: var(--accent-bronze); background: var(--accent-bronze-soft); color: var(--text-primary); }

.shushu-detail-label {
  display: block;
  font-family: var(--font-sans);
  font-size: 11.5px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 3px;
}

/* 盘面网格与动画共用样式 */
.shushu-grid-5x5 {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 4px;
  width: 100%;
  max-width: 400px;
}

.shushu-grid-3x3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 6px;
  width: 100%;
  max-width: 400px;
}

.shushu-grid-4x4 {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 4px;
  width: 100%;
  max-width: 420px;
}

.shushu-cell {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 5px;
  min-height: 54px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.35s ease;
  position: relative;
}

.shushu-cell.hl-red {
  border-color: var(--accent-cinnabar);
  background: var(--accent-cinnabar-soft);
  box-shadow: 0 0 0 2px rgba(178, 56, 42, 0.22);
  animation: shushuPulse 1.8s infinite;
}

.shushu-cell.hl-green {
  border-color: var(--accent-bronze);
  background: var(--accent-bronze-soft);
  box-shadow: 0 0 0 2px rgba(38, 104, 89, 0.2);
}

.shushu-cell.hl-gold {
  border-color: var(--accent-gold);
  background: var(--accent-gold-soft);
  box-shadow: 0 0 0 2px rgba(143, 104, 36, 0.22);
}

.shushu-readout-bar {
  width: 100%;
  margin-top: 12px;
  padding: 8px 12px;
  border-radius: 8px;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 8px;
  font-size: 12px;
}

.shushu-readout-item strong {
  color: var(--accent-cinnabar);
  font-family: var(--font-mono);
}

.shushu-tag {
  display: inline-block;
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 10.5px;
  font-weight: 700;
  line-height: 1.3;
}

.shushu-tag.red { background: var(--accent-cinnabar); color: #FAF7F0; }
.shushu-tag.green { background: var(--accent-bronze); color: #FAF7F0; }
.shushu-tag.gold { background: var(--accent-gold); color: #FAF7F0; }
.shushu-tag.muted { background: var(--bg-subtle); color: var(--text-secondary); border: 1px solid var(--border-color); }

.shushu-coin-spin {
  animation: shushuCoinSpin 0.75s ease-out;
}

.shushu-svg-flow {
  stroke-dasharray: 8 5;
  animation: shushuDashFlow 1.6s linear infinite;
}

.shushu-rotate-ring {
  transition: transform 0.75s cubic-bezier(0.22, 1, 0.36, 1);
  transform-origin: 170px 170px;
}

@keyframes shushuPulse {
  0%, 100% { box-shadow: 0 0 0 1px rgba(178, 56, 42, 0.25); }
  50% { box-shadow: 0 0 0 4px rgba(178, 56, 42, 0.14); }
}

@keyframes shushuCoinSpin {
  0% { transform: rotateY(0deg) scale(0.85); opacity: 0.5; }
  50% { transform: rotateY(360deg) scale(1.1); opacity: 1; }
  100% { transform: rotateY(720deg) scale(1); opacity: 1; }
}

@keyframes shushuDashFlow {
  to { stroke-dashoffset: -26; }
}

@media (max-width: 960px) {
  .shushu-anim-body {
    grid-template-columns: 1fr;
  }
  .shushu-anim-stage {
    border-right: none;
    border-bottom: 1px solid var(--border-color);
  }
  .shushu-step-track {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
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
    collapsedMods: new Set(),
    collapsedGroups: new Set(),
    animTimers: [],
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

  // 4. 渲染首页：01–09 九大模块卡片
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
        const isModCollapsed = !q && state.collapsedMods.has(mod.code);
        const groupsHtml = mod.groups
          .map((grp) => {
            const items = grp.items.filter(
              (item) => !q || item.title.toLowerCase().includes(q) || item.id.toLowerCase().includes(q)
            );
            if (!items.length) return "";

            const grpKey = `${mod.code}::${grp.title}`;
            const isGrpCollapsed = !q && state.collapsedGroups.has(grpKey);

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
            <div class="tree-group ${isGrpCollapsed ? "collapsed" : ""}">
              <div class="tree-group-title" data-grp-toggle="${escapeHtml(grpKey)}">
                <span>${escapeHtml(grp.title)} (${items.length})</span>
                <span class="tree-chevron">${isGrpCollapsed ? "▸" : "▾"}</span>
              </div>
              <div class="tree-group-items">${linksHtml}</div>
            </div>`;
          })
          .join("");

        if (!groupsHtml) return "";
        return `
        <div class="tree-mod-block ${isModCollapsed ? "collapsed" : ""}">
          <div class="tree-mod-header" data-mod-toggle="${escapeHtml(mod.code)}">
            <span>${mod.icon} ${escapeHtml(mod.title)}</span>
            <span class="tree-chevron">${isModCollapsed ? "▸" : "▾"}</span>
          </div>
          <div class="tree-mod-groups">${groupsHtml}</div>
        </div>`;
      })
      .join("");

    // 绑定模块与分组折叠/展开事件
    treeEl.querySelectorAll("[data-mod-toggle]").forEach((hdr) => {
      hdr.addEventListener("click", () => {
        const code = hdr.getAttribute("data-mod-toggle");
        if (state.collapsedMods.has(code)) {
          state.collapsedMods.delete(code);
        } else {
          state.collapsedMods.add(code);
        }
        renderSidebar(document.getElementById("sidebarFilterInput")?.value || "");
      });
    });

    treeEl.querySelectorAll("[data-grp-toggle]").forEach((hdr) => {
      hdr.addEventListener("click", () => {
        const key = hdr.getAttribute("data-grp-toggle");
        if (state.collapsedGroups.has(key)) {
          state.collapsedGroups.delete(key);
        } else {
          state.collapsedGroups.add(key);
        }
        renderSidebar(document.getElementById("sidebarFilterInput")?.value || "");
      });
    });
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
      let rawCode = code;
      let rawLang = infostring;
      if (code && typeof code === "object") {
        rawCode = code.text || "";
        rawLang = code.lang || "";
      }
      const lang = (rawLang || "").trim().toLowerCase();
      if (lang === "mermaid") {
        return `<div class="mermaid-box"><pre class="mermaid">${escapeHtml(rawCode)}</pre></div>`;
      }
      if (lang === "shushu-anim") {
        let cfg = {};
        try {
          cfg = JSON.parse(String(rawCode).trim());
        } catch (e) {
          const mType = String(rawCode).match(/"type"\s*:\s*"([^"]+)"/);
          const mTitle = String(rawCode).match(/"title"\s*:\s*"([^"]+)"/);
          cfg = { type: mType ? mType[1] : "qimen", title: mTitle ? mTitle[1] : "" };
        }
        const animType = escapeHtml(cfg.type || "qimen");
        const animTitle = escapeHtml(cfg.title || "");
        const animPayload = escapeHtml(JSON.stringify(cfg));
        return `<div class="shushu-anim-mount" data-type="${animType}" data-title="${animTitle}" data-config="${animPayload}"></div>`;
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
    // 确保当前文档所属模块与分组在目录树中展开
    if (meta.module) {
      state.collapsedMods.delete(meta.module);
      const modObj = state.manifest.modules.find((m) => m.code === meta.module);
      const grpObj = modObj?.groups.find((g) => g.items.some((it) => it.id === meta.id));
      if (grpObj) {
        state.collapsedGroups.delete(`${meta.module}::${grpObj.title}`);
      }
    }
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

    // 清理旧文档中残留的动画定时器
    if (Array.isArray(state.animTimers)) {
      state.animTimers.forEach((tid) => clearInterval(tid));
      state.animTimers = [];
    }

    // 若关联单卦 (1~64)，渲染「本卦三维联动工作台」；若属 09 数术纲目八大门类，渲染「数术六维联动工作台」
    const wbEl = document.getElementById("hexWorkbench");
    const shushuMatch = meta.id.match(/^09 周易数术纲目\/(0[2-9]_[^/]+)\//);
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
    } else if (shushuMatch) {
      const subDir = shushuMatch[1];
      const prefix = `09 周易数术纲目/${subDir}/`;
      const siblings = state.manifest.searchIndex
        .filter((d) => d.id.startsWith(prefix) && d.name !== "README.md")
        .sort((a, b) => a.id.localeCompare(b.id, "zh-CN"));
      const catNames = {
        "02_太乙神数": "🌌 三式绝学 · 02_太乙神数",
        "03_奇门遁甲": "🌌 三式绝学 · 03_奇门遁甲",
        "04_大六壬": "🌌 三式绝学 · 04_大六壬",
        "05_六爻纳甲": "☯️ 象数卜筮 · 05_六爻纳甲",
        "06_四柱八字": "⭐ 禄命星占 · 06_四柱八字",
        "07_紫微斗数": "⭐ 禄命星占 · 07_紫微斗数",
        "08_风水堪舆": "⛰️ 形法相地 · 08_风水堪舆",
        "09_相术摸骨": "⛰️ 形法相地 · 09_相术摸骨",
      };
      const tabLabel = (item) => {
        if (item.name.startsWith("01_")) return "📜 01 源流详考";
        if (item.name.startsWith("02_")) return "🎓 02 分级教程";
        if (item.name.startsWith("03_")) return "🎬 03 动画实操演练";
        if (item.name.startsWith("04_")) return "📖 04 经典一";
        if (item.name.startsWith("05_")) return "📖 05 经典二";
        if (item.name.startsWith("06_")) return "📖 06 经典三";
        return item.title;
      };
      const badgeText = catNames[subDir] || `🧭 ${subDir}`;
      wbEl.classList.remove("hidden");
      wbEl.innerHTML = `
        <div class="wb-top">
          <div class="wb-title-wrap">
            <span class="wb-shushu-badge">${escapeHtml(badgeText)}</span>
            <div class="wb-guaci">源流详考 · 分级教程 · 动画实操演练 · 三大权威古籍全文（六维联动工作台）</div>
          </div>
        </div>
        <div class="wb-tabs">
          ${siblings
            .map(
              (s) =>
                `<a href="#/doc/${encodeURIComponent(s.id)}" class="wb-tab ${
                  meta.id === s.id ? "active" : ""
                }" title="${escapeHtml(s.title)}">${escapeHtml(tabLabel(s))}</a>`
            )
            .join("")}
        </div>
      `;
    } else {
      wbEl.classList.add("hidden");
    }

    // 渲染正文
    const bodyEl = document.getElementById("markdownBody");
    bodyEl.innerHTML = renderMarkdownWithExtensions(docData.content);

    // 初始化数术交互式 HTML5/SVG 动画沙盘
    initShushuAnimations(bodyEl);

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

  // 12B. 数术交互式 HTML5/SVG 动画实操沙盘引擎 (8大门类)
  const SHUSHU_ENGINES = {
    taiyi: {
      badge: "🌌 三式绝学 · 太乙神数",
      defaultTitle: "太乙神数十六神九宫动态推演沙盘（阳遁局 · 乾一宫例）",
      steps: [
        {
          label: "太乙定宫",
          title: "Step 1 · 太乙入乾一宫（天道总纲定基）",
          mantra: "太乙行九宫：一乾、二离、三艮、四震、中五不居、六兑、七坤、八坎、九巽。",
          formula: "太乙落宫 = 阳遁局数 mod 24（三年一宫），本例定居【乾一宫】",
          boardNote: "太乙星落入内盘东南角（乾六洛书位 / 太乙第一宫），外盘十六神「乾」位同步点亮。",
          dialectics: "以周期性大尺度宏观节律建立时空坐标系，反映古代农业文明对太阳—木星岁差周期的数理抽象。",
        },
        {
          label: "文昌主目",
          title: "Step 2 · 文昌（主目）落外盘酉位",
          mantra: "文昌起申顺行十六神，遇四仲阳九、四维阴六而进退，主一方之纲纪。",
          formula: "主目（文昌）= 酉位（对应内盘兑六宫旁）",
          boardNote: "外盘十六神「酉」位亮起金印，主目文昌由酉位向太乙乾宫建立主方算距连线。",
          dialectics: "「主目」代表既有系统内部的主导秩序与核心观测站，确立主客博弈中的参照基准。",
        },
        {
          label: "始击客目",
          title: "Step 3 · 始击（客目）飞临外盘卯位",
          mantra: "计神起寅逆行，始击自艮顺行十六神，客目动而变生。",
          formula: "客目（始击）= 卯位（对应内盘震四宫旁）",
          boardNote: "外盘「卯」位亮起青铜标记，与对宫文昌形成东西遥峙，牵动外部变量入局。",
          dialectics: "「客目」表征外部冲击变量与突发扰动因素，形成主客双方的矛盾对立统一体。",
        },
        {
          label: "主算主将",
          title: "Step 4 · 计主算（14）定主大将（4）与主参将（2）",
          mantra: "文昌数至太乙前一位得主算；以主算去十用零为大将，三乘大将去十为参将。",
          formula: "主算 = 14 → 主大将 = 4（震四宫），主参将 = (3 × 4) mod 10 = 2（离二宫）",
          boardNote: "内盘震四宫亮起「主大将 4」，离二宫亮起「主参将 2」，主方兵力纵深成形。",
          dialectics: "主算与参将之比体现了内部防御纵深与协同动员能力，属矛盾内因的量化表征。",
        },
        {
          label: "客算客将",
          title: "Step 5 · 计客算（27）定客大将（7）与客参将（1）",
          mantra: "始击顺数至太乙前一位得客算；余数定客大将，三乘客将得客参将。",
          formula: "客算 = 27 → 客大将 = 7（坤七宫），客参将 = (3 × 7) mod 10 = 1（乾一宫）",
          boardNote: "客大将落坤七宫，客参将「1」直入太乙所在乾一宫，形成客将逼宫态势！",
          dialectics: "外部冲击力量沿算程穿透至系统核心节点，揭示危机向中枢传导的临界阈值。",
        },
        {
          label: "定算八门",
          title: "Step 6 · 定算（19）与八门值事（生门）",
          mantra: "太岁合神起定算，配八门值事以辨休咎通塞。",
          formula: "定算 = 19 → 定大将 = 9（巽九宫），定参将 = 7（坤七宫）；值事 = 生门",
          boardNote: "巽九宫与坤七宫点亮定算坐标，乾宫旁注「生门值事」，系统尚存生发调节余地。",
          dialectics: "定算代表整体局势的时空约束边界，八门则对应不同阶段的战略通道开合状态。",
        },
        {
          label: "掩迫决断",
          title: "Step 7 · 掩迫关格扫描与主客强弱决断",
          mantra: "客参将与太乙同宫曰「内迫」，主算14（长和）胜客算27（单阴重迫）。",
          formula: "判据：主算14（和数守稳） vs 客参将1迫太乙（外扰内逼） → 宜守御生门、固本待变",
          boardNote: "全盘高亮主客两线冲突节点：主方固守震离纵深，化解客参将迫宫之势。",
          dialectics: "唯物辩证结语：太乙数理并非天命预言，而是通过主客参量对比揭示系统稳态与外部冲击的张力平衡。",
        },
      ],
      renderStage(step) {
        // 5x5 outer 16 spirits + inner 3x3 Luoshu (row 0..4, col 0..4)
        const outerCells = {
          "0,0": "巽", "0,1": "巳", "0,2": "午", "0,3": "未", "0,4": "坤",
          "1,4": "申", "2,4": "酉", "3,4": "戌",
          "4,4": "乾", "4,3": "亥", "4,2": "子", "4,1": "丑", "4,0": "艮",
          "3,0": "寅", "2,0": "卯", "1,0": "辰",
        };
        // Inner 3x3: Luoshu + Taiyi palace index
        const innerCells = {
          "1,1": { l: "4巽", t: "太乙九巽", k: "p9" },
          "1,2": { l: "9离", t: "太乙二离", k: "p2" },
          "1,3": { l: "2坤", t: "太乙七坤", k: "p7" },
          "2,1": { l: "3震", t: "太乙四震", k: "p4" },
          "2,2": { l: "中5", t: "中五无位", k: "p5" },
          "2,3": { l: "7兑", t: "太乙六兑", k: "p6" },
          "3,1": { l: "8艮", t: "太乙三艮", k: "p3" },
          "3,2": { l: "1坎", t: "太乙八坎", k: "p8" },
          "3,3": { l: "6乾", t: "太乙一乾", k: "p1" },
        };
        let html = `<div class="shushu-grid-5x5">`;
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            const key = `${r},${c}`;
            if (outerCells[key]) {
              const name = outerCells[key];
              let cls = "";
              let tags = [];
              if (name === "乾" && step >= 0) { cls = "hl-red"; tags.push(`<span class="shushu-tag red">太乙</span>`); }
              if (name === "酉" && step >= 1) { cls = "hl-gold"; tags.push(`<span class="shushu-tag gold">文昌</span>`); }
              if (name === "卯" && step >= 2) { cls = "hl-green"; tags.push(`<span class="shushu-tag green">始击</span>`); }
              if (name === "艮" && step >= 5) { tags.push(`<span class="shushu-tag muted">生门</span>`); }
              html += `<div class="shushu-cell ${cls}" style="align-items:center;text-align:center">
                <strong style="font-family:var(--font-serif);font-size:14px">${name}</strong>
                <div style="display:flex;gap:2px;flex-wrap:wrap;justify-content:center">${tags.join("")}</div>
              </div>`;
            } else {
              const info = innerCells[key];
              let cls = "";
              let tags = [];
              if (info.k === "p1" && step >= 0) { cls = "hl-red"; tags.push(`<span class="shushu-tag red">太乙</span>`); }
              if (info.k === "p4" && step >= 3) { cls = "hl-gold"; tags.push(`<span class="shushu-tag gold">主大4</span>`); }
              if (info.k === "p2" && step >= 3) { cls = "hl-gold"; tags.push(`<span class="shushu-tag gold">主参2</span>`); }
              if (info.k === "p7" && step >= 4) { cls = "hl-green"; tags.push(`<span class="shushu-tag green">客大7</span>`); }
              if (info.k === "p1" && step >= 4) { tags.push(`<span class="shushu-tag green">客参1</span>`); }
              if (info.k === "p9" && step >= 5) { tags.push(`<span class="shushu-tag muted">定大9</span>`); }
              if (info.k === "p7" && step >= 5) { tags.push(`<span class="shushu-tag muted">定参7</span>`); }
              if (info.k === "p1" && step >= 6) { tags.push(`<span class="shushu-tag red">迫</span>`); }
              html += `<div class="shushu-cell ${cls}" style="background:var(--bg-subtle)">
                <div style="display:flex;justify-content:space-between;font-size:11px;font-weight:700">
                  <span>${info.l}</span>
                </div>
                <div style="font-size:10px;color:var(--text-muted)">${info.t}</div>
                <div style="display:flex;gap:2px;flex-wrap:wrap">${tags.join("")}</div>
              </div>`;
            }
          }
        }
        html += `</div>`;
        const zhu = step >= 3 ? "14 (大将4 · 参将2)" : "待算";
        const ke = step >= 4 ? "27 (大将7 · 参将1)" : "待算";
        const ding = step >= 5 ? "19 (大将9 · 生门)" : "待算";
        html += `<div class="shushu-readout-bar">
          <div class="shushu-readout-item">太乙：<strong>乾一宫</strong></div>
          <div class="shushu-readout-item">主算：<strong>${zhu}</strong></div>
          <div class="shushu-readout-item">客算：<strong>${ke}</strong></div>
          <div class="shushu-readout-item">定算：<strong>${ding}</strong></div>
        </div>`;
        return html;
      },
    },

    qimen: {
      badge: "🌌 三式绝学 · 奇门遁甲",
      defaultTitle: "奇门遁甲洛书九宫排盘动画（冬至阳遁一局 · 丙寅时）",
      steps: [
        {
          label: "阳遁定局",
          title: "Step 1 · 冬至上元 · 阳遁一局定局",
          mantra: "冬至惊蛰一七四，小寒二八五依次；戴九履一、左三右七。",
          formula: "节气：冬至上元 → 阳遁一局（顺布六仪、逆布三奇，阳遁顺行）",
          boardNote: "3×3 洛书九宫盘确立，配后天八卦名与五行底色（坎水、离火、震巽木、乾兑金、坤艮中土）。",
          dialectics: "以冬至太阳回归点确立年度周期起点，将空间八方与季节五行耦合为九宫拓扑矩阵。",
        },
        {
          label: "地盘奇仪",
          title: "Step 2 · 地盘三奇六仪顺飞落宫",
          mantra: "戊己庚辛壬癸丁丙乙，阳遁顺飞九宫不移位。",
          formula: "1坎戊 → 2坤己 → 3震庚 → 4巽辛 → 5中壬 → 6乾癸 → 7兑丁 → 8艮丙 → 9离乙",
          boardNote: "九宫地盘干依次飞落：甲子戊居坎一宫，月奇丙居艮八宫，日奇乙居离九宫。",
          dialectics: "地盘奇仪构成相对稳定的空间基底条件，后续天人神三盘皆在此基底上产生相对位移。",
        },
        {
          label: "值符值使",
          title: "Step 3 · 甲子戊旬首定天蓬值符与休门值使",
          mantra: "时干丙寅属甲子戊旬，甲子所在之宫星为值符、门为值使。",
          formula: "丙寅时 ∈ 甲子戊旬（地盘1坎） → 值符 = 天蓬星，值使 = 休门",
          boardNote: "坎一宫高亮聚焦：本宫九星「天蓬」定为值符，本宫八门「休门」定为值使。",
          dialectics: "旬首象征当前时间切片的统领变量，「值符/值使」分别主宰宏观天时势能与中观人事通道。",
        },
        {
          label: "天盘九星",
          title: "Step 4 · 天盘九星随值符加临丙寅时干（落艮八宫）",
          mantra: "值符随时干，天蓬携戊加临地盘丙奇（艮八宫），九星顺转一宫。",
          formula: "时干 = 丙（地盘8艮） → 天蓬+戊落艮8，天任+丙落震3，其余顺布",
          boardNote: "天盘九星环顺时针旋转一格，天蓬星携「戊」飞临艮八宫，与地盘「丙」重合。",
          dialectics: "「值符随时干」刻画主导能量随时间流逝在空间拓扑上的迁移与重构规律。",
        },
        {
          label: "人盘八门",
          title: "Step 5 · 人盘八门随值使加临寅支（落艮八宫）",
          mantra: "值使随时宫，休门加临艮八宫（寅艮东北方），八门依序顺转。",
          formula: "艮8休 → 震3生 → 巽4伤 → 离9杜 → 坤2景 → 兑7死 → 乾6惊 → 坎1开",
          boardNote: "八门人盘就位：休门随值使落入艮八宫，开门飞临坎一宫，生门飞临震三宫。",
          dialectics: "八门对应人类实践活动的不同行动策略（休养、开拓、攻伐、闭守），随局势动态流转。",
        },
        {
          label: "神盘八神",
          title: "Step 6 · 神盘八神自值符落宫顺布",
          mantra: "小值符追随大值符，阳顺阴逆布腾蛇、太阴、六合、白虎、玄武、九地、九天。",
          formula: "艮8值符 → 震3腾蛇 → 巽4太阴 → 离9六合 → 坤2白虎 → 兑7玄武 → 乾6九地 → 坎1九天",
          boardNote: "八神层叠入九宫左上角：值符镇守艮八宫，九天高悬坎一宫，六合临离九宫。",
          dialectics: "八神乃抽象心理预期与隐性环境态势的符号化表达，完善「天—地—人—神」四层耦合模型。",
        },
        {
          label: "吉凶判读",
          title: "Step 7 · 吉凶格高亮判读（青龙返首 · 奇仪相合）",
          mantra: "甲子戊加丙奇曰「青龙返首」，若遇值符休门齐聚，百事皆宜。",
          formula: "艮8宫 = 天盘戊 + 地盘丙（青龙返首大吉格）＋ 值符天蓬 ＋ 休门",
          boardNote: "艮八宫触发「青龙返首」金红双光高亮；同时标出乾6「丁+癸朱雀投江」与离9「辛+乙白虎猖狂」凶格作对照。",
          dialectics: "式盘判读的本质是在多维参量交汇处识别最优可行域（艮8奇仪吉格）与高风险盲区（乾6/离9）。",
        },
      ],
      renderStage(step) {
        // Order: 巽4, 离9, 坤2 / 震3, 中5, 兑7 / 艮8, 坎1, 乾6
        const palaces = [
          { no: 4, name: "巽四", elem: "木", color: "#266859", di: "辛", tian: "冲", tg: "庚", men: "伤", shen: "太阴" },
          { no: 9, name: "离九", elem: "火", color: "#B2382A", di: "乙", tian: "辅", tg: "辛", men: "杜", shen: "六合" },
          { no: 2, name: "坤二", elem: "土", color: "#8F6824", di: "己", tian: "英", tg: "乙", men: "景", shen: "白虎" },
          { no: 3, name: "震三", elem: "木", color: "#266859", di: "庚", tian: "任", tg: "丙", men: "生", shen: "腾蛇" },
          { no: 5, name: "中五", elem: "土", color: "#8F6824", di: "壬", tian: "禽", tg: "—", men: "寄", shen: "—" },
          { no: 7, name: "兑七", elem: "金", color: "#7B858E", di: "丁", tian: "芮", tg: "己", men: "死", shen: "玄武" },
          { no: 8, name: "艮八", elem: "土", color: "#8F6824", di: "丙", tian: "蓬", tg: "戊", men: "休", shen: "值符" },
          { no: 1, name: "坎一", elem: "水", color: "#2B5B84", di: "戊", tian: "心", tg: "癸", men: "开", shen: "九天" },
          { no: 6, name: "乾六", elem: "金", color: "#7B858E", di: "癸", tian: "柱", tg: "丁", men: "惊", shen: "九地" },
        ];
        const diOrder = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        let html = `<div class="shushu-grid-3x3">`;
        palaces.forEach((p) => {
          let cls = "";
          if (step === 2 && p.no === 1) cls = "hl-red";
          if (step === 3 && p.no === 8) cls = "hl-gold";
          if (step === 4 && p.no === 8) cls = "hl-green";
          if (step === 5 && p.no === 8) cls = "hl-gold";
          if (step === 6 && p.no === 8) cls = "hl-red";
          if (step === 6 && p.no === 6) cls = "hl-gold";
          const showDi = step >= 1;
          const showTian = step >= 3 && p.no !== 5;
          const showMen = step >= 4 && p.no !== 5;
          const showShen = step >= 5 && p.no !== 5;
          let patternBadge = "";
          if (step >= 6 && p.no === 8) patternBadge = `<span class="shushu-tag red">青龙返首</span>`;
          if (step >= 6 && p.no === 6) patternBadge = `<span class="shushu-tag muted">朱雀投江</span>`;
          if (step >= 6 && p.no === 9) patternBadge = `<span class="shushu-tag muted">白虎猖狂</span>`;

          html += `<div class="shushu-cell ${cls}" style="min-height:82px;border-top:3px solid ${p.color}">
            <div style="display:flex;justify-content:space-between;font-size:10.5px">
              <span style="color:var(--text-muted)">${showShen ? p.shen : ""}</span>
              <span style="font-weight:700;color:${p.color}">${p.name}·${p.elem}</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:13px;font-weight:700;margin:2px 0">
              <span>${showTian ? "天" + p.tian : ""}</span>
              <span style="color:var(--accent-cinnabar)">${showTian ? p.tg : ""}</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:12px">
              <span style="color:var(--accent-bronze);font-weight:700">${showMen ? p.men + "门" : ""}</span>
              <span>${showDi ? "地:" + p.di : ""}</span>
            </div>
            ${patternBadge ? `<div style="margin-top:2px;text-align:center">${patternBadge}</div>` : ""}
          </div>`;
        });
        html += `</div>`;
        html += `<div class="shushu-readout-bar">
          <div class="shushu-readout-item">局数：<strong>冬至阳遁一局</strong></div>
          <div class="shushu-readout-item">时柱：<strong>丙寅 (甲子旬)</strong></div>
          <div class="shushu-readout-item">值符/值使：<strong>${step >= 2 ? "天蓬 / 休门" : "待定"}</strong></div>
          <div class="shushu-readout-item">格局：<strong>${step >= 6 ? "艮8 戊+丙 青龙返首" : "推演中"}</strong></div>
        </div>`;
        return html;
      },
    },

    liuren: {
      badge: "🌌 三式绝学 · 大六壬",
      defaultTitle: "大六壬月将加时与四课三传九宗门沙盘（甲子日 · 亥将辰时）",
      steps: [
        {
          label: "月将登明",
          title: "Step 1 · 雨水后太阳过亥定登明月将",
          mantra: "雨水后日躔娵訾（亥宫），月将即为登明亥。",
          formula: "月将 = 亥（登明）｜ 占时 = 辰时（正时）｜ 日干支 = 甲子",
          boardNote: "地盘十二支方阵中「亥」位高亮，标注登明月将；日干甲寄寅宫、日支在子宫。",
          dialectics: "「月将」本质是太阳黄道实测视位置（太阳过宫），体现六壬重天文实测之科学内核。",
        },
        {
          label: "月将加时",
          title: "Step 2 · 月将亥加正时辰旋转天盘十二宫",
          mantra: "月将加正时，顺转天盘定十二支上下对应。",
          formula: "天盘亥 → 地盘辰（顺移 +7 宫：子上未、寅上酉、未上寅）",
          boardNote: "天盘十二支顺转飞入各宫，「辰」宫上显「亥」，「子」宫上显「未」，「未」宫上显「寅」。",
          dialectics: "将太阳黄道角位置（月将）与地球自转周日角位置（占时）作相位差叠加，形成天地盘耦合。",
        },
        {
          label: "起出四课",
          title: "Step 3 · 甲子日干寄寅、日支子起出四课",
          mantra: "甲课在寅，取干支上神与阴神，排定一二三四课。",
          formula: "一课(干阳): 未/寅 ｜ 二课(干阴): 寅/未 ｜ 三课(支阳): 未/子 ｜ 四课(支阴): 寅/未",
          boardNote: "右侧四课卡依次点亮：呈现干阳未、干阴寅、支阳未、支阴寅（标注甲寄寅与子丑合化推演）。",
          dialectics: "四课构建了主体（日干）与客观处境（日支）的直接作用关系与二阶反馈关系。",
        },
        {
          label: "九宗门筛",
          title: "Step 4 · 九宗门贼克 / 比用 / 涉害筛选动态扫描",
          mantra: "取课先从下贼呼，若无下贼上克初；重克比用择阳比，涉害深浅细权衡。",
          formula: "扫描四课五行生克：未土克子水（上克下）、寅木克未土（上克下） → 经比用/涉害裁定发用",
          boardNote: "四课卡片逐一闪过克贼扫描标尺，锁定发用起点「未」。",
          dialectics: "九宗门实质是一套严谨的多重冲突消解算法，旨在从交错生克中提取主要矛盾（初传）。",
        },
        {
          label: "提取三传",
          title: "Step 5 · 提取初传（未）、中传（寅）、末传（酉）",
          mantra: "既得初传，取其上神为中传，再取中传上神为末传。",
          formula: "初传 = 未 → 地盘未上见【寅】（中传） → 地盘寅上见【酉】（末传）",
          boardNote: "三传阶梯区高亮「未 → 寅 → 酉」，方盘内三宫联动标出传序轨迹。",
          dialectics: "三传对应事物演进的「始因—中转—终局」三阶动力学轨迹，呈现因果链条的时序展开。",
        },
        {
          label: "天将六亲",
          title: "Step 6 · 昼贵人（未）顺布十二天将与遁干六亲",
          mantra: "贵人既定，依亥子丑寅顺行布蛇雀合勾龙空虎常玄阴后。",
          formula: "昼贵在未（未贵、申蛇、酉雀、戌合、亥勾、子龙、丑空、寅虎、卯常、辰玄、巳阴、午后）",
          boardNote: "十二宫天将全面显现；三传标注甲日六亲：未（妻财）、寅（比肩）、酉（官鬼）。",
          dialectics: "天将与六亲系统为动力学轨迹赋予社会关系、组织资源与制度约束的语义映射。",
        },
        {
          label: "三传总断",
          title: "Step 7 · 三传吉凶总断（财→比→官因果链）",
          mantra: "初传未财发用、中传寅比争竞、末传酉官收束，先利后争终归法度。",
          formula: "未土(妻财·贵人) ──克→ 寅木(比肩·白虎) ──克→ 酉金(官鬼·朱雀)",
          boardNote: "全盘高亮三传路径，提示：初得贵人财助，中防同侪分夺（白虎），末宜守正依规（官鬼）。",
          dialectics: "大六壬以精密数学同态变换刻画复杂博弈过程，揭示利益诱发竞争、竞争归于秩序的普遍规律。",
        },
      ],
      renderStage(step) {
        // 4x4 hollow square:
        // Row0: 巳 午 未 申
        // Row1: 辰 [center] 酉
        // Row2: 卯 [center] 戌
        // Row3: 寅 丑 子 亥
        const tianMap = {
          "巳": "子", "午": "丑", "未": "寅", "申": "卯",
          "酉": "辰", "戌": "巳", "亥": "午", "子": "未",
          "丑": "申", "寅": "酉", "卯": "戌", "辰": "亥",
        };
        const jiangMap = {
          "未": "贵人", "申": "腾蛇", "酉": "朱雀", "戌": "六合",
          "亥": "勾陈", "子": "青龙", "丑": "天空", "寅": "白虎",
          "卯": "太常", "辰": "玄武", "巳": "太阴", "午": "天后",
        };
        const layout = [
          ["巳", "午", "未", "申"],
          ["辰", null, null, "酉"],
          ["卯", null, null, "戌"],
          ["寅", "丑", "子", "亥"],
        ];
        let gridHtml = `<div class="shushu-grid-4x4" style="max-width:340px">`;
        for (let r = 0; r < 4; r++) {
          for (let c = 0; c < 4; c++) {
            const zhi = layout[r][c];
            if (!zhi) {
              if (r === 1 && c === 1) {
                const keList = [
                  { name: "一课·干阳", top: "未", bot: "寅", hl: step === 2 || step === 3 },
                  { name: "二课·干阴", top: "寅", bot: "未", hl: step === 2 || step === 3 },
                  { name: "三课·支阳", top: "未", bot: "子", hl: step === 2 || step === 3 },
                  { name: "四课·支阴", top: "寅", bot: "未", hl: step === 2 || step === 3 },
                ];
                const chuanList = [
                  { k: "初传", z: "未", q: "妻财", j: "贵人" },
                  { k: "中传", z: "寅", q: "比肩", j: "白虎" },
                  { k: "末传", z: "酉", q: "官鬼", j: "朱雀" },
                ];
                gridHtml += `<div style="grid-column:2/4;grid-row:2/4;background:var(--bg-surface);border:1px dashed var(--border-strong);border-radius:8px;padding:8px;display:flex;flex-direction:column;justify-content:space-between;font-size:11px">
                  <div style="font-weight:700;color:var(--accent-cinnabar);text-align:center">四课 · 三传中枢</div>
                  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3px;text-align:center">
                    ${keList.map((k) => `<div style="padding:3px 2px;border-radius:4px;border:1px solid ${k.hl ? "var(--accent-cinnabar)" : "var(--border-color)"};background:${step >= 2 ? "var(--bg-subtle)" : "transparent"}">
                      <div style="font-size:9px;color:var(--text-muted)">${k.name.slice(0,2)}</div>
                      <div style="font-weight:700">${step >= 2 ? k.top : "—"}</div>
                      <div>${step >= 2 ? k.bot : "—"}</div>
                    </div>`).join("")}
                  </div>
                  <div style="display:flex;justify-content:space-around;gap:4px;padding-top:4px;border-top:1px dashed var(--border-color)">
                    ${chuanList.map((ch) => `<div style="text-align:center;padding:3px 5px;border-radius:4px;background:${step >= 4 ? "var(--accent-cinnabar-soft)" : "var(--bg-subtle)"};border:1px solid ${step >= 4 ? "var(--accent-cinnabar)" : "var(--border-color)"}">
                      <div style="font-size:9px;color:var(--text-muted)">${ch.k}</div>
                      <div style="font-weight:800;font-size:13px">${step >= 4 ? ch.z : "?"}</div>
                      <div style="font-size:9.5px;color:var(--accent-bronze)">${step >= 5 ? ch.q + "·" + ch.j : ""}</div>
                    </div>`).join("")}
                  </div>
                </div>`;
              }
              continue;
            }
            const tian = tianMap[zhi];
            const jiang = jiangMap[tian];
            let cls = "";
            if (step === 0 && zhi === "亥") cls = "hl-red";
            if (step === 1 && (zhi === "辰" || zhi === "亥")) cls = "hl-gold";
            if (step >= 4 && ["未", "寅", "酉"].includes(tian)) cls = "hl-red";
            if (step === 5 && tian === "未") cls = "hl-gold";
            gridHtml += `<div class="shushu-cell ${cls}" style="min-height:58px">
              <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-muted)">
                <span>地:${zhi}</span>
                <span style="color:var(--accent-bronze);font-weight:700">${step >= 5 ? jiang : ""}</span>
              </div>
              <div style="font-family:var(--font-serif);font-size:15px;font-weight:800;text-align:center;color:var(--accent-cinnabar)">
                ${step >= 1 ? tian : zhi}
              </div>
            </div>`;
          }
        }
        gridHtml += `</div>`;
        gridHtml += `<div class="shushu-readout-bar">
          <div class="shushu-readout-item">月将/占时：<strong>亥将 / 辰时</strong></div>
          <div class="shushu-readout-item">宗门：<strong>${step >= 3 ? "比用 / 涉害" : "待扫描"}</strong></div>
          <div class="shushu-readout-item">三传：<strong>${step >= 4 ? "未 → 寅 → 酉" : "推演中"}</strong></div>
        </div>`;
        return gridHtml;
      },
    },

    liuyao: {
      badge: "☯️ 象数卜筮 · 六爻纳甲",
      defaultTitle: "六爻纳甲摇卦与火天大有变火风鼎全息排盘沙盘",
      steps: [
        {
          label: "铜钱摇卦",
          title: "Step 1 · 三枚乾隆通宝六次摇卦生成主变卦",
          mantra: "一背为单（⚊）、二背为拆（⚋）、三背重（○老阳动）、三字交（×老阴动）。",
          formula: "初爻至上爻自下而上成卦：火天大有 ䷍（初九、九四动）→ 火风鼎 ䷱",
          boardNote: "三枚铜钱动画翻转落定，自下而上生成六爻，初九与九四标出红圈「○ 动」标识。",
          dialectics: "六次独立随机采样将不确定扰动映射为六维二元向量（64卦态空间）及其动态跃迁分量。",
        },
        {
          label: "认宫世应",
          title: "Step 2 · 乾宫归魂认宫定世爻（九三）与应爻（上九）",
          mantra: "八卦之首乾为天，游魂四世归魂三；火天大有乃乾宫归魂卦。",
          formula: "本宫 = 乾宫（金）｜ 世爻 = 九三（主方）｜ 应爻 = 上九（客方）",
          boardNote: "九三亮起「世」金印、上九亮起「应」青印，确立主客对偶参照坐标。",
          dialectics: "「世/应」界定了系统内部主体立场（世）与外部对象（应）之间的位置关系。",
        },
        {
          label: "浑天纳甲",
          title: "Step 3 · 浑天甲子纳本卦与变卦地支",
          mantra: "乾在内子寅辰，离在外酉未巳；巽在内丑亥酉。",
          formula: "本卦（大有）：子、寅、辰、酉、未、巳 ｜ 变卦（鼎）：丑、亥、酉、酉、未、巳",
          boardNote: "本卦与变卦六爻均配齐十二地支与五行属性，打通卦象与干支时序的映射通道。",
          dialectics: "京房纳甲法把离散的易卦符号编码进十二地支时间循环代数结构中。",
        },
        {
          label: "六亲六神",
          title: "Step 4 · 排布乾宫六亲与甲日六神",
          mantra: "乾宫属金，克我官鬼、我克妻财、生我父母、我生子孙、同我兄弟；甲乙起青龙。",
          formula: "六亲：子孙子、妻财寅、父母辰(世)、兄弟酉、父母未、官鬼巳(应)；六神：龙雀陈蛇虎武",
          boardNote: "左侧六神（青龙至玄武）与中央六亲全盘就位，社会与自然属性一目了然。",
          dialectics: "以宫位五行为基准点计算五类相对关系（生、克、同、泄、耗），构建关系网络图谱。",
        },
        {
          label: "月建日辰",
          title: "Step 5 · 注入月建（寅木）与日辰（子水）旺衰标尺",
          mantra: "月建司权掌提纲，日辰冲合定真机；寅月木旺水休土死。",
          formula: "月建 = 寅木（寅财旺、子孙休、辰未土死）｜ 日辰 = 子水（生寅木、助子水、合丑土）",
          boardNote: "顶部月日标尺点亮，各爻旁显示实时旺衰标签（旺/相/休/囚/死）。",
          dialectics: "月建与日辰代表客观环境背景场对局部节点强弱的实时调制（外因制约内因）。",
        },
        {
          label: "动变生克",
          title: "Step 6 · 动爻初九子水化巽木、九四辰土化酉金回头生克连线",
          mantra: "动爻为变机之枢，化生、化克、化合决定事物转折方向。",
          formula: "初九子水（动）化变象（巽木 / 丑合）⊕ 九四（酉金）与辰土父母联动相生（土生金）",
          boardNote: "右侧 SVG 发光弧线连亮：展示动爻向变爻的能量流向与辰酉生合/子丑羁绊连线。",
          dialectics: "静爻代表常态结构，动爻则刻画系统发生质变的突破口及其引发的链式反馈。",
        },
        {
          label: "用神应期",
          title: "Step 7 · 用神与吉凶应期决断",
          mantra: "大有变鼎（革故鼎新），财爻寅木得月建临旺、日辰子水相生。",
          formula: "取妻财寅木为用神：得寅月临值、日水相生、初爻子水动生，主守成革鼎而得实利。",
          boardNote: "全盘高亮用神「九二 寅木 妻财」及「九三 世爻」，完成多维综合判读。",
          dialectics: "唯物结语：纳甲法以多因素权重叠加模拟复杂决策权衡，核心在审时度势（月日旺衰）与抓主要矛盾（用神动变）。",
        },
      ],
      renderStage(step) {
        const yaos = [
          { pos: "上九", yin: false, shen: "玄武", qin: "官鬼", zhi: "巳火", wang: "相", shi: "应", mov: false, bQ: "官鬼", bZ: "巳火" },
          { pos: "六五", yin: true,  shen: "白虎", qin: "父母", zhi: "未土", wang: "死", shi: "",   mov: false, bQ: "父母", bZ: "未土" },
          { pos: "九四", yin: false, shen: "螣蛇", qin: "兄弟", zhi: "酉金", wang: "囚", shi: "",   mov: true,  bQ: "父母", bZ: "辰/酉" },
          { pos: "九三", yin: false, shen: "勾陈", qin: "父母", zhi: "辰土", wang: "死", shi: "世", mov: false, bQ: "兄弟", bZ: "酉金" },
          { pos: "九二", yin: false, shen: "朱雀", qin: "妻财", zhi: "寅木", wang: "旺", shi: "",   mov: false, bQ: "子孙", bZ: "亥水" },
          { pos: "初九", yin: false, shen: "青龙", qin: "子孙", zhi: "子水", wang: "休", shi: "",   mov: true,  bQ: "巽木", bZ: "丑/巽" },
        ];
        // 3 Drylong coins SVG
        const coinSvg = (idx, face) => `<svg width="36" height="36" viewBox="0 0 40 40" class="${step === 0 ? "shushu-coin-spin" : ""}">
          <circle cx="20" cy="20" r="18" fill="#D4A857" stroke="#8F6824" stroke-width="2"/>
          <rect x="14" y="14" width="12" height="12" fill="var(--bg-page)" stroke="#8F6824" stroke-width="1.5"/>
          <text x="20" y="11" text-anchor="middle" font-size="6.5" fill="#4A320A" font-weight="bold">${face ? "乾" : "隆"}</text>
          <text x="20" y="34" text-anchor="middle" font-size="6.5" fill="#4A320A" font-weight="bold">${face ? "宝" : "通"}</text>
        </svg>`;

        let html = `<div style="width:100%;display:flex;flex-direction:column;gap:8px">
          <div style="display:flex;justify-content:space-between;align-items:center;padding:6px 10px;background:var(--bg-surface);border:1px solid var(--border-color);border-radius:8px">
            <div style="display:flex;align-items:center;gap:6px">
              ${coinSvg(0, true)}${coinSvg(1, step !== 0)}${coinSvg(2, true)}
              <span style="font-size:11.5px;color:var(--text-secondary)">乾隆通宝摇卦</span>
            </div>
            <div style="font-size:11.5px;font-weight:700;color:${step >= 4 ? "var(--accent-cinnabar)" : "var(--text-muted)"}">
              ${step >= 4 ? "月建:寅木 ｜ 日辰:子水" : "火天大有 ䷍ → 火风鼎 ䷱"}
            </div>
          </div>
          <div style="position:relative;background:var(--bg-surface);border:1px solid var(--border-color);border-radius:8px;padding:8px">`;

        yaos.forEach((y, i) => {
          const isHl = (step === 1 && y.shi) || (step === 5 && y.mov) || (step === 6 && (y.pos === "九二" || y.shi === "世"));
          const barHtml = y.yin
            ? `<div style="display:flex;justify-content:space-between;width:38px"><span style="width:43%;height:6px;background:var(--text-primary);border-radius:1px"></span><span style="width:43%;height:6px;background:var(--text-primary);border-radius:1px"></span></div>`
            : `<div style="width:38px;height:6px;background:var(--accent-cinnabar);border-radius:1px"></div>`;
          const varYin = (y.pos === "初九" || y.pos === "九四") ? !y.yin : y.yin;
          const varBarHtml = varYin
            ? `<div style="display:flex;justify-content:space-between;width:32px"><span style="width:43%;height:5px;background:var(--text-muted);border-radius:1px"></span><span style="width:43%;height:5px;background:var(--text-muted);border-radius:1px"></span></div>`
            : `<div style="width:32px;height:5px;background:var(--accent-bronze);border-radius:1px"></div>`;

          html += `<div style="display:grid;grid-template-columns:46px 38px 44px 76px 32px 24px 1fr;align-items:center;gap:4px;padding:5px 4px;border-radius:5px;font-size:11.5px;${isHl ? "background:var(--accent-cinnabar-soft);border:1px solid var(--accent-cinnabar)" : "border:1px solid transparent"}">
            <span style="font-size:10.5px;color:var(--text-muted)">${step >= 3 ? y.shen : y.pos}</span>
            <span>${barHtml}</span>
            <span style="font-weight:700;color:var(--accent-gold)">${step >= 1 && y.shi ? "[" + y.shi + "]" : ""} ${y.mov ? "○" : ""}</span>
            <span style="font-weight:600">${step >= 3 ? y.qin + " " : ""}${step >= 2 ? y.zhi : ""}</span>
            <span style="font-size:10.5px;color:var(--accent-bronze);font-weight:700">${step >= 4 ? y.wang : ""}</span>
            <span style="text-align:center;color:var(--text-muted)">→</span>
            <span style="display:flex;align-items:center;gap:6px">${varBarHtml}<span style="font-size:10.5px">${step >= 2 ? y.bZ : ""}</span></span>
          </div>`;
        });

        if (step >= 5) {
          html += `<svg viewBox="0 0 360 190" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none">
            <path d="M 245 85 C 295 75, 295 110, 245 112" fill="none" stroke="var(--accent-bronze)" stroke-width="2" class="shushu-svg-flow"/>
            <path d="M 245 168 C 310 160, 310 135, 245 138" fill="none" stroke="var(--accent-cinnabar)" stroke-width="2" class="shushu-svg-flow"/>
          </svg>`;
        }
        html += `</div></div>`;
        html += `<div class="shushu-readout-bar">
          <div class="shushu-readout-item">卦宫：<strong>${step >= 1 ? "乾宫归魂(金)" : "—"}</strong></div>
          <div class="shushu-readout-item">世/应：<strong>${step >= 1 ? "九三世 / 上九应" : "—"}</strong></div>
          <div class="shushu-readout-item">用神：<strong>${step >= 6 ? "妻财寅木(月旺日生)" : "待断"}</strong></div>
        </div>`;
        return html;
      },
    },

    bazi: {
      badge: "⭐ 禄命星占 · 四柱八字",
      defaultTitle: "四柱八字子平命局与大运流年起伏沙盘（甲子·丙寅·戊辰·壬戌）",
      steps: [
        {
          label: "排定四柱",
          title: "Step 1 · 立春交节排定四柱（甲子·丙寅·戊辰·壬戌）",
          mantra: "年以立春为界，月以节气为纲，日以干支纪历，时以五鼠遁推。",
          formula: "年柱: 甲子 ｜ 月柱: 丙寅 ｜ 日柱: 戊辰（日主戊土） ｜ 时柱: 壬戌",
          boardNote: "四柱八字主表显影，标注立春后寅月建元，日柱天干「戊」标定为命局中心。",
          dialectics: "以太阳回归年（节气）与地球自转周期建立四维时间编码，反映出生时刻的宏观气候初值。",
        },
        {
          label: "地支藏干",
          title: "Step 2 · 拆解十二地支藏干（人元司令）",
          mantra: "子宫单藏癸水，寅藏甲丙戊，辰藏戊乙癸，戌藏戊辛丁。",
          formula: "子[癸] ｜ 寅[甲·丙·戊] ｜ 辰[戊·乙·癸] ｜ 戌[戊·辛·丁]",
          boardNote: "地支底部展开人元藏干抽屉，显出地支内部潜藏的多元五行组分（本气、中气、余气）。",
          dialectics: "地支藏干揭示单一表象（如寅木）内部包含的复杂矛盾组分（木火土共生），体现矛盾复合性。",
        },
        {
          label: "标定十神",
          title: "Step 3 · 以戊土日干为中心标定十神",
          mantra: "同我比劫、生我印枭、克我官杀、我生食伤、我克财才，阴阳异同定十神。",
          formula: "甲=七杀(克戊) ｜ 丙=偏印(生戊) ｜ 戊=日主(比肩) ｜ 壬=偏财(戊克)",
          boardNote: "天干上方全部标出十神徽章，形成「杀、印、身、财」四维角色映射。",
          dialectics: "十神是将自然五行生克抽象为社会职能、资源与压力关系的数学符号投影。",
        },
        {
          label: "身旺身弱",
          title: "Step 4 · 审寅月提纲与辰戌通根定身弱杀旺",
          mantra: "得令者强、失令者弱；春木克土，虽有辰戌通根而木盛水寒。",
          formula: "月令寅木（七杀当令）＋ 年子水时壬水耗土 → 日主戊土【身弱杀旺 · 兼初春寒湿】",
          boardNote: "能量天平展示：克耗（木水 62%）大于生扶（火土 38%），红灯提示身弱急需化杀暖局。",
          dialectics: "衡量系统主体（日主）与外部压力（月令七杀）的动态力量对比，明确主要矛盾。",
        },
        {
          label: "提取用神",
          title: "Step 5 · 扶抑兼调候：提取丙火偏印为第一用神",
          mantra: "杀重身轻，最喜印星通关；初春寅月寒湿，尤须丙火太阳暖局。",
          formula: "甲木(七杀) ──生→ 【丙火(偏印用神)】 ──生→ 戊土(日主) ｜ 通关化杀兼调候",
          boardNote: "丙火亮起金色光环，SVG 流向线演示「木生火、火生土」化敌为友的能量闭环。",
          dialectics: "用神即解决主要矛盾的枢纽抓手——不硬抗七杀，而是引入中间环节（丙火）实现矛盾转化。",
        },
        {
          label: "顺排大运",
          title: "Step 6 · 阳男顺排十年大运时间轴",
          mantra: "阳男阴女顺行，自月柱丙寅顺排丁卯、戊辰、己巳、庚午、辛未。",
          formula: "甲年阳干男命 → 大运：丁卯(10y) → 戊辰(20y) → 己巳(30y) → 庚午(40y) → 辛未(50y)",
          boardNote: "底部五年/五旬大运时间轴依次点亮，火土用神运（戊辰、己巳、庚午）标绿，木旺运（丁卯）标黄。",
          dialectics: "大运刻画十年尺度的阶段性环境变迁，揭示个体生命周期与外部周期的耦合阶段。",
        },
        {
          label: "岁运起伏",
          title: "Step 7 · 大运流年岁运生克起伏曲线",
          mantra: "原局为车、大运为路；行火土暖局助身之运则扶摇直上。",
          formula: "能量指数曲线：丁卯(55) → 戊辰(72) → 己巳(88) → 庚午(92) → 辛未(84)",
          boardNote: "SVG 动态折线图展开，峰值落于「己巳、庚午」火土旺地，直观展示顺应主要矛盾用神后的走势。",
          dialectics: "唯物辩证结语：八字模型揭示「系统初始结构（原局）」与「阶段环境路径（大运）」共同塑造动态演化轨迹。",
        },
      ],
      renderStage(step) {
        const pillars = [
          { lbl: "年柱", god: "七杀", gan: "甲", zhi: "子", c: "#266859", zc: "#2B5B84", cang: "癸(正财)" },
          { lbl: "月柱", god: "偏印(用)", gan: "丙", zhi: "寅", c: "#B2382A", zc: "#266859", cang: "甲·丙·戊" },
          { lbl: "日柱", god: "日主", gan: "戊", zhi: "辰", c: "#8F6824", zc: "#8F6824", cang: "戊·乙·癸" },
          { lbl: "时柱", god: "偏财", gan: "壬", zhi: "戌", c: "#2B5B84", zc: "#8F6824", cang: "戊·辛·丁" },
        ];
        let html = `<div style="width:100%;display:flex;flex-direction:column;gap:10px">
          <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">`;
        pillars.forEach((p, idx) => {
          const isYong = step >= 4 && idx === 1;
          const isSelf = idx === 2;
          html += `<div class="shushu-cell ${isYong ? "hl-red" : isSelf ? "hl-gold" : ""}" style="text-align:center;padding:8px 6px">
            <div style="font-size:11px;color:var(--text-muted)">${p.lbl}</div>
            <div style="font-size:11px;font-weight:700;color:${isYong ? "var(--accent-cinnabar)" : "var(--accent-bronze)"};min-height:16px">${step >= 2 ? p.god : "—"}</div>
            <div style="font-family:var(--font-serif);font-size:22px;font-weight:900;color:${p.c};line-height:1.2">${p.gan}</div>
            <div style="font-family:var(--font-serif);font-size:22px;font-weight:900;color:${p.zc};line-height:1.2">${p.zhi}</div>
            <div style="font-size:10px;color:var(--text-secondary);border-top:1px dashed var(--border-color);padding-top:4px;margin-top:4px;min-height:18px">${step >= 1 ? p.cang : "藏干待拆"}</div>
          </div>`;
        });
        html += `</div>`;

        if (step >= 3) {
          html += `<div style="background:var(--bg-surface);border:1px solid var(--border-color);border-radius:8px;padding:8px 12px;font-size:12px">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px">
              <span>⚖️ 日主强弱评估：<strong>${step >= 4 ? "丙火通关化杀 · 平衡转旺" : "身弱杀旺 · 寅月寒湿"}</strong></span>
              <span style="color:var(--accent-bronze);font-weight:700">${step >= 4 ? "用神：丙火偏印" : "克耗62% vs 生扶38%"}</span>
            </div>
            <div style="height:8px;border-radius:4px;background:var(--bg-subtle);overflow:hidden;display:flex">
              <div style="width:${step >= 4 ? "58%" : "38%"};background:var(--accent-cinnabar);transition:width 0.5s ease"></div>
              <div style="width:${step >= 4 ? "42%" : "62%"};background:var(--accent-bronze);transition:width 0.5s ease"></div>
            </div>
          </div>`;
        }

        if (step >= 5) {
          const dayuns = [
            { gz: "丁卯", age: "10岁", score: 55, good: false },
            { gz: "戊辰", age: "20岁", score: 72, good: true },
            { gz: "己巳", age: "30岁", score: 88, good: true },
            { gz: "庚午", age: "40岁", score: 92, good: true },
            { gz: "辛未", age: "50岁", score: 84, good: true },
          ];
          html += `<div style="background:var(--bg-surface);border:1px solid var(--border-color);border-radius:8px;padding:8px 10px">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:6px">阳男顺排十年大运 &amp; 岁运生克起伏</div>
            <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:5px;text-align:center">
              ${dayuns.map((d) => `<div style="padding:4px;border-radius:5px;border:1px solid ${d.good ? "var(--accent-bronze)" : "var(--accent-gold)"};background:${d.good ? "var(--accent-bronze-soft)" : "var(--accent-gold-soft)"}">
                <div style="font-size:10px;color:var(--text-muted)">${d.age}</div>
                <div style="font-weight:800;font-size:13px">${d.gz}</div>
              </div>`).join("")}
            </div>
            ${step >= 6 ? `<svg viewBox="0 0 360 72" style="width:100%;height:68px;margin-top:6px">
              <polyline points="36,48 108,34 180,18 252,12 324,22" fill="none" stroke="var(--accent-cinnabar)" stroke-width="2.5" class="shushu-svg-flow"/>
              <circle cx="36" cy="48" r="4" fill="var(--accent-gold)"/><circle cx="108" cy="34" r="4" fill="var(--accent-bronze)"/>
              <circle cx="180" cy="18" r="4.5" fill="var(--accent-cinnabar)"/><circle cx="252" cy="12" r="5" fill="var(--accent-cinnabar)"/>
              <circle cx="324" cy="22" r="4" fill="var(--accent-bronze)"/>
              <text x="252" y="9" text-anchor="middle" font-size="9" fill="var(--accent-cinnabar)" font-weight="bold">峰值 92</text>
            </svg>` : ""}
          </div>`;
        }
        html += `</div>`;
        return html;
      },
    },

    ziwei: {
      badge: "⭐ 禄命星占 · 紫微斗数",
      defaultTitle: "紫微斗数十二宫安星与三方四正飞线沙盘（丙寅命宫 · 火六局）",
      steps: [
        {
          label: "安命身宫",
          title: "Step 1 · 生月生时逆顺安命宫（寅）与身宫（午）",
          mantra: "寅上起正月，顺数至生月；再从生月起子时，逆数至生时为命宫，顺数至生时为身宫。",
          formula: "三月寅时例：寅→卯→辰(三月)，逆数子丑寅得【寅宫立命】，顺数子丑寅得【午宫安身】",
          boardNote: "4×4 紫微方盘左下「寅」宫亮起朱红「命宫」印，正上「午」宫亮起青绿「身宫」印。",
          dialectics: "以月（公转季节）定基点、以时（自转昼夜）作逆顺对称分岔，建立先天气质（命）与后天行动（身）双坐标。",
        },
        {
          label: "十二人事",
          title: "Step 2 · 逆排兄弟、夫妻、子女、财帛等十二人事宫位",
          mantra: "命兄夫子财疾迁，奴官田福父依次逆旋。",
          formula: "寅命 → 丑兄 → 子夫 → 亥子 → 戌财 → 酉疾 → 申迁 → 未友 → 午官 → 巳田 → 辰福 → 卯父",
          boardNote: "十二宫人事标签全部填满，清晰呈现出「命(寅)—财(戌)—官(午)—迁(申)」结构。",
          dialectics: "十二宫本质是把个体生命切分为十二个社会功能子系统（财富、事业、人际、家庭等）。",
        },
        {
          label: "五行定局",
          title: "Step 3 · 命宫丙寅纳音炉中火定「火六局」",
          mantra: "五虎遁得命宫干支丙寅，丙寅丁卯炉中火，定为火六局。",
          formula: "命宫干支 = 丙寅 → 纳音炉中火 → 局数 = 6（火六局）",
          boardNote: "中宫仪表盘显示「丙寅 · 炉中火 · 火六局」，为紫微星模运算提供除数基准。",
          dialectics: "五行局数作为周期模数（Modulus），决定十四主星在十二宫中的离散分布步长。",
        },
        {
          label: "安紫微星",
          title: "Step 4 · 生日除以六局定紫微（午宫）并逆布紫微星系",
          mantra: "紫微逆去天机星，隔一太阳武曲辰，连接天同空二格，廉贞居处方是真。",
          formula: "二十七日例：(27+3)÷6 = 5 → 寅起五位落【午宫紫微】；逆布机、阳、武、同、廉",
          boardNote: "紫微入午（官禄身宫），天机在巳、太阳在卯、武曲在寅（坐命）、天同在丑、廉贞在戌。",
          dialectics: "通过带余整除模运算实现群星在环面十二宫上的周期性编排。",
        },
        {
          label: "安天府系",
          title: "Step 5 · 寅申轴对称定天府（戌宫）并顺布天府八星",
          mantra: "午上起紫微，寅申对称必得戌宫天府；天府顺行阴贪巨，相梁杀破相继临。",
          formula: "紫微(午) ↔ 天府(戌)；顺布太阴(亥)、贪狼(子)、巨门(丑)、天相(寅)、天梁(卯)、七杀(辰)、破军(申)",
          boardNote: "南北双星系全盘会师：命宫寅形成「武曲·天相」双星同宫，财帛戌形成「廉贞·天府」双星同宫！",
          dialectics: "紫微（北极/逆行）与天府（南斗/顺行）沿寅申轴镜面对称展开，构成阴阳双螺旋秩序。",
        },
        {
          label: "辅煞四化",
          title: "Step 6 · 安辅弼昌曲煞星与生年四化（禄权科忌）",
          mantra: "甲廉破武阳：廉贞化禄、破军化权、武曲化科、太阳化忌。",
          formula: "生年四化徽章：戌·廉贞[禄] ｜ 申·破军[权] ｜ 寅·武曲[科] ｜ 卯·太阳[忌]",
          boardNote: "各宫主星旁缀上「禄」「权」「科」「忌」彩色印章及左辅右弼徽标。",
          dialectics: "「四化」为静态星曜注入资源增益（禄）、执行张力（权）、声誉秩序（科）与风险短板（忌）四类动态权重。",
        },
        {
          label: "三方四正",
          title: "Step 7 · 命财官迁三方四正飞线高亮与格局解读",
          mantra: "看命先观三方四正：命宫寅、财帛戌、官禄午成三合，迁移申成对冲。",
          formula: "寅(武相科) ↔ 午(紫微·身) ↔ 戌(廉府禄) ↔ 申(破军权) → 「紫府朝垣 · 廉府积富格」",
          boardNote: "中宫 SVG 射出朱红与青绿彩色飞线，贯穿命财官迁四大核心宫位。",
          dialectics: "唯物辩证结语：斗数「三方四正」本质是跨维度系统关联分析——个体发展从不孤立，而是自身能力（命）、资源（财）、平台（官）与外部机遇（迁）的立体共振。",
        },
      ],
      renderStage(step) {
        const grid = [
          ["巳", "午", "未", "申"],
          ["辰", null, null, "酉"],
          ["卯", null, null, "戌"],
          ["寅", "丑", "子", "亥"],
        ];
        const palaceName = {
          "寅": "命宫", "丑": "兄弟", "子": "夫妻", "亥": "子女",
          "戌": "财帛", "酉": "疾厄", "申": "迁移", "未": "交友",
          "午": "官禄·身", "巳": "田宅", "辰": "福德", "卯": "父母",
        };
        const ziweiStars = {
          "午": ["紫微"], "巳": ["天机"], "卯": ["太阳"], "寅": ["武曲"], "丑": ["天同"], "戌": ["廉贞"],
        };
        const tianfuStars = {
          "戌": ["天府"], "亥": ["太阴"], "子": ["贪狼"], "丑": ["巨门"], "寅": ["天相"], "卯": ["天梁"], "辰": ["七杀"], "申": ["破军"],
        };
        const sihua = {
          "戌": { t: "禄", c: "green" },
          "申": { t: "权", c: "gold" },
          "寅": { t: "科", c: "green" },
          "卯": { t: "忌", c: "red" },
        };
        let html = `<div class="shushu-grid-4x4" style="max-width:410px">`;
        for (let r = 0; r < 4; r++) {
          for (let c = 0; c < 4; c++) {
            const zhi = grid[r][c];
            if (!zhi) {
              if (r === 1 && c === 1) {
                html += `<div style="grid-column:2/4;grid-row:2/4;background:var(--bg-subtle);border:1px solid var(--border-strong);border-radius:8px;padding:10px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;font-size:12px">
                  <div style="font-family:var(--font-serif);font-size:15px;font-weight:900;color:var(--accent-cinnabar)">丙寅命盘中枢</div>
                  <div style="margin-top:4px;color:var(--text-secondary)">${step >= 2 ? "纳音炉中火 · 火六局" : "三月寅时生人"}</div>
                  <div style="margin-top:6px;font-size:11px;color:var(--accent-bronze);font-weight:700">${step >= 6 ? "三方四正：紫府朝垣格" : "三方四正：命财官迁"}</div>
                </div>`;
              }
              continue;
            }
            const stars = [
              ...(step >= 3 ? (ziweiStars[zhi] || []) : []),
              ...(step >= 4 ? (tianfuStars[zhi] || []) : []),
            ];
            const sh = step >= 5 ? sihua[zhi] : null;
            const isSanfang = ["寅", "午", "戌", "申"].includes(zhi);
            let cls = "";
            if (step === 0 && (zhi === "寅" || zhi === "午")) cls = "hl-red";
            if (step >= 6 && isSanfang) cls = zhi === "寅" ? "hl-red" : "hl-gold";

            html += `<div class="shushu-cell ${cls}" style="min-height:70px">
              <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-muted)">
                <span style="font-weight:700">${zhi === "寅" ? "丙寅" : zhi}</span>
                <span style="color:var(--accent-cinnabar);font-weight:700">${step >= 1 ? palaceName[zhi] : (zhi === "寅" ? "命宫" : zhi === "午" ? "身宫" : "")}</span>
              </div>
              <div style="font-size:11.5px;font-weight:700;color:var(--text-primary);line-height:1.3;margin:2px 0">
                ${stars.join(" · ") || "<span style='color:var(--text-muted);font-weight:400'>空宫</span>"}
              </div>
              <div style="display:flex;justify-content:flex-end;gap:3px">
                ${sh ? `<span class="shushu-tag ${sh.c}">化${sh.t}</span>` : ""}
              </div>
            </div>`;
          }
        }
        if (step >= 6) {
          html += `<svg viewBox="0 0 400 400" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2">
            <polygon points="50,350 150,50 350,250" fill="none" stroke="var(--accent-cinnabar)" stroke-width="2.2" class="shushu-svg-flow" opacity="0.82"/>
            <line x1="50" y1="350" x2="350" y2="50" stroke="var(--accent-bronze)" stroke-width="2" class="shushu-svg-flow" opacity="0.82"/>
          </svg>`;
        }
        html += `</div>`;
        html += `<div class="shushu-readout-bar">
          <div class="shushu-readout-item">命/身：<strong>寅命 / 午身</strong></div>
          <div class="shushu-readout-item">五行局：<strong>${step >= 2 ? "火六局" : "待定"}</strong></div>
          <div class="shushu-readout-item">核心格：<strong>${step >= 6 ? "武相坐命 · 紫府朝垣" : "安星推演中"}</strong></div>
        </div>`;
        return html;
      },
    },

    fengshui: {
      badge: "⛰️ 形法相地 · 风水堪舆",
      defaultTitle: "三层罗盘旋转与下元八运玄空九宫飞星沙盘（子山午向）",
      steps: [
        {
          label: "峦头四灵",
          title: "Step 1 · 峦头形势：四灵砂水与背山面水审势",
          mantra: "左青龙、右白虎、前朱雀、后玄武；山管人丁水管财。",
          formula: "坐北（玄武靠山稳固）朝南（朱雀明堂开阔 · 纳日照与季风）",
          boardNote: "罗盘确立南北子午主轴：背依北山阻挡冬季寒潮，面向南水迎受夏季湿润南风。",
          dialectics: "峦头形势的科学本质是微气候生态建筑学与聚落安全选址（防风、采光、排水、避滑坡）。",
        },
        {
          label: "正针立向",
          title: "Step 2 · 地盘正针立下元八运「子山午向」（0° / 180°）",
          mantra: "地盘正针格龙立向，分金定在正子正午（0°—180°）天元龙。",
          formula: "地盘正针 = 0° 基准 ｜ 坐山 = 子（坎一） ｜ 向首 = 午（离九）",
          boardNote: "罗盘正针红线锁定「子（正北）— 午（正南）」中轴，确立八运立向坐标。",
          dialectics: "以磁北与真太阳方位角实现建筑轴线的精确空间标定。",
        },
        {
          label: "三针旋转",
          title: "Step 3 · 人盘中针（-7.5°消砂）与天盘缝针（+7.5°纳水）动态旋转",
          mantra: "地盘正针立向，人盘中针退半山消砂，天盘缝针进半山纳水。",
          formula: "人盘中针 Δθ = -7.5°（兼顾山体阴影仰角）｜ 天盘缝针 Δθ = +7.5°（兼顾磁偏与水势）",
          boardNote: "罗盘内圈实时产生 -7.5° 青绿偏转与 +7.5° 金色偏转动画，直观展示三层二十四山错位！",
          dialectics: "「三针差半山（7.5°）」反映了古人对地磁偏角与山地采光/水流倾角的经验修正。",
        },
        {
          label: "八运入中",
          title: "Step 4 · 下元八运八白左辅星入中顺飞运盘",
          mantra: "下元八运（2004—2023）以八白入中，依洛书轨顺飞九宫。",
          formula: "运盘顺飞：5中(8) → 6乾(9) → 7兑(1) → 8艮(2) → 9离(3) → 1坎(4) → 2坤(5) → 3震(6) → 4巽(7)",
          boardNote: "右侧九宫运盘飞入中心大字：坐山坎一得运星「4」，向首离九得运星「3」。",
          dialectics: "将二十年（三元九运土星—木星会合周期）时间参数注入九宫空间矩阵。",
        },
        {
          label: "排山星盘",
          title: "Step 5 · 坐山山星入中飞布（兼三碧/四绿阴阳顺逆演示）",
          mantra: "坐山运星入中宫，按二十四山天元龙阴阳定顺飞或逆飞（坎一子天元阴逆飞）。",
          formula: "坐山星4入中逆飞（兼示阳顺阴逆步法）：中4→乾3→兑2→艮1→离9→【坎8】→坤7→震6→巽5",
          boardNote: "各宫左上角山星飞入：当令旺星「8白」精准落于坐山「坎一宫」！",
          dialectics: "山星表征静态支撑结构与靠山稳定性在各宫位的空间分布。",
        },
        {
          label: "排向星盘",
          title: "Step 6 · 向首向星入中飞布（向星8白到离九向首）",
          mantra: "向首运星入中宫，依向首龙神阴阳顺逆排向星。",
          formula: "向首星3入中逆飞：中3→乾2→兑1→艮9→【离8】→坎7→坤6→震5→巽4",
          boardNote: "各宫右上角向星飞入：当令旺星「8白」精准落于向首「离九宫」！",
          dialectics: "向星表征动态通风、采光与对外流通通道（门窗水口）的效率分布。",
        },
        {
          label: "旺山旺向",
          title: "Step 7 · 旺山旺向格局与城门诀高亮判读",
          mantra: "山星旺8到坐山（坎一）、向星旺8到向首（离九），成「旺山旺向」全吉局！",
          formula: "坎1(山8 · 运4 · 向7) + 离9(山9 · 运3 · 向8) ＋ 城门正副宫：艮8 / 坤2",
          boardNote: "坎一与离九两宫亮起朱红金环，标注「旺山旺向」；旁注城门位「艮八/坤二」宜设辅助动水通气。",
          dialectics: "唯物辩证结语：剥除玄空吉凶附会，其核心是追求建筑「背阴稳固（山）」与「向阳通透（向）」的生态空间均衡。",
        },
      ],
      renderStage(step) {
        const renRot = step >= 2 ? -7.5 : 0;
        const tianRot = step >= 2 ? 7.5 : 0;
        const mts = ["午","丁","未","坤","申","庚","酉","辛","戌","乾","亥","壬","子","癸","丑","艮","寅","甲","卯","乙","辰","巽","巳","丙"];
        let ticks = "";
        mts.forEach((m, i) => {
          const ang = i * 15;
          const rad = (ang - 90) * Math.PI / 180;
          const tx = 170 + 144 * Math.cos(rad);
          const ty = 170 + 144 * Math.sin(rad);
          ticks += `<text x="${tx.toFixed(1)}" y="${ty.toFixed(1)}" text-anchor="middle" dominant-baseline="central" font-size="9.5" fill="${m==="子"||m==="午" ? "var(--accent-cinnabar)" : "var(--text-primary)"}" font-weight="bold">${m}</text>`;
        });

        const luopanSvg = `<svg viewBox="0 0 340 340" style="width:100%;max-width:240px;height:auto">
          <circle cx="170" cy="170" r="160" fill="var(--bg-surface)" stroke="var(--border-strong)" stroke-width="2"/>
          <circle cx="170" cy="170" r="130" fill="none" stroke="var(--border-color)" stroke-width="1"/>
          ${ticks}
          <g class="shushu-rotate-ring" data-target-rot="${renRot}" style="transform:rotate(${step === 2 ? 0 : renRot}deg)">
            <circle cx="170" cy="170" r="112" fill="none" stroke="var(--accent-bronze)" stroke-width="2" stroke-dasharray="6 3"/>
            <line x1="170" y1="58" x2="170" y2="70" stroke="var(--accent-bronze)" stroke-width="3"/>
          </g>
          <g class="shushu-rotate-ring" data-target-rot="${tianRot}" style="transform:rotate(${step === 2 ? 0 : tianRot}deg)">
            <circle cx="170" cy="170" r="88" fill="none" stroke="var(--accent-gold)" stroke-width="2" stroke-dasharray="4 3"/>
            <line x1="170" y1="82" x2="170" y2="94" stroke="var(--accent-gold)" stroke-width="3"/>
          </g>
          <line x1="170" y1="22" x2="170" y2="318" stroke="var(--accent-cinnabar)" stroke-width="1.6" stroke-dasharray="4 3"/>
          <circle cx="170" cy="170" r="24" fill="var(--accent-cinnabar-soft)" stroke="var(--accent-cinnabar)" stroke-width="1.5"/>
          <text x="170" y="166" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--accent-cinnabar)">天池</text>
          <text x="170" y="179" text-anchor="middle" font-size="9" fill="var(--text-secondary)">子山午向</text>
        </svg>`;

        const xkPalaces = [
          { no: 4, nm: "巽4", yun: 7, shan: 5, xiang: 4 },
          { no: 9, nm: "离9(向)", yun: 3, shan: 9, xiang: 8 },
          { no: 2, nm: "坤2", yun: 5, shan: 7, xiang: 6 },
          { no: 3, nm: "震3", yun: 6, shan: 6, xiang: 5 },
          { no: 5, nm: "中5", yun: 8, shan: 4, xiang: 3 },
          { no: 7, nm: "兑7", yun: 1, shan: 2, xiang: 1 },
          { no: 8, nm: "艮8", yun: 2, shan: 1, xiang: 9 },
          { no: 1, nm: "坎1(坐)", yun: 4, shan: 8, xiang: 7 },
          { no: 6, nm: "乾6", yun: 9, shan: 3, xiang: 2 },
        ];
        let gridHtml = `<div class="shushu-grid-3x3" style="max-width:250px">`;
        xkPalaces.forEach((p) => {
          let cls = "";
          if (step >= 6 && (p.no === 1 || p.no === 9)) cls = "hl-red";
          if (step >= 6 && (p.no === 8 || p.no === 2)) cls = "hl-gold";
          gridHtml += `<div class="shushu-cell ${cls}" style="min-height:68px">
            <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:800">
              <span style="color:var(--accent-bronze)">${step >= 4 ? "山" + p.shan : ""}</span>
              <span style="color:var(--accent-cinnabar)">${step >= 5 ? "向" + p.xiang : ""}</span>
            </div>
            <div style="text-align:center;font-size:16px;font-weight:900;color:var(--text-primary)">${step >= 3 ? p.yun : "—"}</div>
            <div style="text-align:center;font-size:10px;color:var(--text-muted)">${p.nm}</div>
          </div>`;
        });
        gridHtml += `</div>`;

        return `<div style="width:100%;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:14px">
          <div>${luopanSvg}</div>
          <div>${gridHtml}</div>
        </div>
        <div class="shushu-readout-bar">
          <div class="shushu-readout-item">中针/缝针：<strong>${step >= 2 ? "-7.5° / +7.5°" : "0° / 0°"}</strong></div>
          <div class="shushu-readout-item">运盘：<strong>${step >= 3 ? "下元八运" : "待起"}</strong></div>
          <div class="shushu-readout-item">飞星局：<strong>${step >= 6 ? "旺山旺向 (坐山8/向首8)" : "推演中"}</strong></div>
        </div>`;
      },
    },

    xiangshu: {
      badge: "⛰️ 形法相地 · 相术摸骨",
      defaultTitle: "相术摸骨颅骨触诊、十二宫与中医五色望诊沙盘",
      steps: [
        {
          label: "五行形局",
          title: "Step 1 · 整体五行形局（金方木瘦水肥火尖土厚）识别",
          mantra: "木形瘦削清奇，火形上锐下阔，土形敦厚方实，金形方正有棱，水形圆润饱满。",
          formula: "面型长宽比 + 下颌角倾角 + 皮下脂肪分布 → 五行体质形局分类",
          boardNote: "左侧 SVG 展示标准端方轮廓与五种体质形局切换标尺。",
          dialectics: "对应现代体质人类学（Sheldon 胚层体型分类与颅面指数），反映遗传基因与内分泌代谢倾向。",
        },
        {
          label: "三停五岳",
          title: "Step 2 · 上中下三停与五岳朝拱标尺测量动画",
          mantra: "发际至眉为上停，眉至鼻准为中停，鼻准至地阁为下停；五岳朝拱贵乎均衡。",
          formula: "三停均等比 ≈ 1 : 1 : 1 ｜ 五岳：中岳鼻、东岳左颧、西岳右颧、南岳额、北岳颏",
          boardNote: "面部拉起三停水平测量标线，鼻、双颧、额、地阁五处亮起金色朝拱节点。",
          dialectics: "对应达·芬奇/现代颌面美学三庭五眼黄金比例，反映颅颌发育对称性与早期营养状况。",
        },
        {
          label: "中轴摸骨",
          title: "Step 3 · 中轴颅骨触诊（日角骨 · 伏犀玉柱骨 · 玉枕骨）",
          mantra: "天庭有日角、月角骨；印堂上贯百会曰伏犀骨；脑后隆起曰玉枕骨。",
          formula: "解剖对应：日角骨(额结节) ｜ 伏犀骨(额骨矢状嵴) ｜ 玉枕骨(枕外隆凸)",
          boardNote: "中轴三处颅骨特征点发出朱红脉冲光环，右上方侧颅轮廓同步高亮枕外隆凸。",
          dialectics: "枕外隆凸与额骨嵴等骨性标志的发达程度，本质上与颈部肌群附着强度及颅骨力学发育相关。",
        },
        {
          label: "侧翼骨度",
          title: "Step 4 · 侧翼骨度触诊（将军骨 · 驿马骨 · 颧骨 · 巨鳌骨）",
          mantra: "眉骨突曰将军，太阳穴旁曰驿马，两颧耸立有肉，耳后高骨曰巨鳌。",
          formula: "解剖对应：将军骨(眶上缘/眉弓) ｜ 驿马骨(颞骨翼点) ｜ 颧骨(颧弓) ｜ 巨鳌骨(乳突)",
          boardNote: "双侧眉弓、太阳穴、颧弓与耳后乳突四组骨性触诊点对称点亮。",
          dialectics: "眉弓与颧弓凸度受雄激素与咀嚼肌力学牵拉调控，古人误将体质刚健外推为宿命性格。",
        },
        {
          label: "十二宫扫",
          title: "Step 5 · 面部十二宫扫描（命宫 · 财帛 · 官禄 · 田宅）",
          mantra: "印堂为命宫，鼻准为财帛，额中为官禄，眉眼之间为田宅。",
          formula: "扫描分区：命宫(眉心印堂) → 官禄(额中央) → 田宅(上睑眼窝) → 财帛(鼻准)",
          boardNote: "扫描光带自上而下略过面部，高亮四大关键宫位标签与局部皮肤纹理。",
          dialectics: "十二宫将情绪微表情高发区（印堂皱眉肌）与皮脂代谢区（鼻准）附会为社会运势标签，需去伪存真。",
        },
        {
          label: "五色望诊",
          title: "Step 6 · 中医五色气血（青赤黄白黑）外显部位演示",
          mantra: "肝青、心赤、脾黄、肺白、肾黑；五色明润者生，枯槁晦滞者病。",
          formula: "青(肝胆·山根目周) ｜ 赤(心脉·面颊印堂) ｜ 黄(脾胃·鼻准) ｜ 白(肺气·两颧) ｜ 黑(肾精·眼眶下)",
          boardNote: "面部各区域呈现半透明五色血氧微循环色晕，精准对应中医《黄帝内经》五色诊部。",
          dialectics: "面色变化直接反映毛细血管灌注、血红蛋白氧合度与肝肾代谢状态，具备明确临床医学价值。",
        },
        {
          label: "综合评估",
          title: "Step 7 · 体质人类学与性格健康综合评估",
          mantra: "去宿命之糟粕，存体质人类学与中医望诊之精华。",
          formula: "骨骼力学发育 + 三停对称度 + 表情肌习惯 + 五色微循环 → 客观身心健康评估",
          boardNote: "全颅点位整合，输出「骨骼发育指数 / 情绪习惯区 / 气血微循环」三维客观总结。",
          dialectics: "唯物辩证结语：否定「骨相定富贵生死」的宿命论，肯定古人在长期观察中积累的体质医学与非言语行为学经验。",
        },
      ],
      renderStage(step) {
        const svg = `<svg viewBox="0 0 360 320" style="width:100%;max-width:350px;height:auto">
          <!-- Front Head Outline -->
          <path d="M 105 70 C 105 22, 215 22, 215 70 L 218 145 C 218 205, 190 258, 160 264 C 130 258, 102 205, 102 145 Z"
                fill="var(--bg-surface)" stroke="var(--border-strong)" stroke-width="2"/>
          <!-- Ears -->
          <path d="M 102 128 C 90 124, 88 164, 102 168" fill="var(--bg-subtle)" stroke="var(--border-strong)" stroke-width="1.6"/>
          <path d="M 218 128 C 230 124, 232 164, 218 168" fill="var(--bg-subtle)" stroke="var(--border-strong)" stroke-width="1.6"/>
          <!-- Facial features -->
          <path d="M 122 124 Q 136 116 148 124" fill="none" stroke="var(--text-secondary)" stroke-width="2"/>
          <path d="M 172 124 Q 184 116 198 124" fill="none" stroke="var(--text-secondary)" stroke-width="2"/>
          <ellipse cx="135" cy="136" rx="10" ry="5" fill="none" stroke="var(--text-muted)" stroke-width="1.3"/>
          <ellipse cx="185" cy="136" rx="10" ry="5" fill="none" stroke="var(--text-muted)" stroke-width="1.3"/>
          <path d="M 160 130 L 154 176 Q 160 184 166 176 Z" fill="none" stroke="var(--text-secondary)" stroke-width="1.5"/>
          <path d="M 143 212 Q 160 220 177 212" fill="none" stroke="var(--text-secondary)" stroke-width="1.8"/>

          <!-- Lateral Cranium Mini Profile for Occiput (玉枕骨/巨鳌骨) -->
          <g transform="translate(245, 22)">
            <path d="M 25 45 C 20 12, 82 8, 92 48 C 98 76, 86 105, 62 114 L 54 134 L 22 134 L 24 108 C 12 96, 18 68, 25 45 Z"
                  fill="var(--bg-subtle)" stroke="var(--border-strong)" stroke-width="1.4"/>
            <text x="56" y="148" text-anchor="middle" font-size="9.5" fill="var(--text-muted)">侧颅枕骨区</text>
            ${step === 2 || step === 6 ? `<circle cx="88" cy="74" r="6" fill="var(--accent-cinnabar)" opacity="0.85"/><text x="64" y="77" font-size="9" fill="var(--accent-cinnabar)" font-weight="bold">玉枕骨</text>` : ""}
            ${step === 3 || step === 6 ? `<circle cx="52" cy="96" r="5.5" fill="var(--accent-bronze)" opacity="0.85"/><text x="52" y="110" text-anchor="middle" font-size="9" fill="var(--accent-bronze)" font-weight="bold">巨鳌(乳突)</text>` : ""}
          </g>

          <!-- Step 1: Five Elements Frame -->
          ${step === 0 ? `<rect x="96" y="28" width="128" height="240" rx="18" fill="none" stroke="var(--accent-gold)" stroke-width="1.6" stroke-dasharray="5 4"/>
            <text x="160" y="288" text-anchor="middle" font-size="11" fill="var(--accent-gold)" font-weight="bold">五行形局基准框：金方 / 木瘦 / 水肥 / 火尖 / 土厚</text>` : ""}

          <!-- Step 2: Three Stops & Five Mountains -->
          ${step === 1 ? `
            <line x1="78" y1="68" x2="232" y2="68" stroke="var(--accent-bronze)" stroke-width="1.2" stroke-dasharray="4 3"/>
            <line x1="78" y1="122" x2="232" y2="122" stroke="var(--accent-bronze)" stroke-width="1.2" stroke-dasharray="4 3"/>
            <line x1="78" y1="184" x2="232" y2="184" stroke="var(--accent-bronze)" stroke-width="1.2" stroke-dasharray="4 3"/>
            <line x1="78" y1="262" x2="232" y2="262" stroke="var(--accent-bronze)" stroke-width="1.2" stroke-dasharray="4 3"/>
            <text x="72" y="96" text-anchor="end" font-size="10" fill="var(--accent-bronze)" font-weight="bold">上停</text>
            <text x="72" y="156" text-anchor="end" font-size="10" fill="var(--accent-bronze)" font-weight="bold">中停</text>
            <text x="72" y="226" text-anchor="end" font-size="10" fill="var(--accent-bronze)" font-weight="bold">下停</text>
            <circle cx="160" cy="92" r="5" fill="var(--accent-gold)"/><circle cx="160" cy="172" r="6" fill="var(--accent-cinnabar)"/>
            <circle cx="122" cy="162" r="5" fill="var(--accent-gold)"/><circle cx="198" cy="162" r="5" fill="var(--accent-gold)"/>
            <circle cx="160" cy="246" r="5" fill="var(--accent-gold)"/>
          ` : ""}

          <!-- Step 3: Midline Bones (日角, 伏犀) -->
          ${step === 2 || step === 6 ? `
            <line x1="160" y1="36" x2="160" y2="125" stroke="var(--accent-cinnabar)" stroke-width="4" opacity="0.55"/>
            <circle cx="140" cy="76" r="5.5" fill="var(--accent-cinnabar)"/><circle cx="180" cy="76" r="5.5" fill="var(--accent-cinnabar)"/>
            <text x="160" y="64" text-anchor="middle" font-size="9.5" fill="var(--accent-cinnabar)" font-weight="bold">伏犀玉柱 · 日角骨</text>
          ` : ""}

          <!-- Step 4: Lateral Bones (将军, 驿马, 颧骨) -->
          ${step === 3 || step === 6 ? `
            <path d="M 120 120 Q 135 112 149 120" fill="none" stroke="var(--accent-cinnabar)" stroke-width="4" opacity="0.7"/>
            <path d="M 171 120 Q 185 112 200 120" fill="none" stroke="var(--accent-cinnabar)" stroke-width="4" opacity="0.7"/>
            <circle cx="107" cy="118" r="5" fill="var(--accent-gold)"/><circle cx="213" cy="118" r="5" fill="var(--accent-gold)"/>
            <circle cx="122" cy="162" r="6" fill="var(--accent-bronze)"/><circle cx="198" cy="162" r="6" fill="var(--accent-bronze)"/>
            <text x="160" y="286" text-anchor="middle" font-size="10" fill="var(--accent-bronze)" font-weight="bold">将军骨(眉弓) · 驿马骨(翼点) · 颧弓</text>
          ` : ""}

          <!-- Step 5: 12 Palaces -->
          ${step === 4 ? `
            <circle cx="160" cy="96" r="9" fill="var(--accent-gold-soft)" stroke="var(--accent-gold)" stroke-width="1.6"/>
            <text x="160" y="84" text-anchor="middle" font-size="9.5" fill="var(--accent-gold)" font-weight="bold">官禄宫</text>
            <circle cx="160" cy="124" r="8" fill="var(--accent-cinnabar-soft)" stroke="var(--accent-cinnabar)" stroke-width="1.8"/>
            <text x="160" y="114" text-anchor="middle" font-size="9.5" fill="var(--accent-cinnabar)" font-weight="bold">命宫(印堂)</text>
            <rect x="122" y="125" width="26" height="10" rx="3" fill="var(--accent-bronze-soft)" stroke="var(--accent-bronze)"/>
            <text x="116" y="133" text-anchor="end" font-size="9" fill="var(--accent-bronze)" font-weight="bold">田宅</text>
            <circle cx="160" cy="174" r="9" fill="var(--accent-cinnabar-soft)" stroke="var(--accent-cinnabar)" stroke-width="1.8"/>
            <text x="160" y="194" text-anchor="middle" font-size="9.5" fill="var(--accent-cinnabar)" font-weight="bold">财帛宫(鼻准)</text>
          ` : ""}

          <!-- Step 6: TCM Five Colors -->
          ${step === 5 ? `
            <circle cx="160" cy="96" r="14" fill="rgba(178,56,42,0.28)"/><text x="160" y="99" text-anchor="middle" font-size="9" fill="#B2382A" font-weight="bold">赤·心</text>
            <circle cx="160" cy="144" r="10" fill="rgba(38,104,89,0.28)"/><text x="160" y="147" text-anchor="middle" font-size="9" fill="#266859" font-weight="bold">青·肝</text>
            <circle cx="160" cy="174" r="12" fill="rgba(212,168,87,0.38)"/><text x="160" y="177" text-anchor="middle" font-size="9" fill="#8F6824" font-weight="bold">黄·脾</text>
            <circle cx="195" cy="160" r="12" fill="rgba(169,178,188,0.35)"/><text x="195" y="163" text-anchor="middle" font-size="9" fill="var(--text-primary)" font-weight="bold">白·肺</text>
            <ellipse cx="135" cy="146" rx="12" ry="5" fill="rgba(28,36,43,0.32)"/><text x="116" y="156" font-size="9" fill="var(--text-primary)" font-weight="bold">黑·肾</text>
          ` : ""}
        </svg>`;
        return `${svg}<div class="shushu-readout-bar">
          <div class="shushu-readout-item">审视维度：<strong>${["五行形局","三停五岳","中轴颅骨","侧翼骨度","面部十二宫","中医五色望诊","体质人类学总评"][step]}</strong></div>
          <div class="shushu-readout-item">方法论：<strong>解剖特征 + 气血微循环</strong></div>
        </div>`;
      },
    },
  };

  function initShushuAnimations(bodyEl) {
    const mounts = bodyEl.querySelectorAll(".shushu-anim-mount");
    mounts.forEach((mount) => {
      const rawType = (mount.getAttribute("data-type") || "qimen").toLowerCase();
      const engine = SHUSHU_ENGINES[rawType] || SHUSHU_ENGINES.qimen;
      const customTitle = mount.getAttribute("data-title") || engine.defaultTitle;

      let stepIdx = 0;
      let timerId = null;

      mount.innerHTML = `
        <div class="shushu-anim-card">
          <div class="shushu-anim-header">
            <div class="shushu-anim-title-wrap">
              <span class="shushu-anim-badge">${escapeHtml(engine.badge)}</span>
              <div class="shushu-anim-title">${escapeHtml(customTitle)}</div>
            </div>
            <div class="shushu-anim-controls">
              <button type="button" class="shushu-ctrl-btn" data-act="prev">⏮ 上一步</button>
              <button type="button" class="shushu-ctrl-btn primary" data-act="play">▶ 自动播放</button>
              <button type="button" class="shushu-ctrl-btn" data-act="next">⏭ 下一步</button>
              <button type="button" class="shushu-ctrl-btn" data-act="reset">🔄 重置</button>
            </div>
          </div>
          <div class="shushu-step-track" data-role="track"></div>
          <div class="shushu-anim-body">
            <div class="shushu-anim-stage" data-role="stage"></div>
            <div class="shushu-anim-detail" data-role="detail"></div>
          </div>
        </div>`;

      const trackEl = mount.querySelector('[data-role="track"]');
      const stageEl = mount.querySelector('[data-role="stage"]');
      const detailEl = mount.querySelector('[data-role="detail"]');
      const prevBtn = mount.querySelector('[data-act="prev"]');
      const playBtn = mount.querySelector('[data-act="play"]');
      const nextBtn = mount.querySelector('[data-act="next"]');
      const resetBtn = mount.querySelector('[data-act="reset"]');

      const stopPlay = () => {
        if (timerId !== null) {
          clearInterval(timerId);
          timerId = null;
        }
        playBtn.textContent = "▶ 自动播放";
      };

      const render = () => {
        const cur = engine.steps[stepIdx];
        trackEl.innerHTML = engine.steps
          .map(
            (s, i) =>
              `<button type="button" class="shushu-step-pill ${i === stepIdx ? "active" : i < stepIdx ? "done" : ""}" data-step="${i}">
                <span class="shushu-step-num">0${i + 1}</span>
                <span class="shushu-step-lbl">${escapeHtml(s.label)}</span>
              </button>`
          )
          .join("");

        trackEl.querySelectorAll(".shushu-step-pill").forEach((btn) => {
          btn.addEventListener("click", () => {
            stopPlay();
            stepIdx = Number(btn.getAttribute("data-step"));
            render();
          });
        });

        stageEl.innerHTML = engine.renderStage(stepIdx);
        const rotRings = stageEl.querySelectorAll(".shushu-rotate-ring[data-target-rot]");
        if (rotRings.length) {
          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              rotRings.forEach((ring) => {
                ring.style.transform = `rotate(${ring.getAttribute("data-target-rot")}deg)`;
              });
            });
          });
        }
        detailEl.innerHTML = `
          <div class="shushu-detail-head">
            <div class="shushu-detail-title">${escapeHtml(cur.title)}</div>
            <span class="shushu-detail-step-tag">Step ${stepIdx + 1} / ${engine.steps.length}</span>
          </div>
          <div class="shushu-detail-block mantra">
            <span class="shushu-detail-label">📜 操作口诀</span>
            ${escapeHtml(cur.mantra)}
          </div>
          <div class="shushu-detail-block formula">
            <span class="shushu-detail-label">📐 数理公式与推演规则</span>
            ${escapeHtml(cur.formula)}
          </div>
          <div class="shushu-detail-block board">
            <span class="shushu-detail-label">🔄 盘面动态变化</span>
            ${escapeHtml(cur.boardNote)}
          </div>
          <div class="shushu-detail-block dialectics">
            <span class="shushu-detail-label">⚖️ 唯物辩证解读</span>
            ${escapeHtml(cur.dialectics)}
          </div>
        `;

        prevBtn.disabled = stepIdx === 0;
        nextBtn.disabled = stepIdx === engine.steps.length - 1;
      };

      prevBtn.addEventListener("click", () => {
        stopPlay();
        if (stepIdx > 0) {
          stepIdx--;
          render();
        }
      });

      nextBtn.addEventListener("click", () => {
        stopPlay();
        if (stepIdx < engine.steps.length - 1) {
          stepIdx++;
          render();
        }
      });

      resetBtn.addEventListener("click", () => {
        stopPlay();
        stepIdx = 0;
        render();
      });

      playBtn.addEventListener("click", () => {
        if (timerId !== null) {
          stopPlay();
          return;
        }
        if (stepIdx >= engine.steps.length - 1) {
          stepIdx = 0;
          render();
        }
        playBtn.textContent = "⏸ 暂停";
        timerId = setInterval(() => {
          if (stepIdx < engine.steps.length - 1) {
            stepIdx++;
            render();
          } else {
            stopPlay();
          }
        }, 2300);
        state.animTimers.push(timerId);
      });

      render();
    });
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
