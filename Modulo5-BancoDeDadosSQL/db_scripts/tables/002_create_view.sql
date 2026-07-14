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
