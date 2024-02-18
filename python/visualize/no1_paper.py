import matplotlib.pyplot as plt
import numpy as np

# 假设timestamps是一个包含69个时间步标签的列表
timestamps = np.arange(0, 69)  # 例如，从1到69

# 假设这三个列表包含了你的实验数据
dmd_data = [0.049323164739338905, 0.04956666193150928, 0.049768131983206634, 0.049959667122304874, 0.05012213777234464, 0.050256993644747845, 0.05038746209491013, 0.05050078993428512, 0.0506122349639074, 0.05073141921333681, 0.0508488736365932, 0.05096711881236428, 0.051092945319708406, 0.05120535872360976, 0.0513286952505228, 0.05144737341529238, 0.05155916797467264, 0.05169010009842766, 0.0518077225464526, 0.05194174785058218, 0.052072984842043875, 0.05220308509182325, 0.05233931716480589, 0.052469946006425, 0.05260552593493605, 0.05274646031175422, 0.052890182493299694, 0.05303663641514322, 0.05319897009955385, 0.053348615091934753, 0.05351612714654712, 0.053674651446115454, 0.05383505804217649, 0.05400177355139434, 0.05415541744849506, 0.05432195294888596, 0.054483638930338786, 0.054648780247938004, 0.054818244314263805, 0.054989888707355765, 0.05515479242893079, 0.05532459190492341, 0.055487980957612065, 0.05564974495354131, 0.05581615100190687, 0.05597314829598714, 0.0561480015993804, 0.056313622579248275, 0.056488116044406046, 0.056657619535190606, 0.056829592385732965, 0.05699752827682406, 0.057164578285842677, 0.057333245930519215, 0.0574969574198492, 0.057672921082459326, 0.057839946998983316, 0.05802453378833464, 0.058196626187096236, 0.05837430648010773, 0.058550159631970286, 0.05872250635515339, 0.0588973167542991, 0.05906864294868016, 0.059246638867550466, 0.05942725229545808, 0.059613259646992385, 0.059793120381223204, 0.059982114503535376]
convlstm_data = [0.02378833634290368, 0.02005892324085814, 0.018989472700491908, 0.01981669462590273, 0.0199090016955981, 0.01940761236041907, 0.017831646152332993, 0.017065171681552836, 0.017563840942173437, 0.018303246680261252, 0.022460546854569392, 0.02079196133431198, 0.020820921805905626, 0.021192255407014034, 0.02240653296353853, 0.02658257169863907, 0.036614870689961866, 0.06054172420684303, 0.10887625554636979, 0.1870840725158344, 0.24620023381572012, 0.2932629606755867, 0.33425999495084974, 0.3785900454489037, 0.4207895543026101, 0.45915906136352186, 0.49325599833407135, 0.5228616495407743, 0.5463051246122084, 0.5613727246383795, 0.5596935742201694, 0.5649002117333316, 0.5645081056569733, 0.5723650406682187, 0.57938544752418, 0.584233467166719, 0.5818517269176151, 0.5757191834626876, 0.5672513686446629, 0.5579962911348744, 0.5502233206738869, 0.5550218423851938, 0.5554557604972015, 0.5618543424839912, 0.5669740824033422, 0.5692761567522833, 0.565865288693275, 0.5588507594663583, 0.5494186676513572, 0.5400327666720631, 0.5387510735651604, 0.542469465768273, 0.5427327637906866, 0.5485955000642502, 0.5539964782193509, 0.557374199937385, 0.5578209966450798, 0.5551972402332559, 0.5497448280831181, 0.5421238759275971, 0.5375556646007287, 0.5350502940185122, 0.5298335463913746, 0.5275662648437218, 0.5170676743558053, 0.49563102027509603, 0.46165278344887933, 0.42075942828518526, 0.379387798643641]
ours_data = [0.004733341922476723, 0.004099957338109668, 0.003440323374243719, 0.0030992529876382887, 0.003051487548010005, 0.003206472675284365, 0.0031765615931805256, 0.0033062804283661377, 0.003398467176080354, 0.0033598960010350967, 0.004744684333321733, 0.00467667295342687, 0.004640661935046747, 0.004805389397618416, 0.00554747215754858, 0.00805175010271793, 0.015254353761171457, 0.03372189897197811, 0.07356306069894032, 0.14462909433601004, 0.28166157024931426, 0.41517908763884304, 0.5269661954780474, 0.5994743675568781, 0.6427050528999106, 0.6763245056171174, 0.712253942766932, 0.7431212582533833, 0.7717897212280999, 0.7937170034964292, 0.48837041472136433, 0.46329650426303565, 0.43639389885606195, 0.41324928065160427, 0.39496546828770457, 0.3870361812954383, 0.39570738526055926, 0.41356506486015177, 0.4366714569163145, 0.46461711597599276, 0.5905482849850158, 0.6128625044852125, 0.6278275783986175, 0.6429823104022288, 0.6524808853638019, 0.6593229310373926, 0.668369854945551, 0.6808779164203933, 0.6928619898034124, 0.7015094265080866, 0.52055020150526, 0.5053386815221235, 0.49787159623970406, 0.5005087501485036, 0.5033114099645678, 0.5067132360259359, 0.5225265916926866, 0.546737295085307, 0.5724132595153547, 0.5909577778340701, 0.7491474853577226, 0.7770999912742059, 0.7943394517462419, 0.8012025599564069, 0.7990823815801784, 0.7953439361270992, 0.7911865697057144, 0.7864050473109974, 0.7850627933219829]

# 绘制折线图
plt.figure(figsize=(12, 10))
plt.plot(timestamps, dmd_data, label='DMD', marker='o')
plt.plot(timestamps, convlstm_data, label='ConvLSTM', marker='s')
plt.plot(timestamps, ours_data, label='Ours', marker='^')

# 添加图例，并设置字体大小
plt.legend(fontsize=23, markerscale=2)

# 添加标题和轴标签
plt.title('DISSIPATION--DM', fontsize=28)
plt.xlabel('TimeStamp', fontsize=28)
plt.ylabel('Value', fontsize=28)


# 设置坐标轴刻度的字体大小
plt.tick_params(axis='both', which='major', labelsize=25)

# 使用bbox_inches='tight'减少空白区域，并通过pad_inches调整边缘空白的大小
# 保存为pdf使用下面的格式
# plt.savefig('DISSIPATION--DM.pdf', bbox_inches='tight', pad_inches=0.1, format='pdf')
# 保存为png使用下面的格式
plt.savefig('DISSIPATION--DM.png', bbox_inches='tight', pad_inches=0.1)

# 显示图表
# plt.show()
