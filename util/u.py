import pandas as pd

def retornaDadoParaInsert(dir):
    df = open(dir,"r")
    dados = df.read()
    return dados


def ler_xlsx_e_gerar_tuples(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo .xlsx e gera um novo arquivo com tuplas no formato desejado.
    
    Args:
        arquivo_entrada (str): Caminho do arquivo .xlsx de entrada.
        arquivo_saida (str): Caminho do arquivo de saída (.txt ou .csv).
    """
    try:
        # Lê o arquivo Excel
        df = pd.read_excel(arquivo_entrada)
        
        # Converte cada linha em uma tupla
        tuplas = [tuple(row) for row in df.values]
        
        # Salva as tuplas no formato desejado
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for i, tupla in enumerate(tuplas):
                if i < len(tuplas) - 1:  # Adiciona vírgula se não for a última linha
                    f.write(f"{tupla},\n")
                else:  # Última linha sem vírgula
                    f.write(f"{tupla}\n")
                    
        print(f"Arquivo gerado com sucesso: {arquivo_saida}")
        return retornaDadoParaInsert(arquivo_saida)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None
        
        

    