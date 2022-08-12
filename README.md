# Sistema Hermes
Sistema que auxilia investidores da Bolsa de Valores.

O nome "Hermes" foi escolhido pelo ato de Hermes ser o deus grego do comércio e mensageiro dos deuses. Como o sistema é voltado para a bolsa de valores e envia informações, recebeu esse nome.

Sistema desenvolvido em um ambiente WSL, utilizando a distro ubuntu 20.04

# Instruções
Seguem as instruções para a utilização do sistema
## E-mail
Na pasta ```hermes/hermes``` crie um arquivo ```info_email.py``` e o preencha da seguinte forma:
```py
usuario = 'email_para_envio_de_notificacoes @ gmaill.com'
senha = 'senha_do_email
```

Para cadastrar novos emails para receber notificações, acesse a página ```mensageiro/cadastro```

## Execução
Na pasta raiz execute o comando ```pip3 install -r requirements.txt``` e depois ```sudo apt install redis-server```

Para rodar o sistema com todas as funcionalidades, abra 4 abas diferentes do terminal e execute os seguintes comandos em cada uma, em ordem:
```console
cd hermes/ && python3 manage.py runserver
redis-server
celery -A hermes worker --pool=solo -l INFO
celery -A hermes beat -l INFO
```

# Outras informações
## Tarefa automáticas
No arquivo ```hermes/hermes/tasks.py``` estão connfiguradas as tarefas realizadas de forma automática pelo sistema

## API
A API utilizada apenas recupera informações de pregões já fechados, ou seja, o valor obtido de um ativo só mudará no dia seguinte. Devido a isso, o itervalo de connsulta é definido em dias.
Informações extras sobre a API podem ser adquiridas em https://www.okanebox.com.br/como-usar/api-de-acoes-empresas-bovespa/

## Lista de Ativos
A lista de ativos presentes na B3 foi retirada de https://www.infomoney.com.br/cotacoes/empresas-b3/. O texto foi copiado, inserido em uma planilha no Google Planilhas, exportada para csv e por fim os dados oram tratados em um Notebook Jupyter, disponível, com outros arquivos, na pasta ```/base_dados/```

## URLs
As urls da aplicação cotacao são acessadas diretamente. Já as da mensageiro precisam de 'mensageiro/' antes. 

## Imagens
Existem duas imagens na pasta raiz: a modelagem do bando de dados, feita em dbdiagram.io e o logo do sistema, feito com o LibreSprite, disponível em https://github.com/LibreSprite/LibreSprite
