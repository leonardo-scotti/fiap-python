print("========== CONTROLE DE COMPRA ==========")
name_product = input("Digite o nome do produto: ")
price_product = float(input("Digite o preço unitário do produto (R$): "))
qtd_product = int(input("Digite a quantidade comprada (R$): "))
discount_product = float(input("Digite a porcentagem de desconto (%): ")) / 100

gross_value = qtd_product * price_product

discount_value = gross_value * discount_product

final_value = gross_value - discount_value

print("\n\n========== RELATÓRIO FINAL =========="
      f"\nProduto: {name_product.upper()}"
      f"\nValor Bruto: R$ {gross_value: .2f}"
      f"\nDesconto: R$ {discount_value: .2f}"
      f"\nValor Final: R$ {final_value: .2f}")