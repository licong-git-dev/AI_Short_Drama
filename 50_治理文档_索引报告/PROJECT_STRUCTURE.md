# 项目结构总览

## 项目定位

`AI_Short_Drama` 是一个短剧/小说混合生产工作区。

它不是单一成品目录，包含：
- 当前正式短剧主线文档
- 已完成的 100 集剧本与 100 章小说
- 多批次小说/短剧素材目录
- 执行计划与说明文档
- 大规模批量生成内容目录
- 工具与代理配置目录

## 顶层结构

### 一、核心主线文档
位于项目根目录，属于当前正式创作主线：
- `outline.md`
- `character.md`
- `episode_index.md`
- `script.progress.md`
- `episodes/`

### 二、主线正文目录
- `episodes/`：100 个分集剧本文档
- `novel/`：100 个小说章节文档

### 三、历史素材与批量内容目录
- `novel_update/`：小规模更新批次
- `novel_other/`
- `novel_other_1/`
- `novel_other_2/`
- `novel_other_3/`
- `novel_other_4/`
- `novel_other_5/`
- `novel_other_6/`
- `novel_other_7/`
- `novel_other_8/`
- `novel_other_9/`

这些目录并非同一规范下的单一项目，更像并行生产区、题材库、拆分稿库、批量产出库。

### 四、过程文档与规划目录
- `Execute_Plan/`：执行方案与阶段性计划
- `docs/`：项目说明与治理文档
- `todos/`：任务记录

### 五、规范与工具目录
- `.claude/`：项目创作规则、代理说明、输出风格
- `.omc/`：运行状态与自动化产物
- `.specstory/`：会话/说明数据
- `.vscode/`、`.ruff_cache/`：工具缓存

## 目录统计摘要

根据当前盘点：

| 目录 | 文件数 | 子目录数 | Markdown 数量 | 说明 |
|---|---:|---:|---:|---|
| `.claude/` | 5 | 2 | 4 | 创作规则与代理配置 |
| `docs/` | 2 | 3 | 2 | 说明文档 |
| `episodes/` | 100 | 0 | 100 | 正式分集剧本 |
| `Execute_Plan/` | 9 | 0 | 9 | 执行方案 |
| `novel/` | 100 | 0 | 100 | 正式小说章节 |
| `novel_other/` | 11 | 0 | 11 | 历史/平行素材 |
| `novel_other_1/` | 11 | 0 | 11 | 历史/平行素材 |
| `novel_other_2/` | 8 | 0 | 8 | 历史/平行素材 |
| `novel_other_3/` | 181 | 1 | 180 | 大量题材稿，含重复备份 |
| `novel_other_4/` | 204 | 15 | 204 | 流程化生产目录 |
| `novel_other_5/` | 105 | 0 | 105 | 命名最规整的分卷样板 |
| `novel_other_6/` | 20016 | 1 | 20007 | 超大批量文档库 |
| `novel_other_7/` | 5004 | 1 | 5003 | 超大批量文档库 |
| `novel_other_8/` | 5004 | 1 | 5003 | 超大批量文档库 |
| `novel_other_9/` | 5004 | 1 | 5003 | 超大批量文档库 |
| `novel_update/` | 11 | 0 | 11 | 更新批次 |
| `todos/` | 5 | 0 | 5 | 待办记录 |

## 当前治理结论

### 正式主线
当前正式主线建议固定为：
- `outline.md`
- `character.md`
- `episode_index.md`
- `script.progress.md`
- `episodes/`

### 历史素材区
以下目录建议视为历史素材或并行生产区：
- `novel/`
- `novel_update/`
- `novel_other*`

### 过程区
以下目录建议视为过程文档区：
- `Execute_Plan/`
- `docs/`
- `todos/`

### 风险点
- `novel_other_6~9` 体量极大，不宜直接重命名或迁移。
- `novel_other_3` 存在 `_duplicates_backup`，需保守处理。
- 同类文档命名体系并不统一，应先建索引，再做整理。

## 整理原则
- 先索引，后归档。
- 先标记，后处理。
- 不删除文件。
- 不移动核心主线文档。
- 大体量目录优先建立说明，不做破坏式改动。
