import matplotlib.pyplot as plt
import numpy as np

# 假设timestamps是一个包含69个时间步标签的列表
timestamps = np.arange(0, 64)  # 例如，从1到69

title = "Interpolation--PSNR"
file_title = "内插--PSNR"

# title = "Interpolation--DISSIPATION"
# file_title = "内插--DISSIPATION"

rt = [39.325037996444436, 29.87002214483165, 30.03964235139323, 28.89959563713862, 29.920043168480458, 30.400522422738653, 30.188725511910448, 30.70298472670374, 38.84427305910791, 29.426721463076923, 29.61616220946588, 28.58630821539622, 29.632411953165683, 30.194818758486246, 29.963600520718053, 30.439943143655416, 38.55639895116906, 29.301339668972936, 29.450962516909076, 28.647397623611283, 29.47583189534115, 30.398903527065308, 30.080360495795567, 30.3549172412694, 38.36639690584461, 29.502722775417546, 29.58130474118662, 28.842681438426627, 29.98584134980411, 30.629482120403964, 30.593623138153, 31.00242576241802, 38.26077335485588, 30.03643941685604, 30.120328912724705, 29.505100673494855, 30.75284103782264, 30.994205291187477, 31.376381108726296, 31.73337039818247, 38.568144747243, 30.76862405161565, 30.84793753961585, 30.347416718823233, 31.451902482976664, 31.41962733966065, 31.924703734138, 32.33539777814203, 38.59964459717568, 31.156573012541386, 31.294144098692364, 30.692345754405785, 31.615796549844145, 31.504631981080095, 32.10733091840184, 32.33034283200297, 38.59772288985078, 31.033478262173347, 31.107029160896467, 30.509299111749666, 31.242335195296974, 31.315944285888747, 31.611562413735722, 31.609948114064803]
rt_singlescale = [46.28414551786048, 40.76227305912398, 40.56264872968461, 39.85641635481765, 41.432990137393595, 42.02450958483418, 41.887334683986154, 43.16206274740093, 46.113112942265005, 40.53605706565249, 40.53434517345557, 39.67643943734546, 41.333497326210626, 41.98379742090278, 42.00192676604425, 43.17623668608838, 45.94305637498696, 40.412692623620394, 40.41755084388755, 39.700593781439196, 41.15094310124685, 42.00769423336066, 41.99150208664514, 43.338483941106595, 45.714842869305414, 40.301769038234, 40.25978417113471, 39.62093058657941, 41.34689381359772, 42.04936087783722, 42.117219246065034, 43.614770300187466, 45.4918681136822, 40.35199226067909, 40.473983025288085, 39.97461962835165, 41.625745378342536, 42.6240111142344, 42.21634124554768, 43.68635186259742, 45.36737222579336, 40.75835188076298, 40.86245598471515, 40.38283553856218, 41.727917159823605, 43.185696214790184, 42.40232681349958, 43.56851851104928, 45.18740492394909, 41.00373943118812, 41.183054167534145, 40.37567668928073, 41.83688577195858, 43.070311624693964, 42.23155445855192, 42.86823777734544, 45.805887522954514, 40.86964219584416, 40.953096656154564, 40.103097028111904, 41.64413557839269, 42.229080434158746, 41.418258644615946, 42.402535062157234]

