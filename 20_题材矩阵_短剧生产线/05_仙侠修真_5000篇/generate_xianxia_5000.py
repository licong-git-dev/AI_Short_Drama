from pathlib import Path
import re

base = Path(r'D:/app/PythonFiles/AI_Short_Drama/novel_other_7')
support = base / '_support'
base.mkdir(parents=True, exist_ok=True)
support.mkdir(parents=True, exist_ok=True)

SECTS = ['太虚宗','青冥观','离火宫','玄冰谷','万剑山','归元殿','九霄门','星河宗','伏龙寺','天机阁','无相峰','长生院']
REALMS = ['炼气','筑基','金丹','元婴','化神','返虚','合道']
IDENTITIES = ['外门弟子','废脉少主','药奴','灵田看守','剑冢弃子','丹房杂役','符坊学徒','镇妖司遗孤','魔宗卧底','世家庶子','天命圣女','被夺舍未遂者']
HOOKS = ['三日后逐出山门','本命剑破碎','灵根被挖','师尊陨落','婚约被毁','洞府被夺','宗门大比倒数第一','全族被屠只剩她','命灯将熄','心魔提前爆发','同门要她替死','天碑点名要她入局']
CHEATS = ['上古残卷','双修假契约','天道日志','残缺剑灵','能看见因果线的眼睛','可逆推丹方的神识','前世战斗记忆','会说话的山海异兽','半块仙骨','镇魔印','时间回溯一炷香','吞噬煞气的体质']
VILLAINS = ['大师兄篡位线','长老夺骨线','世家围剿线','魔尊借壳线','天骄踩压线','同门背刺线','丹阁封锁线','剑峰逐出线','师门灭口线','天道棋局线']
ALLIES = ['冷面剑修','嘴硬丹修','狐族少主','落魄佛子','散修医师','阵法天才','傀儡少女','被封印的器灵','守塔老人','掌灯师姐']
TONES = ['升级流','宗门权谋','复仇流','热血群像','黑化逆袭','诡谲探秘','师徒羁绊','仙门商战','夺宝流','天命对冲']
SCENES = ['断剑崖','镇魔塔','洗剑池','外门食堂','丹房地火室','问心阶','九幽秘境入口','藏经阁顶层','古战场遗址','天碑广场','寒潭洞府','诛邪台','灵兽谷','仙舟甲板','星陨荒原']
NAMES_F = ['云昭','叶清漪','姜晚','宁照雪','苏渡月','沈星回','温扶光','谢灵犀','顾听澜','林照微']
NAMES_M = ['裴照','闻惊寒','秦渡','谢临渊','宋归尘','顾长离','燕无咎','沈孤舟','陆停云','霍星沉']
ENDINGS = ['她终于握住自己的道，不再受任何人摆布。','他走过尸山血海，终于在万众之前改写命盘。','这一局虽赢，天门却在更高处重新打开。','她把仇都还了，却也看见真正的敌人还在云上。','他终于明白，修仙修的不是长生，是不向命低头。']

CHAPTER_SHAPES = [
    ('误入死局','暗中识局','第一次反杀','埋下远钩'),
    ('忍辱藏锋','借势翻面','抢夺机缘','局中再局'),
    ('试剑立威','丹局翻盘','秘境夺命','因果回收'),
    ('山门弃徒','重塑道骨','群敌围猎','天碑点名'),
    ('命灯将熄','仙骨争夺','旧案翻出','道心不折'),
]

MORALS = [
    '她必须在救师姐和夺机缘之间二选一','他必须先放走仇人，才能钓出真正幕后人','她必须承认心魔存在，才能继续破境','他必须让出眼前名声，换一条更长的生路',
    '她必须接受魔气入体，才能护住整座山门','他必须用最恨的人的方法赢一次','她必须毁掉一件至宝，才能保全同门','他必须亲手斩断旧情，才能让道心完整'
]


def pick(pool, idx, mul, add=0):
    return pool[(idx * mul + add) % len(pool)]


