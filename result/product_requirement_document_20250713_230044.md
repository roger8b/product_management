**Documento de Requisitos de Produto (PRD)**

**Título:** Melhoria na Experiência de Rastreamento de Pacotes - Capacidades da Camada de Abstração

**Iniciativa:** Rastreamento Transparente

**Product Manager (Negócio):** (Nome do PM Fictício)
**Product Manager (Plataforma Abstraction Layer):** [Seu Nome/Nome da Equipe]

**Data:** 15/07/2025 (Assumindo data atual para o PRD)
**Versão:** 1.0 (MVP)

---

### **1. Contexto**

Este PRD detalha as capacidades necessárias da **Camada de Abstração (Abstraction Layer)** para viabilizar a iniciativa de "Rastreamento Transparente", proposta pela equipe de produto de negócio. Nosso papel é fornecer uma API unificada, escalável e resiliente que abstraia a complexidade das diversas fontes de dados de rastreamento, permitindo que as equipes de produto construam interfaces de usuário superiores e reduzam o atrito na jornada do cliente.

#### **1.1. Oportunidade**

*   **Problema a ser resolvido:** A principal dor do cliente reside na falta de clareza e complexidade do processo atual para consultar o status de suas entregas. Isso se traduz em alta ansiedade, percepção negativa da marca e sobrecarga do suporte ao cliente.
*   **Para qual público:** Principalmente, os **clientes finais** que realizam compras em nossa plataforma e aguardam suas entregas. Secundariamente, as **equipes de suporte** internas que atualmente despendem grande parte do seu tempo respondendo a dúvidas de rastreamento, e as **equipes de produto frontend** que precisam de dados de rastreamento padronizados e fáceis de consumir.
*   **Por quê:** Resolver este problema impactará diretamente a satisfação do cliente, reduzindo custos operacionais com suporte e aumentando a confiança na marca, o que pode levar a um aumento da recompra.

#### **1.2. Evidências**

*   **Causa Raiz:** **75% dos tickets de suporte** estão relacionados a dúvidas sobre entrega ("Onde está meu pacote?", "Qual o status da minha entrega?").
*   **Impacto no Negócio:** Além do custo operacional do suporte, a fricção gera ansiedade no cliente, impactando negativamente a percepção da marca e a chance de recompra. A falta de transparência é um fator de desistência e frustração significativo.

#### **1.3. Métricas de Sucesso**

As métricas de sucesso para a iniciativa geral são:

*   **Métrica Primária:** Redução de tickets de suporte com o tema "Rastreamento/Entrega" em ≥ 80% após 30 dias do lançamento. (Métrica de Negócio)
*   **Métrica Secundária:** Aumento do CSAT (Customer Satisfaction Score) relacionado à experiência de entrega. (Métrica de Negócio)
*   **Métrica de Engajamento:** Aumento no número de usuários únicos que acessam a tela "Meus Pacotes" por semana. (Métrica de Produto)

Para a Camada de Abstração, contribuiremos para estas métricas através de:

*   **Disponibilidade e Latência da API:** >99.9% de uptime, latência média de resposta <200ms para consultas de rastreamento.
*   **Qualidade e Consistência dos Dados:** Taxa de sucesso na normalização de status >95%. Redução de inconsistências percebidas no status do pacote.
*   **Escalabilidade:** Suporte a um volume X de requisições por segundo, com projeção de crescimento de Y%.

### **2. Escopo da Solução (Camada de Abstração)**

O objetivo da Camada de Abstração é consolidar e normalizar dados de rastreamento de diversas fontes (transportadoras, sistemas legados) e expô-los através de uma API consistente e performática. Esta API permitirá que a equipe de produto de negócio construa a experiência de usuário proposta na tela "Meus Pacotes".

#### **2.1. Requisitos Funcionais e Histórias de Usuário**

As histórias de usuário a seguir são do ponto de vista do consumidor da nossa API (equipes de produto frontend), traduzidas para as capacidades que a Abstraction Layer deve fornecer:

*   **HU 1: Obtenção da Lista Resumida de Pacotes**
    *   **Como** uma equipe de produto frontend, **eu quero** uma API para obter uma lista de todos os pacotes ativos e recém-concluídos de um determinado cliente, **para que** eu possa exibir rapidamente uma visão geral na tela "Meus Pacotes".
    *   **Requisito de Plataforma:** A API deve expor um endpoint que, dado um `user_id`, retorne uma lista de objetos `Pacote`, contendo os seguintes campos:
        *   `id_pacote`: Identificador único do pacote na plataforma.
        *   `identificador_produto`: Nome ou descrição principal do item (ex: "Tênis Runner Pro").
        *   `numero_pedido`: Código único do pedido associado.
        *   `data_compra`: Data em que o pedido foi efetuado.
        *   `ultimo_status_simplificado`: A atualização mais recente do rastreamento, normalizada para um conjunto predefinido de estados (e.g., "Em trânsito", "Saiu para entrega", "Entregue", "Aguardando postagem", "Problema na entrega").

