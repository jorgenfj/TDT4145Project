.headers on
SELECT DISTINCT Teaterstykke.Tittel AS Teaterstykke, Skuespiller.Navn AS Skuespiller, Rolle.Navn AS Rolle 
FROM Teaterstykke, Akt, SpillesIAkt, Rolle, SpillesAv, Skuespiller 
WHERE SpillesIAkt.TeaterstykkeID = Teaterstykke.TeaterstykkeID AND SpillesIAkt.RolleID = Rolle.RolleID 
AND Rolle.RolleID = SpillesAv.RolleID AND SpillesAv.SkuespillerID = Skuespiller.SkuespillerID;

-- Kjør dette i powershell for å kjøre scriptet:
-- Get-Content brukerhistorie5.sql | sqlite3 teater.db