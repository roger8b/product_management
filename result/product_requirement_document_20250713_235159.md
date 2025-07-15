# **Documento de Requisitos de Produto (PRD): Melhoria na Experiência de Rastreamento de Pacotes**

**Time:** Abstraction Layer - Plataforma
**Product Manager Técnico:** [Seu Nome/Nome Fictício]
**Data:** 13 de Julho de 2025
**Status:** Em Desenvolvimento (Fase de Especificação Detalhada e Execução)

---

### **1. Contexto**

Este documento detalha os requisitos para aprimorar a experiência de rastreamento de pacotes, focando na camada de abstração que serve as equipes de produto. O objetivo é fornecer dados de rastreamento normalizados, consolidados e de fácil consumo para que as equipes de front-end e mobile possam construir interfaces de usuário intuitivas.

#### **1.1. Oportunidade (O Problema, Para Qual Público e Por Quê)**

A atual experiência de rastreamento de pacotes é uma das maiores fontes de atrito para nossos clientes. A complexidade e a falta de clareza nas informações geram ansiedade e frustração, culminando em um alto volume de chamados de suporte.

*   **Problema:** Clientes têm dificuldade em obter informações claras e rápidas sobre o status de suas entregas, resultando em insatisfação e sobrecarga do suporte.
*   **Público Alvo:**
    *   **Clientes Finais:** Usuários que realizam compras e desejam rastrear suas encomendas de forma transparente.
    *   **Equipes de Produto (Consumidoras da API):** Desenvolvedores e Product Managers que precisam de acesso simplificado e padronizado aos dados de rastreamento para construir interfaces de usuário robustas.
    *   **Equipes de Suporte:** Profissionais que lidam diariamente com dúvidas sobre o status de entregas.
*   **Por Quê (Valor de Negócio):** Reduzir custos operacionais de suporte, aumentar a satisfação do cliente, melhorar a percepção da marca e fomentar a recompra.

#### **1.2. Evidências (Dados que Validam a Oportunidade)**

*   **75% dos tickets de suporte** estão diretamente relacionados a dúvidas sobre o status de entrega ("Onde está meu pacote?", "Qual o status da minha entrega?").
*   Feedback de clientes indica baixa satisfação com a clareza das informações de rastreamento.
*   Análise de jornada do cliente revela abandono em etapas pós-compra devido à incerteza da entrega.

#### **1.3. Métricas de Sucesso (KPIs Quantitativos e Qualitativos)**

As métricas a seguir serão monitoradas para avaliar o sucesso desta iniciativa:

*   **Primária:** Redução de, no mínimo, **80%** no volume de tickets de suporte relacionados a "Rastreamento/Entrega" nos 30 dias seguintes ao lançamento completo.
*   **Secundárias:**
    *   Aumento do **CSAT (Customer Satisfaction Score)** para a experiência de entrega.
    *   Aumento no número de usuários únicos que acessam a tela "Meus Pacotes" por semana, indicando maior engajamento e confiança na ferramenta.
    *   Melhora na percepção da marca em pesquisas de satisfação de clientes.
    *   Redução do tempo médio de resolução de tickets de rastreamento para o suporte.

---

### **2. Escopo da Solução (Para a Camada de Abstração)**

O time de Abstraction Layer será responsável por consolidar, normalizar e expor dados de rastreamento através de APIs performáticas e escaláveis, abstraindo a complexidade de múltiplas fontes e formatos.

#### **2.1. Requisitos Funcionais e Histórias de Usuário**

**Requisitos Funcionais da Camada de Abstração:**

