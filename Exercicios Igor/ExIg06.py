VT = int( input("Digite um Valor: R$") )
DC = int( input("Digite o Valor da Porcentagem: ") )
SBDC = (DC/100)* VT

print(f"Valor total : R${VT}.00")
print(f"Porcentagem de desconto:{DC}% ")
print(f"Valor do Desconto: R${SBDC}0")
print(f"Valor total com desconto: R${VT-SBDC}0")