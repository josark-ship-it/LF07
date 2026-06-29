-- Erstellt die Tabelle für die Klemmbaustein-Sets
CREATE TABLE IF NOT EXISTS artikel (
    artikel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    netto_preis DECIMAL(10, 2) NOT NULL,
    mwst_satz DECIMAL(4, 2) DEFAULT 19.00
);

-- Erstellt die Tabelle für die Terminbuchungen der Kunden
CREATE TABLE IF NOT EXISTS buchungen (
    buchung_id INT AUTO_INCREMENT PRIMARY KEY,
    kunde_name VARCHAR(100) NOT NULL,
    slot_zeit DATETIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Bestaetigt'
);