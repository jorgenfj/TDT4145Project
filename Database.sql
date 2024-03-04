BEGIN TRANSACTION;

DROP TABLE IF EXISTS Teatersesong;
CREATE TABLE Teatersesong (
    SesongID INT NOT NULL,
    Aar INT NOT NULL,
    Sesong VARCHAR(50) NOT NULL,
    PRIMARY KEY (SesongID)
);

DROP TABLE IF EXISTS TeaterSal;
CREATE TABLE TeaterSal (
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
    SesongID INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID),
    FOREIGN KEY (SalID) REFERENCES TeaterSal(SalID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SesongID) REFERENCES Teatersesong(SesongID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Oppgave;
CREATE TABLE Oppgave (
    OppgaveID INT NOT NULL,
    Tittel VARCHAR(50) NOT NULL,
    Beskrivelse TEXT,
    TeaterstykkeID INT NOT NULL, 
    PRIMARY KEY (OppgaveID),
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Innvolvert;
CREATE TABLE Innvolvert (
    InnvolvertID INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50), --Dersom dere ikke finner status kan dere anta en. Default verdi eller sette basert på oppgaven?
    PRIMARY KEY (InnvolvertID)
);

DROP TABLE IF EXISTS UtforesAv;
CREATE TABLE UtforesAv (
    InnvolvertID INT NOT NULL,
    OppgaveID INT NOT NULL,
    PRIMARY KEY (InnvolvertID, OppgaveID),
    FOREIGN KEY (InnvolvertID) REFERENCES Innvolvert(InnvolvertID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Forestilling;
CREATE TABLE Forestilling (
    Dato DATE,
    Tidspunkt TIME,
    TeaterstykkeID INT,
    PRIMARY KEY (Dato, Tidspunkt, TeaterstykkeID),
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS KundeProfil;
CREATE TABLE KundeProfil (
    KundeID INT NOT NULL,  --Satt kundeID til nøkkel, så vi ikke mister all kundeinformasjon dersom kunden bytter nummer
    Mobilnummer INT NOT NULL, -- 8 siffer
    Navn VARCHAR(50) NOT NULL,
    Adresse VARCHAR(50) NOT NULL,
    PRIMARY KEY (KundeID)

);

DROP TABLE IF EXISTS Billettkjop;
CREATE TABLE Billettkjop (
    KjopID INT NOT NULL,
    Dato DATE NOT NULL,  -- Kan bruke DATE('now') for å sette inn dagens dato
    Tid TIME NOT NULL,   -- Kan bruke TIME('now') for å sette inn dagens tidspunkt, må se an hvordan dette fungerer i SQLite/python
    Totalpris INT NOT NULL,
    KundeID INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KundeID) REFERENCES KundeProfil(KundeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billett;
CREATE TABLE Billett (
    BillettID INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Pris INT NOT NULL,
    KjopID INT NOT NULL,
    ForestillingsDato DATE NOT NULL,
    ForestillingsTidspunkt TIME NOT NULL,
    TeaterStykkeID INT NOT NULL,
    RadNr INT NOT NULL,
    StolNr INT NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    SalID INT NOT NULL,
    PRIMARY KEY (BillettID),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterStykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ForestillingsDato, ForestillingsTidspunkt, TeaterStykkeID) REFERENCES Forestilling(Dato, Tidspunkt, TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SalID) REFERENCES TeaterSal(SalID) ON DELETE CASCADE ON UPDATE CASCADE, --Burde undersøke om denne er nødvendig
    FOREIGN KEY (SalID, RadNr, StolNr, OmraadeNavn) REFERENCES Stol(SalID, RadNr, StolNr, OmraadeNavn) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Stol;
CREATE TABLE Stol (
    SalID INT NOT NULL,
    RadNr INT NOT NULL,
    SeteNr INT NOT NULL,
    OmraadeNavn VARCHAR(50) NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (SalID, StolNr, RadNr, Omraadenavn),
    FOREIGN KEY (SalID) REFERENCES TeaterSal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
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
    Navn VARCHAR(50), --Usikker på om NOT NULL, må se hvordan pyhton logikken fungerer
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
    Navn VARCHAR(50), --Default verdi?
    PRIMARY KEY (TeaterstykkeID, AktNr),
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS SpillerIAkt;
CREATE TABLE SpillerIAkt (
    RolleID INT NOT NULL,
    TeaterstykkeID INT NOT NULL,
    AktNr INT NOT NULL,
    PRIMARY KEY (RolleID, TeaterstykkeID, AktNr),
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE, 
    FOREIGN KEY (TeaterstykkeID, AktNr) REFERENCES Akt(TeaterstykkeID,AktNr) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;