dm = [41.326101357951785, 42.13128114545832, 42.07030598096914, 42.015383038856015, 41.92788883656775, 41.92507328998281, 41.89195096373214, 41.8975085913607, 41.028514664874216, 42.016596407274456, 42.11290578283476, 42.20274314574186, 42.241083704874725, 42.37515517230359, 42.474566911974165, 42.58070172160242, 41.51537335666379, 42.681987580980596, 42.8358354892655, 42.99001275730185, 43.13345771129276, 43.30391954707881, 43.45013777448119, 43.63823437682689, 42.6342898814287, 43.58393683595092, 43.76694551848551, 43.905891876777325, 44.11351880971126, 44.272767782744396, 44.39181217830222, 44.51959533105552, 44.32533711085388, 44.82094746314891, 44.89989440639607, 45.014412456836375, 45.18287806954446, 45.155325301186906, 45.004867755877086, 44.895016525357825, 44.12163053296173, 44.090841878289346, 43.92306809501741, 43.665685409864025, 43.364764161700066, 43.09356028314306, 42.55561588614154, 42.043013382932784, 40.570274497620616, 40.88152675386013, 40.642937174414485, 40.417358320162606, 40.231037753277775, 40.168128156413225, 40.04595099410516, 39.98785023019212, 39.14997025691249, 39.750581881782566, 39.72542273919804, 39.695762802672014, 39.60928354901266, 39.612182120592635, 39.55957526451536, 39.543513736576585]
dm_singlescale = [38.957625723593694, 39.08309043110852, 39.15319757764773, 39.204009725488014, 39.223166373035255, 39.240968029367565, 39.24135067861326, 39.21188455571962, 39.867611320674825, 39.97133906312102, 40.08522738767428, 40.19883345114998, 40.292528386145044, 40.383681611964654, 40.474572513397995, 40.56503584320291, 40.73925757205739, 41.194939932229914, 41.37225562635787, 41.50305855654288, 41.63004318750049, 41.723326856858804, 41.77803154064443, 41.80627766280939, 39.494980448760444, 39.935390521163285, 40.03919821123187, 40.10343155373445, 40.13181830491674, 40.11129045218088, 40.04964980660026, 39.934555883219346, 38.63140197359205, 38.870950219082175, 38.884537264599075, 38.860112029349814, 38.824556301488784, 38.745089446008166, 38.608133005840735, 38.41630249287708, 37.88691994912126, 37.824756097732276, 37.8089410808101, 37.76644625697, 37.67707801068526, 37.54300690854927, 37.361803861656924, 37.119030910230954, 35.98602596738743, 35.96052867892729, 35.95088039142815, 35.95342856787282, 35.941116950714395, 35.90926327246072, 35.85362483086577, 35.784841871733775, 34.45891458117184, 34.35692319185221, 34.353910299775436, 34.33574649450214, 34.31848957895423, 34.32292632166164, 34.320072124525474, 34.32908426032132]

rm = [55.951866384269515, 56.08227770195438, 56.19812057103669, 56.23061982666725, 56.20781206893113, 56.105591130897785, 55.964175199524234, 55.80425638558724, 55.1987605627393, 55.090333043576365, 55.0237603897704, 54.86149404557125, 54.63971443025767, 54.35714273728382, 54.03821871504694, 53.67754969539295, 52.64874742625359, 52.70842904637411, 52.413325036477865, 52.07226257369034, 51.66643139974219, 51.265485355003335, 50.80312107780713, 50.33847556228145, 48.724858978167234, 49.18131295315624, 48.83220753313648, 48.45530182053758, 48.068914672509266, 47.67437127319138, 47.26353053898001, 46.84861962938986, 45.134492302209836, 45.88851060360657, 45.58676313575715, 45.269531167509776, 44.941155797381626, 44.619629577182856, 44.28623165305414, 43.966589852336696, 42.301943945887864, 43.26161160174343, 43.015098542660255, 42.76101336027736, 42.5034072617606, 42.25403357910551, 42.00125559149516, 41.75718853394237, 40.1515086942202, 41.25232963562357, 41.05422178427496, 40.8520741774069, 40.64933340584762, 40.453274401549436, 40.25478972129159, 40.06406463671334, 38.49981154905975, 39.69471292668242, 39.53729517675771, 39.37651316867994, 39.215827861602214, 39.060504311601235, 38.90498078447833, 38.75411147002312]
rm_singlescale = [61.36067610886677, 60.6048111054906, 60.6005588141965, 60.49995676609008, 60.41596703102617, 60.26482561359134, 60.132859257656364, 59.87383491514378, 59.725588102783405, 58.33816536958185, 58.18152758143749, 57.9734100219008, 57.75449542930496, 57.4863969901982, 57.199840406277346, 56.89131278642343, 56.054094821627345, 54.36804198280693, 54.1919303868654, 53.97871890087633, 53.725182833665215, 53.45552323465828, 53.17928032646524, 52.87047482894075, 52.27285320831349, 50.61543841686509, 50.46364239335649, 50.272327159356784, 50.07054915020922, 49.840712605483986, 49.63501274169528, 49.39545177577196, 49.34086930091081, 47.77546346554284, 47.64398667191618, 47.47080650188679, 47.293786446537204, 47.09066357101152, 46.90074200981606, 46.675779855515714, 47.036297478271116, 45.54617921507414, 45.423500201465785, 45.26679435002028, 45.09813175132521, 44.905972651268115, 44.73278808917228, 44.525850103903785, 45.187352966919065, 43.720546750705495, 43.61456992102009, 43.47684727148852, 43.313527249151264, 43.136989487387815, 42.980009428404166, 42.7888492685264, 43.6241382669521, 42.215327172242965, 42.11231599143137, 41.98282633015502, 41.83949506739366, 41.680498988629594, 41.53836514189606, 41.36129057437379]