1.  **Exposição de Lista de Pacotes (API de Visão Geral):**
    *   A camada de abstração deve fornecer um endpoint API que retorne uma lista consolidada de pacotes associados a um cliente (usuário autenticado), incluindo pedidos ativos e recém-concluídos.
    *   Para cada pacote na lista, a API deve expor os seguintes campos normalizados:
        *   `id_pacote`: Identificador único do pacote.
        *   `nome_pacote`: Nome simplificado do produto/encomenda (Ex: "Tênis Runner Pro").
        *   `id_pedido`: Código único do pedido associado.
        *   `data_compra`: Data em que o pedido foi efetuado.
        *   `ultimo_status_simplificado`: A atualização de rastreamento mais recente, em formato amigável e pré-definido (Ex: "Em trânsito", "Saiu para entrega", "Entregue").
        *   `status_detalhado_completo`: O status completo e original, conforme fornecido pela fonte de rastreamento (para casos de depuração ou exibição de mais detalhes pela interface).
        *   `codigo_rastreio`: O código de rastreio completo.
2.  **Exposição de Detalhes de Pacote (API de Histórico Detalhado):**
    *   A camada de abstração deve fornecer um endpoint API para um pacote específico, que retorne todas as informações da visão geral, além de detalhes completos.
    *   Os detalhes devem incluir:
        *   `endereco_entrega`: Endereço completo para onde o pacote está sendo enviado.
        *   `codigo_rastreio`: O código de rastreio completo.
        *   `historico_rastreamento`: Uma linha do tempo estruturada de eventos de rastreamento, ordenada do mais recente para o mais antigo. Cada evento deve conter:
            *   `data_hora`: Data e hora exatas do evento.
            *   `localizacao`: Descrição da localização (Ex: "Centro de Distribuição, Cajamar - SP").
            *   `status_detalhado`: O status exato da etapa (Ex: "Objeto postado", "Objeto em trânsito para a unidade de tratamento").
            *   `status_normalizado`: Versão simplificada do status detalhado, conforme mapeamento interno.
3.  **Normalização de Status:**
    *   A camada de abstração deve implementar um motor de normalização que converta os diferentes formatos e textos de status de diversas transportadoras e sistemas legados em um conjunto padronizado e simplificado de status. Este mapeamento deve ser configurável e expansível.
4.  **Agregação de Dados:**
    *   A camada de abstração deve ser capaz de coletar e agregar dados de rastreamento de múltiplas fontes internas (e.g., OMS - Order Management System, WMS - Warehouse Management System) e externas (e.g., APIs de transportadoras, sistemas legados de rastreamento).
5.  **Frescor e Consistência dos Dados:**
    *   A camada deve garantir que os dados de rastreamento sejam o mais frescos possível, implementando mecanismos de atualização periódica ou baseados em eventos (webhooks de transportadoras, se disponíveis).
    *   Deve-se manter a consistência entre as informações apresentadas, mesmo com múltiplas fontes.
6.  **Performance e Escalabilidade:**
    *   As APIs devem ser performáticas, com tempos de resposta otimizados, e capazes de escalar para suportar o volume esperado de requisições.
    *   Estratégias de cache e otimização de consultas devem ser consideradas.

**Histórias de Usuário (Refletindo o Consumidor da Abstração):**

*   **Como um desenvolvedor front-end**, eu quero consumir uma API de lista de pacotes que me forneça o `id_pacote`, `nome_pacote`, `id_pedido`, `data_compra`, e o `ultimo_status_simplificado`, para que eu possa exibir rapidamente uma visão geral para o cliente.
*   **Como um desenvolvedor front-end**, eu quero consumir uma API de detalhes de pacote que me retorne o `endereco_entrega`, `codigo_rastreio`, e um `historico_rastreamento` estruturado e ordenado por data/hora, para que eu possa expandir a visualização com informações completas sem carregar uma nova página.
*   **Como uma equipe de produto**, queremos que a camada de abstração normalize os status de rastreamento de diferentes transportadoras para um conjunto fixo e compreensível, para que nossa interface de usuário seja consistente e fácil de entender.
*   **Como uma equipe de engenharia**, precisamos que a API de rastreamento seja confiável e performática, capaz de lidar com picos de acesso sem degradação, para garantir uma boa experiência ao usuário final.

#### **2.2. O que está Fora de Escopo (Para a Camada de Abstração)**

