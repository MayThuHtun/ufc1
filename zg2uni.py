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
    ######

    output = output.replace(u"[\u103D\u1087]", u"\u103E")
    #  ha
    output = output.replace(u"\u103C", u"\u103D")
    #  wa
    output = output.replace(u"[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]", u"\u103C")
    #  ya yint (ra)
    output = output.replace(u"[\u103A\u107D]", u"\u103B")
    #  ya

    output = output.replace(u"\u103E\u103B", u"\u103B" + u"\u103E")
    #  reorder

    output = output.replace(u"\u108A", u"\u103D" + u"\u103E")
    #  wa ha

    #  Reordering

    output = output.replace(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u1064", u"\u1064\1\2\3")
    #  reordering kinzi
    output = output.replace(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108B", u"\u1064\1\2\3\u102D")
    #  reordering kinzi lgt
    output = output.replace(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108C", u"\u1064\1\2\3\u102E",)
    #  reordering kinzi lgtsk
    output = output.replace(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108D", u"\u1064\1\2\3\u1036")
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

    #  / Pasint order human error
    output = output.replace(u"([\u1000-\u1021])([\u102C\u102D\u102E\u1032\u1036]){1,2}([\u1060\u1061\u1062\u1063\u1065\u1066\u1067\u1068\u1069\u1070\u1071\u1072\u1073\u1074\u1075\u1076\u1077\u1078\u1079\u107A\u107B\u107C\u1085])", r"\1\3\2")


    #######/

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

    return output