BEGIN TRANSACTION;

DROP TABLE IF EXISTS Teatersal;
CREATE TABLE Teatersal (
    SalID INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    MaksPlasser INT,
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
    TeaterstykkeID INT,
    Dato DATE,
    Tidspunkt TIME,
    PRIMARY KEY (TeaterstykkeID, Dato, Tidspunkt),
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Pristyper;
CREATE TABLE Pristyper (
    TeaterstykkeID INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Pris INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Type),
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
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
    FOREIGN KEY (TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt) 
    REFERENCES Forestilling(TeaterstykkeID, Dato, Tidspunkt) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS ReservererForestilling;
CREATE TABLE ReservererForestilling (
    KjopID INT NOT NULL,
    BillettNr INT NOT NULL,
    SalID INT NOT NULL,
    RadNr INT NOT NULL,
    SeteNr INT NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (SalID, RadNr, SeteNr, Omraadenavn) 
    REFERENCES Stol(SalID, RedNr, SeteNr, Omraadenavn) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Teaterbillett;
CREATE TABLE TeaterBillett (
    KjopID INT NOT NULL,
    TeaterstykkeID INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID) REFERENCES Pristyper(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettype;
CREATE TABLE Billettype (
    KjopID INT NOT NULL,
    BillettNr INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Type) REFERENCES Pristyper(Type) ON DELETE CASCADE ON UPDATE CASCADE
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
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
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
    SkuespillerID INTEGER NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    PRIMARY KEY (SkuespillerID)
);

DROP TABLE IF EXISTS Rolle;
CREATE TABLE Rolle (
    RolleID INT NOT NULL,
    Navn VARCHAR(50),
    SkuespillerID INT NOT NULL,
    PRIMARY KEY (RolleID),
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE
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
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS SpillesIAkt;
CREATE TABLE SpillesIAkt (
    TeaterstykkeID INT NOT NULL,
    AktNr INT NOT NULL,
    RolleID INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID, AktNr, RolleID),
    FOREIGN KEY (TeaterstykkeID, AktNr) REFERENCES Akt(TeaterstykkeID,AktNr) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;