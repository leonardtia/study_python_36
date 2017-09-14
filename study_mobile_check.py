mobile = input('please input mobile:')


def check_mobile(mobile):
    CN_mobile = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157', '158', '159', '182', '183',
                 '184', '187', '188', '147', '178', '1705']
    CN_union = ['130', '131', '132', '155', '156', '185', '186', '145', '176', '1709']
    CN_telecom = ['133', '153', '180', '181', '189', '177', '1702']
    if (len(str(mobile)) < 11):
        print ('input mobile error')
    else:
        mob = str(mobile)[:3]
        mobl = str(mobile)[:4]
        if (mob in CN_mobile) or (mobl in CN_mobile):
            print ('the mobile is CN_mobile')
        elif (mob in CN_union) or (mobl in CN_union):
            print ('the mobile is CN_union')
        elif (mob in CN_telecom) or (mobl in CN_telecom):
            print ('the mobile is CN_telecom')
        else:
            print ('the mobile error')


check_mobile(mobile)