*   **Desenvolvimento da Interface do Usuário (UI) Final:** A construção da tela "Meus Pacotes" (layout, componentes visuais, interações visuais como a expansão "sem carregar nova página") é responsabilidade das equipes de produto que consomem nossa API. Nosso papel é fornecer os dados para habilitar essa UI.
*   **Criação de Novas Integrações com Transportadoras Específicas:** O foco inicial é abstrair as fontes de dados *existentes*. Novas integrações com transportadoras não conectadas à nossa plataforma principal serão consideradas como projetos separados, uma vez que a camada de abstração esteja robusta.
*   **Sistemas de Notificação Proativos (Push, E-mail, SMS):** Embora a camada de abstração possa eventualmente expor eventos de mudança de status, a lógica de envio de notificações para os clientes é de responsabilidade de um time ou serviço dedicado a notificações, que consumiria nossos dados.
*   **Funcionalidades de Suporte Integradas na UI:** Botões "Abrir um ticket" ou "Falar com suporte" diretamente na tela de rastreamento.
*   **Personalização Avançada da Experiência do Usuário:** Como regras complexas de personalização da visualização de pacotes para diferentes perfis de usuário, além do que os dados brutos ou normalizados da API permitem.

---

### **3. Design e Experiência (Foco na API e Modelo de Dados)**

Embora o design da UI seja responsabilidade da equipe de produto-cliente, a arquitetura de nossa API e a estrutura dos dados que ela expõe são cruciais para habilitar a experiência desejada.

#### **3.1. Fluxo da Experiência do Usuário (Habilitado pela API)**

1.  **Acesso à Tela "Meus Pacotes":** A equipe de produto front-end faz uma requisição `GET` para a API de lista de pacotes da Abstraction Layer.
2.  **Visualização da Lista:** A Abstraction Layer retorna uma lista de pacotes, cada um com `id_pacote`, `nome_pacote`, `id_pedido`, `data_compra`, e o `ultimo_status_simplificado`.
3.  **Seleção de um Pacote:** Quando o cliente clica em um item da lista, a equipe de produto front-end faz uma nova requisição `GET` para a API de detalhes de pacote, utilizando o `id_pacote`.
4.  **Expansão da Visualização Detalhada:** A Abstraction Layer retorna os detalhes completos do pacote, incluindo `endereco_entrega`, `codigo_rastreio` e o `historico_rastreamento` estruturado. A equipe de produto front-end renderiza essas informações na mesma página, expandindo a visualização.
5.  **Cópia do Código de Rastreio:** O campo `codigo_rastreio` é facilmente acessível para ser copiado via interface.
6.  **Visualização do Histórico:** O `historico_rastreamento` é exibido como uma linha do tempo clara, com `data_hora`, `localizacao` e `status_detalhado`/`status_normalizado`.

#### **3.2. Protótipos e Design Final (Foco no Modelo de Dados e Contrato da API)**

*   **Modelo de Dados da API (Exemplo):**
    ```json
    // GET /api/v1/orders/{user_id}/packages
    [
      {
        "id_pacote": "PACK12345",
        "nome_pacote": "Tênis Runner Pro",
        "id_pedido": "PED987654",
        "data_compra": "2025-07-10T10:00:00Z",
        "ultimo_status_simplificado": "Em trânsito",
        "status_detalhado_completo": "Objeto em trânsito - unidade de tratamento, Sao Paulo / SP",
        "codigo_rastreio": "AA123456789BR"
      },
      // ... outros pacotes
    ]

    // GET /api/v1/packages/{package_id}/tracking
    {
      "id_pacote": "PACK12345",
      "nome_pacote": "Tênis Runner Pro",
      "id_pedido": "PED987654",
      "data_compra": "2025-07-10T10:00:00Z",
      "ultimo_status_simplificado": "Em trânsito",
      "status_detalhado_completo": "Objeto em trânsito - unidade de tratamento, Sao Paulo / SP",
      "codigo_rastreio": "AA123456789BR",
      "endereco_entrega": "Rua Exemplo, 123, Bairro Centro, Cidade - UF, CEP 12345-678",
      "historico_rastreamento": [
        {
          "data_hora": "2025-07-13T09:30:00Z",
          "localizacao": "Centro de Distribuição, Cajamar - SP",
          "status_detalhado": "Objeto em trânsito para a unidade de tratamento",
          "status_normalizado": "Em trânsito"
        },
        {
          "data_hora": "2025-07-12T18:00:00Z",
          "localizacao": "Unidade de Tratamento, Sao Paulo - SP",
          "status_detalhado": "Objeto recebido na unidade de tratamento",
          "status_normalizado": "Em trânsito"
        },
        // ... eventos anteriores
      ]
    }
    ```
