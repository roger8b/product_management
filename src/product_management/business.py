# -*- coding: utf-8 -*-

"""
Este módulo contém a string com a descrição do problema (pedido de produto)
para ser importada e utilizada em outros scripts.
"""

problem = """
Pedido de criação de POC da plataforma: Abstraction Layer Primeiros passos

Contexto:
A camada de abstração é uma solução que visa simplificar a interação com sistemas complexos, permitindo que desenvolvedores e usuários finais acessem funcionalidades avançadas sem a necessidade de compreender todos os detalhes técnicos subjacentes. 
A POC (Prova de Conceito) tem como objetivo demonstrar a viabilidade e os benefícios dessa abordagem.

No momento estamos no dia zero da equipe, por isso precisamos entender se temos tudo o que precisamos para começar a criar a nossa camada de abstração.

Objetivo:
Criar uma POC que demonstre como a camada de abstração pode ser implementada e utilizada em um cenário real, destacando suas vantagens e funcionalidades principais. Alem disso a poc deve ser utilizada para validar:
- A viabilidade técnica da camada de abstração.
- Uso da plataforma Andes para setup inicial do projeto, pois essa plataforma tem a função de facilitar a vida do desenvolvedor gerando boilerplate e configurando o ambiente de desenvolvimento.
- Validar a nossa arquiteutura inicial.

"""

problem = """
# **Pedido de Produto: Melhoria na Experiência de Rastreamento de Pacotes**

**Iniciativa:** Rastreamento Transparente

**Product Manager:** (Nome do PM Fictício)

**Data:** 13/07/2025

### **1. Contexto e Problema (O Porquê)**

Após um processo de *Discovery*, identificamos que uma das maiores fontes de atrito na jornada do nosso cliente está na falta de clareza sobre o andamento de suas entregas. Atualmente, o processo para consultar o status de um pacote é complexo e as informações são apresentadas de forma pouco intuitiva.

**Dados Relevantes:**

* **Causa Raiz:** Cerca de **75% dos nossos tickets** de suporte estão relacionados a dúvidas sobre entrega ("Onde está meu pacote?", "Qual o status da minha entrega?").

* **Impacto no Negócio:** Além do custo operacional com o time de suporte, essa fricção gera ansiedade no cliente, impactando negativamente a percepção da nossa marca e a chance de recompra.

**Objetivo Principal:**
Reduzir em, no mínimo, **80%** o volume de reclamações e tickets de suporte relacionados ao status de encomendas, melhorando a experiência do usuário e a confiança em nosso serviço.

### **2. Solução Proposta (O Quê)**

Propomos a reestruturação da tela "Meus Pacotes" para oferecer uma experiência de rastreamento proativa e centralizada. A ideia é que o cliente tenha acesso rápido às informações mais importantes sem esforço, em duas camadas de visualização.

#### **2.1. Visão Geral (Lista de Pacotes)**

Ao acessar a tela "Meus Pacotes", o cliente deve visualizar imediatamente uma lista com todas as suas encomendas ativas e recém-concluídas.

**Campos Visíveis na Lista:**

* **Pacote:** Identificador principal do produto ou da encomenda (Ex: "Tênis Runner Pro").

* **Nº do Pedido:** Código único do pedido para referência.

* **Data da Compra:** Data em que o pedido foi efetuado.

* **Último Status:** A atualização mais recente e simplificada do rastreamento (Ex: "Em trânsito", "Saiu para entrega", "Entregue").

#### **2.2. Visão Detalhada (Detalhes do Pacote)**

Ao clicar em um item da lista, a tela deve, **sem carregar uma nova página**, expandir a visualização daquele pacote, revelando informações completas.

**Campos Visíveis no Detalhe:**

* Todas as informações da visão geral.

* **Endereço de Entrega:** Para onde o pacote está sendo enviado.

* **Código de Rastreio:** O código completo, com um botão para copiar.

* **Histórico de Rastreamento:** Uma linha do tempo vertical, clara e visual, mostrando cada etapa do processo de entrega, da mais recente para a mais antiga. Cada etapa deve conter:

  * **Data e Hora**

  * **Localização** (Ex: "Centro de Distribuição, Cajamar - SP")

  * **Status Detalhado** (Ex: "Objeto postado", "Objeto em trânsito para a unidade de tratamento", "Objeto saiu para entrega ao destinatário").

### **3. Impacto Esperado e Métricas de Sucesso**

* **Métrica Primária:** Redução de tickets de suporte com o tema "Rastreamento/Entrega" em ≥ 80% após 30 dias do lançamento.

* **Métrica Secundária:** Aumento do CSAT (Customer Satisfaction Score) relacionado à experiência de entrega.

* **Métrica de Engajamento:** Aumento no número de usuários únicos que acessam a tela "Meus Pacotes" por semana.
"""

# Para usar este módulo em outro arquivo:
# from nome_deste_arquivo import problem
# print(problem)
