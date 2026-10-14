---
name: moonlit-content-engine
description: 月明水清深账号的内容生产与分发主编排入口。按需编排研究、内容、共享配图、公众号、Excalidraw 演示、视频和社交表达，复用同一作品的内容与素材。包含实际配图的正文用 Markdown 图片语法嵌入。当用户要出内容、做一源多形、自动分发或固化月明品牌内容生产时使用。
metadata:
  display_name: 月明·内容引擎
  icon: icon.svg
  version: "0.12.0"
  updated: "2026-10-14"
---

# 🌙 moonlit-content-engine · 主编排入口

> 编排内容生产、去 AI 味、资产核验与多平台发布，按顺序完成一源多形。

## 内容判断的共同起点

先按 [作者表达优先：信达雅](references/editorial-contract.md) 区分表达与研究。用户已提供观点或口述时，直接忠实组织、补充和润色，不自动开启论证或改判语义；以下选题判断流程仅在用户需要选题/研究/从零策划时调用。

## 共用的品牌、创意与反馈（2026-10）

- **品牌令牌**：所有形态的颜色、字体、字号、圆角、缓动和音效档位只取 [brand-tokens.md](references/brand-tokens.md)，各 Skill 不另定义色值。亮色 `paper` 用于封面/公众号/小红书/配图，深色 `night` 用于视频舞台。
- **创意概念**：选题确认后、写稿前按 [creative-concept.md](references/creative-concept.md) 提 3 个不同类型的概念、选 1 个作为本期母意象，写入 content_brief 的 `creative_concept`，脚本、封面、视频、配图从它出发。
- **反馈台账**：用户的审美与质量反馈写入 [feedback-ledger.md](references/feedback-ledger.md) 对应分区；每个 Skill 开工前读通用和本形态分区，交付时说明已自检哪些条目。

进入选题或内容判断前，按当前工程激活列表解析依赖 `moonlit-business-copywriter`，读取其 `references/content-first-principles.md`；不可假定两个 Skill 的物理目录相邻。依赖缺失时报告缺口，不静默改用历史副本。先明确具体处境、关切及其依据、预期观众变化、材料支持、未知与分歧、帮助范围，再选表达与象限。获得感包含理解、区分、判断、尝试和感受；不强制痛点、纠错、确定结论或CTA。使用content_brief传递这些判断，经营目标不替代观众价值。

## When to use

- 用户要为月明水清深账号出内容（任何形态）
- 用户要做"一鱼多吃"
- 用户要自动分发小红书图文、X 线程或已确认成片
- 用户要批量出周选题
- 用户要复用之前的社媒模板

不适用：

- 选题灵感阶段 → 用 `moonlit-topic-engine`
- 品牌规范变更 → 手动改 `moonlit-brand-overlay.md`
- 单纯配图 → 按风格调用独立配图 Skill；封面 → 对应封面 Skill。

## 按需协作流程

### 知识入口与共同任务卡

在 Moonlit Creator 工程中，先读 `首页.md`、`knowledge/知识库入口.md` 和本作品当前记录；按需查创作者、产品、需求、案例、方法、内容六类入口，原事实仍归原记录。不要把旧研究、假设需求或候选案例升格为实测事实。完整交接契约见 [共同任务卡与回流](references/content-master-contract.md)。

新作品或继续多形态制作时，建立/读回已登记的 `contentMaster`，承载命题、观众任务、证据类别与来源、可见结果、已选形态和待验证项。它可以链接现有口述、简述、大纲或公众号；不强制先完成公众号。旧作品缺卡时仅补真实已知信息，不批量伪造历史认可。单形态轻量任务可以让本形态简述兼任任务卡。

已明确的平台不重复询问。各平台从共同命题与证据重新组织观众任务和信息顺序，不能把长稿机械截段。登记下游产物时保留实际 `inputs`、版本与 hash。同一视频多平台复用媒体，渠道文案/封面/发布记录分别维护；只有表达任务确实不同时新增剪辑。

