

from chatterbot.logic import LogicAdapter


class ApiLogic(LogicAdapter):
    def __init__(self, **kwargs):
        super(ApiLogic,self).__init__(**kwargs)

    def can_process(self, statement):
        stlower = statement.text.lower()
        if((stlower.startswith('get') or stlower.startswith('select') or stlower.startswith('retrieve') or stlower.startswith('fetch'))):
            return True
        else:
            return False

    def process(self, statement):
        import json
        import pandas as pd
        import os
        import requests
        from chatterbot.conversation import Statement
        wordList=statement.text.split();
        confidence=0
        stlower=statement.text.lower()
        if((('retrieve' in stlower) or('select' in stlower) or ('fetch' in stlower) or ('get' in stlower)) and ('all' in stlower)):
            try:
                url = 'http://localhost:3000/' + wordList[wordList.index("all") + 1]
                response = requests.get(url)
                dat = response.json()
                data = json.dumps(dat);
                # if (not ('error' in data)):
                #     jsondata = data.get('accounts')
                #     # myjs='[{"a":"B","b":"A"},{"a":"C","b":"D"}]'
                #     js = pd.read_json(json.dumps(jsondata))
                #     js.to_excel('output.xls', index=False)
                #     os.system('start output.xls')
            except Exception as e:
                return Statement("No document found for " + wordList[wordList.index("all") + 1])


        elif ((('retrieve' in stlower) or ('select' in stlower) or ('fetch' in stlower) or ('get' in stlower)) and (
                'details' in stlower) and ('of' in stlower) and ('account' in stlower) ):
            url = 'http://localhost:3000/accountsByAccountNo?acc_no=' + wordList[wordList.index("account") + 1]

            response = requests.get(url)
            dat = response.json()
            data = json.dumps(dat);
            # if (not ('error' in data)):
            #         jsondata = data.get('accounts')
                    # myjs='[{"a":"B","b":"A"},{"a":"C","b":"D"}]'
                    # js = pd.read_json(json.dumps(jsondata))
                    # js.to_excel('output.xls', index=False)
                    # os.system('start output.xls')

        elif((('retrieve' in stlower) or('select' in stlower) or ('fetch' in stlower) or ('get' in stlower)) and ('details' in stlower) and ('of' in stlower)):
            url = 'http://localhost:3000/accountsByName?name='+wordList[wordList.index("of")+1]
            response = requests.get(url)
            dat=response.json()
            data=json.dumps(dat);
            # if (not ('error' in data)):
            #     jsondata = data.get('accounts')
                # myjs='[{"a":"B","b":"A"},{"a":"C","b":"D"}]'
                # js = pd.read_json(json.dumps(jsondata))
                # js.to_excel('output.xls', index=False)
                # os.system('start output.xls')
        else:
            return Statement("I did not understand.. Try again")

        if(response.status_code==200):
            confidence=1

        return Statement(data)
