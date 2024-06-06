# GrossetoDigital

Programma funzionante per il mondo Radioham DMR
Un semplice Bot Telegram che legge i dati dallo streaming mqtt prelevato da "mqtt.iz3mez.it"  ,
seleziona il TG DMR di interesse, poi lo invia come messaggio in una Canale chat 
di Telegram tramite Telegram Api

Per funzionare va creato un file my_API.py che contiene una variabile  API = "IL MIO TOKEN TELEGRAM"
che non ho copiato qui su git per ovvi motivi di sicurezza.

IL sistema per essere utilizzato conun altro bot ed una altro TG va aggiornato alla riga     con il numero del TG da monitorare e alla riga    con il numero della Chat_ID di telegram.
che io non ho parametrizzato perchè il bot nasce solo per questo scopo (ma mentre scrivo mi suona male! quindi magari lo modifichero' in seguito!!)
