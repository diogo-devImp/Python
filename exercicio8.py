preco = float(input('Digite o valor do produto: '))

desc = (preco * 0.1) 
preocf = preco - desc

print(f'Seu desconto é de {desc:.2f} R$')
print(f'Seu preço final ficou {preocf:.2f} R$')