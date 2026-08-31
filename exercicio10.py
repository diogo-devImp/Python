salario = float(input('Informe seu salário fixo R$ '))
vendas = int(input('Informe quantas vendas você fez no mês R$ '))

comissao = (vendas * 0.04)
salario1 = salario + comissao

print(f'Sua comisão este mês foi de R$ {comissao}')
print(f'Seu salário mais as comissões é de R$ {salario1}')