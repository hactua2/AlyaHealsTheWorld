# Auditoria A1 — Inventário de Recursos, Coleta e Ecologia

## Objetivo

Estabelecer uma fotografia do estado atual do projeto antes de propor lewdification, novos recursos ou novos sistemas. Esta auditoria registra apenas o que já existe, o que está implicitamente suportado e o que permanece indefinido.

## Resumo executivo

O jogo já possui infraestrutura conceitual para recursos, produção e obtenção de materiais, mas ainda não possui uma economia canônica detalhada.

O estado atual é, portanto, um esqueleto extensível e não um sistema econômico que precise ser refatorado.

| Camada | Estado |
|---|---|
| Itens e equipamentos concretos | Já existem |
| Recursos genéricos | Confirmados, mas não nomeados |
| Produção na comunidade | Confirmada, mas indefinida |
| Recursos raros de expedições | Confirmados, mas indefinidos |
| Transmutação usando componentes | Confirmada |
| Coleta durante exploração | Implícita no core loop |
| Agricultura específica | Não definida em detalhe |
| Taxonomia de recursos | Não existe |
| Ecologia produtiva detalhada | Não existe |

## 1. Recursos explicitamente existentes

Não existe uma lista canônica de materiais ou recursos individuais. O projeto confirma a existência de recursos, componentes, produção e recursos raros, mas não define categorias, nomes, taxas ou fórmulas.

### Status

- **CANON:** recursos existem.
- **UNSPECIFIED:** quais recursos são esses.

## 2. Itens concretos existentes

Existe uma lista de equipamentos, acessórios, marcas e itens-chave. Eles já associam corpo, transformação, prazer e progressão mecânica.

Esses itens não devem ser confundidos com recursos econômicos:

```text
ITEMS / EQUIPMENT
        !=
RESOURCES / MATERIALS
```

## 3. Produção de recursos

A comunidade possui uma atividade persistente de produção ou obtenção de recursos.

```text
Base
  ↓
Ongoing Production Activity
  ↓
Resources
```

Ainda não estão definidos:

- instalações produtoras;
- recursos produzidos;
- trabalhadores;
- custos;
- intervalos;
- capacidade;
- fórmulas.

**Classificação:** KEEP.

A futura lewdification deve preencher este sistema, e não criar uma arquitetura paralela.

## 4. Farming / agricultura

O projeto suporta a ideia de `resource production/farming`, mas não possui um sistema agrícola detalhado.

Ainda não existem definições para plantações, sementes, ciclos, estações, colheitas, jardins, estufas ou criação de criaturas.

**Conclusão:** farming pode ser uma expressão de Resource Production, sem exigir inicialmente um simulador agrícola separado.

## 5. Transmutação

Existe um loop confirmado:

```text
Village Production
        ↓
Components
        ↓
Transmutation
        ↓
Equipment Empowerment
```

Ainda não existem receitas, categorias de componentes, raridades, probabilidades ou tiers.

**Classificação:** KEEP.

## 6. Expedições e recursos raros

Existe um loop confirmado:

```text
Assign Allies
       ↓
Expedition
       ↓
Rare Resources
       ↓
Return / Additional Opportunities
```

As expedições ainda não possuem duração, risco, tamanho de equipe, fórmulas, categorias de recursos ou regiões detalhadas.

**Classificação:** KEEP.

## 7. Coleta durante exploração

Não existe uma mecânica própria de gathering, mas recursos fazem parte do core loop de exploração.

Possíveis origens já suportadas conceitualmente:

- descoberta;
- exploração;
- encontros;
- quests;
- recompensas.

Ainda não foi decidido se haverá nós de coleta, drops, eventos, gathering manual ou coleta automática.

**Classificação:** KEEP / UNSPECIFIED.

## 8. Ecologia atual

O mundo já possui assentamentos civilizados, grupos tribais, criaturas selvagens, mortos-vivos, seres solitários, criaturas mágicas e regiões inexploradas. Há também um roster concreto de inimigos e povos.

Ainda não existem definições detalhadas para:

- biomas;
- flora;
- fauna não hostil;
- recursos naturais específicos;
- cadeias alimentares;
- ecossistemas;
- espécies cultiváveis;
- materiais por região.

A maior lacuna atual é uma **ecologia econômica**, não a ausência de mais sistemas.

## 9. A Ferida e recursos

A Ferida é fortemente definida narrativamente, mas ainda não possui um sistema canônico de materiais, flora, essências ou recursos derivados.

Esses elementos permanecem como lacunas potenciais e não como conteúdo preexistente a preservar.

## 10. Mapa consolidado

```text
                 EXPLORATION
                      │
          ┌───────────┼────────────┐
          │           │            │
      DISCOVERY    ENCOUNTER      QUEST
          │           │            │
          └───────────┼────────────┘
                      ↓
                  RESOURCES
                      │
          ┌───────────┼────────────┐
          │           │            │
       BASE        EXPEDITION   REWARDS
          │           │            │
          ↓           ↓            │
   RESOURCE PRODUCTION       RARE RESOURCES
          │                        │
          └────────────┬───────────┘
                       ↓
                   COMPONENTS
                       ↓
                  TRANSMUTATION
                       ↓
                    EQUIPMENT
```

## 11. Veredito

### O que deve ser preservado

- recursos genéricos;
- Resource Production;
- farming como possibilidade dentro da produção;
- componentes;
- Transmutation;
- recursos raros de expedição;
- obtenção de recursos através do loop de exploração;
- equipamentos e itens como camada separada.

### O que permanece indefinido

- lista e taxonomia de recursos;
- materiais básicos, biológicos e mágicos;
- recursos da Ferida;
- flora e ecologia produtiva;
- agricultura concreta;
- biomas;
- métodos específicos de coleta;
- drops;
- receitas de transmutação.

## Conclusão estratégica

A estrutura atual é saudável, enxuta e extensível. A próxima etapa deve classificar as lacunas e definir o menor conjunto de categorias sistêmicas necessário para preencher os loops existentes, sem criar uma economia paralela ou novos sistemas sem justificativa.

**Próxima etapa:** Auditoria A2 — Classificação e lewdification das lacunas existentes.
