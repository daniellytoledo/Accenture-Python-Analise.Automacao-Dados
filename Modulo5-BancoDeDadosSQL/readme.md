# 🐍 Módulo 5 — Fundamentos de Banco de Dados e SQL

> **Bootcamp:** Accenture - Python para Análise e Automação de Dados · Plataforma DIO

---

## 📌 Sobre este módulo

Introdução aos conceitos fundamentais de banco de dados relacionais e SQL, com a criação prática de um banco de dados para cartas TCG (Trading Card Game) de Pokémon. Neste módulo, utilizamos IA (Microsoft Copilot) para acelerar a criação do schema, dos scripts de inserção de dados (seeds), das views e de um script de automação para migrations.

---

## 🗂️ Conteúdo

- [Criando o Banco de Dados com Auxílio de IA](#criando-o-banco-de-dados-com-auxílio-de-ia)
- [Script de Criação das Tabelas](#script-de-criação-das-tabelas)
- [Seeds — Inserção de Dados Iniciais](#seeds--inserção-de-dados-iniciais)
- [Views](#views)
- [Script de Migration (PowerShell)](#script-de-migration-powershell)

---

## Criando o Banco de Dados com Auxílio de IA

Para acelerar o processo de modelagem, utilizamos o Microsoft Copilot com um prompt estruturado em blocos de **ação**, **contexto** e **informações**, técnica que ajuda a IA a entender exatamente o que precisa ser gerado.

```
# prompt para criar banco de dados de pokemon card

{ação}
create a script to create a table in postgresql

{contexto}
- the first table is a table to save pokemon TCG cards
- the second table is a table to save colletions set
- conect the tables with foreing keys

{informações}

1. first table: tbl_cards
- HP
- NAME
- TYPE
- STAGE
- INFO 
- ATTACK
- DEMMAGE
- WEAK
- RESSIS
- RETREAT
- CARD NUMBER IN COLLECTION 

2. second table: tbl_colletions
- ID
- COLLETION SET NAME
- RELEASE DATE
- TOTAL CARDS IN COLLECTION
```

> Estruturar o prompt em **ação → contexto → informações** deixa claro para a IA o que fazer, por que fazer e com quais dados trabalhar — reduzindo ambiguidade e retrabalho.

A partir desse prompt, a IA sugeriu normalizar os campos `TYPE` e `STAGE` em tabelas próprias (`tbl_types` e `tbl_stages`), evitando repetição de texto e facilitando futuras consultas e manutenções — uma boa prática de modelagem relacional.

---

## Script de Criação das Tabelas

Schema relacional com quatro tabelas: `tbl_stages`, `tbl_types`, `tbl_collections` e `tbl_cards`, esta última conectada às demais por meio de **chaves estrangeiras (foreign keys)**.

```sql
-- ================================
-- TABLE: Stages
-- ================================
CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stage_name VARCHAR(50) NOT NULL
);

-- ================================
-- TABLE: Types
-- ================================
CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);

-- ================================
-- TABLE: Collections (Sets)
-- ================================
CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collection_name VARCHAR(100) NOT NULL,
    release_date DATE,
    total_cards INTEGER
);

-- ================================
-- TABLE: Cards
-- ================================
CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    hp INTEGER,
    name VARCHAR(100) NOT NULL,
    info TEXT,
    attack VARCHAR(100),
    damage VARCHAR(50),
    weak VARCHAR(50),
    ressis VARCHAR(50),
    retreat VARCHAR(50),
    card_number INTEGER,

    -- Foreign Keys
    collection_id INTEGER NOT NULL,
    stage_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,

    CONSTRAINT fk_collection
        FOREIGN KEY (collection_id)
        REFERENCES tbl_collections(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_stage
        FOREIGN KEY (stage_id)
        REFERENCES tbl_stages(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_type
        FOREIGN KEY (type_id)
        REFERENCES tbl_types(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
```

> As cláusulas `ON DELETE CASCADE` e `ON DELETE RESTRICT` definem o comportamento das tabelas filhas quando um registro relacionado é apagado: `CASCADE` remove os dependentes automaticamente, enquanto `RESTRICT` impede a exclusão caso existam registros vinculados.

---

## Seeds — Inserção de Dados Iniciais

Scripts de **seed** populam o banco com dados iniciais, essenciais para testes e desenvolvimento antes de conectar o banco a uma aplicação real.

```sql
INSERT INTO tbl_stages (stage_name) VALUES
('Basic'),
('Stage 1'),
('Stage 2'),
('EX'),
('V'),
('VSTAR');

INSERT INTO tbl_types (type_name) VALUES
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting'),
('Dark'),
('Metal'),
('Fairy'),
('Dragon');

INSERT INTO tbl_collections (collection_name, release_date, total_cards) VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62),
('Team Rocket', '2000-04-24', 83),
('Neo Genesis', '2000-12-16', 111);

INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, ressis, retreat,
    card_number, collection_id, stage_id, type_id
) VALUES
-- 1. Pikachu (Base Set)
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', 'Metal', '1',
 25, 1, 1, 4),

-- 2. Charizard (Base Set)
(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', 'Fighting', '3',
 4, 1, 3, 1),

-- 3. Blastoise (Base Set)
(100, 'Blastoise', 'Shellfish Pokémon', 'Hydro Pump', '40+', 'Electric', 'None', '3',
 2, 1, 3, 2),

-- 4. Bulbasaur (Base Set)
(40, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', 'Water', '1',
 44, 1, 1, 3),

-- 5. Eevee (Jungle)
(50, 'Eevee', 'Evolution Pokémon', 'Quick Attack', '10+', 'Fighting', 'Psychic', '1',
 51, 2, 1, 5),

-- 6. Snorlax (Jungle)
(90, 'Snorlax', 'Sleeping Pokémon', 'Body Slam', '30', 'Fighting', 'None', '4',
 11, 2, 1, 6),

-- 7. Dragonite (Fossil)
(100, 'Dragonite', 'Dragon Pokémon', 'Slam', '40x', 'Ice', 'Fighting', '2',
 4, 3, 3, 10),

-- 8. Gengar (Fossil)
(80, 'Gengar', 'Shadow Pokémon', 'Nightmare', '30', 'Dark', 'Fighting', '1',
 5, 3, 3, 5),

-- 9. Dark Charmeleon (Team Rocket)
(50, 'Dark Charmeleon', 'Flame Pokémon', 'Fireball', '50', 'Water', 'Grass', '1',
 32, 4, 2, 1),

-- 10. Togepi (Neo Genesis)
(40, 'Togepi', 'Spike Ball Pokémon', 'Charm', '—', 'Metal', 'Dark', '1',
 51, 5, 1, 9);
```

> Os comentários `-- N. Nome (Coleção)` acima de cada linha do `INSERT` ajudam a identificar visualmente qual carta está sendo inserida, facilitando a leitura e a manutenção do script.

---

## Views

Uma **view** é uma consulta salva que se comporta como uma tabela virtual. Facilita a leitura dos dados ao já resolver os `JOIN`s entre as tabelas relacionadas, substituindo os IDs das chaves estrangeiras pelos nomes reais.

```sql
CREATE OR REPLACE VIEW vw_cards_full AS
SELECT
    c.id,
    c.hp,
    c.name,
    c.info,
    c.attack,
    c.damage,
    c.weak,
    c.ressis,
    c.retreat,
    c.card_number,

    -- Replace foreign keys with real names
    s.stage_name AS stage,
    t.type_name AS type,
    col.collection_name AS collection,
    col.release_date AS collection_release_date,
    col.total_cards AS collection_total_cards

FROM tbl_cards c
JOIN tbl_stages s
    ON c.stage_id = s.id
JOIN tbl_types t
    ON c.type_id = t.id
JOIN tbl_collections col
    ON c.collection_id = col.id;
```

> Com a view `vw_cards_full`, basta rodar `SELECT * FROM vw_cards_full;` para consultar todas as cartas já com as informações de tipo, estágio e coleção legíveis, sem precisar reescrever os `JOIN`s a cada consulta.

---

## Script de Migration (PowerShell)

Para organizar a execução dos scripts SQL, criamos um script em **PowerShell** que concatena automaticamente todos os arquivos `.sql` da pasta (tabelas, seeds e views) em um único arquivo de migration, na ordem alfabética dos nomes dos arquivos.

```powershell
# pegar o diretório atual
$scriptDirectory = Split-Path $MyInvocation.MyCommand.Definition -Parent

# arquivo de saída com todos os sql
$OutputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

# verifica se o arquivo já existe, se existir deleta
if (Test-Path $OutputFile){
    Remove-Item $OutputFile
}

# pega os conteúdos dos arquivos
$sqlFiles = Get-ChildItem $scriptDirectory -Filter *.sql -File | Sort-Object Name

# concatena arquivos
foreach($file in $sqlFiles){
    Get-Content $file.FullName | Out-File -Append -FilePath $OutputFile
    "GO" | Out-File -Append -FilePath $OutputFile
}

Write-Host "Todos os arquivos foram combinados $outputFile"
```

> Automatizar a junção dos scripts evita a execução manual e fora de ordem de cada arquivo `.sql`, garantindo que o banco seja sempre montado na sequência correta: tabelas → seeds → views.

---

## 🛠️ Tecnologias utilizadas neste módulo

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Script-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Copilot](https://img.shields.io/badge/Microsoft-Copilot-8A2BE2?style=for-the-badge&logo=microsoft&logoColor=white)
![Claude](https://img.shields.io/badge/Anthropic-Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-README-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

*Documentação gerada como parte do Bootcamp Accenture — Python para Análise e Automação de Dados · DIO*