def verifica_fibonacci(numero):
    # Função para verificar se um número está na sequência de Fibonacci
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def main():
    # Função principal
    try:
        numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
        if verifica_fibonacci(numero):
            print(numero, "é um número da sequência de Fibonacci.")
        else:
            print(numero, "não é um número da sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()