完成研究、制作回顾或发布回执后，将可复用知识链接/沉淀到对应库，运行 `system-sync` 刷新检索与健康。文件生命周期归工作区工具及 `maintenance/lifecycle-policy.json`，内容引擎不另写清理算法、不删除原素材或发布凭证。

1. 按请求范围读取已有作品、研究和定位，只补信息缺口。选题与研究分别由 topic-engine、topic-radar、benchmark-research / redfox-intelligence 负责。
2. 公众号为本次母稿时，由 `moonlit-wechat-article` 忠实组织作者原意，再完成表达连贯性审读及 `moonlit-de-ai-perception`。不自动论证或插入规避性话术。其他单形态任务可从已认可材料直接进入对应内容 Skill。
3. 在内容阶段提出配图需求，由独立配图 Skill 生成或复用素材，登记到同一作品共享清单。公众号在这里嵌入图片；用户已要求继续的形态沿用这些图，不重新生一套。
4. 母稿或当前形态确认后，先询问本期要制作/发布哪些平台，不默认全平台派生。文字平台与视频平台分开询问：文字可选公众号、小红书、X、朋友圈、抖音图文；视频可选抖音、视频号、B站等。用户明确选择后，只为选中的平台生成内容或制作物。
5. 如果用户只选择公众号，只继续公众号排版、预览和发布准备；不生成小红书、X、朋友圈、视频脚本、视频成片或其他平台发布包。用户说“都发”“一源多形”时，才按所选平台批量派生。
6. 各形态独立可理解，共用事实与素材；逐形态核验内容连续性、视觉语义、资产引用与实际打开效果。制作说明留内部，观众可见表达直接讲内容。各阶段缺什么只返回该责任 Skill 修正。
7. **内容准备发布时必须先调用 `guoshen`**，读取并执行 [发布前审核合同](references/publish-review.md)，审核最终文件、正文/声画、封面、渠道文案与设置；修复后重审，生成当前输入绑定的报告和回执，内容门禁通过后可上传未发布草稿并填表；上传后核实际声明/设置与平台封面裁切，最终门禁通过才进入READY或提交。单独调用发布器也不能跳过。用户要求发布时才准备包，沿用会话内已授予的有效授权；没有外发授权不操作平台。发布器核验已确认内容与包的对应关系，按平台记录草稿、待审和已发布状态。
8. 观测结果回到选题、内容和素材需求。按影响范围更新消费者，保留历史发布包。
9. 明确用户纠错、实际失败恢复或规则冲突发生时，修好当前作品后检查本次激活的 Skill；发布前的制作纠错也适用。实际发布流程结束再做一次复盘。按 `moonlit-skill-creator/references/experience-loop.md` 查证据、去重和规则所有者；可复用的改维护源并升级工程运行快照，单次标题、话题、媒体 ID 和审核结果留在作品。无可复用改动时记“无需修改”，不做全库审计。

详见 [协作职责与交接](references/content-asset-collaboration.md)。本 Skill 负责路由与状态，不自行写完所有内容或直接生图。

## ⚠️ 图片嵌入规范（v0.7.1 新约束）

正文需要展示实际配图时，使用 Markdown 图片嵌入语法；研究笔记、配置说明、提词稿不为满足规则强行配图：

```markdown
✅ 正确（图片真嵌入）：
![配图 1：3件事钩子](assets/1-封面-3件事钩子.png)

❌ 错误（图片不显示，只是文字）：
📷 **配图 1**：assets/1-封面-3件事钩子.png
```

详见 `references/09-file-naming.md` 的"图片嵌入规范"章节。

公众号图片必须区分职责：产品截图用于证明，月明材料信息图用于解释机制，月明宇航员用于引导、操作、决策等品牌叙事。IP 不为露出而露出，纯架构图和数据图以信息为主。手绘宇航员解释图调用 `moonlit-astronaut-illustration`，材料信息图调用 `moonlit-material-illustration`。共享素材登记在 `production/illustrations/visual-manifest.json`；文章使用清单导出为文章 assets/visual-manifest.json，进入发布前必须通过 `moonlit-wechat-publisher/scripts/check_visuals.py`。

