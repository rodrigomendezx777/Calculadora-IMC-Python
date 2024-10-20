# Programa para calcular o IMC - Índice de Massa Corporal

def calcular_imc(peso, altura):
    """
    Função para calcular o IMC com base no peso e altura.
    
    Parâmetros:
    peso (float): Peso da pessoa em quilogramas (kg).
    altura (float): Altura da pessoa em metros (m).
    
    Retorna:
    float: O valor calculado do IMC.
    """
    if altura <= 0 or peso <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    """
    Função para classificar o IMC de acordo com os padrões da OMS.
    
    Parâmetros:
    imc (float): O valor do IMC calculado.
    
    Retorna:
    str: A categoria de IMC (Abaixo do peso, Peso normal, etc).
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"


def obter_entrada_numerica(prompt):
    """
    Função auxiliar para garantir a entrada numérica válida pelo usuário.
    
    Parâmetros:
    prompt (str): A mensagem que será exibida ao solicitar a entrada.
    
    Retorna:
    float: O valor numérico inserido pelo usuário.
    """
    while True:
        try:
            valor = float(input(prompt))
            if valor <= 0:
                print("Por favor, insira um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


def main():
    """
    Função principal que executa o cálculo e a classificação do IMC.
    """
    print("Bem-vindo ao Calculador de IMC")

    # Solicitar peso e altura do usuário
    peso = obter_entrada_numerica("Digite seu peso (kg): ")
    altura = obter_entrada_numerica("Digite sua altura (m): ")

    # Calcular o IMC
    imc = calcular_imc(peso, altura)

    # Exibir o resultado
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")


if __name__ == "__main__":
    main()
