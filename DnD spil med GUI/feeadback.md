# Generelt

Feedback vil være placeret i koden som kommentar. Hvis der er nogle generelle ting, så er feedback her i filen. 

## Feedback

Lav en meningsful filstruktur, det er svært at få overblik over Single File Application (SFA)

I overholder ikke jeres Flowchart. 
1. I koden gør i følgende: Hero -> Monster -> map. I flowchart gør i: Map -> Hero & Monster
2. I Flowchart gør: "Check Events" [Quit, No event, Key press] men i koden gør i: "For Events" "check event" [Quit, Key] "Check active" [check which key]
3. I og med at hero og monster er stort set samme kode, kunne i have en class til character, så enten nedarve til monster og hero, eller oprette et monster og hero direkte som character. 
4. Jeres kode er ikke uafhængig. Hvis jeg erstatter Game klassen, så den bruger en ny engine skal jeg genoprette helle mekanismen. 