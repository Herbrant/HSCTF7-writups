# Blurry-eyes

I can't see :(

https://blurry-eyes.web.hsctf.com

## Soluzione

La challenge consisteva nel trovare una flag in un campo nascosto nel seguente link https://blurry-eyes.web.hsctf.com/

Il campo span suggerisce un id di una classe, e analizzando ciò che il sito web scarica si trova un .css che contiene l'id della classe. 
Abbiamo cercato l'id della classe che nascondeva il campo e all'interno troviamo la flag.