def chapter_text(idx, chap_idx, heroine, hero, sect, identity, hook, cheat, villain, ally, tone):
    scene = pick(SCENES, idx + chap_idx, 7, chap_idx)
    a, b, c, d = pick(CHAPTER_SHAPES, idx, 5, chap_idx)
    moral = pick(MORALS, idx, 11, chap_idx)
    p1 = f'{heroine}在{scene}醒来时，指尖先碰到的是冷霜，后碰到的才是血。她如今是{sect}的{identity}，而压在头顶的第一道死线，是“{hook}”。这不是给人喘息的局，她若慢一息，就会被推去做别人活路上的垫脚石。她没有浪费时间哀叹，只在最短的瞬间里确认三件事：谁想她死，谁能暂时利用，谁手里握着真正的钥匙。'
    p2 = f'幸好，她并非毫无筹码。她手中最大的变数，是“{cheat}”。那东西未必稳定，甚至可能随时反噬，可它让她在人人看衰的死局里，看见了一条很细却足够锋利的缝。她没有急着掀牌，而是先在{scene}里做了一个小动作：让敌人误判她的底牌，让旁观者误判她的脾气。修真界最危险的不是法器，是轻敌。'
    p3 = f'真正压过来的重山，来自“{villain}”。对方不怕她现在强，只怕她以后强，所以最好的办法就是在她还没站起来前，先把她踩碎。可{heroine}偏偏最擅长在碎石里找刀。她借{ally}稳住一口气，再借{hero}的名声挡下一轮围杀，把所有目光都拖进自己设计好的死角。等局势最紧时，她才一寸寸亮出自己的牌，不为炫耀，只为改天。'
    p4 = f'这一章真正最难的地方，不是斗法，不是破阵，而是选择——{moral}。她知道修仙不是单纯升级，也不是谁拿到宝物谁就赢。道心、代价、人情、仇恨，这些东西一旦选错，往后每一步都要拿命去填。正因为明白，她才在{scene}里完成了{a}、{b}、{c}、{d}这一整串动作，让原本注定压向她的命盘，第一次偏出刻线。'
    p5 = f'夜深时，{hero}来见她，语气仍旧冷得像雪，却第一次没把她当成随时可弃的棋子。他提醒她，下一道劫不会轻，只会更重。{heroine}只是把掌心的血擦掉，淡淡回了一句：重才好，轻了不配让我赢。她望向远处黑沉沉的山门，忽然觉得自己真正修的，或许从来不是长生，而是如何在所有人都要她低头的时候，仍然把脊梁挺直。'
    return f'## 第{chap_idx}章 {a}{b}\n\n{p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}\n'


def make_story(idx: int) -> str:
    sect = pick(SECTS, idx, 3)
    identity = pick(IDENTITIES, idx, 5)
    hook = pick(HOOKS, idx, 7)
    cheat = pick(CHEATS, idx, 11)
    villain = pick(VILLAINS, idx, 13)
    ally = pick(ALLIES, idx, 17)
    tone = pick(TONES, idx, 19)
    heroine = pick(NAMES_F, idx, 23)
    hero = pick(NAMES_M, idx, 29)
    title_core = f'{sect}{identity}{tone}'
    title = f'{title_core}第{idx:05d}篇'
    intro = f'{heroine}身在{sect}，是人人都觉得活不过三天的{identity}。她面前的死线是“{hook}”，手中唯一足够改变命运的变数，是{cheat}。可修真界从不讲公平，想要活，她就得先学会在“{villain}”织成的局里，把刀从别人手里抢回来。'
    parts = [f"# 《{title}》\n\n## 基本信息\n- 题材：仙侠修真 / {tone}\n- 宗门背景：{sect}\n- 身份：{identity}\n- 核心死线：{hook}\n- 金手指：{cheat}\n\n## 故事简介\n{intro}\n\n## 主要人物\n- **{heroine}**：局中弃子，心硬命更硬。\n- **{hero}**：危险同盟，冷到极致也强到极致。\n- **核心反派**：{villain}。\n- **关键助力**：{ally}。\n\n## 正文\n"]
    for chap in range(1, 21):
        parts.append(chapter_text(idx, chap, heroine, hero, sect, identity, hook, cheat, villain, ally, tone))
    ending = pick(ENDINGS, idx, 31)
    parts.append(f"## 尾声\n\n最后一剑落下时，{heroine}终于明白，修仙不是把自己修得像天，而是在所有天压下来的时候，仍敢逆着劫走。{ending}\n")
    return '\n'.join(parts)

(base / '000_生产规范.md').write_text('# 仙侠修真5000篇生产规范\n\n- 正文编号：001-5000\n- 每篇约1万字\n- 采用多题材池、多身份池、多金手指池、多章节骨架组合\n', encoding='utf-8')
(support / '7000_题材说明.md').write_text('# 仙侠修真题材说明\n\n- 题材：仙侠修真\n- 规模：5000篇\n- 每篇约1万字\n', encoding='utf-8')

for i in range(1, 5001):
    sect = pick(SECTS, i, 3)
    identity = pick(IDENTITIES, i, 5)
    tone = pick(TONES, i, 19)
    title_core = f'{sect}{identity}{tone}'
    safe = re.sub(r'[\\/:*?"<>|]', '', f'{title_core}第{i:05d}篇')
    (base / f'{i:03d}_{safe}.md').write_text(make_story(i), encoding='utf-8')

(support / '7999_最终交付清单.md').write_text('# 最终交付清单\n\n- 当前正文范围：001-5000\n- 题材：仙侠修真\n- 支持文件位于 _support 目录\n', encoding='utf-8')
print('done')