# 假设这三个列表包含了你的实验数据
# dmd_data = [0.4289794973795614, 0.42800151383718527, 0.4270091504692198, 0.42600861722536154, 0.42498736952083865, 0.42402828439892787, 0.42312203183070557, 0.4222557840166214, 0.42140781080434625, 0.42055647683678593, 0.4197069502128803, 0.41882973299270554, 0.41798590195424123, 0.41716836066350443, 0.4164288891712647, 0.41574588623765985, 0.4151125713497543, 0.4144938736401922, 0.41385694913006077, 0.4132584507783631, 0.41270458715035624, 0.41223713687198255, 0.4118180967562931, 0.41147141486830524, 0.41117765942887635, 0.41095382198049035, 0.41080554982509887, 0.41071918243388333, 0.4107400103677225, 0.41085360245025887, 0.4110953639350801, 0.4113921439214796, 0.41173238792355604, 0.41208185048267304, 0.41243962047070826, 0.4128319102399073, 0.41323030894633367, 0.4136287915110423, 0.4139384699757062, 0.41417998540870066, 0.4143259523698296, 0.4143975026121066, 0.41439563389288897, 0.41433861459919674, 0.41423729950259297, 0.41405653070539133, 0.41381366812625897, 0.41345217492654895, 0.4129816097857732, 0.4123888545906904, 0.4117393088763761, 0.4110364110559775, 0.41024614374952956, 0.409362320492905, 0.4083677459327417, 0.40731223014559426, 0.4061768995448772, 0.40500337203327563, 0.40376072844846217, 0.4024815123884117, 0.4011820912225108, 0.3998589513241101, 0.39849799571554834, 0.39707378860104536, 0.3956537358166351, 0.39422641715759715, 0.3928140502987293, 0.3913868224943103, 0.3899647263856478]
# convlstm_data = [0.9986885860934497, 0.9985615865286143, 0.9982921825574377, 0.9978267936180406, 0.9971535384212746, 0.9965300448288835, 0.9954826917466838, 0.9946255601037546, 0.9986946654932344, 0.9986944509950654, 0.9983914420515447, 0.9980386544477469, 0.9974749993478654, 0.9965955056827162, 0.9958103027961651, 0.9947377327711909, 0.9986877072369309, 0.998595599503193, 0.998386777159017, 0.9979657409349408, 0.9973356673898423, 0.9966942170368208, 0.9957397460006276, 0.9946933450992096, 0.9986130893246276, 0.9986719921633533, 0.998278453175538, 0.9978157339285229, 0.9970984555906001, 0.9961985709458547, 0.9951822427859606, 0.9936961272967941, 0.9985630055740025, 0.9983951137291789, 0.9980280018546291, 0.9972861861064357, 0.9966240781978507, 0.9955485859634001, 0.9941660344442504, 0.9928122653664025, 0.9984438412144063, 0.9984114890434509, 0.9979589532261806, 0.9974792315802822, 0.9965881763290598, 0.9956702016688347, 0.9945807546737081, 0.9932008854767221, 0.9983113553402325, 0.9982211394501753, 0.9979180116143059, 0.9972495148301865, 0.9966016125787381, 0.9955317642220424, 0.9944196457045468, 0.9929743788174106, 0.9982490040871045, 0.9982406113640017, 0.9978305642308072, 0.9973363327533058, 0.9964891945589276, 0.9956037472752988, 0.9943294372782085, 0.993111605678556]
# ours_data = [0.9998557508001293, 0.9998033070462279, 0.9998126916911222, 0.9998138737274365, 0.9998093428083682, 0.9998042590101336, 0.9997922382913851, 0.9997771088505465, 0.9998074822790604, 0.9997467275383065, 0.9997512871669347, 0.9997489617210809, 0.9997382188596537, 0.9997272396685657, 0.9997096074249555, 0.9996872378204591, 0.9997228084236799, 0.9995824203444713, 0.9995724208861232, 0.9995524022236858, 0.9995259579490027, 0.9995035125178832, 0.9994727339390069, 0.9994401094659202, 0.9995521007590522, 0.9992693420921227, 0.9992562900369105, 0.9992324724082347, 0.9991981445133958, 0.9991671102249555, 0.9991215703853931, 0.999072970918862, 0.9992998867707547, 0.9988408980568229, 0.9988206635326391, 0.9987962043067451, 0.9987616307098284, 0.998728063650004, 0.9986797442394661, 0.9986300335191163, 0.9989401227100229, 0.9983042343391446, 0.9982908067680188, 0.9982689906650882, 0.9982291139588623, 0.9981830123064052, 0.9981164310112848, 0.9980491005958793, 0.9985083021292437, 0.9976905761220298, 0.997688823524387, 0.9976700096443503, 0.9976309880555684, 0.9975868330618909, 0.9975235132760456, 0.9974559718593108, 0.9980538182229022, 0.9970869326777736, 0.9970884370884919, 0.9970696933455873, 0.9970272225331254, 0.9969725101490953, 0.996899118704191, 0.9968231136519935]

