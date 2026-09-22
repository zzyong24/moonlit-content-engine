# 内容、配图与演示协作

本文件负责跨 Skill 路由。图片字段与版本规则由当前激活的 moonlit-astronaut-illustration/references/asset-contract.md 维护，不复制成第二套 schema。

## 从请求到产物

用户意图 → 读取当前作品/已认可材料 → 按需选题与补证 → 内容论证 → 语言审读 → 配图需求 → 独立配图生成/复用 → 图文预览 → 所选形态的制作与检查 → 用户审阅 → 有外发授权才进入发布 → 反馈进入下一轮。

内容定稿前可以试图验证机制，但不能让模板图决定文章结构。单形态请求只走相应分支；已有母稿、图片和授权优先复用。

## 责任与失败回路

| 输入或问题 | 责任 Skill | 输出或恢复 |
|---|---|---|
| 选题/受众任务不清 | topic-engine，按需 radar / benchmark-research | 选题卡、证据与范围 |
| 观点、事实、因果不通 | wechat-article 或对应内容 Skill | 修正文案与视觉需求 |
| 语言机械、指代断裂、制作话术上屏 | de-ai-perception + 当前内容/演示 Skill | 改观众可见表达 |
| 图片角色/动作/标签错误或缺图 | astronaut-illustration，或材料配图 Skill | 新资产 revision + 检查 |
| 图太小、关系不清、画布难讲 | explainer-canvas | 改布局、原生结构与讲解过渡 |
| 录屏、音频、字幕、剪辑 | 对应成片制作 Skill / video-editing | 媒体预览与验证 |
| 包或平台提交失败 | 对应 publisher | 核验目标状态，恢复同一包 |

名字上所有 moonlit- 前缀省略只为阅读，调用时解析完整 Skill 名。配图 Skill 可以由多个内容消费者调用；画布不会接管生图能力。

## 形态分支

- 公众号：wechat-article → 独立配图 → 图文审阅 → wechat-publisher。
- 演示录屏：已有内容与共享图 → explainer-canvas → .excalidraw + 提词稿 → 用户自行录屏。画布完成是此分支的完成点；后续剪片或发布只有用户另有请求才进入。
- 自动/真人成片：video-script → 按 production_mode 选择 talking-head-video、html-video 或 avatar-video → video-cover → video-publisher。
- 社交：xiaohongshu / x-short / wechat-moments 消费同一事实与适用图片，调整各自表达；小红书/抖音/X 可交 social-publisher。朋友圈当前内容 Skill 不等于自动发布能力。
- 历史 ThirdSpace video-draft-pipeline 只续接用户指定的旧工程，不作为当前作品的第二个入口。

## 内容与元数据

公众号结构作为内部内容依据；对外画布必须像原生讲解。画布里讲“用户确认后写入”，内部映射才记“变化三第 2 段”。原生 text、frame 名称、图片标注、画布总标题、提词正文同样检查。

## 唯一记录与更新

作品 artifacts/version → work.json（current 为兼容投影）；原图与 revision → 共享素材清单；形态使用关系 → 各自 manifest；文章来源对应 → article-map；对外投递凭证 → 不可变 distribution 包。

内容、配图、布局分别变化，只重做受影响部分。生成过、通过检查、用户认可、已投递是不同状态，不能相互推断。
