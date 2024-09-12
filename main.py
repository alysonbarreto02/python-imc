def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc

def fornecer_feedback(imc):
    # Fornece feedback com base no IMC calculado
    if imc < 18.5:
        return f"Seu IMC é {imc:.2f}. Você está abaixo do peso ideal. É importante consultar um nutricionista para avaliar sua alimentação."
    elif 18.5 <= imc < 24.9:
        return f"Seu IMC é {imc:.2f}. Parabéns! Você está com o peso ideal. Continue mantendo uma alimentação equilibrada e praticando atividades físicas regularmente."
    elif 25 <= imc < 29.9:
        return f"Seu IMC é {imc:.2f}. Você está com sobrepeso. É recomendável adotar uma alimentação mais balanceada e aumentar a prática de exercícios físicos."
    elif 30 <= imc < 34.9:
        return f"Seu IMC é {imc:.2f}. Atenção! Você está com obesidade grau I. É importante procurar orientação médica para ajustar sua dieta e rotina de atividades físicas."
    elif 35 <= imc < 39.9:
        return f"Seu IMC é {imc:.2f}. Cuidado! Você está com obesidade grau II. Consultar um médico e um nutricionista é fundamental para cuidar da sua saúde."
    else:
        return f"Seu IMC é {imc:.2f}. Alerta! Você está com obesidade grau III. É essencial procurar um médico o quanto antes para evitar problemas graves de saúde."

def main():
    print("Bem-vindo à Calculadora de IMC!")
    
    # Solicita o peso e a altura do usuário
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        
        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        
        # Exibe o feedback com base no IMC
        feedback = fornecer_feedback(imc)
        print(feedback)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
