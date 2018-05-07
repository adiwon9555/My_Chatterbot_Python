from chatterbot.logic import LogicAdapter


class CMDLogic(LogicAdapter):
    def __init__(self, **kwargs):
        super(CMDLogic,self).__init__(**kwargs)

    def can_process(self, statement):
        stlower = statement.text.lower()
        if(stlower.startswith('open') or stlower.startswith('start')):
            return True
        else:
            return False

    def process(self, statement):
        import os
        from chatterbot.conversation import Statement
        wordList = statement.text.split();
        confidence=1
        stlower=statement.text.lower()
        if(('open' in stlower) or ('start' in stlower)):
            print(stlower[stlower.index(" ")+1:len(stlower)])
            # os.system('start '+stlower[stlower.index(" ")+1:len(stlower)])

        # return Statement(stlower[stlower.index(" ")+1:len(stlower)]+'.exe'+' opened as said..')
        # return Statement(wordList[1])
        return Statement('start '+stlower[stlower.index(" ")+1:len(stlower)])
