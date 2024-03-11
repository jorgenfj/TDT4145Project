BEGIN TRANSACTION;

PRAGMA encoding = "UTF-8";

DROP TABLE IF EXISTS Teatersal;
CREATE TABLE Teatersal (
    SalID INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    MaksPlasser INT NOT NULL DEFAULT 0,
    PRIMARY KEY (SalID)
);

DROP TABLE IF EXISTS Teaterstykke;
CREATE TABLE Teaterstykke (
    TeaterstykkeID INT NOT NULL,
    Tittel VARCHAR(50) NOT NULL,
    Forfatter VARCHAR(50),
    SalID INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID),
    FOREIGN KEY (SalID) REFERENCES Teatersal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Forestilling;
CREATE TABLE Forestilling (
    TeaterstykkeID INT NOT NULL,
    Dato DATE NOT NULL,
    Tidspunkt TIME NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Dato, Tidspunkt),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Pristype;
CREATE TABLE Pristype (
    TeaterstykkeID INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Pris INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Type),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Stol;
CREATE TABLE Stol (
    SalID INT NOT NULL,
    RadNr INT NOT NULL,
    SeteNr INT NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (SalID, RadNr, SeteNr, Omraadenavn),
    FOREIGN KEY (SalID) REFERENCES Teatersal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS ReservererForestilling;
CREATE TABLE ReservererForestilling (
    KjopID INT NOT NULL,
    TeaterstykkeID INT NOT NULL,
    ForestillingsDato DATE NOT NULL,
    ForestillingsTidspunkt TIME NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Teaterbillett(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt) 
    REFERENCES Forestilling(TeaterstykkeID, Dato, Tidspunkt) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS ReservererStol;
CREATE TABLE ReservererStol (
    KjopID INT NOT NULL,
    BillettNr INT NOT NULL,
    SalID INT NOT NULL,
    RadNr INT NOT NULL,
    SeteNr INT NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID, BillettNr) 
    REFERENCES Billettype(KjopID, BillettNr) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SalID, RadNr, SeteNr, Omraadenavn) 
    REFERENCES Stol(SalID, RedNr, SeteNr, Omraadenavn) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Teaterbillett;
CREATE TABLE TeaterBillett (
    KjopID INT NOT NULL,
    TeaterstykkeID INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID) REFERENCES Pristype(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettype;
CREATE TABLE Billettype (
    KjopID INT NOT NULL,
    BillettNr INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Type) REFERENCES Pristype(Type) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettkjop;
CREATE TABLE Billettkjop (
    KjopID INT NOT NULL,
    Dato DATE NOT NULL,
    Tid TIME NOT NULL,
    Totalpris INT NOT NULL,
    KundeID INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KundeID) REFERENCES KundeProfil(KundeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS KundeProfil;
CREATE TABLE KundeProfil (
    KundeID INT NOT NULL,
    Mobilnummer INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    Adresse VARCHAR(50) NOT NULL,
    PRIMARY KEY (KundeID)
);

DROP TABLE IF EXISTS Involvert;
CREATE TABLE Involvert (
    InvolvertID INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50), 
    PRIMARY KEY (InvolvertID)
);

DROP TABLE IF EXISTS Oppgave;
CREATE TABLE Oppgave (
    OppgaveID INT NOT NULL,
    Tittel VARCHAR(50) NOT NULL,
    Beskrivelse TEXT,
    TeaterstykkeID INT, 
    PRIMARY KEY (OppgaveID),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);


DROP TABLE IF EXISTS UtforesAv;
CREATE TABLE UtforesAv (
    InvolvertID INT NOT NULL,
    OppgaveID INT NOT NULL,
    PRIMARY KEY (InvolvertID, OppgaveID),
    FOREIGN KEY (InvolvertID) REFERENCES Involvert(InvolvertID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Skuespiller;
CREATE TABLE Skuespiller (
    SkuespillerID INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    PRIMARY KEY (SkuespillerID)
);

DROP TABLE IF EXISTS Rolle;
CREATE TABLE Rolle (
    RolleID INT NOT NULL,
    Navn VARCHAR(50),
    PRIMARY KEY (RolleID)
);

DROP TABLE IF EXISTS SpillesAv;
CREATE TABLE SpillesAV (
    SkuespillerID INT NOT NULL,
    RolleID INT NOT NULL,
    PRIMARY KEY (SkuespillerID, RolleID),
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Akt;
CREATE TABLE Akt (
    TeaterstykkeID INT NOT NULL,
    AktNr INT NOT NULL,
    Navn VARCHAR(50),
    PRIMARY KEY (TeaterstykkeID, AktNr),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS SpillesIAkt;
CREATE TABLE SpillesIAkt (
    TeaterstykkeID INT NOT NULL,
    AktNr INT NOT NULL,
    RolleID INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID, AktNr, RolleID),
    FOREIGN KEY (TeaterstykkeID, AktNr) 
    REFERENCES Akt(TeaterstykkeID,AktNr) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;