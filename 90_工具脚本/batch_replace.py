# -*- coding: utf-8 -*-
"""
去IP化批量替换脚本
将《星际穿越2》中的版权元素替换为原创内容
"""

import os
import re

# 替换映射表
REPLACEMENTS = {
    # 标题
    '星际穿越2：新纪元': '星海23年',
    '星际穿越2': '星海23年',
    '《星际穿越2》': '《星海23年》',

    # 主要角色
    '库珀': '林远航',
    'Cooper': '林远航',
    '布兰德': '苏雪晴',
    'Brand': '苏雪晴',
    '墨菲': '林小萤',
    'Murph': '林小萤',
    'Murphy': '林小萤',

    # 家人
    '汤姆': '林浩',
    'Tom': '林浩',
    '小汤姆': '小林浩',
    '汤姆三世': '林昊天',
    '汤姆·库珀三世': '林昊天',

    # AI角色
    '塔斯': '小方',
    'TARS': '小方',
    '塔斯2号': '小方二代',
    '塔斯星': '方舟星',

    # 其他角色
    '艾德蒙斯': '陈默',
    'Edmunds': '陈默',

    # 组织
    'NASA': '星际探索署',
    'NASA戈达德太空中心': '星际探索署总部',
    '戈达德太空中心': '星际探索署总部',

    # 飞船
    '永恒号': '启航号',
    'Endurance': '启航号',
    '永恒号二代': '启航二号',
    '漫游者号': '探索者号',

    # 星球
    '艾德蒙斯星球': '希望星',
    '艾德蒙斯星': '希望星',

    # 科技概念
    '五维空间': '高维空间',
    '超立方体': '时空立方',

    # 特定称呼调整
    '库珀先生': '林远航先生',
    '布兰德博士': '苏雪晴博士',
    '墨菲博士': '林小萤博士',
}

# 需要处理的目录
NOVEL_DIR = r'D:\app\PythonFiles\AI_Short_Drama\novel'

def replace_content(content):
    """执行替换"""
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
    return content

def process_file(filepath):
    """处理单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = replace_content(content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"处理文件 {filepath} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("去IP化批量替换脚本")
    print("=" * 50)

    # 获取所有md文件
    files = [f for f in os.listdir(NOVEL_DIR) if f.endswith('.md')]
    files.sort()

    print(f"\n找到 {len(files)} 个文件待处理")

    modified_count = 0
    for filename in files:
        filepath = os.path.join(NOVEL_DIR, filename)
        if process_file(filepath):
            modified_count += 1
            print(f"[OK] 已处理: {filename}")
        else:
            print(f"- 无需修改: {filename}")

    print("\n" + "=" * 50)
    print(f"处理完成！共修改 {modified_count} 个文件")
    print("=" * 50)

if __name__ == '__main__':
    main()
