
# 4 areasrelacionadas ao GIT - repositorio de versionamento
#untracked - arquivo que não esta mapeado pelo git.
#unmodified - arquivo ja mapeado mas não foi modificado
#Modified - arquivo modificado
# Staged - Arquivo preparado para fazer o commit

# adionada nova linha
# git status verifica o status do arquivo
# fica na barra de preparado
# git add .\ nome do arquivo ( pressioana tab para autocompletar) ( coloca o arquivo na area de stage)
# adiciona no repositorio a modificação.
# git commit -m "comentario suscinto do que foi feito"
#
#
#git diff - verifica o que aconteceu no arquivo 
# 
# git log - mostra o historico do arquivo. aperta q para sair
# 
# git restore nome do arquivo
# git restore --staged nome_do_arquivo ,  faz com que o arquivo ao inves de voltar ao que foi feito antes só 
# volta da area de staged para a area de changes #
# 
<<<<<<< Updated upstream
# git remote - visualiza o local do arquivo onde ele se encontra
# git push - vem apos o commit. ele envia tudo para o repositorio online do github 
# git push "origin que é o repositorio remoto" e o "main" ou "master" que é o nosso local. 
# git push  - ele traz modiicações feitas no github online para o seu arquivo e "merge" tudo junto.
# 
# git fetch - ele diferente do git pull ele traz a informação antes. dai voc pode usar o git diff para ver a diferenças
# e depois usar o git pull pra juntar os arquivos caso esteja coerente.
=======
# git remote - antes para acessar o repositorio remoto
# git push - vem apos o commit. ele envia tudo para o repositorio online do github 

# git pull  - ele traz modiicações feitas no github online para o seu arquivo e "merge" tudo junto.
# 
>>>>>>> Stashed changes
