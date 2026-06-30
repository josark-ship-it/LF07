-- Testdaten für die Tabelle 'artikel' einfügen
INSERT INTO artikel (name, netto_preis, mwst_satz) 
VALUES ('Große Ritterburg', 167.97, 19.00);

INSERT INTO artikel (name, netto_preis, mwst_satz) 
VALUES ('Feuerwehrauto Mini', 12.60, 19.00);


-- Testdaten für die Tabelle 'buchungen' einfügen
-- (Hier tragen wir einen Testkunden für einen Termin ein)
INSERT INTO buchungen (kunde_name, slot_zeit, status) 
VALUES ('Max Mustermann', '2026-07-15 14:00:00', 'Bestaetigt');