*   **HU 2: Obtenção do Detalhe Completo do Pacote**
    *   **Como** uma equipe de produto frontend, **eu quero** uma API para obter os detalhes completos de um pacote específico, **para que** eu possa expandir a visualização na tela "Meus Pacotes" sem recarregar a página.
    *   **Requisito de Plataforma:** A API deve expor um endpoint que, dado um `id_pacote`, retorne um objeto `DetalhePacote`, contendo:
        *   Todos os campos da `HU 1`.
        *   `endereco_entrega`: Endereço completo para onde o pacote está sendo enviado.
        *   `codigo_rastreio`: O código de rastreamento completo da transportadora.
        *   `historico_rastreamento`: Uma lista ordenada cronologicamente (da mais recente para a mais antiga) de objetos `EventoRastreamento`, onde cada evento contém:
            *   `data_hora`: Data e hora do evento.
            *   `localizacao`: Local onde o evento ocorreu (ex: "Centro de Distribuição, Cajamar - SP").
            *   `status_detalhado`: Descrição completa do status fornecida pela transportadora (ex: "Objeto postado", "Objeto em trânsito para a unidade de tratamento", "Objeto saiu para entrega ao destinatário").
        *   A Camada de Abstração será responsável por consultar as fontes de dados primárias e traduzir/normalizar os `status_detalhado` para garantir consistência mínima, sem perder o detalhe original da transportadora.

*   **HU 3: Consistência e Atualização dos Dados**
    *   **Como** uma equipe de produto frontend, **eu quero** que as informações de rastreamento na API sejam atualizadas em tempo hábil e consistentes, **para que** os clientes sempre vejam o status mais recente e preciso.
    *   **Requisito de Plataforma:**
        *   Implementar um mecanismo de sincronização e atualização de dados de rastreamento com as transportadoras e sistemas legados (e.g., polling, webhooks se disponíveis).
        *   Definir e aplicar políticas de TTL (Time To Live) para dados em cache, garantindo que as informações não fiquem obsoletas.
        *   Mecanismo de tratamento de erros e retries para falhas na comunicação com sistemas externos.

#### **2.2. O que está Fora de Escopo (para a Camada de Abstração - MVP)**

*   **Implementação da UI/UX frontend:** A responsabilidade de como os dados são visualizados na tela "Meus Pacotes" é da equipe de produto e design de negócio.
*   **Notificações proativas ao cliente:** O disparo de e-mails, SMS ou push notifications sobre mudanças de status (esta funcionalidade consumiria a nossa API, mas não é parte dela).
*   **Previsão de entrega:** Calcular ou exibir estimativas de data de entrega.
*   **Integração com todas as transportadoras existentes no mercado:** O MVP focará nas transportadoras de maior volume/impacto, com um plano de expansão posterior.
*   **Ações transacionais sobre o rastreamento:** Alterar endereço de entrega, reagendar, etc. (o escopo é puramente de consulta).
*   **Rastreamento de pacotes que não são originados de pedidos da nossa plataforma.**
*   **Geração de código de rastreio:** Assumimos que o código de rastreio é fornecido pelos sistemas de pedidos/transportadoras.

### **3. Design e Experiência (da API)**

Embora não sejamos responsáveis pelo design da interface do usuário final, a experiência da nossa API é crucial para a produtividade dos times que a consomem.

#### **3.1. Fluxo da Experiência do Usuário (Habilitada pela API)**

*   **Fluxo de Alto Nível (Frontend habilitado pela Abstraction Layer):**
    1.  Cliente acessa "Meus Pedidos".
    2.  Frontend chama `GET /api/v1/packages?user_id={user_id}` para obter a lista resumida.
    3.  Frontend renderiza a lista com `id_pacote`, `identificador_produto`, `numero_pedido`, `data_compra`, `ultimo_status_simplificado`.
    4.  Cliente clica em um item da lista.
    5.  Frontend chama `GET /api/v1/packages/{id_pacote}/details` para obter os detalhes completos.
    6.  Frontend expande a área de visualização (sem nova página) e renderiza `endereco_entrega`, `codigo_rastreio` e o `historico_rastreamento` em linha do tempo.

#### **3.2. Protótipos e Design Final (da API)**

