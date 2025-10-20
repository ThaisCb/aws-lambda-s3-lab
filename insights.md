## ⚙️ Insights Técnicos — AWS Lambda + S3

### 1. Serverless na prática

O AWS Lambda permite executar código sob demanda, sem precisar gerenciar servidores.
A AWS é responsável por toda a infraestrutura — escalabilidade, disponibilidade e execução.
Na prática, isso reduz custo e simplifica o desenvolvimento, especialmente para tarefas event-driven.

Principais pontos:

Modelo baseado em eventos (executa apenas quando necessário).

Pagamento por execução, não por servidor ativo.

Escalabilidade automática.

---

### 2. Integração Lambda + S3

A integração entre Lambda e S3 é feita por eventos.
Quando um objeto é criado em um bucket (s3:ObjectCreated:*), a Lambda pode ser acionada automaticamente.
Esse tipo de automação é útil para processamento de arquivos, ETL, geração de thumbnails, notificações, etc.

Configuração via CloudFormation (resumo):

Definir o bucket S3 com permissões adequadas.

Criar a função Lambda com código Python ou Node.js.

Adicionar um evento NotificationConfiguration ligando o S3 à Lambda.

---

### 3. IAM Roles e permissões

´´A Lambda precisa de uma IAM Role para executar com segurança.
Essa role define o que a função pode (ou não) acessar dentro da AWS.


Políticas mínimas recomendadas:

Acesso ao S3:
````

"Action": ["s3:GetObject", "s3:PutObject"],
"Effect": "Allow",
"Resource": "arn:aws:s3:::nome-do-bucket/*"
````


Acesso ao CloudWatch Logs:
```

"Action": [
  "logs:CreateLogGroup",
  "logs:CreateLogStream",
  "logs:PutLogEvents"
]
```


### Boas práticas:

Aplicar o princípio de least privilege.

Evitar permissões globais (*).

Versionar as roles e policies junto com o código da função.

---

### 4. Infraestrutura como Código (IaC) com CloudFormation

O CloudFormation permite criar e gerenciar recursos AWS de forma automatizada, usando arquivos YAML.
Com ele, é possível versionar, replicar e atualizar ambientes com consistência.

---


### 5. Versionamento com Git

Durante o desenvolvimento, o Git é essencial para versionar o código e manter histórico de alterações.

Fluxo básico:
```

git add .
git commit -m "Configuração inicial da função Lambda e do template CloudFormation"
git push -u origin main
```



### Problemas comuns e soluções:

non-fast-forward → o repositório remoto tem commits que o local não possui.
➜ Solução: git pull origin main --allow-unrelated-histories.

index.lock → processo Git travado.
➜ Solução: remover o arquivo .git/index.lock.

---

### 6. Logs e Monitoramento com CloudWatch

Cada execução da Lambda gera logs automaticamente no CloudWatch.
Esses logs são fundamentais para depuração e análise de desempenho.



### Boas práticas:

Monitorar erros (ERROR) e tempos de execução (REPORT).

Criar métricas e alarmes personalizados.

Utilizar filtros de log para rastrear eventos específicos.

Comando útil (CLI):

aws logs tail /aws/lambda/nome-da-funcao --follow

---

### 7. Boas práticas de automação

Utilizar variáveis de ambiente na Lambda para configurar parâmetros.

Manter dependências no arquivo requirements.txt (Python) ou package.json (Node.js).

Automatizar a implantação com AWS CLI ou CloudFormation.

Testar localmente antes de fazer deploy na AWS.

Versionar todos os templates e funções no GitHub.
