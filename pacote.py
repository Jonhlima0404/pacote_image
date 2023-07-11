import seu_pacote_de_processamento_de_imagens

# Obter os módulos presentes no pacote
modulos = dir(seu_pacote_de_processamento_de_imagens)
print("Módulos do pacote:")
print(modulos)

# Iterar sobre os módulos e obter informações sobre as classes e funções
for modulo in modulos:
    # Obter as classes presentes no módulo
    if hasattr(seu_pacote_de_processamento_de_imagens, modulo) and \
            isinstance(getattr(seu_pacote_de_processamento_de_imagens, modulo), type):
        classes = dir(getattr(seu_pacote_de_processamento_de_imagens, modulo))
        print(f"\nClasses do módulo {modulo}:")
        print(classes)

        # Obter as funções presentes no módulo
        for classe in classes:
            if callable(getattr(getattr(seu_pacote_de_processamento_de_imagens, modulo), classe)):
                funcoes = dir(getattr(getattr(seu_pacote_de_processamento_de_imagens, modulo), classe))
                print(f"\nFunções da classe {classe}:")
                print(funcoes)
