default hide_dialogue_ui = True

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    slow_cps 16  #每秒出现的字符数
    slow_abortable True  #点击鼠标后全部显现文本







define i = Character("五树")
define j = Character("树里")
define r = Character("润")
define y = Character("芳野")
define f = Character("建昭")
define q = Character("伊势")
define g = Character("青磁")
define n = Character("夏生")





transform realleft:
    xpos 0.25
    xanchor 0.5

transform littleleft:
    xpos 0.35
    xanchor 0.5

transform realright:
    xpos 0.75
    xanchor 0.5

transform littleright:
    xpos 0.65
    xanchor 0.5


transform zi:
    xpos 0.48
    xanchor 0.5
    ypos 0.48
    yanchor 0.5


transform uu:
    yalign 0.15
    xalign 0.5

transform uf:
    yalign 0.25
    xalign 0.5

transform ud:
    yalign 0.3
    xalign 0.5

transform fu:
    yalign 0.4
    xalign 0.5

transform ff:
    yalign 0.5
    xalign 0.5

transform fd:
    yalign 0.6
    xalign 0.5






init python:
    renpy.music.register_channel("remusic", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)











style re_small:
    color "#c00d0d"
    size 35
    textalign 0.5

style re_big:
    color "#c00d0d"
    size 70
    textalign 0.5

style wh_small:
    color "#ffffff"
    size 40
    textalign 0.5

style wh_big:
    color "#ffffff"
    size 80
    textalign 0.5






image t1 = Text("腐姬",style="re_big")
image t2 = Text("neuthanasia",style="re_small")
image t3 = Text("归省",style="wh_big")
image t4 = Text("~jamais vu~",style="wh_small")
image t5 = Text("企画・剧本",style="wh_small")
image t6 = Text("星空めてお",style="wh_big")
image t7 = Text("原画・角色设计",style="wh_small")
image t8 = Text("中村哲也",style="wh_big")
image t9 = Text("背景原画",style="wh_small")
image t10 = Text("米谷要",style="wh_big")
image t11 = Text("合作：スタジオ尻滅裂",style="wh_small")
image t12 = Text("ＣＧ绘制",style="wh_small")
image t13 = Text("しまさらゆめき\n犬太郎\nfmaina\n白鬼",style="wh_big")
image t14 = Text("中村哲也\nK.TEN\n桜瑞",style="wh_big")
image t15 = Text("音乐",style="wh_small")
image t16 = Text("杂音工房NOIZE",style="wh_big")
image t17 = Text("程序",style="wh_small")
image t18 = Text("Wiz codeX",style="wh_big")
image t19 = Text("制作・著作\n\n株式会社ビジネスパートナー\nLiar-soft",style="wh_big")










image bg 0504-dark2 = im.MatrixColor(
    "bg 0504.webp",
    im.matrix.brightness(-0.3))

image bg 0504-dark1 = im.MatrixColor(
    "bg 0504.webp",
    im.matrix.brightness(-0.15))

image z9004-dark2 = im.MatrixColor(
    "z9004.webp",
    im.matrix.brightness(-0.3))

image z9006-dark2 = im.MatrixColor(
    "z9006.webp",
    im.matrix.brightness(-0.3))

image z9006-dark1 = im.MatrixColor(
    "z9006.webp",
    im.matrix.brightness(-0.15))





image bg 0601-dark2 = im.MatrixColor(
    "bg 0601.webp",
    im.matrix.brightness(-0.3))

image bg 0601-dark1 = im.MatrixColor(
    "bg 0601.webp",
    im.matrix.brightness(-0.15))

image z9018-dark2 = im.MatrixColor(
    "z9018.webp",
    im.matrix.brightness(-0.3))

image z9018-dark1 = im.MatrixColor(
    "z9018.webp",
    im.matrix.brightness(-0.15))


image z9019-dark1 = im.MatrixColor(
    "z9019.webp",
    im.matrix.brightness(-0.15))

image z9020-dark1 = im.MatrixColor(
    "z9020.webp",
    im.matrix.brightness(-0.15))

image z9021-dark1 = im.MatrixColor(
    "z9021.webp",
    im.matrix.brightness(-0.15))












label splashscreen:

    
    $ renpy.movie_cutscene("mov/0002.mpg")
    $ renpy.movie_cutscene("mov/0001.mpg")


    return














