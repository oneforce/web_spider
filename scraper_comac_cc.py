# coding:utf-8

import datetime
import codecs
import requests
import os
import time
from pyquery import PyQuery as pq


markdownFileContent = """
---
tags:
    - {jobName}
岗位名称: {jobName}
文件地址: 2023/商飞/{companyName}/{deptName}/{companyName}_{deptName}_{jobName}_{jobId}.md
招聘年份: 2023
发布时间: {publishTime}
地点: {address}
招聘人数: {num}
学历要求: {education}
单位: {companyName}
部门: {deptName}
工作年限: {workYears}
岗位薪资: {salary}
语言: {language}
专业: {speciality}
---

# {companyName}_{deptName}_{jobName}

[{jobName}]({url})


## 部门描述

{deptDescription}

## 岗位职责

{jobDescription}

 ## 条件要求

{condition}
"""

def createMarkdown(filename):
    # 获取文件所在的目录路径
    directory_path = os.path.dirname(filename)

    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def scrape(jobId):
    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }


    url = 'http://zhaopin.comac.cc/zp/ct/out/position/positionDetail?planid={jobId}'.format(jobId=jobId)
    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200
    
    d = pq(r.content)
    # items = d('div.gwjs div.layui-col-md3')
    # items2 = d('div.gwjs div.layui-col-md9')

    
    # codecs to solve the problem utf-8 codec like chinese
    # with codecs.open(filename, "a", "utf-8") as f:
    #     for item in items:
    #         i = pq(item)
    #         label = i(".vlab").text().replace("：","")
    #         value = i(".vsap").text()
    #         # f.write(u"{label}: {value}\n".format(lable=lable, value=value))
    #         print(u"{label}: {value}\n".format(label=label, value=value))
    #     for item in items2:
    #         i = pq(item)
    #         label = i(".vlab").text().replace("：","")
    #         value = i(".vsap").text()
    #         # f.write(u"{label}: {value}\n".format(lable=lable, value=value))
    #         print(u"{label}: {value}\n".format(label=label, value=value))
    deptDescription = d("label:contains('部门描述：')").next().next().text().replace("；","；\n")
    jobDescription = d("label:contains('岗位职责：')").next().next().text().replace("；","；\n")
    condition = d("label:contains('条件要求：')").next().next().text().replace("；","；\n")
    jobName = d('div.zp-title span').text()
    publishTime = d("label.vlab:contains('发布时间')").next().text()
    address = d("label.vlab:contains('地点')").next().text()
    num = d("label.vlab:contains('招聘人数')").next().text()
    education = d("label.vlab:contains('学历要求')").next().text()
    companyName = d("label.vlab:contains('单位')").next().text()
    deptName = d("label.vlab:contains('部门')").next().text()
    workYears = d("label.vlab:contains('工作年限')").next().text()
    salary = d("label.vlab:contains('岗位薪资')").next().text()
    language = d("label.vlab:contains('语言')").next().text()
    speciality = d("label.vlab:contains('专业')").next().text()

    
    print(markdownFileContent.format(deptDescription=deptDescription,jobDescription=jobDescription,condition=condition,jobName=jobName,publishTime=publishTime,address=address,num=num,education=education,companyName=companyName,deptName=deptName,workYears=workYears,salary=salary,language=language,speciality=speciality,jobId=jobId, url=url))
    filename = "2023/商飞/{companyName}/{deptName}/{companyName}_{deptName}_{jobName}_{jobId}.md".format(deptDescription=deptDescription,jobDescription=jobDescription,condition=condition,jobName=jobName,publishTime=publishTime,address=address,num=num,education=education,companyName=companyName,deptName=deptName,workYears=workYears,salary=salary,language=language,speciality=speciality,jobId=jobId)
    createMarkdown(filename)
    with codecs.open(filename, "a", "utf-8") as f:
        f.write(markdownFileContent.format(deptDescription=deptDescription,jobDescription=jobDescription,condition=condition,jobName=jobName,publishTime=publishTime,address=address,num=num,education=education,companyName=companyName,deptName=deptName,workYears=workYears,salary=salary,language=language,speciality=speciality,jobId=jobId,url=url))
    