*   **Estilo da API:** RESTful, seguindo padrões de design de APIs da empresa.
*   **Autenticação:** Token JWT ou chave de API para equipes internas.
*   **Endpoints Propostos:**
    *   `GET /v1/users/{user_id}/packages`
        *   **Parâmetros de Query:** `status` (opcional, e.g., `active`, `completed`), `limit`, `offset`.
        *   **Resposta (Exemplo JSON):**
            ```json
            {
              "data": [
                {
                  "id_pacote": "PACK12345",
                  "identificador_produto": "Tênis Runner Pro",
                  "numero_pedido": "PED98765",
                  "data_compra": "2025-07-01",
                  "ultimo_status_simplificado": "Em trânsito"
                },
                {
                  "id_pacote": "PACK67890",
                  "identificador_produto": "Fone de Ouvido XYZ",
                  "numero_pedido": "PED12345",
                  "data_compra": "2025-06-20",
                  "ultimo_status_simplificado": "Entregue"
                }
              ],
              "meta": {
                "total_records": 2,
                "limit": 25,
                "offset": 0
              }
            }
            ```
    *   `GET /v1/packages/{id_pacote}/details`
        *   **Resposta (Exemplo JSON):**
            ```json
            {
              "id_pacote": "PACK12345",
              "identificador_produto": "Tênis Runner Pro",
              "numero_pedido": "PED98765",
              "data_compra": "2025-07-01",
              "ultimo_status_simplificado": "Em trânsito",
              "endereco_entrega": "Rua das Flores, 123, Apto 45, Bairro Jardim - São Paulo/SP",
              "codigo_rastreio": "AA123456789BR",
              "historico_rastreamento": [
                {
                  "data_hora": "2025-07-15T10:30:00Z",
                  "localizacao": "Centro de Distribuição, Cajamar - SP",
                  "status_detalhado": "Objeto em trânsito para a unidade de tratamento"
                },
                {
                  "data_hora": "2025-07-14T18:00:00Z",
                  "localizacao": "Agência Correios, Pinheiros - SP",
                  "status_detalhado": "Objeto postado"
                }
                // ... mais eventos, do mais recente para o mais antigo
              ]
            }
            ```
*   **Padronização de Status:** Será definido um *mapeamento* de status detalhados das transportadoras para o `ultimo_status_simplificado` (e.g., "Objeto em trânsito", "Saiu para entrega", "Entregue", "Aguardando retirada", "Problema na entrega"). Isso será mantido em um dicionário de dados ou micro-serviço de configuração.

### **4. Detalhes de Execução**

#### **4.1. Implicações Técnicas e Dependências**

*   **Integração de Dados:**
    *   **Fonte de Pedidos:** Dependência do `Sistema Legado de Pedidos` para obter informações como `numero_pedido`, `data_compra`, `identificador_produto` e `user_id`. Será necessário uma integração via API ou banco de dados, dependendo da maturidade do sistema legado.
    *   **Fontes de Rastreamento (Transportadoras):** Integração com APIs das principais transportadoras (Correios, Jadlog, Loggi, etc.). Isso pode envolver:
        *   Modelagem de dados para diferentes formatos de resposta das transportadoras.
        *   Gerenciamento de credenciais e chaves de API para cada transportadora.
        *   Adaptação a diferentes protocolos (REST, SOAP, FTP de arquivos, etc.).
    *   **Normalização de Dados:** Implementação de um serviço de normalização de status que transforma os status brutos das transportadoras em um conjunto unificado e simplificado.
*   **Arquitetura:**
    *   Microsserviço(s) dedicado(s) para o rastreamento, desacoplado(s) dos sistemas legados.
    *   Camada de persistência para cache de dados de rastreamento e otimização de consultas às APIs das transportadoras (reduzindo chamadas e respeitando limites de rate-limit).
    *   Mecanismo de workers/jobs para sincronização assíncrona dos status de rastreamento, evitando latência no caminho crítico da requisição da API.
*   **Infraestrutura:** Uso de conteiners (Docker/Kubernetes), CI/CD, monitoramento robusto (APM, logs, métricas) para visibilidade da saúde da API e das integrações.
*   **Performance e Escalabilidade:**
    *   Estratégias de caching (no serviço de Abstraction Layer) para reduzir a carga nas APIs das transportadoras e melhorar a latência.
    *   Gerenciamento de rate-limits e quotas das APIs de terceiros.
    *   Circuit Breakers para lidar com falhas de transportadoras.
*   **Observabilidade:** Geração de logs estruturados e métricas (e.g., número de pacotes rastreados, sucesso/falha de integração por transportadora, latência de cada integração).

#### **4.2. Plano de Lançamento (Go-to-Market)**

