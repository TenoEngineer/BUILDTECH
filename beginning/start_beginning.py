# FIXAR PASTA DA BUILDTECH COMO PADRÃO PARA ABRIR OUTRAS PASTAS
# ABRIR TODOS ARQUIVOS .dwg
# RODAR O SCRIPT PADRÃO EM TODOS
# COLAR OS BLOCOS
# TAREFA MANUAL DE RECONHECER SE É RGE OU CEEE
# SE FOR RGE É NECESSÁRIO AVALIAR SE É RURAL OU URBANO
# ANALISAR SE PRECISA IMPLEMENTAR ALGUM POSTE
# SE FOR CEEE É SÓ RODAR O SCRPIT NEWETN
# FECHAR ARQUIVO
# APÓS FECHAR OS ARQUIVOS
# FAZER UMA CÓPIA DE TODOS ARQUIVOS .dwg QUE NÃO CONTENHAM A PALAVRA "PERFIL"
# ABRIR TODAS ESSAS CÓPIAS
# APÓS ISSO É MANUAL EM RODAR OS SCRIPTS E DEPOIS OS CRUZAMENTOS
# FEITO ISSO DA PRA GERAR OUTRA AUTOMAÇÃO QUE VAI ABRIR OS ARQUIVOS DE AUTOMAÇÃO NO EXCEL
# INPUTAR OS ARQUIVOS NO VBA E RODAS TODOS ELES UM POR UM EM CADA AUTOMAÇÃO E PULAR QUANDO NÃO TIVER PARA AUTOMATIZAR
# RODAR ABRIS OS AUTOCAD DE NOVO E RODAS OS SCRIPTS DELES

taqi = os.path.join((os.path.dirname(sys.argv[0])), taqi_png)
acesso = py.locateOnScreen(taqi, grayscale=True, confidence=0.9)
