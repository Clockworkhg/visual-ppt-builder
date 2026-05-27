# Visual PPT Builder

[English](README.md)

Visual PPT Builder 是一个 Codex skill，用于根据简短需求、产品图、头像、
参考风格、提纲或文案，生成视觉精美且可编辑的 PowerPoint 演示文稿。

这个 skill 面向一种更实用的工作流：AI 负责生成高质量视觉稿和素材方向，
最终 PPTX 里的文字、简单几何图形、图片素材和版式对象仍然保持可编辑，
可以继续在 PowerPoint 或 WPS 中修改。

## 它能做什么

- 当用户只给一句简短需求时，先询问关键风格选项
- 在生图前设计 `visual_prompt_strategy.md` 视觉提示词方案
- 为每一页生成独立的 16:9 视觉草图
- 在拆素材前校验视觉草图比例
- 用 PPT 原生形状、独立 PNG 素材和可编辑文本框重建幻灯片
- 校验最终 PPTX 的页数、文本对象和图片对象

## 适合场景

- 产品介绍 PPT
- 个人介绍 / 简历展示 PPT
- 视觉型方案汇报 PPT
- 课程或活动展示 PPT
- 需要 AI 视觉效果、但文字仍需可编辑的演示文稿

它不适合高度依赖动画的演示、超长研究报告，或强依赖 Excel 数据联动的财务分析
PPT。

## 核心流程

1. 根据用户需求整理 brief。
2. 当风格、受众、页数、精细度或事实信息会影响结果时，先询问用户。
3. 创建 `slide_plan.json`。
4. 创建 `visual_prompt_strategy.md` 和 `image_prompts.json`。
5. 为每一页生成一张独立的 16:9 视觉草图。
6. 使用 `scripts/validate_drafts.py` 校验草图比例。
7. 拆出有价值的图片素材，并将简单几何元素重建为 PPT 原生形状。
8. 组装带可编辑文本层的 PPTX。
9. 校验 PPTX，并生成构建报告。

## 预期输出

```text
outputs/<task-slug>/
  final_deck.pptx
  slide_plan.json
  visual_prompt_strategy.md
  image_prompts.json
  asset_manifest.json
  build_report.md
  drafts/
  assets/
  images/
  previews/
```

## 使用示例

```text
使用 $visual-ppt-builder，根据这张产品图生成一个 6 页可编辑产品介绍 PPT。
风格清新、高级，主色调为白色和薄荷绿。
```

```text
使用 $visual-ppt-builder，根据这张头像做一份个人介绍 PPT。
先询问我想要的视觉风格，然后生成视觉草图，并重建为文字可编辑的 PPTX。
```

```text
使用 $visual-ppt-builder，做一个 6 页社区反诈活动方案 PPT。
页面结构你来定，但选择视觉方向前先问我。
```

## 校验

校验 skill 文件夹：

```bash
python C:/Users/hersh/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./visual-ppt-builder
```

校验生成的视觉草图：

```bash
python scripts/validate_drafts.py outputs/demo/drafts --expect-count 6 --report outputs/demo/draft_validation_report.md
```

校验生成的 PPTX：

```bash
python scripts/validate_ppt.py outputs/demo/final_deck.pptx --expect-slides 6 --report outputs/demo/validation_report.md
```

## 安装

将此文件夹复制到 Codex skills 目录：

```powershell
Copy-Item -Path .\visual-ppt-builder -Destination "$env:USERPROFILE\.codex\skills\visual-ppt-builder" -Recurse -Force
```

然后重启或刷新 Codex，让它重新发现 skill 元数据。

## 文件指南

查看 [INDEX.md](INDEX.md) 了解完整 Markdown 索引和维护地图。
查看 [RULES.md](RULES.md) 了解不应偏离的核心规则。
修改 skill 前，先阅读 [AGENTS.md](AGENTS.md)。