## 内容、素材与制作的责任边界

| 角色 | Skill | 主要产物 |
|---|---|---|
| 主编排 | moonlit-content-engine | 范围、路由、当前状态 |
| 母稿写作 | moonlit-wechat-article | 作者原意的正文表达、配图需求 |
| 语言审读 | moonlit-de-ai-perception | 连贯、自然的内容 |
| 可复用配图 | moonlit-astronaut-illustration / moonlit-material-illustration | 图片与素材版本 |
| 自由讲解 | moonlit-explainer-canvas | 原生画布、讲解稿、内部映射 |
| HTML 翻页讲解 | moonlit-ppt-html | 可编辑截图的 HTML PPT、独立讲解稿、离线文件 |
| 社交表达 | moonlit-xiaohongshu / moonlit-x-short / moonlit-wechat-moments | 形态文案与素材引用 |
| 视频策划 | moonlit-video-script | 脚本、画面职责、制作模式 |
| 成片制作 | 三类独立制作 Skill | 预览、成片、媒体验收 |
| 封面 | moonlit-video-cover | 对应作品的封面 |
| 发布风险预检 | guoshen，合同由本Skill的 references/publish-review.md 维护 | 各平台语义报告、证据与版本绑定回执 |
| 发布 | moonlit-wechat-publisher / moonlit-social-publisher / moonlit-video-publisher | 发布包与平台记录 |

从当前工程激活目录解析这些 Skill，不使用历史 .nomi 路径猜测来源。

## 图文与 X 自动分发（v0.9.2）

当用户选择一源多形自动分发时，或在平台询问中明确勾选对应形态时：

1. `moonlit-xiaohongshu` 默认输出 `single_cover`、1 张封面、配文和 5–8 个话题；只有图片各自提供独立证据、步骤、数据或对照时输出 `carousel` 与 2–18 张固定路径。
2. `moonlit-x-short` 默认使用 `thread` 模式，把同一命题改写成 5–8 个连续帖子；不是把小红书正文机械切段。
3. 抖音短图文使用 `douyinGraphic`；公众号同源长文、正文超过 1000 字或用户要求“和公众号一样”时使用 `douyinArticle`，进入原生“发布文章”编辑器，保留完整论证与正文配图。
4. `moonlit-social-publisher` 先把所选平台都准备到 `READY`，再消费用户本次明确授权。
5. 小红书发布后以笔记管理核验；抖音图文以内容管理中的标题和图文体裁核验；X 使用原生线程编辑器的 `Post all`，以线程详情页核验顺序和数量。
6. 平台审核中统一记为 `submitted`；只有确认公开可见才记为 `published`。同一平台的视频和图文必须分别记录，不能互相覆盖状态。

### 平台询问门槛

公众号母稿确认后，必须先问一次平台范围，再继续下游工作。询问要让用户可以只选一个平台，也可以分别选择文字和视频：

> 这期准备发哪些平台？
>
> 文字：公众号 / 小红书 / X / 朋友圈 / 抖音图文
>
> 视频：抖音 / 视频号 / B站 / 暂不做视频

如果用户只说“继续”“往下走”但没有选择平台，先完成这次询问，不创建下游平台文件。用户已经在当前消息明确说了平台的，视为已选择，不重复询问。

“发哪些平台”和“是否现在发布”是两件事：平台选择只决定生成哪些内容与发布准备，不能推断用户授权外发。每个平台仍需经过对应 Skill 的核验和用户明确的发布授权。

小红书和 X 共用事实与证据，不共用一模一样的开头、段落节奏和 CTA。用户明确要求抖音图文与公众号相同时，按上面的 `wechat_same_story` 规则处理。X 每帖最多附 4 个媒体项；图片应分配到解释它的帖子。