*   **Fase 1: Lançamento Interno/Beta Fechado (1 semana)**
    *   API disponível para equipe de produto de negócio e QA.
    *   Equipe de suporte começa a usar uma ferramenta interna (protótipo da tela "Meus Pacotes") que consome a nova API para familiarização e coleta de feedback.
    *   Monitoramento intensivo da API e das integrações.
*   **Fase 2: Rollout Gradual (A/B Test - 2-4 semanas)**
    *   Disponibilização da nova tela "Meus Pacotes" para um pequeno percentual (e.g., 5-10%) dos usuários reais.
    *   Comparação das métricas de suporte e CSAT entre o grupo de controle e o grupo A/B.
    *   Coleta de feedback direto dos usuários (se possível).
*   **Fase 3: Lançamento Completo (Ramp-up)**
    *   Aumento gradual do percentual de usuários expostos à nova experiência, até 100%.
    *   Comunicação de marketing (liderada pela equipe de negócio) sobre a nova funcionalidade.
    *   Continuidade do monitoramento das métricas primárias e secundárias.

#### **4.3. Plano de Desenvolvimento (Marcos Principais)**

*   **Sprint 1-2: Setup e Integração Base (MVP para 1 transportadora)**
    *   Definição e documentação detalhada dos contratos da API (OpenAPI/Swagger).
    *   Implementação dos endpoints `GET /v1/users/{user_id}/packages` e `GET /v1/packages/{id_pacote}/details`.
    *   Integração inicial com o Sistema Legado de Pedidos.
    *   Integração com a primeira transportadora (ex: Correios) e lógica de normalização de status básicos.
    *   Implementação do cache básico.
*   **Sprint 3-4: Resiliência e Refinamento**
    *   Melhoria dos mecanismos de resiliência (retries, circuit breakers) para integrações externas.
    *   Refinamento da lógica de normalização de status para cobrir mais cenários e edge cases.
    *   Implementação de logging e métricas de observabilidade.
    *   Testes de carga e performance da API.
*   **Sprint 5+: Expansão e Otimização**
    *   Integração com transportadoras adicionais (priorizadas por volume/impacto).
    *   Exploração de webhooks de transportadoras para atualizações mais próximas do real-time.
    *   Otimizações de performance e escalabilidade (e.g., melhorias no cache, otimização de consultas).
    *   Iteração com a equipe de produto de negócio para possíveis refinamentos de dados.

### **5. Riscos**

*   **Qualidade e Consistência dos Dados de Terceiros:** A variabilidade na qualidade e frequência de atualização dos dados fornecidos pelas APIs das transportadoras é um risco inerente. Isso pode levar a informações desatualizadas ou incorretas, apesar dos nossos esforços.
    *   **Mitigação:** Monitoramento ativo da data de última atualização do status e alerta para dados "stale". Implementação de políticas claras de "data freshness". Possibilidade de indicar a fonte do status e a data/hora da última atualização.
*   **Latência e Disponibilidade de APIs Externas:** Falhas ou lentidão nas APIs das transportadoras podem impactar a performance e disponibilidade da nossa própria API.
    *   **Mitigação:** Estratégias robustas de caching, circuit breakers, retries com backoff exponencial e fallback para o último status conhecido em caso de falha. Acordos de nível de serviço (SLAs) com transportadoras, quando possível.
*   **Complexidade de Normalização de Status:** A tradução de uma vasta gama de status de transportadoras para um conjunto simplificado e consistente pode ser complexa e sujeita a erros, impactando a clareza para o usuário final.
    *   **Mitigação:** Envolvimento contínuo da equipe de produto de negócio e suporte na validação dos status normalizados. Manutenção de um dicionário de mapeamento de fácil atualização. Implementar validação e testes extensivos sobre os mapeamentos.
*   **Escalabilidade das Integrações:** À medida que o volume de pedidos cresce, o número de chamadas às APIs das transportadoras pode se tornar um gargalo ou exceder limites de rate-limit.
    *   **Mitigação:** Otimização do scheduler de atualização, uso eficiente do cache, negociação de limites de rate-limit mais altos com transportadoras-chave, exploração de arquiteturas de fan-out para distribuição de carga.
*   **Dependência do Sistema Legado:** A integração com o sistema legado de pedidos pode apresentar desafios de performance, disponibilidade e qualidade de dados, impactando a base da informação de rastreamento.
    *   **Mitigação:** Realizar um mapeamento detalhado dos dados necessários do sistema legado. Estabelecer um canal de comunicação claro com as equipes responsáveis pelo legado. Implementar tratamentos de erro e logs específicos para essa integração.

---