image bg room = "places/house/room.png"
image bg living_room = "places/house/living_room.jpg"
image bg second_floor = "places/house/second_floor.jpg"
image bg staircase = "places/house/staircase.png"

image bg dream = "images/dream.png"

label house:
    jump dream

label dream:

    scene bg dream

    '...E mi addormentai...\nSfinito e dolorante iniziai a sognare:'

    'Sognai la mia famiglia e la mia vecchia casa.'

    'Sognai grandi mulini e piccole cascate nascoste dal fitto di una fiabesca foresta.'
    
    'Sognai intrichi di arabeschi simboli e architetture stupende e lontane, ma anormale.'

    'Vidi e Sentii cose che non riesco tutt\'ora a descrivere o anche solo ricordare nitidamente'

    'Ma una cose è certa,'

    'per tutto il sogno fui accompagnato da una melodia.'

    'Triste e cupa, piena di emozioni complicate e distorte... Era una cantilena assordante e sfiancante... Ne fui incantato e spaventato allo stesso tempo.'

    'Gli acuti strillavano nei loro alti come fossero saette e i profondi rimbombavano come in un abisso pregno di immonde forme ed inudibili suoni.'

    'Risuonò e Risuonò finché non inghiottì tutto, lasciando solo il più totale vuoto.'

    jump room

label room:

    scene bg room

    show h at left

    h 'Anf...Anf...'

    'È un violino...\nSembra provenire dalla stanza accanto...?'

    #Potenziale transizione verso ipotetica finestra posta al lato del letto atta a inquadrare l'alba.

    'Non ho tempo di pensare a certe cose, sta sorgendo l\'Alba... Ho del lavoro da sbrigare.'

    #Pistole e Proiettili sul comodino inquadrati.

    'Questa maledetta gamba non la smette di farmi male, forse dovrei farlo presente alla signora Wellis...O forse no.\nMeglio evitare di farglielo notare, servirebbe solo a farla preoccupare.'

    'Mi alzo faticosamente dal letto, appoggiandomi al ruvido muro della mia camera.\nRaggiungo altrettanto faticosamente i miei vestiti per indossarli, ma la testa mi gira e non riesco a pensare lucidamente...'
    
    h 'Non mi farò più cogliere impreparato, qualunque o qualsiasi cosa fosse... Me la paghera cara.'

    'Afferro la pistola e la carico, senza fretta.\nTendo ad essere troppo impulsivo quando non mi sento al sicuro, ne sono consapevole, ma non per questo mi farò fottere un\'altra volta.'

    'Apro lentamente la porta, non vorrei svegliare la signora Wellis, ma un odore di caffè appena fatto mi entra furiosamente nelle narici.'
    
    'Quest\'odore mi rallagra un po\'.
    
    '\nSono ancora furioso per quello che è successo ieri, ma non ho motivo di essere troppo pessimista...\nOra come ora, sfiorando la pistola, penso solo che vorrei non doverla usare.'

    ''



    jump second_floor

label staircase:

    scene bg staircase

    show j at right

    j 'Buon giorno giovanotto! Che scorrerie hai fatto ieri fino a tardi? Non ti ho sentito nemmeno rincasare.'

    show h at left

    h 'Non si preoccupi signora, non sono andato a fare danni, sono solo uscito a fare un giro e mi sono perso.'

    h 'Non ho mai avuto un gran senso dell\'orientamento, mi perdoni se l\'ho fatta preoccupare.'

    j 'Pff... Per questa volta ti crederò, ma non mentirmi, sei pur sempre sotto il mio tetto giovanotto!'

    jump living_room

label second_floor:

    scene bg second_floor

    h 'Sto al secondo piano'

    jump staircase

label living_room:

    scene bg living_room
    
    show j at right

    'Penso si sia accorta della ferita alla gamba (?)'

    h 'Oh questo? Non si preoccupi, mi sono tagliato ieri sera con dei rami bassi nelli vicinanze del bosco, non è davvero nulla di cui preoccuparsi.'

    # [J.W. Scrolla le spalle e sorride]

    j 'Chiaro chiaro, non mi immischierò nelle tue faccende giovinastro, sappi solo che se ti serve qualcosa puoi far affidamento sulla vecchia Janet!'

    h 'Ci sarebbe una cosa.'
    h 'Che ore sono?'

    j 'Certo figliuolo, dammi un secondo.'

    # [-J.W. scompare dall’inquadratura, per poi tornare con la stessa espressione-]

    j 'Sono le 06:50 in punto; tra poco suonerà la campana delle 07:00 per annunciare l’inizio del lavoro dei contadini'
    h 'Strano, non possiede nemmeno lei un’orologio?'

    j 'Ciao'

    jump town
