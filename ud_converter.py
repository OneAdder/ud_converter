import re

data = [('хватит', 'хватить.PRS-3SG'), ('собянить', 'собянить.PST-INF'), ('Москву', 'Москва-ACC.SG')]

def to_ud(data):
    ud_words = []
    for word in data:
        glosses = re.split('-|=|\.|-=', word[1])
        ud_token = word[0]
        ud_glosses = []
        ud_lemma = ''
        has_lemma = 0
        for gloss in glosses:
            if gloss:
                if not gloss.isupper():
                    if not has_lemma:
                        #if there are more than one lemmas, we take the first one
                        ud_lemma = gloss
                        has_lemma = 1
                    else:
                        #other lemmas we consider affixes
                        ud_glosses.append(gloss + '=True')
                else:
                    ud_glosses.append(gloss + '=True')
        #if there's no lemma, we consider the first gloss to be a lemma
        if not ud_lemma:
            ud_lemma = ud_glosses[0]
        ud_word = '{lemma} {glosses} {token}'.format(
            lemma=ud_lemma,
            glosses=' '.join(ud_glosses),
            token=ud_token,
        )
        ud_words.append(ud_word)
    return '\n'.join(ud_words)

print(to_ud(data))
            
