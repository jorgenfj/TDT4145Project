BEGIN TRANSACTION;

DROP TABLE IF EXISTS Teatersal;
CREATE TABLE Teatersal (
    SalID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    MaksPlasser INT NOT NULL DEFAULT 0
);

INSERT INTO Teatersal (Navn, MaksPlasser) VALUES ('Hovedscenen', 520);
INSERT INTO Teatersal (Navn, MaksPlasser) VALUES ('Gamle Scene', 332);

DROP TABLE IF EXISTS Teaterstykke;
CREATE TABLE Teaterstykke (
    TeaterstykkeID INTEGER PRIMARY KEY,
    Tittel VARCHAR(50) NOT NULL,
    Forfatter VARCHAR(50),
    SalID INT NOT NULL,
    FOREIGN KEY (SalID) REFERENCES Teatersal(SalID) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Teaterstykke (Tittel, Forfatter, SalID) VALUES ('Kongsemnene', 'Henrik Ibsen', 1);
INSERT INTO Teaterstykke (Tittel, Forfatter, SalID) VALUES ('Størst av alt er kjærligheten', 'Jonas Corell Petersen', 2);

DROP TABLE IF EXISTS Forestilling;
CREATE TABLE Forestilling (
    TeaterstykkeID INT NOT NULL,
    Dato DATE NOT NULL,
    Tidspunkt TIME NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Dato, Tidspunkt),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Forestillinger for Kongsemnene
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (1, '2024-02-01', '19:00:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (1, '2024-02-02', '19:00:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (1, '2024-02-03', '19:00:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (1, '2024-02-05', '19:00:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (1, '2024-02-06', '19:00:00');

-- Forestillinger for Størst av alt er kjærligheten
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-06', '18:30:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-07', '18:30:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-03', '18:30:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-12', '18:30:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-13', '18:30:00');
INSERT INTO Forestilling (TeaterstykkeID, Dato, Tidspunkt) VALUES (2, '2024-02-14', '18:30:00');


DROP TABLE IF EXISTS Akt;
CREATE TABLE Akt (
    TeaterstykkeID INT NOT NULL,
    AktNr INT NOT NULL,
    Navn VARCHAR(50),
    PRIMARY KEY (TeaterstykkeID, AktNr),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insertions into Akt for 'Kongsemnene'
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (1, 1, '');
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (1, 2, '');
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (1, 3, '');
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (1, 4, '');
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (1, 5, '');

-- Insertion into Akt for 'Størst av alt er kjærligheten'
INSERT INTO Akt (TeaterstykkeID, AktNr, Navn) VALUES (2, 1, '');

DROP TABLE IF EXISTS Skuespiller;
CREATE TABLE Skuespiller (
    SkuespillerID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL
);

-- Insertions for Skuespiller
INSERT INTO Skuespiller (Navn) VALUES ('Arturo Scotti');
INSERT INTO Skuespiller (Navn) VALUES ('Ingunn Beate Strige Øyen');
INSERT INTO Skuespiller (Navn) VALUES ('Hans Petter Nilsen');
INSERT INTO Skuespiller (Navn) VALUES ('Madeline Brandtzæg Nilsen');
INSERT INTO Skuespiller (Navn) VALUES ('Synnøve Fossum Eriksen');
INSERT INTO Skuespiller (Navn) VALUES ('Emma Caroline Deichmann');
INSERT INTO Skuespiller (Navn) VALUES ('Thomas Jensen Takyi');
INSERT INTO Skuespiller (Navn) VALUES ('Per Bogstad Gulliksen');
INSERT INTO Skuespiller (Navn) VALUES ('Isak Holmen Sørensen');
INSERT INTO Skuespiller (Navn) VALUES ('Fabian Heidelberg Lunde');
INSERT INTO Skuespiller (Navn) VALUES ('Emil Olafsson');
INSERT INTO Skuespiller (Navn) VALUES ('Snorre Ryen Tøndel');
INSERT INTO Skuespiller (Navn) VALUES ('Sunniva Du Mond Nordal');
INSERT INTO Skuespiller (Navn) VALUES ('Jo Saberniak');
INSERT INTO Skuespiller (Navn) VALUES ('Marte M. Steinholt');
INSERT INTO Skuespiller (Navn) VALUES ('Tor Ivar Hagen');
INSERT INTO Skuespiller (Navn) VALUES ('Trond-Ove Skrødal');
INSERT INTO Skuespiller (Navn) VALUES ('Natalie Grøndahl Tangen');
INSERT INTO Skuespiller (Navn) VALUES ('Åsmund Flaten');

DROP TABLE IF EXISTS Rolle;
CREATE TABLE Rolle (
    RolleID INTEGER PRIMARY KEY,
    Navn VARCHAR(50)
);

-- Insertions for Rolle
-- Kongsemnene
INSERT INTO Rolle (Navn) VALUES ('Haakon Haakonssønn');
INSERT INTO Rolle (Navn) VALUES ('Dagfinn Bonde');
INSERT INTO Rolle (Navn) VALUES ('Jatgeir Skald');
INSERT INTO Rolle (Navn) VALUES ('Sigrid');
INSERT INTO Rolle (Navn) VALUES ('Ingebjørg');
INSERT INTO Rolle (Navn) VALUES ('Baard Bratte');
INSERT INTO Rolle (Navn) VALUES ('Skule Jarl');
INSERT INTO Rolle (Navn) VALUES ('Inga frå Vartejg');
INSERT INTO Rolle (Navn) VALUES ('Paal Flida');
INSERT INTO Rolle (Navn) VALUES ('Ragnhild');
INSERT INTO Rolle (Navn) VALUES ('Gregorius Jonssønn');
INSERT INTO Rolle (Navn) VALUES ('Margrete');
INSERT INTO Rolle (Navn) VALUES ('Biskop Nikolas');
INSERT INTO Rolle (Navn) VALUES ('Peter');

-- Størst av alt er kjærligheten
INSERT INTO Rolle (Navn) VALUES ('Sunniva Du Mond Nordal');
INSERT INTO Rolle (Navn) VALUES ('Jo Saberniak');
INSERT INTO Rolle (Navn) VALUES ('Marte M. Steinholt');
INSERT INTO Rolle (Navn) VALUES ('Tor Ivar Hagen');
INSERT INTO Rolle (Navn) VALUES ('Trond-Ove Skrødal');
INSERT INTO Rolle (Navn) VALUES ('Natalie Grøndahl Tangen');
INSERT INTO Rolle (Navn) VALUES ('Åsmund Flaten');

DROP TABLE IF EXISTS SpillesAv;
CREATE TABLE SpillesAV (
    SkuespillerID INT NOT NULL,
    RolleID INT NOT NULL,
    PRIMARY KEY (SkuespillerID, RolleID),
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Spilles av for Kongsemnene
INSERT INTO SpillesAv VALUES (1, 1);
INSERT INTO SpillesAv VALUES (2, 8);
INSERT INTO SpillesAv VALUES (3, 7);
INSERT INTO SpillesAv VALUES (4, 10);
INSERT INTO SpillesAv VALUES (5, 12);
INSERT INTO SpillesAv VALUES (6, 4);
INSERT INTO SpillesAv VALUES (6, 5);
INSERT INTO SpillesAv VALUES (7, 13);
INSERT INTO SpillesAv VALUES (8, 11);
INSERT INTO SpillesAv VALUES (9, 9);
INSERT INTO SpillesAv VALUES (10, 6);
INSERT INTO SpillesAv VALUES (11, 3);
INSERT INTO SpillesAv VALUES (11, 2);
INSERT INTO SpillesAv VALUES (12, 14);

-- Spilles av for Størst av alt er kjærligheten
INSERT INTO SpillesAv VALUES (13, 15);
INSERT INTO SpillesAv VALUES (14, 16);
INSERT INTO SpillesAv VALUES (15, 17);
INSERT INTO SpillesAv VALUES (16, 18);
INSERT INTO SpillesAv VALUES (17, 19);
INSERT INTO SpillesAv VALUES (18, 20);
INSERT INTO SpillesAv VALUES (19, 21);

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

-- SpillesIAkt for Kongsemnene
INSERT INTO SpillesIAkt VALUES (1, 1, 1);
INSERT INTO SpillesIAkt VALUES (1, 2, 1);
INSERT INTO SpillesIAkt VALUES (1, 3, 1);
INSERT INTO SpillesIAkt VALUES (1, 4, 1);
INSERT INTO SpillesIAkt VALUES (1, 5, 1);
INSERT INTO SpillesIAkt VALUES (1, 1, 2);
INSERT INTO SpillesIAkt VALUES (1, 2, 2);
INSERT INTO SpillesIAkt VALUES (1, 3, 2);
INSERT INTO SpillesIAkt VALUES (1, 4, 2);
INSERT INTO SpillesIAkt VALUES (1, 5, 2);
INSERT INTO SpillesIAkt VALUES (1, 4, 3);
INSERT INTO SpillesIAkt VALUES (1, 1, 4);
INSERT INTO SpillesIAkt VALUES (1, 2, 4);
INSERT INTO SpillesIAkt VALUES (1, 5, 4);
INSERT INTO SpillesIAkt VALUES (1, 4, 5);
INSERT INTO SpillesIAkt VALUES (1, 1, 6);
INSERT INTO SpillesIAkt VALUES (1, 1, 7);
INSERT INTO SpillesIAkt VALUES (1, 2, 7);
INSERT INTO SpillesIAkt VALUES (1, 3, 7);
INSERT INTO SpillesIAkt VALUES (1, 4, 7);
INSERT INTO SpillesIAkt VALUES (1, 5, 7);
INSERT INTO SpillesIAkt VALUES (1, 1, 8);
INSERT INTO SpillesIAkt VALUES (1, 3, 8);
INSERT INTO SpillesIAkt VALUES (1, 1, 9);
INSERT INTO SpillesIAkt VALUES (1, 2, 9);
INSERT INTO SpillesIAkt VALUES (1, 3, 9);
INSERT INTO SpillesIAkt VALUES (1, 4, 9);
INSERT INTO SpillesIAkt VALUES (1, 5, 9);
INSERT INTO SpillesIAkt VALUES (1, 1, 10);
INSERT INTO SpillesIAkt VALUES (1, 5, 10);
INSERT INTO SpillesIAkt VALUES (1, 1, 11);
INSERT INTO SpillesIAkt VALUES (1, 2, 11);
INSERT INTO SpillesIAkt VALUES (1, 3, 11);
INSERT INTO SpillesIAkt VALUES (1, 4, 11);
INSERT INTO SpillesIAkt VALUES (1, 5, 11);
INSERT INTO SpillesIAkt VALUES (1, 1, 12);
INSERT INTO SpillesIAkt VALUES (1, 2, 12);
INSERT INTO SpillesIAkt VALUES (1, 3, 12);
INSERT INTO SpillesIAkt VALUES (1, 4, 12);
INSERT INTO SpillesIAkt VALUES (1, 5, 12);
INSERT INTO SpillesIAkt VALUES (1, 1, 13);
INSERT INTO SpillesIAkt VALUES (1, 2, 13);
INSERT INTO SpillesIAkt VALUES (1, 3, 13);
INSERT INTO SpillesIAkt VALUES (1, 3, 14);
INSERT INTO SpillesIAkt VALUES (1, 4, 14);
INSERT INTO SpillesIAkt VALUES (1, 5, 14);

-- SpillesIAkt for Størst av alt er kjærligheten
INSERT INTO SpillesIAkt VALUES (2, 1, 15);
INSERT INTO SpillesIAkt VALUES (2, 1, 16);
INSERT INTO SpillesIAkt VALUES (2, 1, 17);
INSERT INTO SpillesIAkt VALUES (2, 1, 18);
INSERT INTO SpillesIAkt VALUES (2, 1, 19);
INSERT INTO SpillesIAkt VALUES (2, 1, 20);
INSERT INTO SpillesIAkt VALUES (2, 1, 21);

DROP TABLE IF EXISTS Involvert;
CREATE TABLE Involvert (
    InvolvertID INTEGER PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50)
);

-- Involverte for Kongsemnene
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Yury Butusov', 'yury@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Aleksandr Shishkin-Hokusai', 'aleksandr@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Eivind Myren', 'eivind@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Mina Rype Stokke', 'mina@gmail.com', 'fast ansatt');

-- Involverte for Størst av alt er kjærligheten
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Jonas Corell Petersen', 'jonas@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('David Gehrt', 'david@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Gaute Tønder', 'gaute@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Magnus Mikaelsen', 'magnus@gmail.com', 'fast ansatt');
INSERT INTO Involvert (Navn, Epost, AnsattStatus) VALUES ('Kristoffer Spender', 'kristoff@gmail.com', 'fast ansatt');

DROP TABLE IF EXISTS Oppgave;
CREATE TABLE Oppgave (
    OppgaveID INTEGER PRIMARY KEY,
    Tittel VARCHAR(50) NOT NULL,
    Beskrivelse TEXT,
    TeaterstykkeID INT,
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Oppgaver for Kongsemnene
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Regi og musikkutvelgelse', 'Regissør og ansvarlig for utvalgt muskk for Kongsemnene', 1);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Scenografi og kostymer', 'Scene og kostymer for Kongsemnene', 1);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Lysdesign', 'Design av lys for Kongsemnene', 1);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Dramaturg', 'Ansvar for drama for Kongsemnene', 1);

-- Oppgaver for Størst av alt er kjærligheten
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Regi', 'Regissering av stykket for Størst av alt er kjærligheten', 2);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Scenografi og kostymer', 'Scene og kostymer for Størst av alt er kjærligheten', 2);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Musikalsk ansvarlig', 'Ansvarlig for musikk for Størst av alt er kjærligheten', 2);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Lysdesign', 'Design av ly for Størst av alt er kjærlighetens', 2);
INSERT INTO Oppgave (Tittel, Beskrivelse, TeaterstykkeID) VALUES ('Dramaturg', 'Ansvar for drama for Størst av alt er kjærligheten', 2);

DROP TABLE IF EXISTS UtforesAv;
CREATE TABLE UtforesAv (
    InvolvertID INT NOT NULL,
    OppgaveID INT NOT NULL,
    PRIMARY KEY (InvolvertID, OppgaveID),
    FOREIGN KEY (InvolvertID) REFERENCES Involvert(InvolvertID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Oppgaver utføres av for Kongsemnene
INSERT INTO UtforesAv VALUES (1, 1);
INSERT INTO UtforesAv VALUES (2, 2);
INSERT INTO UtforesAv VALUES (3, 3);
INSERT INTO UtforesAv VALUES (4, 4);

-- Oppgaver utføres av for Størst av alt er kjærligheten
INSERT INTO UtforesAv VALUES (5, 5);
INSERT INTO UtforesAv VALUES (6, 6);
INSERT INTO UtforesAv VALUES (7, 7);
INSERT INTO UtforesAv VALUES (8, 8);
INSERT INTO UtforesAv VALUES (9, 9);

DROP TABLE IF EXISTS Pristype;
CREATE TABLE Pristype (
    TeaterstykkeID INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Pris INT NOT NULL,
    PRIMARY KEY (TeaterstykkeID, Type),
    FOREIGN KEY (TeaterstykkeID) 
    REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Pristype for Kongsemnene
INSERT INTO Pristype VALUES (1, 'ORDINAER', 450);
INSERT INTO Pristype VALUES (1, 'HONNOR', 380);
INSERT INTO Pristype VALUES (1, 'STUDENT', 280);

-- Pristype for Størst av alt er kjærligheten
INSERT INTO Pristype VALUES (2, 'ORDINAER', 350);
INSERT INTO Pristype VALUES (2, 'HONNOR', 300);
INSERT INTO Pristype VALUES (2, 'STUDENT', 220);
INSERT INTO Pristype VALUES (2, 'BARN', 220);

DROP TABLE IF EXISTS KundeProfil;
CREATE TABLE KundeProfil (
    KundeID INTEGER PRIMARY KEY,
    Mobilnummer INT NOT NULL,
    Navn VARCHAR(50) NOT NULL,
    Adresse VARCHAR(50) NOT NULL
);

-- Kundeprofiler
INSERT INTO KundeProfil VALUES (0, 99999999, 'Testbruker', 'Testveien 1');

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
    REFERENCES Stol(SalID, RadNr, SeteNr, Omraadenavn) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Teaterbillett;
CREATE TABLE TeaterBillett (
    KjopID INT NOT NULL,
    TeaterstykkeID INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (KjopID) REFERENCES Billettkjop(KjopID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Billettype;
CREATE TABLE Billettype (
    KjopID INT NOT NULL,
    BillettNr INT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    PRIMARY KEY (KjopID, BillettNr),
    FOREIGN KEY (KjopID) REFERENCES Teaterbillett(KjopID) ON DELETE CASCADE ON UPDATE CASCADE
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


COMMIT;