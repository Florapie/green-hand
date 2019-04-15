"""
Usage:
    testDoc.py [-dgktz] <from> <to> <date> ...
    testDoc.py (-h | --help)
Arguments:
    from    current location
    to    destination
    date    the date you want to set out, you can choose more than one day
Options:
    -h,--help    show this
    -d    Dongche
    -g    Gaotie
    -k    kuaiche
    -t    tekuai
    -z    zhida

Examples:
    testDoc.py -gd shanghai shangqiu 20190201
"""


from docopt import docopt
print('***test case***')
if __name__=="__main__":
    argu=docopt(__doc__)
    print(argu)
    from0=argu['<from>']
    to0=argu['<to>']
    date0=argu['<date>']
    print('from>',from0)
    print('to>',to0)
    print('date>',date0)
