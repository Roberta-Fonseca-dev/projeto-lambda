# 🚀 Executando Tarefas Automatizadas com AWS Lambda e S3

Este repositório contém a solução para o desafio **"Executando Tarefas Automatizadas com Lambda Function e S3"** da DIO.

## 📌 Objetivo
- Criar uma função **AWS Lambda** que processa arquivos enviados para um **bucket S3**.
- Automatizar a execução de tarefas sem necessidade de servidores dedicados.
- Documentar a prática e registrar aprendizados.

## 📂 Estrutura do Repositório
- `lambda_function.py` → Código da função Lambda em Python.
- `template.yaml` → Template CloudFormation para provisionar a infraestrutura (S3 + Lambda).
- `imagens/` → Evidências, anotações e insights sobre a prática.

## 🧠 Insights Anotados
- Lambda é ideal para tarefas event-driven (gatilho de eventos).
- Integração com S3 permite automação no upload de arquivos.
- Infraestrutura como código (IaC) facilita a reprodutibilidade.

## ▶️ Como Executar
1. Crie um bucket S3 no console da AWS ou via CloudFormation.
2. Faça o deploy da função Lambda com o código `lambda_function.py`.
3. Configure o gatilho do S3 para a Lambda.
4. Teste enviando um arquivo para o bucket.

---
📌 *Desafio concluído com documentação e boas práticas de versionamento.*
