import re
valid_conditions = ["VI","NP","HG", "NS", "NC", "DR", "PO", "ST", "PH"]
id_types = ["license_plate", "phone", "email"]


class TokenizerError(Exception):
    INVALID_TOKEN = 0
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code

class ParserError(Exception):
    UNEXPECTED_ID = 0
    UNEXPECTED_CONDITION = 1
    NEVER_RECEIVED_ID = 2
    def __init__( self, msg, code):
        self.msg = msg
        self.code = code

class ParseNode(object):
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

class Request(object):
    def __init__(self, req_id, parse_nodes):
        self.req_id = req_id
        self.parse_nodes = parse_nodes

class Report(object):
    def __init__(self, req_id, conditions, parse_nodes):
        self.req_id = req_id
        self.conditions = conditions
        self.parse_nodes = parse_nodes


class MessageParser(object):
    def parse(self, message):
        return Parser().parse(Tokenizer().parse(message))

class Parser(object):
    def parse(self, tokens):
        waiting_for_id = True
        current_id = None
        waiting_for_conditions = False
        conditions = []
        parsed_tokens = []
        for tok in tokens:
            if tok.token_type in id_types:
                if waiting_for_id:
                    waiting_for_id = False
                    waiting_for_conditions = True
                    current_id = tok
                else:
                    raise ParserError("Unexpected ID - %s :(" % tok, ParserError.UNEXPECTED_ID)

            elif tok.token_type == "condition":
                if waiting_for_conditions:
                    conditions.append(tok)
                else:
                    raise ParserError("Unexpected conditions - %s  :(", ParserError.UNEXPECTED_CONDITION)
            parsed_tokens.append(tok)
        if not current_id:
            raise ParserError("We never received an ID. We can't do anything with this", ParserError.NEVER_RECEIVED_ID)
        if conditions:
            return Report(current_id.value, map(lambda x: x.value, conditions), parsed_tokens)
        else:
            return Request(current_id.value, parsed_tokens)

class Tokenizer(object):
    def parse(self, astr):
        astr=astr.replace('-','')
        astr=astr.replace('(','')
        astr=astr.replace(')','')

        tokens=astr.split()
        result=[]
        for tok in tokens:
            license_plate_match = re.match("^[a-zA-Z]{2}\*[a-zA-Z0-9-* ]{2,8}$", tok)
            phone_match = re.match("^[0-9]{9,10}$", tok)
            email_match = re.match("^[^@ ]+@[^@ ]+$", tok)

            if license_plate_match:
                result.append(ParseNode(tok, "license_plate"))
                continue
            if phone_match:
                result.append(ParseNode(tok, "phone"))
                continue
            if email_match:
                result.append(ParseNode(tok, "email"))
                continue
            if tok.upper() in valid_conditions:
                result.append(ParseNode(tok, "condition"))
                continue
            #we've failed
            raise TokenizerError("we received the token of %s and I had no idea how to handle that" % tok, TokenizerError.INVALID_TOKEN)

        return result
