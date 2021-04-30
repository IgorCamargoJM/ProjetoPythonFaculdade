from datetime import datetime

#função para armazenar as linhas de separações
def linha():
    print('--------------------------------------------------------------------------------')
    print()

#função para obter o limite do usuário
def obter_limite():
    cargo = input('Qual o seu cargo atual? ')
    salario = input('Qual o seu salário mensal? R$ ')
    #laço de repitação para verificar se é formato valido
    while type(salario) == str:
        try:
            float(salario)
        except:
            salario = input("Erro!! Insira um valor decimal, acima de 0: ")
        else:
            break
    ano_de_nascimento = input('Qual o seu ano de nascimento? ')
    #laço de repitação para verificar se é formato valido
    while type(ano_de_nascimento) == str:
        try:
            int(ano_de_nascimento)
        except:
            ano_de_nascimento = input("Erro!! Insira uma data válida: ")
        else:
            break
    linha()
    #exibição dos dados digitados pelo usuario
    print('Cargo informado:', cargo)
    print('Salario:', salario)
    print('Ano de Nascimento:', ano_de_nascimento)

    #irá realizar a análise de crédito
    ano = datetime.now()
    ano_atual = int(ano.strftime("%Y"))
    idade = (ano_atual - int(ano_de_nascimento))
    print('A sua idade aproximada é de:', idade, ' anos')
    linha()
    limite = float(salario) * (int(idade)/1000)+100
    print('Nosso sistema gerou um valor de R$%.2f'%limite, 'de limite para gasto')
    print()
    linha()
    return limite, idade


#função para verificar o produto e calcular valor final do produto
def verificar_produto(limite):
    nome_do_produto = str(input('Digite o nome do produto desejado: '))
    valor_do_produto = float(input('Digite o preço do produto desejado: '))
    print()
    #condicional para ver se libera para o cliente
    global bloqueado                         
    bloqueado = 0
    if valor_do_produto > limite:
        bloqueado = 1
        return bloqueado
        
    #calcular o desconto do cliente 
    if valor_do_produto <= (0.6 * limite):
        print('Liberado!')
    elif valor_do_produto <= (0.9 * limite):
        print('Liberado ao parcelar em até 2 vezes')
    elif valor_do_produto <= limite:
        print('Liberado ao parcelar em 3 ou mais vezes')

    #comandos para verificar quantidade de caracteres
    nome_completo = ('Igor Jaime Moreira Camargo')
    tamanho_nome_completo = len(nome_completo)
    primeiro_nome = (nome_completo.split()[0])
    tamanho_primeiro_nome = len(primeiro_nome)

    #condicional para verificar o desconto
    if tamanho_nome_completo <= valor_do_produto and valor_do_produto <= idade:
        desconto = tamanho_primeiro_nome
        valor_final = valor_do_produto - desconto
        print('Você terá um desconto de R$ %.2f' %desconto)
        print('O valor final do seu produto é R$ %.2f' %valor_final)
        print()
        print('--------------------------------------------------------------------------------')
    elif idade <= valor_do_produto and valor_do_produto <= tamanho_nome_completo:
        desconto = tamanho_primeiro_nome
        valor_final = valor_do_produto - desconto
        print('Você terá um desconto de R$ %.2f' %desconto)
        print('O valor final do seu produto é R$ %.2f'%valor_final)
        print()
        print('--------------------------------------------------------------------------------')
    else:
        valor_final = valor_do_produto
        print('Não houve desconto!')
        print()
        print('--------------------------------------------------------------------------------')
    print()

    return valor_final
    
#início do código com apresentação
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')
print('                Olá!Seja bem-vindo! Esta é a loja Império  ')
print('         Aqui é o Igor Jaime Moreira Camargo, estou pronto para te ajudar :)')
print('')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(' ')
print('Iremos realizar sua análise de crédito, ok!?')
print('')
print('Precisamos que o(a) Sr(a), insira alguns dados: ')
print()
linha()

#chamando função para gerar o limite
limite, idade = obter_limite()

#verificar quantos produtos serão cadastrados
quantidade_de_produtos = int(input('Quantos produtos você deseja cadastrar? '))
print()
linha()

valor_total = 0
#chamando funçao e calculando saldo
for i in range(quantidade_de_produtos):
    valor_final = verificar_produto(limite)
    if bloqueado:
        linha()
        print('Bloqueado')
        print()
        linha()
        break
    limite -= valor_final
    print('Limite disponível R$ %.2f' %limite)
    print()
    linha()
    valor_total += valor_final

if not bloqueado:
    print('Total cadastrado R$ %.2f' %valor_total)

print('+++Obrigado pela preferência+++/n---Volte Sempre!---')
    
        