# 绘制折线图
plt.figure(figsize=(12, 10))
# plt.plot(timestamps, dmd_data, label='DMD', marker='o', markersize=7)
plt.plot(timestamps, rt, label='RT', marker='o', markersize=7)
plt.plot(timestamps, rt_singlescale, label='RT-SingleScale', marker='>', markersize=7)
plt.plot(timestamps, dm, label='DM', marker='d', markersize=7)
plt.plot(timestamps, dm_singlescale, label='DM-SingleScale', marker='p', markersize=7)
plt.plot(timestamps, rm, label='RM', marker='v', markersize=7)  # 选择了另外一个marker作为示例
plt.plot(timestamps, rm_singlescale, label='RM-SingleScale', marker='h', markersize=7)  # 选择了另外一个marker作为示例

# 设置Y轴为对数尺度
# plt.yscale('log')

# 添加图例，并设置字体大小
plt.legend(fontsize=23, markerscale=2, loc='upper left')

# 添加标题和轴标签
plt.title(title, fontsize=28)
plt.xlabel('TimeStamp', fontsize=28)
plt.ylabel('Value', fontsize=28)


# 设置坐标轴刻度的字体大小
plt.tick_params(axis='both', which='major', labelsize=25)



# 使用bbox_inches='tight'减少空白区域，并通过pad_inches调整边缘空白的大小
# 保存为pdf使用下面的格式
plt.savefig(f'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/图片/消融实验/是否单尺度/{file_title}.pdf', bbox_inches='tight', pad_inches=0.1, format='pdf')
# 保存为png使用下面的格式
plt.savefig(f'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/图片/消融实验/是否单尺度/{file_title}.png', bbox_inches='tight', pad_inches=0.1)

# 显示图表
plt.show()