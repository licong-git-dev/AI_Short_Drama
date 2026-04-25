# 项目结构总览（任务 #3）

## 1. 盘点范围
- 根目录：`D:/app/PythonFiles/AI_Short_Drama`
- 盘点深度：顶层到三级目录
- 目标：明确目录分层、文档类型分布、关键路径与备份候选

## 2. 顶层目录与文件分布（Level 1）

### 2.1 核心文档（根目录）
- `outline.md`
- `character.md`
- `episode_index.md`
- `script.progress.md`
- `rhythm.md`

### 2.2 顶层目录（含条目数）
- `episodes/`（100）
- `novel/`（100）
- `novel_update/`（11）
- `novel_other/`（11）
- `novel_other_1/`（11）
- `novel_other_2/`（8）
- `novel_other_3/`（107）
- `novel_other_4/`（16）
- `novel_other_5/`（105）
- `novel_other_6/`（20010）
- `novel_other_7/`（5003）
- `novel_other_8/`（5003）
- `novel_other_9/`（5003）
- `docs/`（7）
- `Execute_Plan/`（9）
- `todos/`（5）

### 2.3 顶层工具脚本/说明
- `batch_replace.py`
- `batch_replace_episodes.py`
- `name_mapping.md`
- `copyright_info.md`

## 3. 二~三级目录重点（Level 2-3）

### 3.1 正式创作主线
- `episodes/EP-01.md` ~ `episodes/EP-100.md`
- 与 `outline.md` / `character.md` / `episode_index.md` / `script.progress.md` 构成主线闭环

### 3.2 历史素材与批量产出
- `novel/`：100章历史长文素材
- `novel_other*`：并行产线与题材库
- 超大体量区：
  - `novel_other_6/`（20010）
  - `novel_other_7/`（5003）
  - `novel_other_8/`（5003）
  - `novel_other_9/`（5003）

### 3.3 过程文档与治理文档
- `docs/`
  - 已有：`PROJECT_STRUCTURE.md`、`DOCUMENT_INDEX.md`、`DOCUMENT_REVIEW.md`
  - `superpowers/plans/`、`superpowers/specs/`
- `Execute_Plan/`：`00_总览.md`~`08_风险预案.md`
- `todos/`：`00_市场趋势总览.md`~`04_创作行动清单.md`

### 3.4 生产流水线样板（novel_other_4）
- `01_prompts/`（1）
- `02_drafts/`（9）
- `03_reviewed/`（1）
- `04_final/`（104）
- `05_quality_reports/`（0）
- 同层还包含总控、裁决、去重相关文档

### 3.5 备份候选与重复稿区域
- `novel_other_3/_duplicates_backup/`：75 个重复稿备份候选

## 4. 文档类型分布

### 4.1 核心文档（当前主线）
- `outline.md`
- `character.md`
- `episode_index.md`
- `script.progress.md`
- `episodes/*.md`

### 4.2 历史素材文档
- `novel/*.md`
- `novel_other*/**/*.md`
- `novel_update/*.md`

### 4.3 过程文档
- `docs/**/*.md`
- `Execute_Plan/*.md`
- `todos/*.md`
- `.omc/state/*`（状态与运行痕迹）

## 5. 可落地关键路径
- 主线创作路径：
  - `D:/app/PythonFiles/AI_Short_Drama/outline.md`
  - `D:/app/PythonFiles/AI_Short_Drama/character.md`
  - `D:/app/PythonFiles/AI_Short_Drama/episode_index.md`
  - `D:/app/PythonFiles/AI_Short_Drama/episodes/`
  - `D:/app/PythonFiles/AI_Short_Drama/script.progress.md`
- 治理路径：
  - `D:/app/PythonFiles/AI_Short_Drama/docs/`
- 历史素材路径：
  - `D:/app/PythonFiles/AI_Short_Drama/novel*`

## 6. 结论
- 该项目是“主线创作 + 历史素材 + 多批次产线”混合工作区。
- 主线文档集中且完整，适合持续增量创作。
- `novel_other_6~9` 属于高体量区域，后续应优先采用“先索引后治理”的低风险策略。
- `_duplicates_backup` 已形成明确备份候选集合，可作为后续归档策略入口。
