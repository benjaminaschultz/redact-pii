import re
import simplejson

first_names = simplejson.load(open('./names.json'))
apt_regex = re.compile('(?P<apt_prefix>apt|bldg|dept|fl|hngr|lot|pier|rm|ste|slip|trlr|unit|#)\.? *[a-z0-9-]+', re.IGNORECASE)
po_box_regex =  re.compile('P\.? ?O\.? *Box +\d+', re.IGNORECASE)
road_regex = re.compile('(?P<street_type>street|st|road|rd|avenue|ave|drive|dr|loop|court|ct|circle|cir|lane|ln|boulevard|blvd|way)\.?', re.IGNORECASE)

regexes = {
    'name_regex':  re.compile('\\b({})\\b\s*((\w+)[- ]?){{0,3}}'.format('|'.join(first_names))),
    'credit_card_number_regex':  re.compile('\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}', re.IGNORECASE),
    'street_address_regex':  re.compile('\d+\s*(?P<street_name>\w+ ){{1,2}}{}(?P<apt_full>\s+{})?|(?P<po_box_full>{})'.format(
        road_regex.pattern,
        apt_regex.pattern,
        po_box_regex.pattern
        ), re.IGNORECASE),
    'zipcode_regex':  re.compile('\\b(?P<zip_code>\d{5}\\b(-\d{4})?)', re.IGNORECASE),
    'phone_number_regex':  re.compile('(\(?\+?[0-9]{1,2}\)?[-. ]+)?(\(?[0-9]{3}\)?|[0-9]{3})[-. ]+([0-9]{3}[-. ]+[0-9]{4}|\b[A-Z0-9]{7}\b)', re.IGNORECASE),
    'ip_address_regex':  re.compile('(\d{1,3}(\.\d{1,3}){3}|[0-9A-F]{4}(:[0-9A-F]{4}){5}(::|(:0000)+))', re.IGNORECASE),
    'email_address_regex':  re.compile('([a-z0-9_\-.+]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-z0-9-]+\.)+))([a-z]{2,4}|[0-9]{1,3})(]?)', re.IGNORECASE),
    'username_regex':  re.compile('\\b(user( ?name)?|login): \S+', re.IGNORECASE),
    'password_regex':  re.compile('\\b(pass(word|phrase)?|secret): \S+', re.IGNORECASE),
    'credentials_regex':  re.compile('\\b(login( cred(ential)?s| info(rmation)?)?|cred(ential)?s) ?:\s*\S+\s+\/?\s*\S+', re.IGNORECASE),
    'company_regex':  re.compile('\\b([A-Z&][\w,]* ){0,2}(I[Nn][Cc](orporated)?|C[Oo](rp(oration)?)?|LLP|llc|LLC|plc|gmbh)\.?', re.IGNORECASE),
    'salutation_regex':  re.compile('\\b(dear|hi|hey|hello|greetings|yo) ([^,:;\s]+(,? )?){1,5}[,;\n]', re.IGNORECASE),
    'valediction_regex':  re.compile('(thanks|cheers|sincerely|regards|respectfully|best|best regards|yours truly)\s*,?\s*([\w&]+\s?){1,5}', re.IGNORECASE)
}
