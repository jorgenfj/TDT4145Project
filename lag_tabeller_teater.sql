-- Endringer fra innlevering 1:
-- 1. Endret alle int til integer for å få auto-increment til å fungere
-- Endret til en mer logisk rekkefølge på tabellene
-- Pristyper endret til Pristype
-- Fremmednøkkel i Teaterbillett(TeaterstykkeID) refererer til teaterstykke istedenfor pristype
-- Fjernet fremmednøkkel(Type) i Billettype
-- Billettype har fremmednøkkel(KjopID) til Teaterbillett istedenfor billettkjop

BEGIN TRANSACTION;

DROP TABLE IF EXISTS Teatersal;
CREATE TABLE Teatersal (
    SalID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    MaksPlasser INTEGER NOT NULL DEFAULT 0
);

DROP TABLE IF EXISTS Teaterstykke;
CREATE TABLE Teaterstykke (
    TeaterstykkeID INTEGER PRIMARY KEY,
    Tittel VARCHAR(50) NOT NULL,
    Forfatter VARCHAR(50),
    SalID INTEGER NOT NULL,
    FOREIGN KEY (SalID) REFERENCES Teatersal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Forestilling;
CREATE TABLE Forestilling (
    TeaterstykkeID INTEGER NOT NULL,
    Dato DATE NOT NULL,
    Tidspunkt TIME NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Dato, Tidspunkt),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Akt;
CREATE TABLE Akt (
    TeaterstykkeID INTEGER NOT NULL,
    AktNr INTEGER NOT NULL,
    Navn VARCHAR(50),
    PRIMARY KEY (TeaterstykkeID, AktNr),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Skuespiller;
CREATE TABLE Skuespiller (
    SkuespillerID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS Rolle;
CREATE TABLE Rolle (
    RolleID INTEGER PRIMARY KEY,
    Navn VARCHAR(50)
);

DROP TABLE IF EXISTS SpillesAv;
CREATE TABLE SpillesAV (
    SkuespillerID INTEGER NOT NULL,
    RolleID INTEGER NOT NULL,
    PRIMARY KEY (SkuespillerID, RolleID),
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS SpillesIAkt;
CREATE TABLE SpillesIAkt (
    TeaterstykkeID INTEGER NOT NULL,
    AktNr INTEGER NOT NULL,
    RolleID INTEGER NOT NULL,
    PRIMARY KEY (TeaterstykkeID, AktNr, RolleID),
    FOREIGN KEY (TeaterstykkeID, AktNr) 
    REFERENCES Akt(TeaterstykkeID,AktNr) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Involvert;
CREATE TABLE Involvert (
    InvolvertID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50)
);

DROP TABLE IF EXISTS Oppgave;
CREATE TABLE Oppgave (
    OppgaveID INTEGER PRIMARY KEY,
    Tittel VARCHAR(50) NOT NULL,
    Beskrivelse TEXT,
    TeaterstykkeID INT,
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS UtforesAv;
CREATE TABLE UtforesAv (
    InvolvertID INTEGER NOT NULL,
    OppgaveID INTEGER NOT NULL,
    PRIMARY KEY (InvolvertID, OppgaveID),
    FOREIGN KEY (InvolvertID) REFERENCES Involvert(InvolvertID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Pristype;
CREATE TABLE Pristype (
    TeaterstykkeID INTEGER NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Pris INTEGER NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Type),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS KundeProfil;
CREATE TABLE KundeProfil (
    KundeID INTEGER PRIMARY KEY,
    Mobilnummer INTEGER NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    Adresse VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS Stol;
CREATE TABLE Stol (
    SalID INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    SeteNr INTEGER NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (SalID, RadNr, SeteNr, Omraadenavn),
    FOREIGN KEY (SalID) REFERENCES Teatersal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS ReservererForestilling;
CREATE TABLE ReservererForestilling (
    KjopID INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    ForestillingsDato DATE NOT NULL,
    ForestillingsTidspunkt TIME NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Teaterbillett(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt) 
    REFERENCES Forestilling(TeaterstykkeID, Dato, Tidspunkt) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS ReservererStol;
CREATE TABLE ReservererStol (
    KjopID INTEGER NOT NULL,
    BillettNr INTEGER NOT NULL,
    SalID INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    SeteNr INTEGER NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID, BillettNr) 
    REFERENCES Billettype(KjopID, BillettNr) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SalID, RadNr, SeteNr, Omraadenavn)
    REFERENCES Stol(SalID, RadNr, SeteNr, Omraadenavn) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Teaterbillett;
CREATE TABLE TeaterBillett (
    KjopID INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettype;
CREATE TABLE Billettype (
    KjopID INTEGER NOT NULL,
    BillettNr INTEGER NOT NULL,
    Type VARCHAR(50) NOT NULL,
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID) REFERENCES Teaterbillett(KjopID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettkjop;
CREATE TABLE Billettkjop (
    KjopID INTEGER NOT NULL,
    Dato DATE NOT NULL,
    Tid TIME NOT NULL,
    Totalpris INTEGER NOT NULL,
    KundeID INTEGER NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KundeID) REFERENCES KundeProfil(KundeID) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;