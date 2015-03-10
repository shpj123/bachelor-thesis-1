'''
Created on Feb 20, 2013

@author: maribelacosta
'''

import hashlib

__author__ = "Maribel Acosta"
__copyright__ = "Copyright 2013"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Maribel Acosta"
__email__ = "maribel.acosta@kit.edu"
__status__ = "Development"

def calculateHash(text):
    return hashlib.md5(text).hexdigest()


def splitIntoParagraphs(text):
    paragraphs = text.split("\n\n")

    return paragraphs

    
def splitIntoSentences(text):
    p = text

    p = p.replace('.', '.@@@@')
    p = p.replace('\n', '\n@@@@')
    p = p.replace(';', ';@@@@')
    p = p.replace('?', '?@@@@')
    p = p.replace('!', '!@@@@')
    #p = p.replace('.{', '.||{')
    #p = p.replace('!{', '!||{')
    #p = p.replace('?{', '?||{')
    p = p.replace('>{', '>@@@@{')
    p = p.replace('}<', '}@@@@<')
    #p = p.replace('.[', '.||[')
    #p = p.replace('.]]', '.]]||')
    #p = p.replace('![', '!||[')
    #p = p.replace('?[', '?||[')
    p = p.replace('<ref', '@@@@<ref')
    p = p.replace('/ref>', '/ref>@@@@')
    
    
    while '@@@@@@@@' in p :
        p = p.replace('@@@@@@@@', '@@@@')

    sentences = p.split('@@@@')
        
    return sentences


def splitIntoWords(text):
    p = text
    words = p.split()
        
    return words
    

def computeAvgWordFreq(text_list, revision_id=0):
    
    d = {}
    
    for elem in text_list:
        if not (d.has_key(elem)):
            d.update({elem : text_list.count(elem)})
    
    if ('<' in d):        
        del d['<']
    
    if ('>' in d):
        del d['>']
        
    if ('tr' in d):
        del d['tr']
    
    if ('td' in d):
        del d['td']
    
#    if ('(' in d):
#        del d['(']
#        
#    if (')' in d):
#        del d[')']
        
    if ('[' in d):
        del d['[']
        
    if (']' in d):
        del d[']']
        
#    if ('"' in d):
#        del d['"']
        
#    if ('|' in d):
#        del d['|']

    
    if (len(d) > 0):                 
        return sum(d.values())/float(len(d))
    else:
        return 0
