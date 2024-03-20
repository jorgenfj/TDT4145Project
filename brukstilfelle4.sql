SELECT Dato, T.Tittel, Tidspunkt, COALESCE(COUNT(S.BillettNr), 0) 
FROM Forestilling AS F 
LEFT JOIN Teaterstykke as T ON F.TeaterstykkeID = T.TeaterstykkeID 
LEFT JOIN ReservererForestilling as R ON T.TeaterstykkeID = R.TeaterstykkeID 
AND F.Dato = R.ForestillingsDato 
LEFT JOIN ReservererStol as S ON R.KjopID = S.KjopID 
WHERE Dato IS ?
GROUP BY T.TeaterstykkeID 
ORDER BY F.Tidspunkt