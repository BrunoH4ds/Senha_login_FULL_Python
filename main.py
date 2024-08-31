import time

user_data = [("admin@gmail.com", "adminnotoque1234")]

def Login():
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        while True:
            email = input("Digite seu email: ").strip()

            if '@' in email:
                local_part, dominio = email.rsplit('@', 1)
                dominio = dominio.lower()
                email = f'{local_part}@{dominio}'
            else:
                print("\nEmail inválido. O email deve conter '@'.\n")
                continue

            senha = input("Digite sua senha: ").strip()

            if (email, senha) in user_data:
                print("\nLogin efetuado com sucesso!\n")
                return
            else:
                tentativas += 1
                print(f"\nSeu email ou senha estão incorretos. Tentativa {tentativas} de {max_tentativas}.\n")

            if tentativas >= max_tentativas:
                print("\nNúmero máximo de tentativas atingido. Tente novamente após 5 segundos!\n")
                for i in range(5, 0, -1):
                    print(f"\r{i} segundos restantes...", end="")
                    time.sleep(1)
                print()
                return

def Sign_Up():
    while True:
        email_cad = input("Digite seu email: ").strip()

        if email_cad == '':
            print("\nO email não pode estar vazio.\n")
            continue

        if '@' in email_cad:
            local_part, dominio = email_cad.rsplit('@', 1)
            dominio = dominio.lower()

            if dominio not in {'gmail.com', 'hotmail.com', 'outlook.com'}:
                print("\nEmail inválido. Por favor, insira um email válido com @gmail.com, @hotmail.com ou @outlook.com.\n")
                continue

            email_cad = f"{local_part}@{dominio}"

            if any(email == email_cad for email, _ in user_data):
                print("\nEste email já foi cadastrado.\n")
                return

        else:
            print("\nEmail inválido. O email deve conter '@'.\n")
            continue

        senha_cad = input("Digite sua senha: ").strip()

        if len(senha_cad) < 8:
            print("\nSua senha deve ter pelo menos 8 caracteres. Tente novamente.\n")
            continue

        caracteres = any(c.isalpha() for c in senha_cad)
        numeros = any(c.isdigit() for c in senha_cad)
        tem_maiuscula = any(c.isupper() for c in senha_cad)

        if not caracteres:
            print("\nSua senha deve conter pelo menos uma letra. Tente novamente.\n")
            continue
        if not numeros:
            print("\nSua senha deve conter pelo menos um número. Tente novamente.\n")
            continue
        if not tem_maiuscula:
            print("\nSua senha deve conter pelo menos uma letra maiúscula. Tente novamente.\n")
            continue

        confirmar_senha = input("Confirme sua senha: ").strip()

        if senha_cad == confirmar_senha:
            user_data.append((email_cad, senha_cad))
            print("\nEmail e senha cadastrados com sucesso.\n")
            break
        else:
            print("\nAs senhas não coincidem. Tente novamente.\n")
            continue

def Sair():
    print("\nSaindo...\n")
    exit()

main_menu = {
    1: Login,
    2: Sign_Up,
    3: Sair
}

while True:
    print("\nMain Menu:")
    print("1. Login")
    print("2. Cadastro")
    print("3. Sair\n")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("\nEscolha uma das opções existentes.\n")
        continue

    if opcao in main_menu:
        main_menu[opcao]()
    else:
        print("\nOpção inválida. Tente novamente.\n")
