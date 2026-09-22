![内容引擎：一个命题，长出多种表达](assets/readme/hero.png)

# 月明·内容引擎

围绕同一个作品命题，按需要组织研究、写作、配图、演示、视频和平台表达。

## 你会得到什么

- 围绕一个核心命题的内容与证据交接
- 按用户选择生成的文章、视频脚本或社交表达
- 不同形态共用的素材引用与制作交接

## 试着这样说

```text
用 moonlit-content-engine。把这次实测做成一篇公众号和一份现场讲解画布。复用同一套事实和素材，先从已有作品继续。
```

## 安装与首次使用

将本仓库的完整目录交给支持本地 Skill 的 Agent 安装，保留 `SKILL.md` 与随附资源。已有同名版本时先检查差异；使用版本锁的工作区沿用自身升级机制。

让 Agent 安装：

```text
请安装这个 Skill：https://github.com/zzyong24/moonlit-content-engine
```

也可通过 Skills CLI 安装：

```bash
npx skills add zzyong24/moonlit-content-engine
```

## 配置与依赖

这是编排入口，需要按所选任务安装对应的月明 Skill。内容判断依赖 moonlit-business-copywriter；研究、写作、配图、制作与发布分别路由。当前实现依赖 Moonlit Creator 的作品管理和账号品牌配置。

## 数据与使用边界

单独安装编排入口不会自动获得所有制作工具、音色和品牌素材。数据按实际调用的研究、生图、配音或平台服务流转；选择平台不自动授权发布。请提供自己的账号配置与素材。

## 配套 Skill

[business-copywriter](https://github.com/zzyong24/moonlit-business-copywriter)

## 详细说明

执行流程与资源导航见 [SKILL.md](SKILL.md)。安装检查不代表真实业务验收；需要外部服务、账号登录或付费生成的步骤，应在使用者自己的环境中验证。

---

月明水清深 · `moonlit-content-engine`

首图为 AI 生成的品牌概念插画，不是工具截图或执行结果。

## 技能导航

- [宇航员线稿配图](https://github.com/zzyong24/moonlit-astronaut-illustration) — 让动作，讲清一个观点
- [数字人横版视频](https://github.com/zzyong24/moonlit-avatar-video) — 让人物与信息，沿同一条时间线推进
- [对标研究](https://github.com/zzyong24/moonlit-benchmark-research) — 从真实内容里，找到可借鉴的结构
- [商业内容写作](https://github.com/zzyong24/moonlit-business-copywriter) — 把真实任务，写成观众关心的内容
- [内容引擎](https://github.com/zzyong24/moonlit-content-engine) — 一个命题，长出多种表达
- [文案去 AI 味](https://github.com/zzyong24/moonlit-de-ai-perception) — 保留事实与口吻，让表达自然一点
- [抖音数据萃取](https://github.com/zzyong24/moonlit-douyin-extractor) — 让作品指标与评论，成为复盘材料
- [解说画布](https://github.com/zzyong24/moonlit-explainer-canvas) — 边指、边缩放，把关系讲清楚
- [HTML 信息视频](https://github.com/zzyong24/moonlit-html-video) — 让旁白、字幕与画面，同步讲清机制
- [材料信息图](https://github.com/zzyong24/moonlit-material-illustration) — 把看不见的关系，变成看得懂的图
- [口述成纲](https://github.com/zzyong24/moonlit-oral-to-outline) — 把你讲过的想法，整理成清晰大纲
- [Skill 设计师](https://github.com/zzyong24/moonlit-skill-creator) — 把可重复的任务，做成可维护的能力
- [社交图文发布](https://github.com/zzyong24/moonlit-social-publisher) — 一次准备，逐平台核对与提交
- [真人出镜视频](https://github.com/zzyong24/moonlit-talking-head-video) — 让实录与证据，共同推进讲解
- [选题引擎](https://github.com/zzyong24/moonlit-topic-engine) — 找到值得讲、也有依据讲的那一题
- [选题雷达](https://github.com/zzyong24/moonlit-topic-radar) — 从信息信号里，找到你的内容角度
- [视频封面](https://github.com/zzyong24/moonlit-video-cover) — 把这一期讲什么，压缩成一眼可读
- [四平台视频发布](https://github.com/zzyong24/moonlit-video-publisher) — 核对每个草稿，再提交每个平台
- [视频脚本](https://github.com/zzyong24/moonlit-video-script) — 每句旁白，都有该解释的画面
- [公众号写作](https://github.com/zzyong24/moonlit-wechat-article) — 让主张、证据和解释，组成一篇文章
- [朋友圈文案](https://github.com/zzyong24/moonlit-wechat-moments) — 用一个具体片段，说出你的判断
- [公众号排版与草稿](https://github.com/zzyong24/moonlit-wechat-publisher) — 排好文章，再写入草稿箱
- [X 短帖与线程](https://github.com/zzyong24/moonlit-x-short) — 一个洞察，或一条连续的论证
- [小红书图文](https://github.com/zzyong24/moonlit-xiaohongshu) — 一张封面，配一段值得读的内容
