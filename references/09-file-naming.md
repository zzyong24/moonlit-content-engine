---
title: title.md
status: active
---

# ⚠️ 图片嵌入规范（v0.5.2 新增）

## 强制要求

**.md 文件必须用标准 markdown 语法嵌入图片**：

```markdown
![配图 1：XXX](assets/1-封面-3件事钩子.png)
```

❌ **禁止用文字说明代替真图片**：
```markdown
📷 **配图 1**：assets/1-封面-3件事钩子.png    ← 这种只是文字，渲染器不会显示图片
```

## 为什么

- 文字说明在 markdown 渲染器里只显示路径文字，**不显示实际图片**
- 用户打开 .md 文件看到的是"assets/1-封面-3件事钩子.png"这段文字，**不是图**
- 必须用 `![alt](path)` 语法，markdown 渲染器才会**真的显示图片**

## 语法格式

```
![alt 描述](相对路径)
```

### 要素

- `!`：标记这是图片
- `[alt]`：图片描述（给读者看，也是 SEO 文本）
- `(path)`：相对路径（相对于 .md 文件位置）

### 示例

```markdown
![配图 1：3件事钩子](assets/1-封面-3件事钩子.png)

![封面图：爆款方法论](assets/1-封面-XXX.png)

![金句卡：核心洞察](assets/金句-XXX.png)
```

## 路径规则

- **相对路径**（不是绝对路径）
- 相对于 .md 文件所在目录
- 输出文件统一在 `outputs/MMDDHHMM-[主题]/`
- 图片在 `outputs/MMDDHHMM-[主题]/assets/`
- 引用写：`assets/1-封面-XXX.png`

## 多图嵌入（小红书 9 图）

```markdown
![封面图](assets/1-封面-XXX.png)

![图 2](assets/2-XXX.png)
![图 3](assets/3-XXX.png)
...
![图 9](assets/9-CTA-XXX.png)
```

或用表格列出：

```markdown
| 图序 | 嵌入 |
|---|---|
| 1 | ![封面图](assets/1-封面-XXX.png) |
| 2 | ![图 2](assets/2-XXX.png) |
| ... | |
```

## 自检清单

发布前确认：
- [ ] 所有图片都用 `![alt](相对路径)` 语法
- [ ] 没有 `📷 XXX：path.png` 这种纯文字
- [ ] alt 描述简洁（不超过 20 字）
- [ ] 路径相对当前 .md 文件位置

## Pitfalls

- ❌ 用绝对路径（`/Users/...`）——文件移动就失效
- ❌ alt 描述太长（变成噪音）
- ❌ 路径错误（typo 或大小写）
- ❌ 文件不存在（图片显示裂图）
- ❌ 用 base64 内嵌（文件太大）