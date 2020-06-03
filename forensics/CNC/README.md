# CNC

La sfida chiedeva di trovare la flag (scomposta in 3 parti) all'interno di un file .eo1 (Encase Image File) e attraverso un analisi di lettura con il software AccessDataFK Manager.
Al suo interno troviamo due cartelle: [root] e [unallocated space].
All'interno di root è palese che ci siano dei file interessanti: in particolare un file .zippato (!iles.zip) e Password.xsl.

Il file zip è protetto da password e abbiamo dedotto che poteva essere contenuto nel file xsl. 
Il file xsl era composto da centinaia di password, come se fosse un dizionario e da un dizionario con password email.

Mentre provavavamo un attacco a dizionario bruteforce e  una volta fallito abbiamo provato le 35 password che contenevano anche email, in particolare l'ultima veniva associata
ad un "gcode folder". La password associata 'passw0rd' era corretta e siamo riusciti a decomprimere.

Abbiamo  analizzato il contenuto della cartella stl stuff. 
Dopo un po' abbiamo capito che si trattava di file della stampante 3D e abbiamo usato un sito online https://ncviewer.com/ per mostrare il contenuto
dei vari file.
Solo nel file
"According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because"
è possibile trovare la prima parte della flag.

Successivamente abbiamo cercato le flag all'interno di stl stuff con la stessa tecnica, ma senza successo.
Su directory Homework non c'erano molti indizi interessanti e dopo un'analisi non abbiamo trovato nulla.
Rimaneva la cartella [unallocated space] che mostrava dei contenuti anomali. Provando ad aprirli attraverso testo ci siamo accorti che 02541 era un file png e anche 02599.
I restanti no.
Così abbiamo analizzato i due file su un sito online di stecanografia per vedere se contenevano del testo nascosto
https://stylesuxx.github.io/steganography/
e così è stato. In 02599 era contenuta l'altra seconda parte di flag.

Dopo un po' di tentativi abbiamo trovato la terza parte di flag nel file 00005. 
