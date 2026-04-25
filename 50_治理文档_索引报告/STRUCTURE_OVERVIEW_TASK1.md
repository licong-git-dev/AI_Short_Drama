# 目录结构与文档分布总览（任务#1）

## 1) 范围与目标
- 范围：`D:/app/PythonFiles/AI_Short_Drama`
- 目标：梳理顶层到三级目录，标注核心文档、历史素材、过程文档、备份候选分布。

## 2) 顶层目录结构（Level 1）
- 配置与流程：`.claude/`、`.omc/`、`.specstory/`、`.vscode/`
- 创作主线文档：`outline.md`、`character.md`、`episode_index.md`、`script.progress.md`、`rhythm.md`
- 正式剧本输出：`episodes/`
- 素材与批量产出：`novel/`、`novel_update/`、`novel_other/`、`novel_other_1`~`novel_other_9`
- 文档区：`docs/`、`todos/`、`Execute_Plan/`
- 脚本/映射：`batch_replace.py`、`batch_replace_episodes.py`、`name_mapping.md`、`copyright_info.md`

## 3) 二~三级目录重点（Level 2-3）

### A. 正式创作主线
- `episodes/`：`EP-01.md` ~ `EP-100.md`（100集正文）
- 根目录主线文档：
  - `outline.md`（故事大纲）
  - `character.md`（人物小传）
  - `episode_index.md`（集目录）
  - `script.progress.md`（进度记录）

### B. 历史素材/候选库（高体量）
- `novel/`：100章历史小说素材
- `novel_update/`：11个更新稿
- `novel_other/`：11个文件
- `novel_other_1/`：11个文件
- `novel_other_2/`：8个文件
- `novel_other_3/`：107个文件（含备份子目录）
  - `novel_other_3/_duplicates_backup/`：75个重复稿备份候选
- `novel_other_4/`：流程化生产目录（见下）
- `novel_other_5/`：105个文件
- `novel_other_6/`：20010个文件（超大体量）
- `novel_other_7/`：5003个文件
- `novel_other_8/`：5003个文件
- `novel_other_9/`：5003个文件

### C. 过程文档/生产流水线
- `novel_other_4/`（流程化最完整）
  - `01_prompts/`：1
  - `02_drafts/`：9
  - `03_reviewed/`：1
  - `04_final/`：104
  - `05_quality_reports/`：0
  - 同层含`00_master_plan.md`、`00_生产线总控表.md`、`06_版本裁决表.md`等过程控制文档
- `docs/`
  - 现有治理文档：`PROJECT_STRUCTURE.md`、`DOCUMENT_INDEX.md`、`DOCUMENT_REVIEW.md`
  - `superpowers/plans/`、`superpowers/specs/`：设计/规划文档
- `Execute_Plan/`：`00_总览.md` 到 `08_风险预案.md`
- `todos/`：`00_市场趋势总览.md` 到 `04_创作行动清单.md`

### D. 隐藏目录（流程运行痕迹）
- `.claude/`：本项目代理与输出样式配置（含`agents/`、`output-styles/`）
- `.omc/state/`：会话状态、任务追踪、agent-replay日志
- `.specstory/`：历史记录与CLI配置

## 4) 分类分布结论

### 核心文档（Core）
- 主线创作最关键路径：
  1. `outline.md`
  2. `character.md`
  3. `episode_index.md`
  4. `episodes/EP-xx.md`
  5. `script.progress.md`

### 历史素材（History）
- 主要集中在`novel*`系列目录。
- `novel_other_6`与`novel_other_7~9`为最大体量区，需单独治理策略（索引/归档分层）。

### 过程文档（Process）
- 主要集中在`novel_other_4`、`docs/`、`Execute_Plan/`、`todos/`、`.omc/state/`。
- `novel_other_4`具备“提示词→草稿→复核→成稿”可追溯链路。

### 备份候选（Backup Candidates）
- 已明确备份候选：`novel_other_3/_duplicates_backup/`（75个）
- 疑似待归档区域：`novel_other_6~9`（高重复/高体量风险区，建议后续由索引任务进一步细分）

## 5) 关键路径清单
- 主线创作：
  - `D:/app/PythonFiles/AI_Short_Drama/outline.md`
  - `D:/app/PythonFiles/AI_Short_Drama/character.md`
  - `D:/app/PythonFiles/AI_Short_Drama/episode_index.md`
  - `D:/app/PythonFiles/AI_Short_Drama/episodes/`
  - `D:/app/PythonFiles/AI_Short_Drama/script.progress.md`
- 治理文档：
  - `D:/app/PythonFiles/AI_Short_Drama/docs/`
- 历史素材：
  - `D:/app/PythonFiles/AI_Short_Drama/novel*`
