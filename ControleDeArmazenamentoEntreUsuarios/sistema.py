def tratar_dados_usuario(dados: list):
    # entrada_funcao ->['IDs Usuarios\n', '1   jessica22\n', '2   carlos97\n', '3   ana_luiza\n']
    # saida_funcao ->{1: 'jessica22', 2: 'carlos97', 3: 'ana_luiza'}
    dados.pop(0)
    dados_tratados = {}

    for k, v in enumerate(dados):
        nome_usuario = []
        if k == len(dados) - 1:
            id = int(str(v[:4]).strip())
            nome_usuario.append(v[4:])

        else:
            id = int(str(v[:4]).strip())
            nome_usuario.append(v[4:-1])

        dados_tratados[id] = nome_usuario
    return dados_tratados


def bytes_para_kb(b):
    return b / 1024


def bytes_para_mb(b):
    return b / (1024 * 1024)


def bytes_para_gb(b):
    return b / (1024 * 1024 * 1024)


def convertor(valor):
    gb = bytes_para_gb(valor)
    mb = bytes_para_mb(valor)
    kb = bytes_para_kb(valor)

    valores = {"GB": gb,
               "MB": mb,
               "KB": kb}
    for k, v in valores.items():
        if v >= 1:
            v = f"{v:.2f}"
            return f"{v:<7}{k}".replace(".", ",")


def converter_dados(dados_tratados: dict):
    for k, v in dados_tratados.items():
        dados_tratados[k] = convertor(v)
    return dados_tratados


def tratar_dados_arm_usuario(dados: list):
    # entrada_funcao ->['id_usuario  usu_espaco_byte\n', '2           3,625,882,004\n', '3           4,720,102,391\n']
    # saida_funcao ->{2: 3625882004, 3: 4720102391}
    dados.pop(0)
    dados_tratados = {}
    auxiliar = []
    valor_em_byte_tratado = []

    for k, v in enumerate(dados):
        if k == len(dados) - 1:
            auxiliar.append(str(v[12:]))
        else:
            auxiliar.append(str(v[12:-1]))

    for v in auxiliar:
        x = v.replace(",", "")
        x = int(x)
        valor_em_byte_tratado.append(x)

    for k, v in enumerate(dados):
        id = int(str(v[:12]).strip())
        dados_tratados[id] = valor_em_byte_tratado[k]
    return dados_tratados


def ler_arquivo_arm_usuario():
    with open('arm_usuarios.txt', mode='r') as arm_usuario:
        dados = arm_usuario.readlines()
    return dados


def ler_arquivo_usuario():
    with open('usuarios.txt', mode='r', ) as usuarios:
        dados = usuarios.readlines()
    return dados


def mesclar_tabelas(usuarios: dict, arm_usuario: dict, tabela_porcentagem: dict):
    # entrada_funcao -> {1: 'jessica22', 2: 'carlos97', 3: 'ana_luiza}-usuarios
    # entrada_funcao -> {2: 3625882004, 3: 4720102391, 4: 4557893203}-arm_usuario
    # entrada_funcao -> {2: 6.75, 3: 8.79, 4: 8.49}-tabela_porcentagem
    # saida_funcao ->   {1: ['jessica22', '5,26 GB', 10.52], 2: ['carlos97', '3,38 GB', 6.75]}

    for k, v in usuarios.items():
        usuarios[k].append(arm_usuario[k])
        usuarios[k].append(tabela_porcentagem[k])
    return usuarios


def escrever_relatorio(tabela: dict):
    with open("relatorio.txt", mode='r+') as relatorio:
        if len(relatorio.readlines()) == 0:
            relatorio.write(f'{"Id":<5}{"Usuário":<20}{"Espaço Ultilizado":<20}{"%Uso":<6}\n')
            relatorio.write(f"{'=' * 50}\n")
        for k, v in tabela.items():
            relatorio.write(f"{k:<5}{v[0]:<20}{v[1]:<20}{v[2]:<6}\n")


def add_coluna_porcentagem(dados_tratados, arm_servidor_gigas):
    tabela_porcentagem = {}
    for k, v in dados_tratados.items():
        tabela_porcentagem[k] = f"{bytes_para_gb(v) * 100 / arm_servidor_gigas:.2f}%"
    return tabela_porcentagem


usuarios = ler_arquivo_usuario()
usuarios = tratar_dados_usuario(usuarios)
arm_usuario = ler_arquivo_arm_usuario()
arm_usuario = tratar_dados_arm_usuario(arm_usuario)

tabela_porcentagem = add_coluna_porcentagem(arm_usuario, 25)
arm_usuario = converter_dados(arm_usuario)

tabela_final = mesclar_tabelas(usuarios, arm_usuario, tabela_porcentagem)

escrever_relatorio(tabela_final)




