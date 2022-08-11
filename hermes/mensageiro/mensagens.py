def msg_compra(nome, valor_compra, valor_ativo, ativo):
    linhas = [
        f'Olá {nome},\n',
        f'o ativo {ativo} atingiu o valor de R$ {valor_ativo}, que está abaixo do valor de compra definido.\n',
        f'Como o valor de compra era de {valor_compra} e o valor do ativo está abaixo, recomendamos a sua compra.\n',
        '\n',
        'Atenciosamente,\n',
        'Sistema Hermes'
    ]
    mensagem = ""
    for linha in linhas:
        mensagem += linha
    return mensagem

def msg_venda(nome, valor_venda, valor_ativo, ativo):
    linhas = [
        f'Olá {nome},\n',
        f'o ativo {ativo} atingiu o valor de R$ {valor_ativo}.\n',
        f'Como o valor de venda era de {valor_venda}, recomendamos a sua venda.\n',
        '\n',
        'Atenciosamente,\n',
        'Sistema Hermes'
    ]
    mensagem = ""
    for linha in linhas:
        mensagem += linha
    return mensagem