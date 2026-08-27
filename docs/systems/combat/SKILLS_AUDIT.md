# Ayla Heals the World — Auditoria e Expansão do Sistema de Skills

> Documento de design consolidado. Decisões aprovadas na análise de lacunas do sistema de skills e atualizadas após a auditoria de convergência.

## 1. Objetivo

O sistema deve deixar de ser uma coleção de ações individuais e formar loops de gameplay reconhecíveis. Cada build deve ter formas próprias de gerar recursos, explorar estados, reagir à pressão e finalizar encontros.

## 2. Vocabulário mecânico compartilhado

| Mecânica | Função |
|---|---|
| Control | Recurso/estado da Dominance, acumulado por comando, manipulação, hipnose e restrição; prepara controle, captura, submissão e finishers. |
| Surrender | Recurso/estado da Submission, acumulado por ações submissas e vulnerabilidade deliberada; fortalece respostas e abre janelas de finisher. |
| Cruelty | Recurso do Sadism, gerado ao explorar vulnerabilidades e pressionar inimigos debilitados; intensifica dano e debuffs. |
| Endurance | Recurso do Masochism, acumulado ao receber dano, resistir e sobreviver sob pressão; pode ser convertido em defesa, retaliação e poder. |
| Exploit | Skill recebe bônus contra estados específicos. |
| Consume | Skill consome stacks/recursos para um efeito maior. |
| Chain | Skill se fortalece em sequência ou repetição. |
| Threshold | Efeito muda conforme HP, H-gauge ou outro medidor. |
| Overflow | Interação com o transbordamento do H-gauge. |

## 3. Arquétipos emergentes

| | Sadist | Masochist |
|---|---|---|
| Dominant | Control → Exploit → Finish | Provoke → Endure → Control |
| Submissive | Expose → Retaliate → Finish | Receive → Build → Overflow |

Não são classes rígidas. A identidade emerge de atributos, skills, equipamentos, curses, escolhas e progressão.

## 4. Conjunto existente

As skills existentes permanecem válidas e são reinterpretadas dentro das famílias acima. Famílias identificadas:

- **Controle/Dominance:** Flirt, Hypnotize, Sensory Deprivation, Bind, Bully, Aphrodisiac, Prolonged Pleasure, Enslave.
- **Submission:** Get Spanked, Bl-job, Lay, Grope, Service, H-job, Bend, AS, Paizuri, Swallow, Deepthroat, Worship C, G-bang e Bkakke.
- **Sadism:** Spank, Bite, Bully, Bind, Stomp, F-fk, A-penetration e Enslave.
- **Masochism:** Get Spanked, Bend, AS, Bondage, Swallow, Deepthroat, Worship C e passivas relacionadas.
- **Magia/Mind:** Sensory Enhancement, Hypnotize, Sensory Deprivation, Aphrodisiac, P-growth, Pink Mist, Summon Tentacles e demais skills mágicas.
- **Passivas:** S Symbol, Otherworldly Charm, Piercing Stares, Sadism, Masochism, Moans, Extra Tips, Cuteness, Naughty Thoughts, C-drinker, Ecstasy Aftershocks e Divine Health.

### Integrações obrigatórias das skills existentes

- Body Parts devem interagir com os multiplicadores Ass, Breasts, Crotch, Mouth e Mind.
- Physical e Magical devem resolver problemas diferentes, não apenas usar fórmulas de dano diferentes.
- Skills devem reconhecer estados compartilhados e palavras-chave consistentes.
- O sistema deve comportar Enemy Intent e respostas defensivas/reativas.
- Passivas devem ser organizadas em Core Passive, Build Passives e Equipment/Conditional Passives.
- Vitória deve distinguir Kill, Knockout, Capture, Submission, Escape e Objective Complete.

## 5. Novas skills aprovadas

### Tier 1

| Skill | Identidade | Função |
|---|---|---|
| Provoke | Dominant + Masochist | Aumenta/força a prioridade de ataques contra Ayla; receber o ataque gera Endurance. |
| Endure | Masochist | Reduz dano recebido e obtém benefício proporcional ao dano bloqueado. |
| Countertease | Submissive + Sadist | Após receber H-damage, responde com H-damage ou efeito retaliatório. |
| Command | Dominant | Aplica Control e altera comportamento/prioridade do alvo. |
| Recover Composure | Mind / Self | Reduz H-gauge e remove parte dos efeitos negativos. |

### Tier 2

| Skill | Identidade | Função |
|---|---|---|
| Exploit Weakness | Exploit | Recebe bônus contra estados específicos e pode converter parte de H-damage em Health Damage. |
| Break Will | Control | Usa Control para reduzir resistência e preparar finisher. |
| Turn the Tables | Submissive + Sadist | Converte vulnerabilidade recente em vantagem ofensiva. |
| Ecstatic Focus | Masochist + Magical | Quanto maior a H-gauge, maior a eficácia da próxima ação. |
| Command Ally | Dominant + Support | Melhora a próxima ação de um aliado ou concede ação tática imediata. |

### Tier 3

| Skill | Identidade | Função |
|---|---|---|
| Absolute Control | Dominant / Consume Control | Consome Control para incapacitar, subjugar ou tornar o alvo capturável. |
| Unbroken | Masochist / Consume Endurance | Consome Endurance para evitar grande dano ou derrota iminente. |
| Overflow Engine | Overflow | Transforma Overflow em dano, buffs, cura ou recursos conforme a build. |
| Mutual Ruin | Hybrid / High Risk | Forte impacto nos dois lados; ferramenta para builds extremas. |

## 6. Resultado da auditoria

Após as 14 novas skills, não há lacuna crítica que justifique adicionar mais habilidades genéricas agora.

O sistema cobre ataque físico e mágico, H-damage e Health Damage, controle, vulnerabilidade, Submission/Surrender, Sadism/Cruelty, Masochism/Endurance, retaliação, defesa ativa, suporte, manipulação de H-gauge, Thresholds, Chains, Consume, Exploit, Overflow, finishers e builds híbridas.

## 7. Estado das antigas lacunas

A arquitetura posterior resolveu estruturalmente várias dependências que antes estavam abertas:

| Tema | Estado atual |
|---|---|
| Sinergias específicas com aliados | Arquitetura de aliados definida; conteúdo concreto ainda pendente. |
| Ações específicas de captura | Encerramento de combate pode abrir elegibilidade para reabilitação; ações concretas ainda pendentes. |
| Técnicas específicas por facção | Arquitetura de inimigos/famílias e camadas Organization/Wound definida; distribuição concreta pendente. |
| Skills exclusivas de outfits | Itens/equipamentos funcionam como habilitadores de build; roster concreto pendente. |
| Positioning | Continua pendente de definição da estrutura final de combate; não é necessário expandir skills antes disso. |
| Maior profundidade por Body Part | Conteúdo futuro de skills, itens e passivas. |
| Reações avançadas a Enemy Intent | Dependente da implementação final de Enemy Intent. |

## 8. Regra de continuidade

A auditoria de skills está estruturalmente fechada. Próximas adições devem ser conteúdo específico ou responder a uma lacuna demonstrada por testes/implementação, não simplesmente aumentar a quantidade de skills.

A próxima camada de trabalho é a especificação de contratos entre combate, status, equipamento, aliados, encounters e encerramentos de combate, incluindo a ponte entre elegibilidade de recrutamento e reabilitação comunitária.
