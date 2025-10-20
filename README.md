# ☁️ AWS Lambda + S3 — Laboratório Prático

Este projeto foi desenvolvido como um **laboratório prático de automação em nuvem**, aplicando os conceitos de **Serverless Computing** na AWS.  
O objetivo é criar e gerenciar recursos de forma automatizada utilizando **AWS Lambda** e **Amazon S3**, explorando também a automação por **AWS CloudFormation**.

---

## 🎯 Objetivo do Projeto

Consolidar o entendimento de como funções Lambda podem ser acionadas automaticamente a partir de eventos no S3, automatizando fluxos de processamento em nuvem.  
Durante o laboratório, são aplicados conceitos fundamentais de **Infraestrutura como Código (IaC)** e **automação de deploys**.

---


## ⚙️ Funcionalidades

- Criação automática de **bucket S3**  
- Função **AWS Lambda** acionada por eventos `s3:ObjectCreated:*`  
- Permissões configuradas via **IAM Role**  
- Deploy completo via **CloudFormation template**  

---

## 🚀 Passo a Passo — Execução

### 1️⃣ Criar o Bucket e a Função Lambda (CloudFormation)
No terminal (AWS CLI configurado):

```bash
aws cloudformation create-stack \
  --stack-name lambda-s3-lab \
  --template-body file://templates/lambda-s3-template.yaml \
  --capabilities CAPABILITY_IAM
````
Isso criará o bucket, a função Lambda e a role necessária para execução.

---

### 2️⃣ Verificar o Deploy
```
aws cloudformation describe-stacks --stack-name lambda-s3-lab
```

---


### 3️⃣ Testar o Funcionamento

Vá até o console S3.

Faça o upload de qualquer arquivo no bucket criado.

No CloudWatch Logs, verifique que a Lambda foi acionada automaticamente.


---





---

### 🪶 Tecnologias Utilizadas

AWS Lambda

Amazon S3

AWS CloudFormation

Python 3.12

AWS CLI

---


### 🧩 Próximos Passos

Adicionar triggers mais complexas (como eventos DynamoDB ou SNS).

Configurar deploy automatizado via AWS SAM ou Terraform.

Implementar um pipeline CI/CD no GitHub Actions.

---

## Conclusão

A execução deste projeto permitiu compreender a importância de eventos e triggers entre serviços AWS, bem como a aplicação prática de boas práticas de IAM, CloudFormation e monitoramento. Automatizar processos reduz erros, aumenta a eficiência e prepara o caminho para arquiteturas mais complexas e escaláveis.





