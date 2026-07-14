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
