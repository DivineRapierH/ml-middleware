import hanlp

split_sent = hanlp.load(hanlp.pretrained.eos.UD_CTB_EOS_MUL)
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
# Ref: https://hanlp.hankcs.com/docs/annotations/ner/ontonotes.html
OntonotesTags = {
    'PERSON': True,
    'NORP': True,
    'FACILITY': True,
    'ORGANIZATION': True,
    'GPE': True,
    'LOCATION': True,
    'PRODUCT': True,
    'EVENT': True,
    'WORK_OF_ART': True,
    'LAW': True,
    'DATE': False,
    'TIME': False,
    'PERCENT': False,
    'MONEY': False,
    'QUANTITY': False,
    'ORDINAL': False,
    'CARDINAL': False,
    'ORG': True,
    'LANGUAGE': True,
    'LOC': True,
    'FAC': True
}
# Ref: https://hanlp.hankcs.com/docs/annotations/pos/pku.html
PKUWorkClasses = {
    'Ag': False,
    'a': False,
    'ad': False,
    'an': True,
    'Bg': False,
    'b': False,
    'c': False,
    'Dg': False,
    'd': False,
    'e': False,
    'f': False,
    'h': False,
    'i': False,
    'j': True,
    'k': False,
    'l': False,
    'Mg': False,
    'm': False,
    'Ng': False,
    'n': True,
    'nr': True,  # merge if having multiple occurrence
    'ns': True,
    'nt': True,
    'nx': False,
    'nz': True,
    'o': False,
    'p': False,
    'q': False,
    'Rg': False,
    'r': False,
    's': False,
    'Tg': False,
    't': False,
    'u': False,
    'Vg': False,
    'v': False,
    'vd': False,
    'vn': False,
    'w': False,
    'x': False,
    'Yg': False,
    'y': False,
    'z': False
}


class AnnotationResult:
    def __init__(self, tokFine, posPKU, nerOntonotes, index):
        self.tokFine = tokFine
        self.posPKU = posPKU
        self.nerOntonotes = nerOntonotes
        self.index = index


class NLPTag:
    def __init__(self, name, wordClass, entityClass):
        self.name = name
        self.wordClass = wordClass
        self.entityClass = entityClass


def annotate(sourceStrList) -> list[AnnotationResult]:
    size: int = len(sourceStrList)
    wholeRes = HanLP(sourceStrList, tasks=['tok/fine', 'pos/pku', 'ner/ontonotes'])
    annotateResList = []
    for i in range(size):
        tokFine = wholeRes['tok/fine'][i]
        posPKU = wholeRes['pos/pku'][i]
        nerOntonotes = wholeRes['ner/ontonotes'][i]
        annotateRes = AnnotationResult(tokFine, posPKU, nerOntonotes, i)
        annotateResList.append(annotateRes)
    return annotateResList


def extractTag(annotationList) -> list[list[NLPTag]]:
    returnList: list[list[NLPTag]] = []
    for annotation in annotationList:
        tagList: list[NLPTag] = []
        entityList = filter(lambda e: OntonotesTags[e[1]] is True, annotation.nerOntonotes)
        indexToOmit: list[int] = []
        for entity in entityList:
            tag = entity[0]
            tagClass = entity[1]
            tagList.append(NLPTag(tag, '', tagClass))
            indexRange = range(entity[2], entity[3])
            indexToOmit += indexRange

        tokLen: int = len(annotation.tokFine)
        for i in range(tokLen):
            tok = annotation.tokFine[i]
            pos = annotation.posPKU[i]
            if PKUWorkClasses[pos] is True and not indexToOmit.__contains__(i):
                tagList.append(NLPTag(tok, pos, ''))
        returnList.append(tagList)

    return returnList


def splitAndAnnotate(sourceStrList) -> list[AnnotationResult]:
    sentenceList: list[str] = []
    for s in sourceStrList:
        sentenceList.extend(split_sent(s))
    return annotate(sentenceList)