## 视频交付路由（v0.8.0）

AI 视频旁白默认复用 MiniMax 真人复刻音色 `YOUR_AUTHORIZED_VOICE_ID`（`speech-2.8-hd`），制作细则由 `moonlit-html-video/references/voiceover.md` 维护。已确认音色后直接推进完整制作。更换旁白必须联动字幕、场景、章节、音效及作品状态，不能只交付新脚本或音频。用户已有的明确授权在当前任务中持续有效，不因为切换 Skill 重复索取。

`moonlit-video-script` 只负责口播组织与分镜，不决定成片技术；观点论证仅在用户明确请求时另行处理。脚本确认后必须写入 `production_mode`，再选择独立制作链路：

| production_mode | 制作 Skill | 用途 |
|---|---|---|
| `talking_head_broll` | `moonlit-talking-head-video` | 真人实录出镜＋证据/演示 |
| `html_explainer` | `moonlit-html-video` | 纯 AI PPT/信息演示＋配音 |
| `avatar_explainer` | `moonlit-avatar-video` | 复用手势库的 AI 数字人＋信息/演示 |
| `excalidraw_explainer` | `moonlit-explainer-canvas` | 自由讲解的原生画布＋独立提词稿，完成后交用户录屏 |
| `html_presentation` | `moonlit-ppt-html` | 手动翻页的 HTML 演示稿＋讲解稿，固定宇航员与月牙 IP，支持截图拖动和离线保存 |

用户说“HTML PPT”“网页演示”“像 CreatorOS 那样边翻页边录屏”时选择 `html_presentation`。先做 HTML 演示稿不触发配音、SRT、成片渲染或平台发布询问；已确认内容可直接制作可审看版本。

成片三类默认 16:9 横版，除非用户明确要求其他画幅。入口按 production_mode 路由，独立制作逻辑不合并；成片共用配音时钟与媒体验收合同。Excalidraw 分支只复用内容与素材，不自动进入配音、数字人、HTML 成片或发布。

不同制作类型完成成片后统一调用 `moonlit-video-cover`，按当前工程 AGENTS 与用户确认的品牌规范处理。Moonlit Creator 的平台封面默认暖白、深蓝、铜橙、本人真实形象与本期证据，纯 AI 视频也遵守；HTML 演示稿自身的宇航员视觉另按其已确认例外。按当前工作区的确认或Agent验收委托完成逐平台画幅封面后，再生成包含最终视频、标题、简介、关键词/话题、原创状态和封面绝对路径的发布交接包。交接包确认后才进入 `moonlit-video-publisher`；制作 Skill 不操作平台，`moonlit-video-publisher` 不修改视频和封面设计。

## 内容交接前去 AI 味

所有产物**必须**过 `moonlit-de-ai-perception` 才能发布**。

11 类检测项：
- 高频词（"此外""综上所述""值得注意的是"）
- 过度结构化、虚假客观性、机械化连接词
- 完美主义陷阱、公式化结尾、过度修饰
- 情感缺失、"不是而是"假靶子
- 莫名其妙的比喻、高频堆叠副词

### 语言审读不改判作者观点

作者表达与明确更正的范围，以 [内容与样例规则](references/editorial-contract.md) 为准。内容引擎只把本次授权的表达修订传给已选择形态，内部编辑原因留作品记录。

## ⚠️ skill 目录保持干净

每个 sub-skill 目录只放：
- `SKILL.md`、`references/`、`templates/`、`scripts/`

**禁止**：articles/、内容文件、配图；这些产物应放在当前 `works/YYYY/W-*/content/` 或 `production/` 中。

## 文件命名规范（强制 v0.5.1）

```
MMDDHHMM-[纯中文主题]-[平台].md
```

## 🆔 ID 锁定（v0.5）

**`月明水清深`**

## Pitfalls