*   **Protótipos de Interface:** (A serem fornecidos pela equipe de Design e UX, consumindo nossa API. Este PRD foca no *contrato* de dados que habilita esses protótipos).

---

### **4. Detalhes de Execução**

#### **4.1. Implicações Técnicas e Dependências (Para a Camada de Abstração)**

*   **Integração com Fontes de Dados:**
    *   Necessidade de integração robusta com o **Sistema de Gerenciamento de Pedidos (OMS)** para obter a lista de pedidos e dados básicos do pacote.
    *   Integração com **APIs de Transportadoras Externas** (Correios, JadLog, Loggi, etc.) para obter o histórico de rastreamento.
    *   Integração com **Sistemas Legados de Rastreamento Internos** (se houver) para pacotes específicos ou fases iniciais da cadeia logística.
*   **Motor de Normalização de Status:**
    *   Desenvolvimento de um serviço/componente dedicado para mapear e traduzir status brutos em um conjunto finito e padronizado de `ultimo_status_simplificado` e `status_normalizado`. Este motor deve ser flexível para adição/ajuste de regras.
*   **Persistência de Dados (Opcional, mas Recomendado):**
    *   Considerar o armazenamento em cache ou persistência de dados de rastreamento frequente para otimizar performance e reduzir chamadas a sistemas legados/externos. Estratégias de TTL (Time-To-Live) e invalidade de cache serão cruciais.
*   **Design de APIs (RESTful/GraphQL):**
    *   Definição de contratos de API claros, versionamento e documentação (Swagger/OpenAPI).
    *   Implementação de autenticação e autorização para o consumo das APIs.
*   **Monitoramento e Observabilidade:**
    *   Implementação de métricas para latência da API, taxa de sucesso/erro, volume de requisições, e tempo de processamento de cada etapa da pipeline de agregação.
    *   Logging detalhado para rastreamento de eventos e depuração.
*   **Escalabilidade e Resiliência:**
    *   Arquitetura de microsserviços para permitir escalabilidade horizontal.
    *   Mecanismos de circuit breaker e retries para lidar com falhas de sistemas dependentes (transportadoras, legados).
    *   Estratégia de tratamento de volumes de dados e picos de acesso.
*   **Governança de Dados:**
    *   Definição clara de quem é o proprietário dos dados de rastreamento em cada etapa e como a qualidade dos dados é assegurada.

#### **4.2. Plano de Lançamento (Go-to-Market)**

*   **Fase 1: Teste Interno (Alpha/Beta Privado):**
    *   Lançamento da nova API e serviços para equipes de desenvolvimento internas e alguns usuários "beta testers" selecionados. Coleta de feedback técnico e funcional.
*   **Fase 2: Lançamento Controlado (Rollout em %):**
    *   Liberação gradual para uma porcentagem da base de usuários (Ex: 5%, 10%, 25%) em conjunto com o time de produto que está implementando a nova UI. Monitoramento de métricas e performance em tempo real.
*   **Fase 3: Lançamento Completo:**
    *   Disponibilização da nova experiência para 100% dos usuários.
*   **Comunicação e Treinamento:**
    *   Alinhamento com equipes de Suporte ao Cliente para treinamento sobre a nova experiência e dados disponíveis.
    *   Comunicação interna para outras equipes sobre o lançamento e suas capacidades.
    *   Plano de comunicação para clientes (se aplicável), informando sobre a melhoria.

#### **4.3. Plano de Desenvolvimento (Marcos Principais)**