def job():


    # write markdown
    scrape('3377cceb40354133b1ed83f6358ec8ec')
    scrape('d4e76b2dd82a44dda92b2a55c1bb5a32')
    scrape('82c255cfd0644192b36139e75e3f6575')
    scrape('266984cbefa647d2b9c37383fb084e1c')
    scrape('058a891e29944079b38e6f8b0bec1581')
    scrape('8a3dca47749d4ce1b32723f1b971ce35')
    scrape('ce4739a2e38d46ad863a3a5845ba7201')
    scrape('06e401cea32c43a19265d20d576c4dab')
    scrape('9b2dca2e08bf4be8bbbda8ee23514e98')
    scrape('a06baa103028446c9af21344877649f2')
    scrape('6675cb7ea1d94cb89ad5925cc4ea89bd')
    scrape('1751d1f9c5134c789190214312dc94b4')
    scrape('f050d7ffcbdb40abbeb37036d5a24f71')
    scrape('da1fe8a1017a4253abb3a8ad5045bb01')
    scrape('e43c0deb248f4bafbd5d50be9ad97635')
    scrape('d9e2e7949845495e85974863711f9cb4')
    scrape('1bf621818f4146668cac9f6f4b1e7532')
    scrape('6b45804f7e1d4855b5376d28422e5409')
    scrape('3aceb19bf6474997842682a43cacb193')
    scrape('5e1ca4521d364a6198799c639eba8caa')
    scrape('f426098ebee1478eb1563617baf6c469')
    scrape('2a5d08663af1406f8ebbcab7b41cbc84')
    scrape('9bf8c969494e4c829477aee2a5a0681a')
    scrape('6bacf1a246e4495a9c3fce5faefd9831')
    scrape('841090990c504ffbbba8cdd578fdfd5a')
    scrape('d29df356f1244c49b829bb27bfc61269')
    scrape('22c302fe09604de9a49162fdd9e59f4e')
    scrape('b502685f39a04c99adce50214a5c7446')
    scrape('34ae03ab62454541a9ae407060fce83f')
    scrape('190e5b1a9076486b8dfcee87aa506006')
    scrape('a1201e61c9f640598053ba0c68cacced')
    scrape('36689e2dfad74f4a855679784fdada55')
    scrape('731d40fd5d5843f88a29bad94e28d495')
    scrape('ee31dcc1c9824d04bb5c63ce5fbc4f54')
    scrape('5250b514ad014ce78c3a5172f02fd827')
    scrape('0ae29453657442bcbeb1296962cf0b89')
    scrape('7475bc8224d64ec4ac9106d606d927b5')
    scrape('b12a579e7f944c02bc3c25a7fa7663e5')
    scrape('c6c8134112d1434ca27c0111b3f7b209')
    scrape('3e7422e52e9045469f99935f175993c1')
    scrape('8a1e5be2592e44eea5493b7428c3c011')
    scrape('b7080ea3286444deb9b1e11867c127f2')
    scrape('a4ce3ea3d3c5466d85a4b4624f3abcbe')
    scrape('9c6b98629f0f46a4ad3757780d0fc955')
    scrape('1a3c7d3ff3494dfea23eb126b16991bc')
    scrape('d91321640d834d1bb5cac549a4f1e21d')
    scrape('6ef6a91257d44ccf890fe4d06b4a4c29')
    scrape('05caced7ebd04711a448d6510ef67261')
    scrape('aaf00c261df04b6294898c00bc21090a')
    scrape('08e5820a239542d5b55f022e7b434497')
    scrape('96e477fb181c4aafa77c91bf78426531')
    scrape('03f5ba5fc52e4d92bd688809dbbda896')
    scrape('d8e19c01d7844768a3f53729bc66182f')
    scrape('eb2e7c442084403db28a9556051d55ef')
    scrape('643af83b2bbf4c00a4e2b213e5124d44')
    scrape('15dc29b4eddd46cfbf06cdc0722be20c')
    scrape('340684949da244edb14632996a5a876c')
    scrape('f8389f905180488bb7b8b6cc9a65b90b')
    scrape('d4e13b69a84c4a5f98379994904314bb')
    scrape('ace102c46a4f491fadf1778dd9974c01')
    scrape('28777bfadd8542dab0c0401634fb1c96')
    scrape('8cbabfa6235145fdbc91ff9e61aa443c')
    scrape('1ba6c27953434117a6037d0c2ae07614')
    scrape('542b7b841f72407d947bd8b7f38fb792')
    scrape('a2ba3c6d4fdf4581a365c9ac40a56783')
    scrape('cce427cb2c324a3a9e223bb3b7265a50')
    scrape('6731697002214d40963858ac86348038')
    scrape('39a97e2dd755487a97e1a99f154274a4')
    scrape('6b1043089a2e436da77323652656d587')
    scrape('a09a6164afa4403a8caeec991948aaa7')
    scrape('966990843cfa4874a1dd47d88cb17ae4')
    scrape('7f561cbc12b64daba5eca6fffda65189')
    scrape('8d4bc037605246d7a80975d34c694f51')
    scrape('31fa55d3e31a4e2698adfa1aaa30b356')
    scrape('ca0e3f6d9b944adc801020b0b8199d0e')
    scrape('e596ccb9063d4271b41f767be4f16ca5')
    scrape('547c6576e5a14d98b4dd3bef861bdd0c')
    scrape('a8e64348f05c40f3bba000a61ec32c50')
    scrape('38d426c7194e4f55b4b8fe4dc9ffae89')
    scrape('ec15dbdea8cb430bb2eae8cd163b6e5b')
    scrape('935cde73027e4a38b6e1a71a3ff962e7')
    scrape('62c0d87694eb4224967f433a64b9ecb6')
    scrape('24342a1eda844987b88a6f7ab1af8b4c')
    scrape('7aff41b87b3e4fab9f405cbfcc459065')
    scrape('93ad272ad16e4947bc660ebf3134ff3d')
    scrape('6dc761881fe94764945a7a6fc8168b5e')
    scrape('bbc5ebabfe7a45bb9f55f1787c4b9969')
    scrape('e310662334b241239867725a9d5342c6')
    scrape('e0e61ae1c846494181f16835d61aae21')
    scrape('449e6a9ec12a4c9cacef62bc223df3d3')
    scrape('9ccfb2fb158649f29884032bb384d185')
    scrape('99f60b73e94b4dffb2ade2ffb6c7e059')
    scrape('b91a89fb64e54352bb6c88ae6ffcf939')
    scrape('ed77b90b77d04eb0aee2e8e42471fee4')
    scrape('03dd0b45d5344a5b924c5b7444cabf52')
    scrape('4fcd4b10c0144792b071043e6953d1cd')
    scrape('b057411239e1412d97756c329932ff98')
    scrape('5df8210a8dbc4bb58f0653926b153cf5')
    scrape('3aaa9238dd9b4dd1a77dc34676d7825a')
    scrape('f5c62cbde96844079804be417d5411eb')
    scrape('8cb841a3ce2b4c7dae960aa36441fd47')
    scrape('ae4fc83c45924ee891c60648cf796353')
    scrape('912c43a936984e9e98ce3658f41a097b')
    scrape('78dd397d937c40d98e66030b3a25bcc4')
    scrape('6ee025ac9f0f4e4998b2c4690e6f2f81')
    scrape('73b869444ba14a2c83c543099de66fb2')
    scrape('0d4dc7bcf817427fb46eabd34d34da47')
    scrape('8b52693d9f90472c8d60a190289e651e')
    scrape('8031d8cc0cbc4ca2b63c87faaa93a8cc')
    scrape('a44ec2b38cf3422faf02196e3a1ca051')
    scrape('fb3b6e64ae4f4b64b49e1549613405b0')
    scrape('60e31e0ec43a4d2480d39720f71540be')
    scrape('ebf60b7cd01c46cb859580c34d745378')
    scrape('2a808fc6c9b84989bef728d4c608d68c')
    scrape('d510a8b07546484e81b388e3455e3031')
    scrape('419459d905fc42d18c7ca2bd1bbfb734')
    scrape('6e7fc8df611241f49cd07ef3a7149988')
    scrape('b4df2de978354751a6312ba6f48930c7')
    scrape('e38f49e91f8d4203bfe93fa580631c00')
    scrape('22bad3a8c89247c8a72ff818339c5148')
    scrape('b7b00f25301a46df8e6c75ebb2126494')
    scrape('28280dbc4fbe43d8b3ae1246006635fe')
    scrape('691b48121f2f48c8b295ff38bf71d10e')
    scrape('08e4c59ef31045b4af678d94cc2c96e1')
    scrape('4a6f423e78034aeeaeb0157220b76ccd')
    scrape('a399cabb84aa41d3967f637f82b8812a')
    scrape('d43ac216e0714b188e7b998258249d20')
    scrape('c60bfa30512a428da8de379e5d0a1331')
    scrape('f470ddaf8777440683615de171133b9a')
    scrape('3e6e638cbf7444a785ac5ef004855017')
    scrape('77a003eec42b45a1803a01b9568ccc4d')
    scrape('d74bca9e25cb424ab561faa3df72c9ac')
    scrape('1428c3a82295423d8e9aeda22dce5ff6')
    scrape('373d0393a15e4d6eb499f1b859c20e02')
    scrape('5583806bb9274704bfafa50fc5be6db7')
    scrape('b3cb8048b0c54619ad6c505a8622b664')
    scrape('c7a7968dbb424365a2486983b228b4cf')
    scrape('7e8d7a2a0e9148a5be2109e8ef334e34')
    scrape('b4fc7fdb10034cf8802de43671df2d1b')
    scrape('e6d8167fb6ff4849b160daa7fe849dd1')
    scrape('eb7b8fee6afb42288f2057240d44cee2')
    scrape('17d6c4f6a25143fda7e442f9195f70ac')
    scrape('921b31ef0af240e891e11809e12eeff0')
    scrape('2c9979526355411a8a8c58a78513990e')
    scrape('7094acc6874e417e8f236ea314416e15')
    scrape('3ca4acf6d2cc449a81884ee770cd6585')
    scrape('a53a946611044b1089314ab01869c01b')
    scrape('b839814273cb41f8b98ea1f1a62a7ca9')
    scrape('516dce4114784fa98d0cf15047429f74')
    scrape('24de592f173147cab6790188d38c0a73')
    scrape('9309902df1ba46dd9c412e878414f340')
    scrape('436781fd2c7d4afa9b0a7d8a3df296f3')
    scrape('ed866930fb4144a7ae6463dd09cc703f')
    scrape('114339922ca74cbab9ef1706584f8cbc')
    scrape('20240a23c1614bd5824db8ee03aaeb21')
    scrape('3e9d44e5856c44ca908a98172a5a8ca2')
    scrape('5382c5e9b0b74442b8bafca2550eaf18')
    scrape('e67b089abe584f739089824e6811c5ed')
    scrape('f71cdfaf6dc14888be72dd6d3192f23e')
    scrape('bea9aa2fdb704aa9b1a6af25a293d4f9')
    scrape('4f06c756ef32498e8f96409e031d2648')
    scrape('6d54cd8d15894fe2bc855edbe3e737a2')
    scrape('6503d9f9cf6547d694db20ab91e0c04f')
    scrape('67bb83599bb446c696a861cae62ca141')
    scrape('ac7f9e05dd9441aa8ef63bbdf773f4c4')
    scrape('c37f97b53a404ce48dc8b4f6ad0504f4')
    scrape('c266b71aa6814e7ea4a24cdf3b29af07')
    scrape('12a415c541984760b0c59cfb948cfdc1')
    scrape('202171d0ef0e40bbb893983004779974')
    scrape('ef18d9d055254ea8a75039f2f7dd7ae6')
    scrape('37ab21a2c05b4f4eb0b4be9458f76272')
    scrape('de65ac5bf6eb4884ae7538ce10c8386e')
    scrape('c3866f9c52334fd39528c0afcaeae654')
    scrape('cb038f41c8fc48a880d28091ffbfa2ea')
    scrape('19ad351089454150bdea12032020e46d')
    scrape('2be5bd5b701d4bdf8debaac61c0534ca')
    scrape('463f8f5b6dda42388e2ee527f20ea8dc')
    scrape('1392c9d3a8064f2e9312bea79e995e3e')
    scrape('6fb03887bb46493880ca1d43a9d973a6')
    scrape('30611a05238a460fa1a901ebb655114a')
    scrape('85f02e578e2c47c186c71c76733cc9bc')
    scrape('eaf7531a20f34416942b0923fc88efc0')
    scrape('9355a82a4a954d75b2e06701700c0ddb')
    scrape('11f88ec9934c4e2dacff3c6aa123e95c')
    scrape('da9fbeb55d0d49cea6e82ccb8e593ef1')
    scrape('8f4a6eb700af46d78d2ae6d63c8d274f')
    scrape('7040292b4e5245b98b478365b380716f')
    scrape('18f7e3abbb7a4476b802676a07f784a2')
    scrape('087d0f5952d64b27ad76e2a3f3ce7e15')
    scrape('5645641e40d5497a9bb8659799643dc1')
    scrape('374037be136a42ec8aa7f844404b31da')
    scrape('2f8e9b97428b4a6fb5dcedd6d6e4bc43')
    scrape('fab839a0e1714f67808447719761cb6c')
    scrape('4d596c8942634ce493f7fc1fffa18a11')
    scrape('aeef1d83866d4cf5bd0612199c73da24')
    scrape('71af282199c3468cbba700dab2dbb2fb')
    scrape('0030e15c92fd43dc8e398b593710b8c0')
    scrape('61d9cfe523ce4bf48ebc87d499dca0e5')
    scrape('2e8841ad1e9f4a17820050a690793506')
    scrape('5e5ac9cd0e164e89b2b70489382e272c')
    scrape('7207073ebe524f99b13891473b37f786')
    scrape('ecc130b37a944a12a14fd9efc5adab4b')
    scrape('a4bb39db247d4eca8d631d0d23950b23')
    scrape('5330219653ac4b7fb98d03f8c606071e')
    scrape('4e6353c2a1614ef98c8ea61c4636ab76')
    scrape('5e7c47bb7cef402f9d7432a574f125ee')
    scrape('405802b9130c4afdb94a624fbb690ce1')
    scrape('fd0e862c75154aa388a5c3fa9e9f0e96')
    scrape('ad27cd07c95043bca0f3646a9294c009')
    scrape('4aa25735b11b4f2b8f4f34a235d00dab')
    scrape('4e6eb8ac04c04f80abeeee2b150dfc01')
    scrape('35487f7b2ad242e5a9bf209324d0a07a')
    scrape('d7319102a66247bba5c7f4afebb61ef0')
    scrape('3f934c0ef28f46c99dc84f8e156b71fd')
    scrape('70b75a5331084fb883d00bcca061a0d8')
    scrape('c350aacc1c6f4b87ad8fd14b50d26f34')
    scrape('83b543371d3e434395e7e0191b9ace12')
    scrape('fcabac0e42494233b01437406c1b9d5f')
    scrape('08e5f96e932a4ff0bf79464a33a7a3c2')
    scrape('69d7ef3e75c14b7cbcc47abaa15b305e')
    scrape('3eeccc2791f74c029a96489af46d31eb')
    scrape('064eea93d248485c86406df647991156')
    scrape('0b08b487b0574442a5eee2a44bbd026a')
    scrape('1af6fa3bcc6246a7ab8717793a8396da')
    scrape('7d6c953f159648b992a249c9003039ff')
    scrape('b43b43eca9394976880a8652504437d5')
    scrape('a3f0217e1ac8432796d641c43be8eba7')
    scrape('f5bbd51cebc9403ca6b7dd7346fa29e8')
    scrape('2b1aa014c0bc4a95aa1aa966eb04f32a')
    scrape('85a4d6fe3e0f4f99a03212a6cdf26f61')
    scrape('3a76210af15340179d8bfbc763317b2a')
    scrape('2cf3713151dc4c998a315301240ff971')
    scrape('2f969965422e4ed39beab0db8c919c3e')
    scrape('f2803bece0d843e18a52a9cc8fa410b8')
    scrape('0b51e5160ef94a2a806651ace8320683')
    scrape('8f6841a2d885426489b0d791d1ac8139')
    scrape('4a140a7e409f49dbb669c4942288f9bd')
    scrape('aa8dbe58d197472b938239c54cb9dc7a')
    scrape('b4fe815ab21f46899a17fe3a7e1c1eb0')
    scrape('3b9fd892b4064bb185f2e871dd2ed13d')
    scrape('b3017113cf724e489b9a0bf3e885f9a6')
    scrape('6837d4aad4a845609637394eeb0ea268')
    scrape('3cd2115ec42445b68a6a4f585d15a2df')
    scrape('7a3e31f8fdd947b89e56bcea8d976594')
    scrape('3cd91bb284d74cf08db55df979f9ecb4')
    scrape('1bbc4c7f734447c8b024deadf4c581cd')
    scrape('5e79afc310624ea992008bfd8b87ce72')
    scrape('64d944491b3c4888b3f6bdd633696227')
    scrape('8da8504796ec4c87b06097fceda8af93')
    scrape('6c4e4aed2eea43d4a7fd6c0d7226076c')
    scrape('c8b6b1235aa04c58b1481a0fffe59b5f')
    scrape('e89a5dfd95cb42e1ab110fce127de08d')
    scrape('2058812b591f431886822ff71342986a')
    scrape('8a40f7d81ff1442bbaff0acbfc3f14b3')
    scrape('552cb7214963406d83d2cc0915e8ee17')
    scrape('da0f9f3922ae48bb9e2ea0926beec7db')
    scrape('8594b2bbbf684b6d8dac0551a8033716')
    scrape('106d8879826b45c2ae5c7c90932e5c0f')
    scrape('f7c0f5ac76af495da442dc05a3608bb5')
    scrape('197710515495407a8599de51a41e5a9d')
    scrape('a29609dd700e4307b4bfd0e0438a3d0f')
    scrape('9815c8aeed204a1bad65213bd296d071')
    scrape('f63232a555604a90bd3360d87c8956e7')
    scrape('b0e15a4a190e4b0091089e49bf631563')
    scrape('16a1df523d234af794e89b35d26092b5')
    scrape('53489cc30c174b32baa293124e186a03')
    scrape('8f0ee854425945a5824454d2879a861f')
    scrape('f15406f6f352457598a4c4be7dc73e2c')
    scrape('ad91fbec858548c9b7793ee0e3795b87')
    scrape('994d23405e9043eaa2d9e1d6448fb650')
    scrape('7b322f97e7c543b39c231eddfed1da40')
    scrape('95a64235629745b497f976d2c62fe2f2')
    scrape('0f7dcd0ca97647bd932b4dfc29f71b80')
    scrape('6c8e07eb7d444ab2beafdd8362da6101')
    scrape('fa405eaa00c84afd93ee7b22a222f1ba')
    scrape('c5ee419359c240feb9dc2b106a7fa00d')
    scrape('fbe697a17cde4708afbf29de635d21d9')
    scrape('e53c8a37ef154822b42fda9b1a0cdf4c')
    scrape('5260ddbfdfcb4c8dabc536c4121b1bd8')
    scrape('8817be2d80d141fa88e155df471f1bed')
    scrape('9628ce506a554f4f9ef2308eec6bd852')
    scrape('5a6196ab1ab04176962b5354a928788c')
    scrape('fff1d710114f492196e9f12ff2263e71')
    
    # git add commit push
    # git_add_commit_push(strdate, filename)


if __name__ == '__main__':
    job()