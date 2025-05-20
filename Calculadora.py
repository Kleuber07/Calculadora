def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida.")


while True:
    try:
        # Solicita os dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        # Realiza o cálculo
        resultado = calcular(num1, num2, operacao)

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.\n")
        continue
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}. Tente novamente.\n")
        continue
    except Exception:
        print("Erro inesperado. Tente novamente.\n")
        continue
    else:
        print(f"Resultado: {resultado}")
        break
