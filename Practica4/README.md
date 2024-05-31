# Practica 4 paradigmas
### Solis Orozco Emanuel
### 00369154
---
#### Que es Prolog?

Prolog o PROgramación es lenguaje de cuarta generación que soporta el paradigma de programación declarativa
adecuado para programas que involucran cálculos simbólicos

Prolog es un lenguaje de programación lógico que combina propiedades declarativas e imperativas, este permite expresar hechos y reglas utilizando cláusulas lógicas, lo que lo hace adecuado para cálculos simbólicos

La programación lógica utiliza hechos declaraciones verdaderas y reglas para representar el conocimiento, Las consultas permiten a los usuarios hacer preguntas al sistema lógico.
Los hechos y las reglas se escriben como relaciones, mientras que las consultas se escriben sin un punto al final.
El sistema lógico busca en su base de conocimientos para encontrar coincidencias con la consulta y devuelve los resultados.

Prolog usa relaciones para conectar objetos y propiedades. Los hechos son verdades, mientras que las reglas infieren relaciones.

Las relaciones son complejas y se pueden representar en prolog para crear árboles genealógicos

Prolog usa constantes y relaciones para representar y consultar información. Las variables anónimas ocultan valores irrelevantes.

#### Conjunción:
La conjunción AND se implementa con la coma ",". Dos predicados separados por una coma se unen con una declaración AND. Por ejemplo, si tenemos parent(jhon, bob) ("Jhon es padre de Bob") y male(jhon) ("Jhon es hombre"), podemos crear father(jhon,bob) ("Jhon es padre de Bob") definiendo que un padre es alguien que es padre Y hombre.

#### Disyunción:

La disyunción OR se implementa con el punto y coma ";". Dos predicados separados por un punto y coma se unen con una declaración OR. Por ejemplo, si tenemos father(jhon, bob) ("Jhon es padre de Bob") y mother(lili,bob) ("Lili es madre de Bob"), podemos crear child() ("hijo") que será verdadero cuando father(jhon, bob) sea verdadero O mother(lili,bob) sea verdadero.

 