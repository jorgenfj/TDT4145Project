SELECT DISTINCT Teaterstykke.Tittel, s1.Navn, s2.Navn 
FROM (SELECT * FROM Skuespiller WHERE Navn = ?) AS s1 
JOIN SpillesAv AS sa1 ON s1.SkuespillerID = sa1.SkuespillerID 
JOIN SpillesIAkt AS sia1 ON sa1.RolleID = sia1.RolleID 
JOIN Akt AS a1 ON sia1.AktNr = a1.AktNr AND sia1.TeaterstykkeID = a1.TeaterstykkeID 
JOIN Teaterstykke ON a1.TeaterstykkeID = Teaterstykke.TeaterstykkeID 
JOIN SpillesIAkt AS sia2 ON a1.TeaterstykkeID = sia2.TeaterstykkeID AND a1.AktNr = sia2.AktNr 
JOIN SpillesAv AS sa2 ON sia2.RolleID = sa2.RolleID 
JOIN Skuespiller AS s2 ON sa2.SkuespillerID = s2.SkuespillerID AND s1.SkuespillerID <> s2.SkuespillerID;