label start:

    stop music
    play sound "0602.mp3"

    pause(5)

    "雨水从车窗倾泻而下，打湿了我的手臂。"

    "列车驶过了无人值守的天满泽站。\n"

    extend "离终点稻荷森站不远了。"

    stop sound fadeout 1

    play music "t07.mp3" fadein 1.0

    "我抱着胳膊看着天花板，\n放松已经僵硬的身体。"

    "不久，列车静静地滑入站台。\n然而并没有一直以来的广播，取而代之的是一如既往的寂静。"

    scene bg 0655 with Dissolve(.5)

    "乘客们下了车，\n稀稀拉拉地走向了检票口。"

    "柴油车低沉的运作声渐渐消失，最终只剩下滴答滴答的雨声笼罩着这座木质火车站。"

    "我站在车站内，\n一边挥去身上的茫然与慵懒，\n一边随意地环顾四周。"

    "浓密的雨雾模糊了枯尾沼与车站的界限。"

    "即使是夏季，这里也难得见到晴天。"

    "我又望向木质楼梯连接的站台。"
    
    "那边的站台早已废弃不用了。"
    
    "在我还是小孩子时，\n那些货运列车就搁置在那里不再运行了。"
    
    "车站倒是得到很好的维护，\n现如今也依然整洁。"
    
    "只有铁路锈迹斑驳，\n延伸着隐没在山谷的矿山遗址里。"

    show j 1902
    with Dissolve(1)

    j "哥哥。"
    
    "我的思绪从周围的风景中被拉了回来。"
    
    i "————树里。"
    
    j "嗯？"
    
    j "怎么了，哥哥？"

    "树里，\n我的妹妹。"

    "少女歪着头站在我旁边，\n我顺着她的视线望去——"

    hide j
    with Dissolve(.5)

    j "……那个站台和铁路，\n其实早都不被人需要了吧。"

    i "…………"

    pause(0.5)

    j "不过总觉得，\n像这样一直等下去的话……"

    j "以前的列车，\n会从对面哐当哐当地驶来也说不定。"

    pause(0.5)

    "从过去驶来的列车啊……"

    "如果真心许下乘坐这个列车的愿望的话，\n它会向我驶来吗？"

    i "你是来接我的吗？"

    show j 1901
    with Dissolve(1)

    j "啊，嗯。\n我就想着，哥哥一定快到了。"

    i "……真是少见。"

    show j 1904
    with Dissolve(.5)

    j "啊，好过分诶！"

    j "哥哥，你没带伞吧？"

    "我老老实实点了头。"

    show j 1901
    with Dissolve(.5)

    j "看吧，果然跟我想的一样。"

    "然而一脸得意的树里手里，\n只拿着一把湿漉漉的女子伞。"

    i "………那，我的伞呢？"

    j "我忘了呢，嘿嘿。"

    "依然一脸得意的树里这么说。"

    i "……"

    j "啊，不过，润酱应该带了。大概。"

    i "……谁？"

    j "欸？润酱就是润酱啊。\n哥哥，你不记得润酱了？"

    "是树里学校的朋友吗……"

    hide j
    with Dissolve(.5)

    "不过，她从没带过任何人到家里玩过。"

    "我被树里拽着手臂穿过检票口，\n结果看到了一个熟悉的身影。"

    show r 4603
    with Dissolve(1)

    r "那个……你、你好……"

    i "……古泽……？"

    "的确是古泽。"

    "紧张到身体僵硬的少女低下了头。"

    i "你怎么在这儿？"

    r "那个，那是因为……"

    "这个舌头打结，转眼间脸就变红了的少女，\n毫无疑问，是我打工场所的后辈──古泽。"

    j "呐，有事回家再说吧。"

    j "润酱有多带伞吗？"

    r "啊？没有呢，毕竟突然就出门了。"

    "树里突然冷不防地盯向不知所措的古泽，\n目光落在她手里握着的伞上。"
    
    show r 4705
    show j 1901
    with Dissolve(.5)

    j "你那把更大。\n呐，和我换换呗。"

    r "这个？\n啊，呃……"

    "树里从古泽手中接过雨伞，直接递给了我。"

    j "就这样，你跟哥哥打一把伞吧。"

    i "你又这样只顾自己的舒服了。"

    j "难得有可爱的妹妹来接哥哥，\n看这个份上我这样做也行吧。"

    i "真正可爱的妹妹可不会这么自夸吧。"

    show j 1904
    with Dissolve(.5)

    i "真是的……\n不好意思啊，古泽。"

    show r 4702
    with Dissolve(.5)

    r "没、没什么，我完全不在意的。"

    show j 1901
    with Dissolve(.5)

    j "还是早点回去吧。\n"
    
    extend "啊，或者便利店逛逛？"

    i "到底是想怎样啊。"

    hide r
    hide j
    with Dissolve(.5)

    "当我撑起伞时，\n树里趁机钻入我的臂膀下，\n紧紧依在我的身上。"
    
    "她纤细的锁骨从松开的领口露出。"

    "这是自春天过后第一次看到树里，\n但没看出她有什么变化。"

    "她一如既往充满活力，\n注视我的目光也始终笔直。"

    pause(1)
    scene bg 0999 with fade











    pause(1)
    play music "t01.mp3" fadein 1.0
    scene bg 0702 with fade
    show z1046
    show z9001
    show z9002
    show z9003
    show z1024

    "从我懂事起，\n芳野阿姨就和我们有紧密的生活往来。"

    "直到上中学之前，\n我跟树里都不是用“芳野阿姨”，\n而是用“芳野妈妈”来称呼她。"

    "我并不对芳野阿姨跟父亲再婚这事儿感到意外，\n毕竟这是很理所当然的。"

    "应该只是为了避开不好的传言。"

    "所以才会在我和树里的生母朱音\n离世一年半后的现在才决定。"

    "刚才还跟我们坐一起的茂晴伯父也是早就在劝他们再婚。"

    "而且，我和树里也没理由反对。"

    "唯一让我感到意外的，\n是芳野阿姨的这个女儿。"

    "不，老实说，\n我之前听芳野阿姨说过她有个不需操心的女儿。"

    "然而芳野阿姨也没说过更多的了。"

    "因为之前没见过芳野阿姨带她女儿来，\n所以至今为止都没将这一信息作为事实理解。"

    "所以今天的主题，与其说是让再婚的两人得到家人的理解，"

    "倒不如说是把古泽——\n不对，\n是把润作为家里新的一员来加以介绍吧。"

    "被芳野阿姨催促的润端正了坐姿。"

    show r 4602
    with Dissolve(.5)

    r "我是润，请多多关照！"

    "润虽然有些紧张，\n但还是认真地做了自我介绍。"

    "就像她打工的第一天那样。"

    "与仍有些稚气的外表相反，\n润是个很可靠的女孩子。"

    "芳野阿姨露出微笑，\n对树里说道："

    hide r
    with Dissolve(.5)
    show y 3254
    with Dissolve(.5)

    y "树里还记得润吧？"

    show j 1901
    with Dissolve(.5)

    j "嗯，当然啦！"

    "树里爽朗地回答道。"

    j "以前在旧建筑物的中庭里一起玩过吧。"

    i "……那是哪里？"

    f "是我之前带你去青山公寓那会儿。"

    f "那时候五树刚上小学。"

    y "对，虽然那里现在已经被拆除了。"

    y "是啊，毕竟十多年前的事了，不记得也正常。"

    hide j
    hide y
    with Dissolve(.5)

    y "扑哧。"

    "一听到芳野阿姨抬高了嗓音，\n润就吃惊地僵住了脸。"

    show y 3101
    with Dissolve(.5)

    y "润那孩子还因为害怕野猫哭了起来……"

    y "是五树哥哥帮了你吧？"

    show r 4706
    with Dissolve(.5)

    r "妈！"

    i "还有这种事儿吗？"

    show r 4702
    with Dissolve(.5)    

    r "妈……别提这些陈芝麻烂谷子的事啦……"

    show y 3107
    with Dissolve(.5)    

    y "唉，好吧好吧。"

    j "……还发生过这些事啊。"

    hide r
    hide y
    with Dissolve(0.5)

    "爸爸吸了一口气后，向润鞠了个躬。"

    f "谢谢你，润。"

    f "真心谢谢你能同意我和你母亲的再婚。"

    f "也同时谢谢你能选择来到稻荷森。"

    show r 4605
    with Dissolve(.5)    

    r "（点头）"

    "润拘谨地点了点头。"

    f "我和芳野成为夫妻，\n同时意味着润成了五树的妹妹和树里的姐姐。"

    f "不过你和五树年龄相近，\n也不可能突然就像兄妹一样相处吧。"

    f "所以你能与他暂且作为朋友吗？"

    r "啊，好的。"

    show r 4602
    with Dissolve(.5)    

    r "我这边才是，请大家多多关照。"

    f "五树跟树里也来。"

    "在正点头的我的身旁，树里夸张地担保道："

    hide r
    show j 1901
    with Dissolve(.5) 

    j "爸爸别担心，我们会成为好姐妹的。"

    j "暑假结束后，一起上学吧？"

    show r 4703
    with Dissolve(.5) 

    r "应、应该可以……\n妈妈？"

    y "你和树里在同一所学校哦，\n以后就是乘列车上下学了呢。"

    j "乘列车上学真是超悠闲的～"

    i "如果要考虑升学的话，\n一般都是在上学路上这段时间学习吧。"

    show j 1903
    with Dissolve(.5) 

    j "哥哥，学习这种事是该在学校里进行的哦。"

    i "……啊，是么？"

    "值得一提的是，树里虽然平时不学习，但成绩却很好。"

    "真是令人羡慕啊。"

    show j 1901
    with Dissolve(.5) 

    j "不过真令人期待啊，感觉会很开心呢。"

    "树里来回望着两位新的家人。"

    show j 1903
    with Dissolve(.5) 

    j "……妈妈……啊。"

    show j 1901
    with Dissolve(.5) 

    j "我也可以叫芳野妈妈吧？"

    "突然，胸口一阵剧痛。"

    y "当然啦，我也很乐意呢。"

    show r 4708
    with Dissolve(.5) 

    r "…………"

    hide j
    hide r
    with Dissolve(0.5)
    
    "芳野阿姨那温和的声音貌似掺杂了些许的痛苦。"

    show y 3351
    with Dissolve(0.5)

    y "五树能呆到放河灯那时候吗？"

    i "……好像是周末吧。"

    show j 1901
    with Dissolve(0.5)

    j "是哦，哥哥可不要又太早回去了哟。"

    pause(2)
    stop music fadeout 1
    scene bg 0999 with fade










    scene bg 0654
    with fade
    pause(4)
    
    scene bg 0999
    with fade

    "铅色的乌云积压在天空。"

    play sound "0064.mp3"

    "——雨，偷袭了晚秋。"

    play sound "0605.mp3" fadeout 1

    "因为前一家咖啡厅没位置，于是我又找了另一家。"

    "明明是在休息日，但这家却也是鲜有空位。"

    "“可以在吸烟区拼桌吗？”"

    "听服务员这么说，我虽然很烦恼，\n但再看了一下外面的天气后，也只好回答：“好的。”"

    "我对面的座位上，是一位正在查看文件的白衣男性。"

    "桌上摆着烟灰缸，上面放着他刚开始抽的香烟。"

    "又过了一会儿，香烟仍这样摆在上面。"

    q "啊，我不介意的。"

    "男子默默点头，\n随后又将注意力放到文件上，并没去伸手拿烟。"

    scene bg 0999
    with fade
    play sound "0604.mp3" fadeout 1

    "拿铁已经被喝去了一半。"

    "我轻轻靠着飘窗，将视线转向外面。"

    "车灯像玻璃球一样，在湿淋淋的路面上跃动着。"

    "我又一次喝了小口咖啡，\n这时，\n我注意到了与我拼桌的男性的视线。"

    play music "t03.mp3" fadein 1

    "当我被吸引而转过头后，\n他行了一礼，\n说出了出乎我意料的话语。"

    g "您是R大的人……吧？"

    q "啊咧？"

    q "啊，对，我是。"

    q "那个，我们在哪儿见过吗？"

    g "果然啊，认出您时我也吃了一惊。"

    g "我们之前没说过话，我也不过是在R大附近看到过您而已。"

    g "和您搭话，只是，在想，我们是不是有同样的熟人————"

    "男性轻轻地清了清嗓子。"

    g "您知道簸川吗？就是观光学部的那个。"

    "这位瘦高男性的声音意外地深沉，\n即使是在人声嘈杂的店里，\n他的声音也能被清楚地听到。"

    "我笨拙地点了点头。"

    "这位名叫山鹿青磁的男性是簸川五树的旧友。"

    "据他所说，他平时在东京都内的医院工作，\n但这些天找母校有事，所以偶尔也会来这一带。"

    "看起来是个很诚实的人，我老实地倾听着。"

    g "不好意思，问您这么没礼貌的事。"

    q "不不不，没什么的。山鹿君……您是医生吗？"

    q "或者说实习医生之类？"

    g "诶？啊啊，是因为这个吗？"

    "青磁君指着自己的白衣笑了笑。"

    g "不，不是的，我不是医生。"

    g "我是专门做协助医生的工作。"

    g "穿这身是学生时代的习惯罢了，\n在校园外也偶尔会在无意中把它穿到上衣里边。"

    q "那您是茶水桥对面的那个学校的？"

    g "对，我是I大附属学校的毕业生。"

    g "五树他——不，簸川他现在过得怎么样？"

    g "不对，我不应该对初次对话的人这样问啊。"

    g "实在不好意思，\n因为那个家伙老是不聊他自己，\n所以我就不自觉地这样问了。"

    q "…………"
    
    "我该怎么办才好呢？他一定是误会了。"

    "也许是因为工作的性质，即便是面对初次对话的对象，\n青磁君的搭话也是很自然，不显得亲密也不拘礼。"

    "明明我不是很喜欢那些穿白大褂的人，\n但不可思议地，我对他并没有这种厌恶感。"

    "他……"
    
    "正当我犹豫着要不要照实说出我跟簸川五树之间那有所不和的关系，"

    "青磁君又开了口。"

    g "以前在学校附近与簸川碰头的时候，刚好看到你经过……"

    g "听五树说你们是同一个社团的。"

    g "虽然除此之外，五树也没说别的什么——"

    g "只是，他好像很在意你，所以也给我留下了印象。"

    g "于是就不由自主地问了……不好意思，这太突然了吧。"

    "“没有”，我摇着头，尽可能让我的言语不染上我心中的刻薄。"

    q "那个，我已经退出社团了。"

    "青磁君的表情发生了小小的变化。"

    q "因为个人的一点小事情……"

    g "这样啊。"

    q "在社时也没用心参与社团活动，和簸川君没说过多少话。"

    g "……原来如此。"

    g "先前的话给您造成困扰了，实在不好意思。"

    q "没什么，不用介意的。"

    "看着耷拉着肩的青磁君，我感到有些莫名的内疚。"

    q "不过，嗯，如果可以，我说说我所知道的事吧？"

    g "嗯，也好。"

    q "簸川君有很多朋友，在社团里很受欢迎。"

    q "他本人不是那种开朗的类型，\n但却能让周围人自然地变得开朗。"

    g "…………"

    "这时，仅仅一瞬间——"

    "我感觉他的眼神仿佛看透了我的内心。"

    g "是这样啊……谢谢你。"

    "青磁先生静静地点着头。"

    g "不知道为什么，\n会不由自主地觉得你们之间是那种亲密的关系——"

    q "……没关系，请不要介意。"

    "之后就是一些无关紧要的对话。"

    "离别之际，虽然认为彼此不会见面了，但我还是选择了自报姓名。"

    q "我是伊势，伊势雾子。"

    g "青磁。"
   
    "“即便有跟簸川对话的机会，也请你不要把我们的对话告诉他。”\n青磁先生说了这样的话，而后向我鞠躬，离开了。"

    scene bg 0999
    with fade

    "……呼……"

    "看来雨一时半会儿还不会停。"

    "在我还犹豫着要不要用他留下的伞时，\n外面的天色渐渐变得更暗了。"

    "我看向残留在烟灰缸里的烟灰。"

    "…………真老成啊。"

    "明明和自己年龄没差多少。"

    "他和他，\n在这些点上很相似。"

    "一年过后，我才明白，\n"
    
    extend "那不叫做老成，\n"
    
    extend "那是孤独与寂寞。"

    pause(2)

    stop sound fadeout 1
    stop music fadeout 1















    
    scene bg 0755
    with fade

    scene bg 0507
    with Fade(4.0, 1.0, 0.5)
    
    "归省第二天。"

    "在我被家里要求向润介绍稻荷森后，\n我把一脸苦涩的润带到了外面。"

    show z9015
    with Dissolve(0.5)

    j "那我要待在家里吗？"

    "被拒绝同行后，树里很干脆地放弃了。"

    j "嗯，那我就在家帮忙干家务活吧！"

    j "哥哥，润酱，路上小心～"






    scene bg 0508
    with Fade(1.0, 1.0, 1.0)
    show z9016
    show z9017
    play music "t09.mp3" fadein 1
    play remusic "0603.mp3" fadein 1

    "报废的铁路线在青草堆中延续。"

    "“我还是第一次见要这样换道的线路。”\n润那总是小心谨慎的言语这时多了份欣喜。"

    i "对了，古泽——"

    i "啊，已经不能这样叫了吧。"

    i "那……可以叫你‘润’吗？"

    "在轨道上摇摇晃晃走着的润听后猛地转过头看向我。"

    r "诶？"

    r "啊，疼————"

    "她失去平衡，把手搭在我肩膀上。"

    show r 4608
    with Dissolve(0.5)

    r "那、那我是叫你哥、哥、哥哥吗？"

    "她声音里掺杂了一丝怨气。"

    i "不行的话……就喊我‘大哥’之类的？"

    r "你真觉得可以？"

    i "哈哈，果然一下子适应不了啊。"

    r "当然啦。"

    i "也是啊。"

    r "…………"

    hide r
    with Dissolve(0.5)

    "烈日的炎热穿透厚厚的云层，灼烧着我们的肌肤。"

    "润似乎还没有习惯这里的气候。"

    "有时她会为了吹风卷起衬衫。"

    show i 2108
    with Dissolve(0.5)

    i "昨天有睡好吗？"

    show r 4703
    with Dissolve(0.5)

    r "还行吧……"

    r "但是周围太安静了，总感觉我的耳朵直响。"

    i "汽车跟飞机都不经过附近呢……"

    i "没事儿，等过几天，‘かじか’发出叫声就会好了。"

    r "‘かじか’是啥？"

    i "一种青蛙。"

    r "呱、呱呱呱呱……？"

    i "它们的叫声是更清脆一些的。\n‘噜噜噜噜’，像口哨一样。"

    r "嘿诶……真是奇怪的青蛙。"

    "我们又说回了昨晚的事。"

    i "最紧张最吃惊的就是你了吧。"

    show r 4705
    with Dissolve(0.5)

    r "前辈你那时也不知道吗？"

    r "我和前辈是，那个，会成为户籍上的兄妹……这件事。"

    i "嗯。直到昨天为止，我都完全不知道。"

    show r 4708
    with Dissolve(0.5)

    i "只是听说要介绍芳野阿姨的孩子。"

    i "没想到会是你。"

    "润垂着肩膀。"

    r "因为……"
    
    r "这不就像漫画情节一样嘛。"

    i "是啊……"

    hide r
    hide i
    with Dissolve(0.5)

    "看着怅然的润，我耸了耸肩。"

    "在蝉鸣的包围中，\n我们两人就这样走在废弃的铁路线上。"

    "本想告诉她这里是上学的必经之路，\n但我脑海里浮现出了自己很在意的其它事。"

    i "你没有生气吗？"

    r "……诶？生什么气？"

    i "……因为树里真的很傲慢啊。"

    i "所以你会不会很生气啊，明明她比你还小。"

    show r 4708
    with Dissolve(0.5)

    r "……你就是因为这个才把她抛到一边带我出来的吗？"

    "润瞪了我一眼后，叹了口气。"

    show r 4705
    with Dissolve(0.5)    

    r "我没什么要发牢骚的。"

    r "毕竟我也是在了解这些后才选择跟着妈妈的。"

    show r 4708
    with Dissolve(0.5)

    r "嘛啊……就是没想到……她会是那种超级偶像系的女生……"

    "‘不过啊，为什么我的周围老是……’，她这样小声诉苦。"

    i "不用客气的。"

    i "如果遇上讨厌的事，要跟我或者老爸说啊。"

    i "不要勉强自己。"

    show r 4704
    with Dissolve(0.5)  

    r "才不会勉强呢！"

    i "那我就放心了。"

    "仰起头，面朝天空的润露出了开朗的笑容。"

    stop remusic fadeout 1.0
    scene bg 0510
    with fade

    "穿过车站后，我们爬上长长的坡道。"

    "不久，\n坐落着一排排涂上柿漆的木制宅邸的旧市街呈现在了我们眼前。"

    "脖子被汗水浸湿。"

    "润也流着汗，好奇地来回望着街道。"

    "稻荷森。"

    "——四季在呼吸的间隙中时刻变化着，却没有任何改变的地方。"

    scene bg 0523
    show z9031
    show z9032
    with fade    

    r "话说。"

    r "我在家里被拜托去买东西了，是要去干菜店吧？"

    r "是在那条街吗？走吧。"

    i "啊，等等。"

    i "你还是一如既往地行动力强啊。"

    r "反正我就是急性子。"

    i "别那么急，给家里买东西又不是上班。"

    i "再说我还要给润介绍稻荷森呢，等会儿再去买东西吧。"

    r "……嗯，那就这样吧。"

    "她不情愿地转向右边，回到了散步路线。"

    i "这个城镇很有趣吧。"

    i "虽然一堆台阶跟坡道，走路会很辛苦。"

    r "啊哈……"

    r "感觉如果每天都这样的话，就不会觉得有趣了……"

    "褪色的光景里，到处都沾染着我少年时代的痕迹。"

    "我们走着路，由我讲述当地各种各样的事。"

    "润乖乖地侧耳倾听着，但不久后便冒出一句。"

    r "…………太……"

    r "太狡猾了。"

    show r 4604
    with Dissolve(0.5)

    "她咬着嘴唇，低着头。"

    i "……诶？"

    r "太狡猾了。"

    r "前辈不要这么轻易地——"

    r "觉得我在这里是理所当然的。"

    hide r
    with Dissolve(0.5)

    "然后，润俯视着枯尾沼，面朝悬崖。"

    scene bg 0521
    show z9027
    show z9028
    with Dissolve(1.0)

    r "太狡猾了……"

    "淡色的头发轻抚着她被染红的侧脸。"

    i "…………"

    "润会烦躁是理所当然的。"

    "当时听她说她要辞去喜欢的兼职工作，决定搬家……"

    "在我目送她离去的那一晚，润哭了。"

    "我第一次见到像那样失去冷静的她。"

    "我试图让她平静下来，但她拨开我的手臂，大声地责难。"

    "结果，我们并没有说什么话，就这样分别了。"

    "那是发生在大约一个月前的事。"

    "没想到后面会有这么不凑巧的偶然等着我们。"

    show r 4607
    with Dissolve(0.5)

    r "呜……对不……起…………"

    "润垂下头反省着。"

    r "因为那时候，我的脑海一片混乱……"

    r "然后……对前辈说了过分的话……"

    i "我并没有介意哦。"

    show r 4601
    with Dissolve(0.5)

    r "我、我知道前辈你是不会介意的。"

    "润露出自嘲的笑容。"

    r "我知道前辈是个善良的人。"

    "润伸了伸腰，扭过脸。"

    hide r
    with Dissolve(0.5)    

    "只见她挺起胸膛，用张开的手臂抓住护栏。"

    r "……是我沉浸在自己的世界里了。"

    r "等等，这就像悲剧的女主角啊……什么的。"

    r "也可能是美好的一幕…………哈哈……"

    i "…………"

    show r 4801
    with Dissolve(0.5)

    r "这次也不是因为有了新的家人、兄妹什么的……"

    r "只不过是找到了新的逃避的地方而已。"

    r "能在这世上养活妈妈和我那样的人，也就只有……"

    r "只要有房子住就已经很满足了。"

    "听到润与不同以往的自卑语气，我平静地添上一句。"

    show i 2557
    with Dissolve(0.5)

    i "……你妈应该不会想得那么卑屈吧。"

    show r 4803
    with Dissolve(0.5)    

    "润一脸苦涩地，边看着城镇边听着。"

    i "如果没有芳野阿姨的支持的话，\n我们家都不知道会变成什么样。"

    i "曾经体弱多病的树里能变得像常人一样健康。"

    i "我能够离开这个城镇升学。"

    i "都是因为芳野阿姨在身边。"

    i "而且最重要的是，是她支撑了我的父亲。"

    "视线落在遥远的枯尾沼上。"

    "从这望去，发现我们的家被山脊遮住了。"

    i "虽然可能因为眼睛看不见会被别人认为她很柔弱，\n但其实她一直都是个坚强的人啊。"

    i "这点你应该比我更清楚。"

    i "不过她常不在家，你是对这点感到愤恨吗？"

    i "是觉得她放着你不管了吗？"

    show r 4802
    with Dissolve(0.5)

    r "…………"

    "润默默地摇了摇头。"

    "我把身子靠着旁边的栏杆。"

    hide r
    hide i
    with Dissolve(0.5)

    i "古泽。"

    "虽然一不小心用了这个称呼，但我还是继续说着。"

    r "…………"

    r "虽然只要你觉得呆在这里挺好的话就行了。"

    r "但是你如果不喜欢这个城镇的话，去东京怎么样？"

    show r 4608
    with Dissolve(0.5)   

    r "嗯……啊？"

    i "如果不喜欢这里的话，要来东京吗？"

    show r 4606
    with Dissolve(0.5)   
 
    r "诶————！！"

    "润瞪大了眼睛。"

    r "前、前辈，你在说什么？"

    i "我很认真的啊。"

    i "反正都是需要一个人来帮忙自立的，那我也行啊。"

    i "升学就，嘛，今年是不行了吧，那就暂时当个失学学生吧。"

    i "直到你能独立生活那天为止，可以住我的公寓。"

    r "那、那前辈呢！？"

    i "当然也住在我的公寓啊。"

    show r 4602
    with Dissolve(0.5)   
 
    r "那、那，那不就是同居了吗？"

    i "我们是兄妹啊。"

    r "不要用家人关系来方便自己啦！"

    r "不对，等、等等——"

    hide r
    with Dissolve(0.5)

    "润猛地伸出双手拒绝着。"

    "不，不行。"

    show r 4605
    with Dissolve(0.5)

    r "……前辈有喜欢的人吧！？"

    "看到不禁张皇失措的我，润好像确信了这点。"

    show r 4607
    with Dissolve(0.5)

    r "……我在店里听前辈的朋友们说的。"

    r "我不知道对方是谁，也没有见过。"

    r "但，如果真这样的话……我不想变成前辈的负担。"

    show r 4605
    with Dissolve(0.5)

    r "前辈？"

    i "欸…………"

    "我不由自主地叹了口气。"

    i "她已经拒绝跟我交往了。"

    i "而且还说得很干脆。"

    show r 4603
    with Dissolve(0.5)

    r "……诶？"

    "润摆出一副难以言喻的微妙的表情，僵住了。"

    r "……………………真……"

    r "真的吗？"

    r "不骗你。"

    show r 4606
    with Dissolve(0.5)

    r "…………好、好过分……"

    r "她真的是人类吗？竟然拒绝了前辈……"

    "面对喋喋不休的润，我为了掩饰羞涩而说道。"

    hide r
    show i 2108
    with Dissolve(0.5)

    i "别在意我啦。"

    i "搬去东京那事，也可以不用立刻决定。"

    i "我也就只是给你一个可行的方案而已。"

    i "你先考虑考虑。"

    hide i
    show r 4802
    with Dissolve(0.5)  

    r "…………嗯。"

    "她现在也只能这样回应了。"

    play sound "0614.mp3"
    "歇了一口气后，突然听到悬崖喷水口的声音。"

    scene bg 0523
    show z9033
    with Dissolve(1.0) 

    show i 2401
    with Dissolve(0.5) 

    i "你渴了吧？"

    stop music fadeout 1.0
    i "买东西时顺道去一下自动贩卖机吧。"

    r "嗯。"

    i "啊，你可以不用跟来，在树荫下休息就好。"

    r "那我要喝可乐。"

    i "没有可乐，只有海带茶，或者是柠檬水…"

    r "诶！？竟然没有可乐？"

    i "开玩笑的。"

    i "OK，等我一会儿。"

    hide i
    with Dissolve(0.5)

    r "……………………呼……"

    r "……和前辈……"

    r "…………"

    stop sound fadeout 1.0

    r "……一起？"

    r "…………"

    play sound "0606.mp3" fadeout 1.0
    r "……………………？"

    play sound "0608.mp3" fadeout 1.0

    r "…………"

    play music "t02.mp3" fadeout 1.0
    r "…………树里……？"

    play sound "0607.mp3" fadeout 1.0
    "你是……跟过来了吗？"

    show z9035
    with Dissolve(0.5)

    r "…………树……"

    hide z9035
    with Dissolve(0.5)

    r "…………是谁……"











    hide z9033
    with Dissolve(1.0)
    pause 1.0
    show z9034
    with Dissolve(1)
    pause 1.0
    hide z9034
    with Dissolve(1)
    scene bg 0524
    with Dissolve(1.0)
    pause 2.0
    play sound "0610.mp3" fadeout 1.0
    scene bg 0527
    with Dissolve(1.0)
    show z9041
    with Dissolve(1.0)
    pause 1.5
    hide z9041
    show z9040
    with Dissolve(1.0)
    pause 1.5
    hide z9040
    show z9042
    with Dissolve(1.0)
    pause 1.5
    hide z9042
    with Dissolve(1.0)
    pause 1
    scene bg 0515
    with Dissolve(1.0)
    pause 2.0
    scene bg 0522
    with Dissolve(1.0)
    show z9030
    with Dissolve(1.0)
    pause 1
    show z9029
    with Dissolve(1)
    pause 1
    hide z9030
    with Dissolve(1)
    pause 1
    hide z9029
    with Dissolve(1)
    pause 1
    scene bg 0511
    with Dissolve(1.0)
    pause 2
    scene bg 0525
    with Dissolve(1.0)
    show z9036
    with Dissolve(1.0)
    pause 1
    hide z9036
    with Dissolve(1.0)
    stop sound fadeout 1
    scene bg 0526
    with Dissolve(1.0)
    pause 1
























    show r 4903
    with Dissolve(1.0)

    r "是树里吧……"

    r "别搞恶作剧了。"

    hide r
    with Dissolve(0.5)

    r "…………树里……"

    r "……………………"

    r "……前辈……"

    show z9039
    with Dissolve(0.5)

    r "…………前辈…………！"

    stop music fadeout 1.0
    play sound "0612.mp3" fadeout 1.0

    r "…………！？"

    show n 5201
    with Dissolve(0.5)

    n "怎么了？你在找什么东西吗？"

    hide z9039
    show z9037
    show z9038
    hide n
    show r 4602 at realleft
    with Dissolve(1.0)

    r "啊，不是……"

    n "嗯……？…………哦～"

    hide r
    hide z9037
    hide z9038
    show n 5301
    with Dissolve(0.5)

    n "稍等，我想起了什么，让我再想想。"

    r "诶？"

    show n 5307
    with Dissolve(0.5)

    n "那~~个"

    play music "t10.mp3" fadein 1.0

    show n 5301
    with Dissolve(0.5)

    n "对了，难道你是芳野的女儿？润酱小姐？"

    show z9037
    show z9038

    hide n
    show r 4708
    with Dissolve(0.5)   

    r "酱小姐？"

    show r 4705
    with Dissolve(0.5)   

    r "啊，对，我是。"

    show n 5101 at littleright
    with Dissolve(0.5)

    n "果然！"

    n "我是夏生，簸川夏生。"

    r "簸川……"

    show n 5104
    with Dissolve(0.5)    

    n "对的，我在办事处工作，我已经听说过你的事了。"

    n "簸川健昭是我的叔父。"

    show r 4701
    with Dissolve(0.5)      

    r "嗯……那我就是您的堂妹吧。"

    n "就是这样，请多关照哦。"

    show n 5101
    with Dissolve(0.5)

    n "……话说回来，你迷路了？"

    show r 4702
    with Dissolve(0.5)   

    r "说来惭愧……"

    n "哎呀哎呀～"

    stop music fadeout 1.0
    pause 1
    play sound "0013.mp3" fadeout 1
    scene bg 0543
    with fade
    pause 5






    scene bg 0702 with fade
    play music "t05.mp3" fadein 1

    "芳野阿姨、润、树里，\n三位女性同时站在厨房的情景相当引人注目。"

    "就连平时对料理不感兴趣的树里也进了厨房。"

    "她凭自己模模糊糊的记忆挑战自己在电视上看到的食谱，\n结果酿成了大惨案。"

    "润边帮炒猪肝的芳野阿姨打下手，\n边准备着作为副菜的牛萝丝和凉拌羊栖菜。"

    "她麻利的干活样子让人看得心情舒畅。"

    "她还及时制止了总是失手的树里——\n每次试味都会悄悄靠近垃圾桶。"

    "总算是将厨房恢复原样了。"

    "从客厅看，感觉真是忙来忙去。"

    scene bg 0707 with fade

    "热闹的晚餐结束后，过了一段时间——"

    "看到浴室已经有人正用着了，我走到通风处又折回。"

    "听到了头上楼梯平台那传来的声音。"
    
    show z9009 with dissolve

    y "健昭他去了本家。"

    y "因为要商量关于祭典的事。"

    y "……是五树吧？"

    i "嗯。"

    "芳野阿姨边扶着扶手，边稳稳地下着楼梯。"

    hide z9009
    show y 3104
    with Dissolve(0.5)

    y "果然会在后天回去吗？"

    i "……对不起。"

    show y 3101 with Dissolve(0.5)

    y "没关系啦，毕竟你很忙吧。"

    y "然后，如果可以的话想跟你说件事。"

    i "那就到客厅说吧，我去沏大麦茶。"

    "芳野阿姨摇了摇头。"

    show y 3109 with Dissolve(0.5)

    y "在这儿说就行了。"

    y "因为风吹得很舒服。"

    i "是嘛。"

    "在坐着楼梯的芳野阿姨旁边，我也怯生生地坐下了。"

    hide y
    show z9010
    show z9011
    with Dissolve(0.5)

    y "我想现在是跟你说这些话的好机会。"

    y "因为感觉五树自己一定是不会来问我的。"

    "氛围稍微有些不同的芳野阿姨将自己毫无防备的一面展露给我看。"

    y "在这之前你就已经和润相互认识了吧。"

    i "嗯。虽然是偶然在打工场所结识的。"

    y "……是嘛。"

    y "她为什么不事先告诉我五树的事呢。"

    y "润生气了……"

    y "我有在反省。"

    "她低下头。"

    i "哈哈。"

    y "呼呼。不过，不知道为什么。"

    y "感觉润和五树肯定没问题的。"

    "芳野阿姨突然抬头看向远方。"

    y "润的父亲是一位叫桐生秀人的著名建筑师哦。"

    i "我知道这个名字，还跟他见过一次面。"

    y "是呢，毕竟也是健昭的工作地点。"

    y "健昭和朱音来东京的时候，照顾他们各种事的也是他。"

    y "这间屋子也是他造的……"

    "芳野阿姨将白皙的手指搭在栏杆上。"

    i "那……您跟桐生先生离婚了……？"

    y "不是哦，桐生先生另有家室。"

    y "我之前是他的情人。"

    y "也就是未婚妈妈。这样说吧，健昭是我第一个结婚的对象。"

    y "对不起啊，跟你说这些话。"

    i "没……也就是有点吃惊而已，没关系的。"

    pause(1)
    show y 3108 at realleft
    with Dissolve(1)

    y "……谢谢。"

    y "变得成熟了呢，五树。"

    y "…………"
    
    "怀念着过去的芳野阿姨的侧脸，比记忆中稍显得有些憔悴。"

    y "……自从健昭开始在桐生先生的工作场所出入，\n我有时也会跟他说说话。"

    y "然后，也是在那时候知道了有孕在身的朱音……"

    y "这样无用的我，突然开始想着自己能不能做些什么。"

    y "在那之前一直不知为何而活的我，稍微有些改变了。"

    show y 3109 at realleft

    y "在那之后，我和健昭保持了很久的好友关系。"

    y "…………"

    hide y with Dissolve(0.5)
    
    y "桐生先生肯定到现在都不认为自己把我舍弃了。"

    y "他才华横溢，所做之事都很宏大。"

    y "他是个单纯的，总是想着别人感到天马行空之事的人。"

    y "而健昭不一样。"

    y "健昭每次想到的，都是关于家人的事情。"

    i "……是吗。"

    i "他总是忙着自己的摄影工作，几乎不在家。"

    show y 3108 at realleft
    with Dissolve(1)    

    y "……你是在埋怨健昭吗？五树。"

    "没想到她竟然会提出跟润一样的问题。"

    "这时我才意识到，自己是将不安发泄在润上了。"

    i "…………"

    i "……不……我不怨他。"

    i "只是不太清楚父亲的事。"

    y "……说不定父亲就是那样的存在吧。"

    y "随着年龄增长，会不会越来越了解父亲呢？"

    i "…………"
    
    i "芳野阿姨不会感觉我们给你添麻烦了吗？"

    show y 3109 at realleft
    with Dissolve(0.5)    

    y "辛苦的话当然是很辛苦。"

    show y 3101 at realleft
    with Dissolve(0.5)    

    y "不过在帮助健昭的同时关注着你们的成长，\n是我活下去的意义啊。"

    y "自从五树和树里出生之后，我一直都看在眼里。"

    y "当然，润也是。"

    y "真的是很早啊……简直就像昨天才来这个家一样。"

    y "……再次跟你说一声，润就请你多多关照了。"

    y "……明明我马上又要回东京了？"

    y "嗯。"
    
    y "即使分离各地，我们也依旧是家人。"

    i "……"

    hide y
    with Dissolve(1)    

    "突然，从走廊那传来了嘈杂声。"

    show z9012
    with Dissolve(0.75)

    show z9013
    with Dissolve(0.75)  

    "刚洗完澡的润和树里出现在通风处。"

    "只见润红着脸，止不住地咳嗽。"

    y "怎么了？"

    r "咳……我都以为差点要被杀掉了！"

    j "抱歉，润酱。"

    i "……你做了什么？树里。"

    j "潜水游戏。"

    j "日本新记录。"

    i "……？"
    
    r "哈啊……哈啊……出……汗……"

    "看到我后，穿着睡衣的润迟迟地缩着身子。"

    i "你很害羞吗？润酱。"

    "树里哧哧地笑了。"
    
    hide z9010
    show z9014
    with Dissolve(0.5)

    "芳野阿姨立刻站了起来。"

    play music "t07.mp3" fadein 1

    "她摆出了与和谐空气不相称的僵硬表情。"

    y "……润，不要在浴室嬉闹。"

    y "会意外受伤的。"

    r "妈妈你说什么呢！是树里她先……"

    hide z9014
    show y 3207 at littleleft
    with Dissolve(0.5)

    y "听话，润。"

    "芳野阿姨发出低沉的音调。"

    hide y
    show z9014
    with Dissolve(0.5)

    r "…………知道了……"

    y "……树里也是。"

    j "知道了。"

    j "芳野妈妈。"

    show i 2504
    with dissolve
    pause(1)































    stop music fadeout 1
    scene bg 0711 with fade
    play sound "0611.mp3"
    scene bg 0999 with dissolve

    "人们快步路过，将近废弃的车站。"

    "自己一身湿透，茫然地靠着墙壁；有人对我露出了与旁人不同的奇怪眼神。"

    g "……伊势女士？"
        
    g "是伊势雾子小姐吧？"

    "穿着大衣的高个子男性点头致意。"

    g "我是之前跟你见过面的山鹿青磁。"

    g "你怎么了，这么狼狈……"

    "我摘下满是水珠的眼镜，看向青磁先生模糊的脸。"

    q "晚上好。"

    q "山鹿先生没有归省啊？"

    g "我是因为工作在身……不，比起这事——"

    "他肯定是被我这样子给惊到了。"

    q "没什么。"

    q "只是稍微迟了一下没赶上班车而已……"

    "我那完全变得惨白的嘴唇有好好在笑吗？"

    "……总觉得这种时候还在掩饰的自己很卑微可笑。"

    "冰冷的内心深处，聚集着扭曲的热量。"

    "眼泪和呜咽，\n再一次，\n溢了出来。"

    pause(2)
    play sound "0615.mp3" fadeout 1

    "从青磁先生的公寓那借了浴室，冰冷的身体变得暖和起来。"

    "坐在椅子上，闻到了从简易木质地板的房间那传来的香烟气味。"

    play music "t03.mp3" fadein 1

    "这不是那么令人讨厌的气味。"

    "意识恢复了一点后，又突然开始强烈地颤抖。"

    "想必我是感冒了。"

    g "给。"

    "他递给我冒着热气的水杯。"

    g "先喝一点吧，过会儿给你药。"

    q "嗯……"

    "我紧抱着开襟羊毛衫，像特别老实的猫一样听话。"

    "即食的洋葱汤温暖着胃。"

    "过了一会儿，青磁先生的目光从桌上的笔记本电脑转向我。"

    g "冷吗？头疼不疼？"

    g "……应该是发烧了，请躺在床上休息。"

    "他熟练地支撑着我的胳膊，带我到了隔壁的卧室。"

    "是有护理腿部残疾的人的经验吧。"

    "等我缓过来后，突然感觉很害羞。"

    g "明天带你去医院检查后，我会再把你送到家。"

    g "今晚就睡我的床吧。"

    q "实在不好意思。"

    g "让你穿着男性的睡衣睡在这么乱的房间，\n感觉反而是我该说抱歉呢。"

    q "那里……这比我的房间还干净呢。"

    "我低着昏沉的头，表达感谢。"

    "心里满是感激与愧疚。"

    q "那个……山鹿先生今晚要怎么办呢？"

    g "我有登山用的睡袋，房间暖和就行了。"

    q "真是给您添麻烦了啊。"

    g "没有没有。"

    q "那个……内衣之类的，你为我在便利店买了啊？"

    g "哈哈，虽然有点紧张。"

    "拿到医院的处方药后，我躺在床上。"

    "话说，我还没有涂化妆水……\n这种悠然的想法在我脑子里一闪而过。"

    "关灯后，我用万分虚弱的声音问道。"

    q "青磁先生。"

    g "怎么了？"

    "变成黑影的青磁先生看着我。"

    "看来烧得相当厉害。"

    q "你能告诉我簸川五树的事吗？"

    g "……告诉你五树的事？"

    q "什么都好……拜托了。"

    g "…………"
        
    g "……嗯，当然可以。"

    g "不过，你现在得先静养。"

    q "嗯……"
        
    q "青磁先生，谢谢你。"

    "从隔壁传来的打字机声音变得遥远。"

    "不久后，\n连擦去再次慢慢溢出的泪水的力气都没有的我，\n沉入了睡眠中。"

    stop music fadeout 2
    pause(3)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    scene bg 0512 with fade
    pause(2)
    scene bg 0513 with fade
        
    "今天也是夏日。"

    "薄薄的云层下，隐藏着清澈的天空。"

    "我在餐厅『GITOGITO』露了一下脸后，\n就骑着自行车下坡回去了。"

    play sound "0613.mp3"

    "只见一辆擦肩而过的自行车，\n在响着短暂的刹车声后停了下来。"

    i "夏生——"

    play sound "0617.mp3"
    show n 5251 with dissolve

    "回过头去，\n看到正把自行车靠到路边的堂姐抬起头。"

    n "你回来啦。"

    n "看上去没怎么变呢。"

    n "嗯。"

    "在不那么亲密的距离下，我们视线相对。"

    hide n with dissolve

    i "谢谢你把润送回家。"

    show n 5104 at realleft with dissolve

    n "没什么啦，\n对负责乡村振兴的公务员来说，\n这是理所应当的职责。"

    "看到这非常有夏生感觉的带有演技成分的姿态，\n我暗自嘻笑。"

    n "看起来是个好孩子呢。"

    show z9025 at littleright
    show z9026 at zi with dissolve
        
    "看到我点头后，夏生靠着车座继续和我聊着。"

    n "在有着这么重要的考试的夏天，\n来到这么落伍的偏僻地区什么的……"

    n "“那该是多会惹是生非的孩子啊——”，\n事务所的大家都挺提心吊胆的。"

    i "什么嘛那是。"

    hide n with dissolve

    "夏生边绽开笑容，边往我这儿靠近一步。"

    n "不要紧哦。"

    n "夏生姐姐很喜欢她哟。"

    i "那真是太好了。"

    i "拜托你了，这可是我重要的后辈。"

    n "——？后辈？"

    "我跟夏生说了自己跟润奇妙的机缘。"

    "夏生吃惊地听着。"

    "在会话途中，她突然望向手表。"

    n "啊，不好。"

    show i 2108 with dissolve

    i "差不多该回去工作了吧。"

    n "看来的确是这样。"

    n "那就这样，五树。"

    i "嗯，别骑得太快。"

    n "好啦好啦。"

    hide i with dissolve

    "在快走的时候，她又叫住了我。"

    show n 5108 at realleft with dissolve

    n "五……五树……"

    "她含糊地说道。"

    n "…………"

    i "嗯？"

    pause(1)

    n "你能在这儿呆到什么时候？"

    i "明天走。"

    n "诶……明天……？"
        
    n "这么快啊……"

    i "嗯，抱歉。"

    n "没、没事啦。这样啊……"

    n "我、我啊……"

    n "…………"

    "夏生像是很痛苦地一时语塞。"

    show n 5104 at realleft with dissolve

    n "要、要我去给你送行吗？"

    i "……送行？"
        
    i "这种事你不是一次都没做过嘛，无所谓啦。"

    n "也、也是啊，哈哈。"

    i "不用担心啦。别看我这样，好歹也是个大学生。"

    i "今天能见到你真是太好了。"

    show n 5108 at realleft with dissolve

    n "…………"
        
    n "一定没问题的吧，毕竟是五树呢。"

    scene bg 0999 with fade




















    play sound ["0052.mp3", "0055.mp3"] fadein 0.5 fadeout 0.5

    pause(9.5)
    play sound "0603.mp3"
    scene bg 0503 with fade
    show z9022
    show z9023 

    j "不去里边看看吗？"

    r "不用了……"

    r "你是想从外面把我困住吧？"

    j "才不会做那种幼稚的事呢。"

    r "…………呜……"
        
    show j 1952 with dissolve

    j "润酱可真是多疑呢。"

    show r 4608 at littleright with dissolve

    r "我说啊，"

    show r 4604 at littleright with Dissolve(0.5)

    r "突然被抱住潜进浴池里什么的，\n不管是谁都会产生心理阴影的吧。"

    "面对着一脸苦涩的润，树里开心地笑了。"

    show j 1951 with Dissolve(0.5)

    j "抱歉啊，我们家泳池不是很大。"
        
    hide j with dissolve
    hide r with dissolve

    r "嗯……啊？"

    j "“这又是哪儿跟哪儿啊……”，\n润边这样发着牢骚边应和着。"

    j "妈妈就是在那里去世的。"

    r "……诶？…………"

    hide z9023 with dissolve
    play music "t06.mp3" fadein 1

    "把不知所措的润放在一边，\n树里轻快地走向前去，\n和黑暗融为一体。"

    scene bg 0504-dark2
    show z9004-dark2 with fade
    pause(1)

    show z9006-dark2 with dissolve
    pause(1)

    scene bg 0504-dark1
    show z9006-dark1 with dissolve
    pause(1)

    scene bg 0504
    show z9007
    show z9006 with dissolve

    r "…………"

    "润在后面战战兢兢地踏了进去。"

    "铁锈和泥土的味道杂糅在空气中，\n一切物品都散发着岁月的气息。"

    "周围一片寂静。"

    r "这里……还在用吗？"

    pause(1)
    "树里什么也没说，只是站在那里。"
    pause(2)

    j "……姑且是呢，但很少打开。"

    j "其实，每天不保养的话仓库也会受损。"

    r "是嘛。"

    r "果然是因为有古董之类的吗？"

    j "有的吧，像手枪什么的。"

    r "手枪？"

    j "反正已经生锈得不能使用了。"
    
    r "……差不多该走了吧。"

    pause(1)
        
    j "…………"
        
    r "树里？关上吧。"

    j "嗯……"
        
    j "让我自己在这儿待会儿，润酱你先走吧。"

    pause(0.5)

    r "也行……"

    hide z9007 with dissolve
    pause(2)

    j "…………"

    hide z9006 with dissolve

    show z9008 with Dissolve(2)

    show z9005 with Dissolve(2)

    pause(2)
        
    j "………………"
        
    j "不能哭。"

    pause(1)

    j "妈妈————"

    show j 1905 at littleright with dissolve

    j "妈妈已经，\n不在这儿了。"

    j "所以，\n不能哭。"

    j "不要让我\n发火。"

    hide j with dissolve

    j "快点消失……"

    pause(2)
        
    j "快消失…………"

    pause(2)
    hide z9005 with dissolve
    pause(1.5)
    hide z9008 with dissolve
    pause(1.5)
















    scene bg 0601-dark2 
    show z9018-dark2
    with Fade(1,3,1)

    "我突然醒来，距离黎明还有好一段时间。"

    scene bg 0601-dark1 
    show z9018-dark1
    show z9019-dark1
    with Dissolve(2)

    "在黑暗中，隐隐约约浮现出白色的纤细后背。"

    "坐在我身旁的树里凝视着我。"

    "她赤裸着。\n夜晚阴凉的空气中飘斥着她浓密的汗味。"

    "沉浸在模糊的睡眠中，我与少女目光交织。"

    "少女的身体悄悄地流入薄薄的被子。"

    hide z9018-dark1
    hide z9019-dark1
    show z9020-dark1
    with Dissolve(3)

    "她像猫一样蜷缩着，将湿润的后背压在我的身上。"

    "那甜美到腐烂的余香，告知我鱼水交合后的余韵。"

    "撩开她湿漉漉的头发，\n轻轻地将指尖放在女孩的太阳穴上。"

    "就像是，\n我一直以来对病床上的树里做的那样。"

    "滚烫的脸颊回应了我的指尖，默默地疼爱着我。"

    "这就是我们的交流方式。"

    "依靠着令人怀念的温暖与往日的思绪。"

    "我终于,\n回到了理应回到的地方。"

    "回到了，我唯一的归属。"

    pause(2)

    j "你醒了……哥哥…………"

    pause(1)

    "颤抖的低语中流露着久远的痛苦。"

    "昏黄的焰舔舐和燃烧着少女的心。"

    "犹如失调的乐器强行演奏的悲鸣。"

    "悲伤的音色，在这一刻也仍在呐喊——"

    pause(1)

    j "哥哥，你知道吗？"

    j "妈妈和爸爸是兄妹"

    i "…………"
    
    i "我知道"
    
    "我很早就已经知道了。"

    "我很早就知道我们的父母是被簸川家捡回来的孤儿了。"

    "在这个不大的小镇里，\n很少有什么事是能隐藏到底的。"

    "也许是出于使两人出走的愧疚，\n大家后来对他们的态度变得友善。"

    pause(1)

    "他们两人说不定是兄妹……\n不过也没人知道真相。"

    j "…………"
    
    j "如果真这样的话，那我们将会更不一般。"

    j "那是兄妹以上、孪生未满的什么关系……"

    pause(1)

    "她用她的唇，\n通过轻蔑的话语压抑自己，\n但语气中流出了心里暗藏的喜悦。"

    "我道出她的徒劳："

    i "你我的关系是外人啊，所有人都如此。"

    i "不管怎么做，人与人都无法成为一体。"

    j "就算像这样被哥哥抱着……？"

    i "是的……"
    
    j "就算是，一整天和哥哥做爱，一辈子都和哥哥做爱，\n到死为止都在哥哥做爱？"

    i "是的…………"

    i "就算交欢到厌烦，\n即就算彼此的心意如何相近，\n我们都不可能真正地成为一体。"

    i "爸爸他就是因为这点而疲惫不堪的。"

    j "哥哥……你和父亲不同……"

    i "一样的啊，\n不变的心，亦或是不死的心，\n这种东西不会存在啊。"

    i "我有的，只是一颗脆弱的心。"

    "树里像是要反抗我的胡话一样，\n将身体与我紧紧交缠。"

    j "不，哥哥是不一样的。"

    j "哥哥，你是，特别的……"

    j "…………"
    
    pause(3)

    j "我该怎么办……"

    j "大家相信着生的谎言，\n把手伸向幸福的幻影，\n最后又愚蠢的死去。"

    j "那今天或是明天还有什么意义？"

    j "意义到底存在在哪里？"

    j "…………"

    j "我无从得知。"

    i "…………"

    "这孑然一身的世界毫无意义……"

    "那如果树里和我化作这个世界的全部，\n我们的行为会被原谅吗？"

    "树里像是读懂了我的内心一般，继续说着："

    j "小时候，这个世界确实只有我和哥哥两个人……"

    j "然而，从什么时候起……"

    j "是从我初潮那天开始……哥哥，你这样想吗……？"

    i "放弃吧。"

    j "不要。"

    "我们两人都沉默了，沉默中，只剩时间在慢慢流逝。"

    "伴随着不安，早晨又将来临。"

    "似乎睡着了的树里突然又张开了嘴。"

    j "……明天就要走了吧。"

    j "不过……哥哥还是会回来的。"

    i "…………下次不回来了。"

    j "骗人。"

    j "把润酱就这样丢下不管，也可以吗？"

    i "不要伤害润。"

    i "无视她吧。"

    j "…………"
    
    i "树里……"

    "就算我用着责备似的语气喊着树里，\n她也仍是用头蹭着我的胸膛。"

    "似是淘气地嘟着。"

    j "润酱真可怜啊……"

    j "她明明都没有被你爱着，\n你只是一直温柔地对待她什么……"

    j "但她的存在还是令人觉得厌烦。"

    j "哥哥和爸爸一样残酷呢。"

    i "…………"

    scene bg 0999 with fade
    stop music fadeout 1





















    "差点儿得肺炎的伊势雾子就那样睡了一整天。"

    "次日，即使相当虚弱，她还是倔强地离开了青磁家。"

    "虽说拒绝了青磁送她回家的提议，\n但伊势雾子还是选择了遵从青磁的医嘱。"

    pause(1)

    play sound "0616.mp3"

    "几天后某日，青磁刚回到家，\n耳边就传入了阵阵“嗡嗡”声，似乎响了很久。"

    "夜已深，日期将变。"

    "出现在屏幕上的是陌生的号码。"

    "犹豫了一会儿，他拿起了电话。"

    g "您好，我是山鹿。"

    "「…………」"

    g "您好……？"

    "在因对方保持沉默，自己准备放下听筒的时候，\n对面传来了细微的嘶哑声音。"

    "「青……」"

    play music "t08.mp3" fadein 1

    g "是五树吗……？"

    "青磁的神情一下子变得严肃。"
        
    "「青……」"

    g "怎么了？"

    "青磁故作镇静地问着。"

    "「…………只是想听到你的声音而已。」"

    g "…………"
        
    g "跟我说说吧。"

    g "你有话想说吧。"

    "「………………」"

    "「早已结束了……」"

    "「过去的日子早已烟消云散了……」"

    "「只有我还在原地徘徊……」"

    g "…………"

    "「我想我想让树里解放……」"

    "「不想让她再这样痛苦下去了……」"

    g "…………"

    "「青…………」"

    "「向青的父亲伸出援手的，是青吧？」"

    g "啊……"

    "「医学已经救不了树里了，\n她的心已经与自己的身体分离了…………」"

    "「每天晚上像动物一样怪叫，\n为了活下去却必须忍受这样的不堪…………」"

    "「我的母亲朱音也是——」"

    g "别说了，五树！"

    "「……」"

    "我与伊势见了面，打听了你的一些近况。"

    "「…………」"

    g "伊势她把你——"

    "「伊势……她……是个好人。」"

    g "啊……"

    g "我相信，她能成为你的支柱。"

    g "不行的话……就来……依靠我啊……"

    g "……不要什么事都独自一人……\n不要一个人背负一切啊……"

    g "……………………"
        
    i "「……我已经在你那里依靠的够多了。」

    g "…………"
        
    "「哈……哈哈……」"

    "「我只是想让你担心我一下。」"

    "「没事，我已经精神了……」"

    "「抱歉……打扰你了啊……」"

    g "……………"

    stop music fadeout 1
    play sound "0619.mp3"

    pause(4)
    stop sound fadeout 1
    scene bg 0555
    show z9043
    show z9044 with dissolve

    r "虽然我也喊了树里……\n但她说着好困之类的话，继续睡去了。"

    r "那家伙可真是的……"

    i "你考虑好了吗？润。"

    r "嗯…………"

    r "…………"

    "润咬着嘴唇，低下头犹豫一阵后，又下定决心看向五树。"

    r "前辈，果然还是算了吧。"

    i "……"

    r "我不能放着妈妈不管。"

    "看到少女依旧凝视着自己，五树轻轻地点了点头。"

    r "而且果然还是不想走捷径，觉得必须自己想办法。"

    r "所以……"

    r "我会把那个时候收到的耳机当作前辈的替身，\n继续努力的。"

    i "这样啊……"

    i "润果然可靠啊，比我这种人可靠多了。"

    r "啊……没有这种事……"

    i "不过,就目前而言，\n作为学生还是别太躁动为好。"

    r "啊哈哈哈，前辈你别说笑。"

    r "真是的，我在说什么啊。"

    "汽笛的声音把润和五树的笑声盖过。"

    scene bg 0999 with fade

    play sound "0618.mp3"
    pause(12)

    scene bg 0555
    show j 1901 with dissolve

    j "啊~啊，哥哥走了？"

    r "树里……"
        
    r "你怎么现在才来？火车刚刚已经开走了。"

    show j 1903 with Dissolve(0.5)

    j "哎呀——"

    show r 4704 with dissolve

    r "唉…………"

    r "该说你是我行我素，还是令人担心好呢……"

    r "你不好好振作起来的话，\n前辈在那边也会担心啊。"

    hide j with dissolve
    hide r with dissolve

    j "…………"

    r "啊…………"

    r "………抱歉，我说得太过了。"

    r "我并没有装作姐姐对你说教的意思……"

    show j 1909 with dissolve

    j "没事啦……我不介意的。"

    j "反而是润酱的眼眶湿润了哦。"

    r "欸…………？"

    r "啊，这是……"
        
    j "好吧\n"
        
    extend "就当是眼里进沙子了吧。"

    hide j with dissolve
    show r 4608 with Dissolve(0.5)

    r "啊……是…………"

    hide r with dissolve
    show j 1901 with Dissolve(0.5)
        
    j "所以，我们去吃刨冰吧，润酱。"

    r "啊？你话题变得太突然了。"

    r "想去的话你就自己去吃——"

    show j 1905 with Dissolve(0.5)

    j "我要凉凉的蕨麻糬。"

    r "我又不是来这里旅游吃喝的。"

    show j 1901 with Dissolve(0.5)

    j "无所谓啊，反正也是闲着。"

    r "才不闲！所以说，我可是考生啊。"

    show j 1904 with Dissolve(0.5)

    j "润酱是因为不知道蕨麻糬的美味，\n所以才会这么说的。"

    r "你是小孩吗！"

    r "真是的……"

    r "那种东西只要有面粉就能做吧。"

    r "回去后我给你做。"

    show j 1903 with Dissolve(0.5)
        
    j "哇——～"

    show j 1901 with Dissolve(0.5)

    j "润酱真温柔啊。"

    r "别……别开我玩笑了！"

    show j 1902 with Dissolve(0.5)
    stop sound fadeout 1
    pause(2)

    scene bg 0601-dark1 
    show z9020-dark1 with Dissolve(3)

    "　　　　………………"

    "………有时候觉得，\n"
        
    extend "即使每天只是重复着一些司空见惯的事情，\n"

    extend "这样稀疏平常的日子却也很重要。"

    "不论是谁……\n"
        
    extend "都只是活在当下的一瞬间而已。"

    "　　……我对这一事实\n"
        
    extend "　　　不感兴趣。"

    "　　　　……树里……"

    hide z9020-dark1 with dissolve
    show z9021-dark1 with Dissolve(2)
    pause(2)
        
    "　　　　　树里……"

    "　　我们也会改变的。"

    "　　　　我们已不能……\n　　　　
    紧紧联系在一起了……"

    "　　　可以的，可以维持这份永恒的"

    "　　哥哥一直都是……"

    "　渴望并终将归省的人啊……"

    pause(2)

    scene bg 0999 with dissolve







    play music "t04.mp3" fadeout 3




    pause(1)
    scene bg 0555 with fade
    pause(0.75)
    show z9045 with Dissolve(1.75)
    pause(2.5)
    hide z9045 with dissolve
    pause(1.5)

    scene bg 0999
    show t1 at uu
    show t2 at uf
    with fade
    pause(1)

    show t3 at fu
    show t4 at ff
    with dissolve
    pause(2.5)

    scene bg 0999
    with dissolve

    show t5 at fu
    show t6 at ff
    with dissolve
    pause(4)

    scene bg 0999
    with dissolve



    scene bg 0511 with dissolve
    show z9024 with dissolve
    pause(2)
    hide z9024 with dissolve
    scene bg 0911 with dissolve

    scene bg 0999 
    show t7 at fu
    show t8 at ff
    with fade
    pause(4)

    scene bg 0999
    with dissolve



    scene bg 0524 with dissolve
    show z9046 with dissolve
    pause(2)
    hide z9046 with dissolve
    scene bg 0924 with dissolve
    
    scene bg 0999 
    show t9 at fu
    show t10 at ff
    show t11 at fd
    with fade
    pause(4)
    scene bg 0999
    with dissolve




    scene bg 0552 with dissolve
    show z9047 with dissolve
    pause(2)
    hide z9047 with dissolve
    scene bg 0952 with dissolve
    
    scene bg 0999 
    show t12 at ud
    show t13 at ff
    with fade
    pause(2.5)

    scene bg 0999
    with dissolve    

    show t12 at ud
    show t14 at ff
    with dissolve
    pause(4)
    scene bg 0999
    with dissolve



    scene bg 0553 with dissolve
    show z9048 with dissolve
    pause(2)

    hide z9048
    show z9049
    with dissolve
    pause(2)

    hide z9049 with dissolve
    scene bg 0953 with dissolve
    
    scene bg 0999 
    show t15 at ud
    show t16 at fu
    show t17 at ff
    show t18 at fd
    with fade
    pause(4)
    scene bg 0999
    with dissolve



    scene bg 0544 with dissolve
    show z9050 with dissolve
    pause(2)

    hide z9050
    show z9051
    with dissolve
    pause(2)

    hide z9051
    show z9052
    with dissolve
    pause(2)

    hide z9052 with dissolve
    scene bg 0944 with dissolve
    
    scene bg 0999
    show t19 at fu
    with fade
    pause(4)
    scene bg 0999
    with dissolve
    
    stop music fadeout 3
    pause(2)

    

    
    return

 

