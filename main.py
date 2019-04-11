from argparse import ArgumentParser
import sys
import os

templatePath = './templates/'
outputDir = './documents/'
resourceDir = './documents/resource'

def getTemplates():
    templates = []
    for item in os.listdir(templatePath):
        if item[-3:] == 'tex':
            templates.append(item)
    return templates

def createDocuments(template, docName):
    fileName = templatePath+template+'.tex'
    file = os.path.exists(fileName)
    if not file:
        print('Template does not exist')
        return
    target = outputDir+docName+'.tex'
    with open(fileName, 'r') as tf:
        content = tf.read()
        with open(target, 'w')as f:
            f.write(content)

def init():
    if not os.path.exists('./documents'):
        os.makedirs('./documents')
    if not os.path.exists('./documents/resource'):
        os.makedirs('./documents/resource')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-l", "--list", help="List all available templates", action="store_true")
    parser.add_argument("-t", "--template", dest="tem", help="The latex template you want to use")
    parser.add_argument("-d", "--document", dest="doc", help="The file name you want to create")
    args = parser.parse_args()

    init()

    if args.list:
        tem = getTemplates()
        for t in tem:
            print(t[:-4])

    if args.tem is not None and args.doc is not None:
        createDocuments(args.tem, args.doc)