- ❌ 在用户要求公众号母稿的一源多形任务中跳过已约定的公众号母稿先做其他
- ❌ 公众号确认后默认生成全平台内容
- ❌ 用户只选择公众号时创建小红书、X、朋友圈或视频脚本
- ❌ 把“继续流程”理解成“所有平台都做”
- ❌ 忽略用户已给出的内容认可与后续制作授权，反复要求同一确认
- ❌ **跳过成稿的语言审读**
- ❌ **用 `📷 文字说明` 代替真图片嵌入**（v0.7.1 关键）
- ❌ 为凑数量上传没有独立信息价值的小红书图片，或在纯架构图、数据图中硬塞 IP
- ❌ 产出物放进 skill/articles/ 目录
- ❌ 文件名用英文连字符
- ❌ 漏改 ID 写成"月明水情深"
- ❌ 正常发布时重复运行 Bootstrap
- ❌ 未经用户确认预览就上传图片或创建公众号草稿
- ❌ 把 `html_explainer` 的画面规则套到真人口播或其他视频类型
- ❌ 在成片未确认前生成四平台发布任务，或让发布 Skill 反向修改成片
- ❌ 把小红书图文发布逻辑塞进视频发布器，或用视频状态覆盖图文状态
- ❌ 把抖音图文当作抖音视频发布，或向抖音图文上传 GIF
- ❌ 把 X 线程当作一条超长单帖，或先发主帖再无保护地逐条补回复
- ❌ 把发布授权写进配置、发布包或下一次任务
- ❌ 把作者或 AI 的理解错误写成面向读者的“澄清”“纠正”“不是 X 而是 Y”

## 研究、选题与发布反馈交接

## 对外表达与内部来源

“母稿、文章主线、开篇、收束、据母稿绘制”等制作元信息只进 notes、方向文档与内部映射，不能输出到演示、图片标签或朗读稿。每种形态都要独立可理解，并保留相邻内容的因果与指代。

真实外部来源与用户明确要比较的资料属于内容；按理解需要保留作者、出处链接和事实限定。不能把内部制作说明禁令扩大成删除必要来源，也不机械附上一整张内部研究清单。

路由按请求范围：取数用 redfox-intelligence，对标与商业推演用 moonlit-benchmark-research，热点用 moonlit-topic-radar，选题用 moonlit-topic-engine。只要选题/研究时停在那里；上面的全流水线用于用户明确要求一源多形，单形态请求只制作该形态，不强制先写公众号。

制作前读取当前认可scope与选题卡，将topic_id映射到新建work_id；共同字段按 moonlit-benchmark-research 的 references/research-contract.md。来源、证据状态、结构卡、去重范围、单一CTA和观测指标随内容传递。不同平台共享核心命题，改变受众表达与入口，不为一次分发另建作品。

发布后按 moonlit-topic-engine/references/07-data-loop.md 回写观测窗口、任务对应指标与下轮决策；不以播放量代替成交。计划中的周更频率与服务方向保持实验状态，未经证实不宣称来自对标的成功路径。不扩展用户已有发布授权范围。

Skill 复盘按 `moonlit-skill-creator/references/experience-loop.md` 处理：先分清平台真实失败、工具拦截、作者偏好和一次性内容选择；查实际调用与结果后再修改，避免把一条工具错误扩大为整个发布通道不可用。修改维护源、验证后用工作区 `skills-pin --skill` 升级本次涉及的 Skill，并在作品内记录已执行的修复与尚未实测的部分。普通内容任务只审本次实际用到的 Skill，不触发全库审计。

## 工程接入与公共内容规则

开始任务先读 [editorial-contract.md](references/editorial-contract.md)，只加载当前形态需要的专业 Skill。Moonlit Creator 工程若有 maintenance/WORKFLOW.md，按其命令登记产物、检查手工编辑、查询修改影响与锁定版本；work.json 的 artifacts 是当前产物权威记录，current 和索引由工具派生。
