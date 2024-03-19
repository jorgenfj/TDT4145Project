.headers on
SELECT T.Tittel, F.Dato, COUNT(S.BillettNr) AS SolgtePlasser 
FROM Forestilling AS F 
LEFT JOIN Teaterstykke as T ON F.TeaterstykkeID = T.TeaterstykkeID 
LEFT JOIN ReservererForestilling as R ON T.TeaterstykkeID = R.TeaterstykkeID 
AND F.Dato = R.ForestillingsDato 
LEFT JOIN ReservererStol as S ON R.KjopID = S.KjopID 
GROUP BY T.TeaterstykkeID, F.Dato 
ORDER BY SolgtePlasser DESC