*   **Mês 1-2: Descoberta e Planejamento Técnico:**
    *   Refinamento do contrato da API (especificação OpenAPI/Swagger).
    *   Mapeamento detalhado das fontes de dados existentes e seus desafios.
    *   Definição da arquitetura e tecnologia para o motor de normalização.
    *   Início da integração com o OMS.
*   **Mês 2-3: Desenvolvimento Core:**
    *   Implementação da API de "lista de pacotes" (MVP de dados).
    *   Desenvolvimento do motor de normalização de status (primeira versão com status-chave).
    *   Integração com a primeira transportadora principal.
*   **Mês 3-4: Refinamento e Expansão:**
    *   Implementação da API de "detalhes de pacote" e histórico completo.
    *   Integração com transportadoras adicionais e sistemas legados críticos.
    *   Testes de performance e carga.
    *   Início dos testes de integração com a equipe de produto front-end.
*   **Mês 4-5: Testes Finais e Preparação para Lançamento:**
    *   Refinamento do mapeamento de status e regras.
    *   Testes de ponta a ponta (end-to-end) com as interfaces de usuário construídas.
    *   Implementação de monitoramento e alertas.
    *   Desenvolvimento de planos de rollback.
*   **Mês 5+: Lançamento e Iteração:**
    *   Execução do plano de lançamento.
    *   Monitoramento pós-lançamento, coleta de feedback e iterações para otimização contínua.

---

### **5. Riscos**

#### **5.1. Suposições a serem Testadas e Riscos em Aberto**

*   **Qualidade e Consistência dos Dados de Origem:**
    *   *Risco:* Dados incompletos ou inconsistentes dos sistemas legados ou de APIs de transportadoras podem impactar a qualidade da informação exibida, levando a uma experiência ruim apesar da nossa abstração.
    *   *Mitigação:* Investir em monitoramento da qualidade dos dados nas fontes. Desenvolver regras de validação e tratamento de erros na camada de abstração.
*   **Latência e Confiabilidade de APIs Externas:**
    *   *Risco:* Dependência de APIs de terceiros (transportadoras) que podem ter latência elevada, baixa disponibilidade ou limites de requisição, afetando a performance e confiabilidade do nosso serviço.
    *   *Mitigação:* Implementar caching agressivo. Utilizar padrões de resiliência (circuit breaker, retries com backoff exponencial). Negociar SLAs com transportadoras.
*   **Complexidade e Manutenção do Mapeamento de Status:**
    *   *Risco:* A diversidade de status entre transportadoras pode tornar o motor de normalização complexo de desenvolver e manter, especialmente com a introdução de novas transportadoras ou mudanças nos status existentes.
    *   *Mitigação:* Desenvolver uma ferramenta de configuração para o mapeamento de status. Priorizar os status mais comuns e importantes. Envolver especialistas de negócio no processo de definição dos status normalizados.
*   **Escalabilidade do Histórico de Rastreamento:**
    *   *Risco:* O volume de eventos de rastreamento pode ser muito grande para armazenar e consultar de forma eficiente para todos os pacotes.
    *   *Mitigação:* Otimizar esquema de banco de dados. Implementar particionamento de dados. Avaliar a necessidade de purgar dados muito antigos ou agregá-los.
*   **Alinhamento e Dependência com Equipes de Produto Consumidoras:**
    *   *Risco:* A equipe de produto front-end pode ter necessidades específicas de UI que não são totalmente atendidas pelos contratos iniciais da API, ou pode haver atrasos na implementação da UI que impactem o ROI da nossa entrega.
    *   *Mitigação:* Colaboração contínua com as equipes de produto desde o início (durante a especificação da API). Feedback loops frequentes. Comunicação clara sobre dependências e prazos.
*   **Scope Creep:**
    *   *Risco:* Pedidos para adicionar funcionalidades que vão além da abstração de dados (ex: cálculo de frete na API de rastreamento, sugestão de próxima ação para o usuário) que desviam o foco da equipe.
    *   *Mitigação:* Reafirmar o escopo da camada de abstração e direcionar novas necessidades para outras equipes ou como próximas iterações separadas. Manter o foco no problema principal de clareza do rastreamento.