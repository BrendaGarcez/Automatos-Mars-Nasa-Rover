class CuriosityAutomato:
    def __init__(self):
        self.estado_atual = 'descida_mardi'
        self.estados_finais = {'transmissao'}
        
        self.transicoes = {
            ('descida_mardi', 'tocar_solo'): 'superficie',
            ('superficie', 'medir_clima'): 'clima',
            ('clima', 'medir_radiacao'): 'radiacao',
            ('radiacao', 'medir_hidrogenio'): 'subsolo',
            
            ('subsolo', 'enviar_terra'): 'transmissao',
            
            ('subsolo', 'iniciar_deslocamento'): 'navegacao',
            ('navegacao', 'chegar_alvo'): 'alvo_atingido',
            ('alvo_atingido', 'ativar_chemcam'): 'laser_chemcam',
            
           
            ('laser_chemcam', 'analisar_superficie'): 'mahli',
            ('mahli', 'ativar_camera'): 'apxs',
            
            ('apxs', 'iniciar_perfuracao'): 'perfuracao',
            ('perfuracao', 'coletar_po'): 'coleta',
            ('coleta', 'analisar_chemin'): 'chemin',
            ('chemin', 'inserir_forno_sam'): 'aquecimento_sam',
            ('aquecimento_sam', 'analisar_sam'): 'analise_sam',
            ('analise_sam', 'enviar_terra'): 'transmissao',
            
            ('transmissao', 'reiniciar_ciclo'): 'superficie'
        }

    def processar_fita(self, fita):
        print("-" * 50)
        print(f"Iniciando processamento da fita ({len(fita)} comandos)...")
        print("-" * 50)
        
        for simbolo in fita:
            chave = (self.estado_atual, simbolo)
            if chave in self.transicoes:
                novo_estado = self.transicoes[chave]
                print(f"({self.estado_atual}, {simbolo}) -> {novo_estado}")
                self.estado_atual = novo_estado
            else:
                print(f"({self.estado_atual}, {simbolo}) -> TRANSIÇÃO INVÁLIDA")
                return False
        
        aceito = self.estado_atual in self.estados_finais
        print("=" * 50)
        print(f"ESTADO FINAL: {self.estado_atual}")
        print(f"RESULTADO: {'PALAVRA ACEITA' if aceito else 'PALAVRA REJEITADA'}")
        print("=" * 50, "\n")
        return aceito

robo = CuriosityAutomato()

fita_teste_valido = [
    'tocar_solo', 'medir_clima', 'medir_radiacao', 'medir_hidrogenio',
    'iniciar_deslocamento', 'chegar_alvo', 'ativar_chemcam', 'analisar_superficie',
    'ativar_camera', 'iniciar_perfuracao', 'coletar_po', 'analisar_chemin', 
    'inserir_forno_sam', 'analisar_sam', 'enviar_terra'
]

fita_teste_invalido = [
    'tocar_solo', 'medir_clima', 'medir_radiacao', 'medir_hidrogenio',
    'iniciar_deslocamento', 'chegar_alvo', 'inserir_forno_sam'
]

print("\n--- INICIANDO TESTE VÁLIDO ---")
robo.processar_fita(fita_teste_valido)

print("\n--- INICIANDO TESTE INVÁLIDO ---")
robo2 = CuriosityAutomato()
robo2.processar_fita(fita_teste_invalido)