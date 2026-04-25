# 文档索引

## 1. 正式主线入口

以下文件应视为当前项目的正式主入口：

### 核心文档
- `D:\app\PythonFiles\AI_Short_Drama\outline.md`
- `D:\app\PythonFiles\AI_Short_Drama\character.md`
- `D:\app\PythonFiles\AI_Short_Drama\episode_index.md`
- `D:\app\PythonFiles\AI_Short_Drama\script.progress.md`

### 正式正文
- `D:\app\PythonFiles\AI_Short_Drama\episodes\`
- `D:\app\PythonFiles\AI_Short_Drama\novel\`

## 2. 规范说明入口

- `D:\app\PythonFiles\AI_Short_Drama\.claude\CLAUDE.md`
- `D:\app\PythonFiles\AI_Short_Drama\.claude\agents\script-aligner.md`
- `D:\app\PythonFiles\AI_Short_Drama\.claude\agents\script-record.md`

说明：
- `.claude/CLAUDE.md` 提供理想流程与模板基线。
- 当前实际文档结构比模板更扩展，应以“实际主线 + 规则基线”共同治理。

## 3. 过程文档区

### 计划与执行
- `D:\app\PythonFiles\AI_Short_Drama\Execute_Plan\`
- `D:\app\PythonFiles\AI_Short_Drama\docs\`
- `D:\app\PythonFiles\AI_Short_Drama\todos\`

### 其他辅助文件
- `name_mapping.md`
- `rhythm.md`
- `copyright_info.md`

这些文档不属于正式剧情主线，但对生产流程、命名统一、节奏控制和版权说明有辅助价值。

## 4. 历史素材区

### 中小规模目录
- `novel_update/`
- `novel_other/`
- `novel_other_1/`
- `novel_other_2/`

### 中大规模目录
- `novel_other_3/`
- `novel_other_4/`
- `novel_other_5/`

### 超大规模批量目录
- `novel_other_6/`
- `novel_other_7/`
- `novel_other_8/`
- `novel_other_9/`

说明：
- 这些目录建议统一视为“历史素材/批量生产区”。
- 暂不作为正式主线入口。
- 后续若要归档，应先建立更细粒度索引，不直接动文件。

## 5. 重点目录说明

### `novel_other_3/`
- 大量题材稿混排。
- 含 `_duplicates_backup/`，存在重复/备份候选。
- 适合建立“主稿 / 备份 / 待比对”三级标记。

### `novel_other_4/`
- 采用流程式目录：如 `01_prompts/`、`02_drafts/`、`03_reviewed/`、`04_final/`、`05_quality_reports/`。
- 适合作为“流程型生产目录”样板。

### `novel_other_5/`
- 命名最规整。
- 采用 `大纲_区间`、`正文_区间`、`正文样稿_区间` 结构。
- 可作为批量文档命名规范参考样板。

### `novel_other_6~9/`
- 文档量极大。
- 优先做目录级说明与分类，不建议做细粒度人工整理。

## 6. 当前推荐分区

| 分区 | 路径 | 当前角色 |
|---|---|---|
| 正式主线 | 根目录四件套 + `episodes/` | 正式创作入口 |
| 正式长文 | `novel/` | 已完成长文正文 |
| 规范规则 | `.claude/` | 创作规范与代理配置 |
| 过程文档 | `Execute_Plan/`、`docs/`、`todos/` | 计划、说明、待办 |
| 历史素材 | `novel_update/`、`novel_other*` | 素材、批量产出、旧稿 |
| 工具状态 | `.omc/`、`.specstory/` 等 | 自动化运行痕迹 |

## 7. 整理建议
- 主线文档保持不动。
- 历史素材先索引，不迁移。
- 重复候选先标记，不删除。
- 后续如需统一命名，优先参考 `novel_other_5/` 的区间命名法。
