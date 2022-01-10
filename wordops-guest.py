# Importando os modulos cuidado para não ser taxado
import getpass
import paramiko

# Dados de acesso sem ele você não faz o login
ip = input("digite o ip do seu servidor: \n" )  # IP do Servidor Linux
usuario = input("digite usuario ssh: \n")  # Usuário de acesso
senha = getpass.getpass("Digite sua senha: \n")  # Senha de acesso

# Criando a conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=usuario, password=senha)


# Função com o Menu (Só Deus sabe como conseguir fazer)
def print_menu():
    print(30 * "-", "OPÇÕES", 30 * "-")
    print("1. Instalar o Sistema")
    print("2. Instalar stack webserver ")
    print("3. criar site")
    print("4. lista sites")
    print("5. Update de php 7.4")
    print("6. Turbinar o Wordpress com redis server")
    print("7. Deletar site")
    print("8. Remover stack")
    print("9. Limpar cache")
    print("10. Alterar credencial de back-end")
    print("11. Exit")
    print(67 * "-")


loop = True

while loop:
    print_menu()
    opcao = input("Selecione sua opção [1-8]: ")

    if opcao == '1':
        # Executando o UPDATE
        print('\n----------------------------------\nAguarde alguns minutos estamos preparando o servidor\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command('wget -qO wo wops.cc && sudo bash wo --force \n')
        result = stdout.readlines()
        print(result, sep='')

    elif opcao == '2':
        # Executando o UPGRADE
        print('\n----------------------------------\nInstalando Stack Wordops\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command('wo stack install\n')
        stdin.write('y\n')
        stdin.flush()
        print(*stdout.readlines(), sep='')

    elif opcao == '3':
        site = input("digite o dominio do seu site: ")
        print(f'\n----------------------------------\nCriando site: {site}\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command(f'wo site create {site} --wp'  )
        print(*stdout.readlines(), sep='')

    elif opcao == '4':
        print('\n----------------------------------\nListando sites instalados\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command('wo site list\n')
        print(*stdout.readlines(), sep='')


    elif opcao == '5':
        list_sites = input("digite o seu site que quer fazer atualização para php7.4: ")
        print(f'\n----------------------------------\nFazendo update do site {list_sites} para php 7.4\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command(f'wo site update {list_sites} --php74')
        print(*stdout.readlines(), sep='')

    elif opcao == '6':
        site_redis = input("Digite qual site você quer TURBINAR: ")
        print(f'\n----------------------------------\nYEAAAAAA!! vamos turbinar o site: {site_redis} para WordPress com redis-cache!!!\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command(f'wo site update {site_redis} --wpredis\n')
        print(*stdout.readlines(), sep='')

    elif opcao == '7':
        delete_site = input("Digite o site que gostaria de deletar: ")
        print(f'\n----------------------------------\nA exclusão do site {delete_site} está sendo iniciada\n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command(f'wo site delete {delete_site} --no-prompt\n')
        print(*stdout.readlines(), sep='')

    elif opcao == '8':
        ssl_site = input("Digite o site que é para gerar o ssl. ATENÇÃO O DOMINIO TEM QUE ESTÁ APONTADO PARA O SERVIDOR: ")
        print(f'\n----------------------------------\nGerando ssl DO SITE: {ssl_site} \n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command('wo stack uninstall\n')
        print(*stdout.readlines(), sep='')

    elif opcao == '9':
        print('\n----------------------------------\nRemover stack \n----------------------------------')
        stdin, stdout, stderr = ssh.exec_command('wo stack uninstall\n')
        print(*stdout.readlines(), sep='')

    elif opcao == '11':
        loop = False

    else:
        print('\nOpção incorreta. Tente novamente.\n')

# Encerrando a conexão SSH ainda vou colocar mais funções
ssh.close()