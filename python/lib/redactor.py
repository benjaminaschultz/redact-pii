from patterns import regexes as default_regexes


class Redactor(object):
    
    def __init__(self, regexes=default_regexes):
        self._regexes = regexes
        self.sub_dict = {rname.split('_regex')[0].upper(): rexp for rname, rexp in self._regexes.items()}

    def redact(self, text):
        for sub_text, regex in self.sub_dict.items():
            text = regex.sub(sub_text, text)
        return text
