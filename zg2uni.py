# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input
    output = output.replace(u"\u106A", u"\u1009")
    output = output.replace(u"\u1025(?=[\u1039\u102C])", u"\u1009")

    output = output.replace(u"\u1025\u102E", u"\u1026")

    output = output.replace(u"\u106B", u"\u100A")
    output = output.replace(u"\u1090", u"\u101B")
    output = output.replace(u"\u1040", u"\u1040")

    output = output.replace(u"\u108F", u"\u1014")
    output = output.replace(u"\u1012", u"\u1012")
    output = output.replace(u"\u1013", u"\u1013")

    #  yayit
    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')

    ##########
    #  1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #  2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

    #  yayit
    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')

    #  yapin
    output = output.replace(u'\u103A', u'\u103B')

    #  nya
    output = output.replace(u'\u106B', u'\u100A')

    #  hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u107D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #  yakaut
    output = output.replace(u'\u1090', u'\u101B')

    #  htawonbae
    output = output.replace(u'\u1092', u'\u100C')

    #  dayinkaut
    output = output.replace(u'\u106E', u'\u100D')

    #  tatalin
    output = output.replace(u'\u1097', u'\u100B')

    #  na
    output = output.replace(u'\u108F', u'\u1014')

    #  athat
    output = output.replace(u'\u1039', u'\u103A')

    #  waswae
    #  thagyi
    output = output.replace(u'\u1086', u'\u103F')

    #  outkamyint
    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')

    ##########

    ######

    output = output.replace(u"[\u103D\u1087]", u"\u103E")
    #  ha
    output = output.replace(u"\u103C", u"\u103D")
    #  wa
    output = output.replace(u"[\u103A\u107D]", u"\u103B")
    #  ya

    output = output.replace(u"\u103E\u103B", u"\u103B" + u"\u103E")
    #  reorder

    output = output.replace(u"\u108A", u"\u103D" + u"\u103E")
    #  wa ha

    #  Reordering

    output = re.sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u1064", u"\u1064\1\2\3", output)
    #  reordering kinzi
    output = re.sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108B", u"\u1064\1\2\3\u102D", output)
    #  reordering kinzi lgt
    output = re.sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108C", u"\u1064\1\2\3\u102E", output)
    #  reordering kinzi lgtsk
    output = re.sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108D", u"\u1064\1\2\3\u1036", output)
    #  reordering kinzi ttt

    ##

    output = output.replace(u"\u105A", u"\u102B" + u"\u103A")
    output = output.replace(u"\u108E", u"\u102D" + u"\u1036")
    #  lgt ttt
    output = output.replace(u"\u1033", u"\u102F")
    output = output.replace(u"\u1034", u"\u1030")
    output = output.replace(u"\u1088", u"\u103E" + u"\u102F")
    #  ha u
    output = output.replace(u"\u1089", u"\u103E" + u"\u1030")
    #  ha uu

    ##

    output = output.replace(u"\u1039", u"\u103A")
    output = output.replace(u"[\u1094\u1095]", u"\u1037")
    #  aukmyint

    #######
    output = output.replace(u"\u1064", u"\u1004\u103A\u1039")

    output = output.replace(u"\u104E", u"\u104E\u1004\u103A\u1038")

    output = output.replace(u"\u1086", u"\u103F")

    output = output.replace(u"\u1060", u"\u1039\u1000")
    output = output.replace(u"\u1061", u"\u1039\u1001")
    output = output.replace(u"\u1062", u"\u1039\u1002")
    output = output.replace(u"\u1063", u"\u1039\u1003")
    output = output.replace(u"\u1065", u"\u1039\u1005")
    output = output.replace(u"[\u1066\u1067]", u"\u1039\u1006")
    output = output.replace(u"\u1068", u"\u1039\u1007")
    output = output.replace(u"\u1069", u"\u1039\u1008")
    output = output.replace(u"\u106C", u"\u1039\u100B")
    output = output.replace(u"\u1070", u"\u1039\u100F")
    output = output.replace(u"[\u1071\u1072]", u"\u1039\u1010")
    output = output.replace(u"[\u1073\u1074]", u"\u1039\u1011")
    output = output.replace(u"\u1075", u"\u1039\u1012")
    output = output.replace(u"\u1076", u"\u1039\u1013")
    output = output.replace(u"\u1077", u"\u1039\u1014")
    output = output.replace(u"\u1078", u"\u1039\u1015")
    output = output.replace(u"\u1079", u"\u1039\u1016")
    output = output.replace(u"\u107A", u"\u1039\u1017")
    output = output.replace(u"\u107B", u"\u1039\u1018")
    output = output.replace(u"\u107C", u"\u1039\u1019")
    output = output.replace(u"\u1085", u"\u1039\u101C")
    output = output.replace(u"\u106D", u"\u1039\u100C")

    output = output.replace(u"\u1091", u"\u100F\u1039\u100D")
    output = output.replace(u"\u1092", u"\u100B\u1039\u100C")
    output = output.replace(u"\u1097", u"\u100B\u1039\u100B")
    output = output.replace(u"\u106E", u"\u100D\u1039\u100D")
    output = output.replace(u"\u106F", u"\u100E\u1039\u100D")

    ##########
    output = re.sub(u"(\u103C)([\u1000-\u1021])(\u1039[\u1000-\u1021])?", r"\2\3\1", output)
    #  reordering ra

    output = re.sub(u"(\u103E)(\u103D)([\u103B\u103C])", r"\3\2\1", output)
    output = re.sub(u"(\u103E)([\u103B\u103C])", r"\2\1", output)

    output = re.sub(u"(\u103D)([\u103B\u103C])", r"\2\1", output)


    return output