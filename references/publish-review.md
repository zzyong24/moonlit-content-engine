# 发布前必须运行 guoshen

## 触发与顺序

任何内容进入发布准备时执行：最终内容及配图/成片 → 去 AI 味与媒体验收 → **guoshen 风险预检** → 修复并重审 → 上传前内容门禁 → 上传未发布草稿/填表 → 实际页面设置与封面裁切复审 → 最终门禁/READY → 本次发布授权 → 提交与平台回读。发布器被单独调用也执行本步骤；包含公众号草稿上传、图文、X、视频、重发和跨平台复用。写作初稿、预览渲染、只读调研不强制跑审核，不能把本地渲染成功当作内容过审。

按名称解析当前激活 `guoshen`，读取其 SKILL.md。上游视频流程联合独立语音、字幕、全画面OCR与原帧语义检查，候选扫描不代表审核完成。不能只查字幕、只抽一张图或只跑敏感词表。上传前检查最终标题、简介、话题、封面文件、正文/成片及声明意图；仅上传后才出现的实际原生设置与封面槽位/裁切在草稿阶段检查；内部文件路径不当公开内容，但录屏中可见的地址栏要审。

目标平台明确后只审所选平台。上游注册表支持小红书、抖音、B站、视频号；公众号、X、朋友圈执行同一通用审核方法，并联网阅读该平台当前官方条款，补充对应平台审核。不把视频号规则当公众号规则，也不虚构上游已支持其他平台。资料或识别缺失时完成能做的部分，结果写需复核/未检查，不能生成完整通过回执。

严格零网址、国外AI推广等属于用户明确选择的配置，不因为安装自动启用。作者表达阶段不自动改判观点；**本步骤是用户明确要求的发布风险审核**，发现问题写内部报告，按语义给出具体修改，不往正文插入规避性小字、不推荐谐音拆字绕审。普通技术名词和真实收益复盘不机械判违规。审核通过不保证平台通过，也不代替本次外发授权。

## 产物和门禁

产物留在作品 `production/publish-review/<版本>/`：规则上下文、提取证据、候选、完整语义报告、结构化 `receipt.json`。不得上传私人原片或报告到 fork/上游。社区贡献另需具体公开授权。

报告按 guoshen 的五类结论逐平台输出；内容的明确风险、需复核、按用户要求修改或必要内容材料未检查，先解决再重审。仅未出现的原生设置和平台裁切可在内容阶段明确延期；不得将它们写成已检查，也不得借此跳过正文、语音、画面、版权、封面文件或渠道文案。回执只在实际语义审核完成后写，不由扫描器自动写“通过”。`inputs` 绑定实际发布文件和设置；正文/图/音轨/字幕/封面/渠道文案改变，旧回执失效。每个新的发布请求都重新执行 guoshen 的语义复核，不能拿上次回执免跑；同一次请求恢复时可复用未变且有效的证据。每次发布核验，24小时后再次审核，规则或Skill版本升级也重新审核。

回执示意（占位值不能作为真实回执）：

```json
{
  "schemaVersion": 1,
  "skill": "guoshen",
  "skillTreeSha256": "当前激活目录完整内容hash，按scripts/publish_review_gate.py的tree_sha计算",
  "reviewedAt": "带时区的实际审核时间",
  "skillFiles": {"SKILL.md": "实际SHA256", "resources/VERSION": "实际SHA256"},
  "inputs": [{"path": "相对回执的实际发布文件", "sha256": "实际SHA256"}],
  "report": [{"path": "report.md", "sha256": "实际SHA256"}],
  "ruleContext": [{"path": "rule-context.json", "sha256": "实际SHA256"}],
  "evidence": [{"path": "evidence.json", "sha256": "实际SHA256"}],
  "platforms": {"douyin": {
    "decision": "未发现明显问题", "blockingFindings": 0,
    "coverage": "complete", "semanticReview": true, "officialSourcesReviewed": true
  }}
}
```

对于公众号等注册表外平台，结果还需 `supplementalPlatformReview: true`，报告列真实补充规则来源与适用媒体形态。`complete` 指本次实际发布包和必需证据已经检查，OCR仍记录采样范围；不能拿抽样得出严格全片零网址。

门禁命令（从当前激活名称解析路径，不猜物理兄弟目录）：

```bash
python3 <moonlit-content-engine>/scripts/publish_review_gate.py \
  --guoshen-dir <当前激活guoshen目录> --receipt <receipt.json> \
  --platform <目标平台ID> --file <最终发布文件> --file <发布设置或渠道文案文件>
```

对每个实际输入重复 `--file`，正文内嵌图片、视频和封面也要传入。门禁只验证回执完整性、时效和输入一致，语义判断仍由执行 guoshen 的助手完成；不能靠伪造回执绕过步骤。报告原件和回执一起登记到作品 `publishRiskReview`，技术通过与用户认可/平台通过分开记录。

发布命令所需共享依赖采用显式环境变量注入：`MOONLIT_GUOSHEN_GATE` 为本Skill门禁脚本，`MOONLIT_GUOSHEN_DIR` 为当前激活guoshen目录，`MOONLIT_GUOSHEN_RECEIPT` 为本包回执路径。不得写死个人绝对路径，不得加入跳过审核开关。浏览器手工流程在上传前调用content门禁，最终提交前调用默认final门禁，页面内容变化后重新审。

## 分阶段回执

新回执按每个平台的 `stages.content` / `stages.final` 记录独立结论，各阶段仍须decision、blockingFindings、coverage、semanticReview、officialSourcesReviewed。内容阶段允许 `deferredChecks` 只含 `nativeSettings`、`platformCoverCrop`；这表示可上传未发布草稿并填表，不是READY或提交通过。最终阶段必须完成真实原生设置与封面验收，将 `nativeSettingsEvidence`、`platformCoverEvidence` 的路径/hash同时纳入inputs。没有这些证据，默认final门禁必须失败。旧回执继续按完整审核验证，不自动降格成内容通过。

门禁新增 `--stage content|final`，默认final。上传、草稿填表用content；READY/最终提交用final。不能添加跳过门禁的开关。发布器可以先收集页面证据，但只有final通过才报告READY。上传许可与本次最终发布授权分别按用户已授权范围执行，不重复确认已有授权。

## 缺失与恢复

依赖缺失、审核失败、产物变化或规则信息不足时停止外部上传/提交，继续完成本地修复和复核。不能把“没跑”写成“未发现问题”。本次内容发布授权持续有效时，修复完可继续，不重复询问同一授权；修改作者主张所需选择仍尊重当前授权范围。
