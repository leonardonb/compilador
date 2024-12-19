class Symbol:
    def __init__(self, id, token, name, kind, line):
        self.id = id
        self.token = token
        self.name = name
        self.kind = kind
        self.line = line

    def __repr__(self):
        return f"Symbol(id='{self.id}', token='{self.token}', name='{self.name}', kind='{self.kind}', line={self.line})"

    @staticmethod
    def symbol_table(tokens) -> list:
        symbol_table = []
        for token_id, token_type, token_value, token_line in tokens:
            if token_type == 'IDENTIFIER':
                symbol_table.append(Symbol(token_id, token_value, 'IDENTIFIER', '', token_line))
        return symbol_table
