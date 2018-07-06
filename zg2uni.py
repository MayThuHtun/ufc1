# -*- coding: utf-8 -*-
import re


def replace(input):
    output = input

    #  nyalay
    output = output.replace(u'\u106A', u'\u1009')

    #  1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #  2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

    #  hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #  waswae
    output = output.replace(u'\u103C', u'\u103D')

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
    output = output.replace(u'\u107D', u'\u103B')

    #  nya
    output = output.replace(u'\u106B', u'\u100A')

    #  yakaut
    output = output.replace(u'\u1090', u'\u101B')

    #  htawonbae

    #  dayinkaut

    #  tatalin

    #  na
    output = output.replace(u'\u108F', u'\u1014')

    #  athat
    output = output.replace(u'\u1039', u'\u103A')

    #  thagyi
    output = output.replace(u'\u1086', u'\u103F')

    #  outkamyint
    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')

    return output


def decompose(input):
    output = input

    output = re.sub(u'\u105A', u'\u102B' + u'\u103A', output)
    #  yaychar-htoe

    output = re.sub(u'\u108A', u'\u103D' + u'\u103E', output)
    #  wa-hatoe

    output = re.sub(u'\u1088', u'\u103E' + u'\u102F', output)
    #  hatoe-1chaung

    output = re.sub('\u1089', u'\u103E' + u'\u1030', output)
    #  hatoe-2chaung

    output = re.sub(u'\u103E\u103B', u'\u103B' + u'\u103E', output)
    #  yapin-hatoe

    output = re.sub(u'\u108E', u'\u102D' + u'\u1036', output)
    #  lgt-ttt

    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102D', output)
    #  ngathat-lgt

    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102E', output)
    #  ngathat-lgtsk

    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u1036', output)
    #  ngathat-ttt

    output = re.sub('\u1064', u'\u1004\u103A\u1039', output)
    #  up-ngathat

    output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038', output)
    #  la-gaung



    return output

def visual2logical(input):
    output = input
    #  Pattern

    output = re.sub(
        u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103B)?)((?:\u103D)?)((?:\u103E)?)((?:\u1037)?)((?:\u102C)?)',
        r'\3\2\4\5\6\1\7\8', output)
    return output


def convert(input):
    output = input
    replace(input)
    decompose(input)
    visual2logical(input)
    return output

