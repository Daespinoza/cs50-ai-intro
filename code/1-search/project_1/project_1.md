# Especificación del Proyecto: IA para Tres en Raya usando Minimax

## Enunciado 
**Usando Minimax, implementa una IA para jugar al Tres en Raya de manera óptima.**

## Juego 
**Juego de Tres en Raya (Tic-Tac-Toe)**

## Descripción General  
**Comprensión**  
<span style="color:green"> There are two main files in this project: `runner.py` and `tictactoe.py`. `tictactoe.py` contains all of the logic for playing the game, and for making optimal moves. `runner.py` has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you've completed all the required functions in `tictactoe.py`, you should be able to run `python runner.py` to play against your AI!
</span>  
Hay dos archivos principales en este proyecto: `runner.py` y `tictactoe.py`. `tictactoe.py` contiene toda la lógica para jugar el juego y para hacer movimientos óptimos. `runner.py` ha sido implementado para ti, y contiene todo el código para ejecutar la interfaz gráfica del juego. Una vez que hayas completado todas las funciones requeridas en `tictactoe.py`, deberías poder ejecutar `python runner.py` para jugar contra tu IA.

<span style="color:green">Let's open up `tictactoe.py` to get an understanding for what's provided. First, we define three variables: `X`, `O`, and `EMPTY`, to represent possible moves of the board.</span>

Abramos `tictactoe.py` para entender lo que se proporciona. Primero, definimos tres variables: `X`, `O` y `EMPTY`, para representar los movimientos posibles del tablero.

<span style="color:green">The function `initial_state` returns the starting state of the board. For this problem, we've chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either `X`, `O`, or `EMPTY`. What follows are functions that we've left up to you to implement!</span>

La función `initial_state` devuelve el estado inicial del tablero. Para este problema, hemos elegido representar el tablero como una lista de tres listas (que representan las tres filas del tablero), donde cada lista interna contiene tres valores que son `X`, `O` o `EMPTY`. Lo que sigue son funciones que hemos dejado para que implementes.

## Especificación Técnica
**Especificación**   
Completa las implementaciones de `player`, `actions`, `result`, `winner`, `terminal`, `utility` y `minimax`.

### Función `player`
<span style="color:green">**The player function should take a board state as input, and return which player's turn it is (either X or O).**</span>

**La función `player` debe tomar un estado del tablero como entrada y devolver de qué jugador es el turno (ya sea X o O).** 

<span style="color:green">In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.</span>  
En el estado inicial del juego, X tiene el primer movimiento. Posteriormente, el jugador alterna con cada movimiento adicional.  

<span style="color:green">Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).</span>

Cualquier valor de retorno es aceptable si se proporciona un tablero terminal como entrada (es decir, el juego ya terminó).

### Función `actions` 
**La función `actions` debe devolver un conjunto de todas las acciones posibles que se pueden tomar en un tablero dado.**  

<span style="color:green">Each action should be represented as a tuple `(i, j)` where `i` corresponds to the row of the move (0, 1, or 2) and `j` corresponds to which cell in the row corresponds to the move (also 0, 1, or 2). </span>

Cada acción debe representarse como una tupla `(i, j)` donde `i` corresponde a la fila del movimiento (0, 1 o 2) y `j` corresponde a qué celda en la fila corresponde al movimiento (también 0, 1 o 2).  

<span style="color:green">Possible moves are any cells on the board that do not already have an X or an O in them.</span>

Los movimientos posibles son cualquier celda en el tablero que aún no tenga una `X` o una `O`.  

<span style="color:green">Any return value is acceptable if a terminal board is provided as input.</span>

Cualquier valor de retorno es aceptable si se proporciona un tablero terminal como entrada.

### Función `result` 
**La función `result` toma un tablero y una acción como entrada, y debe devolver un nuevo estado del tablero, sin modificar el tablero original.**  

<span style="color:green">If action is not a valid action for the board, your program should raise an exception.</span>

Si la acción no es una acción válida para el tablero, tu programa debe generar una excepción.  

<span style="color:green">The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.</span>

El estado del tablero devuelto debe ser el tablero que resultaría de tomar el tablero de entrada original y permitir que el jugador cuyo turno es haga su movimiento en la celda indicada por la acción de entrada.  

<span style="color:green">Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You'll likely want to make a deep copy of the board first before making any changes.
</span>

Es importante que el tablero original se deje sin modificar: ya que Minimax requerirá considerar muchos estados de tablero diferentes durante su cálculo. Esto significa que simplemente actualizar una celda en el tablero mismo no es una implementación correcta de la función `result`. Probablemente querrás hacer una copia profunda (deep copy) del tablero primero antes de hacer cualquier cambio.

### Función `winner` 
**La función `winner` debe aceptar un tablero como entrada y devolver el ganador del tablero si hay uno.** 

<span style="color:green">If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.</span>

Si el jugador `X` ha ganado el juego, tu función debe devolver `X`. Si el jugador `O` ha ganado el juego, tu función debe devolver `O`.  

<span style="color:green">One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
</span>

Se puede ganar el juego con tres de sus movimientos seguidos horizontalmente, verticalmente o diagonalmente.  

<span style="color:green">You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
</span>

Puedes asumir que habrá como máximo un ganador (es decir, ningún tablero tendrá nunca ambos jugadores con tres seguidos, ya que ese sería un estado de tablero inválido).  

<span style="color:green">If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.  
</span>

Si no hay ganador del juego (ya sea porque el juego está en progreso o porque terminó en empate), la función debe devolver `None`.

### Función `terminal` 
**La función `terminal` debe aceptar un tablero como entrada y devolver un valor booleano que indique si el juego ha terminado.**  

<span style="color:green">If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.</span>

Si el juego ha terminado, ya sea porque alguien ha ganado el juego o porque todas las celdas se han llenado sin que nadie gane, la función debe devolver `True`.

<span style="color:green">Otherwise, the function should return False if the game is still in progress. </span>

De lo contrario, la función debe devolver `False` si el juego todavía está en progreso.

### Función `utility`
**La función `utility` debe aceptar un tablero terminal como entrada y devolver la utilidad del tablero.** 

<span style="color:green">If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.  </span>

Si `X` ha ganado el juego, la utilidad es 1. Si `O` ha ganado el juego, la utilidad es -1. Si el juego ha terminado en empate, la utilidad es 0. 

<span style="color:green"> 
You may assume utility will only be called on a board if terminal(board) is True. 
</span>

Puedes asumir que `utility` solo se llamará en un tablero si `terminal(tablero)` es `True`.

### Función `minimax`

**La función `minimax` debe tomar un tablero como entrada y devolver el movimiento óptimo para el jugador que debe mover en ese tablero.**  

<span style="color:green">
The move returned should be the optimal action `(i, j)` that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable. </span>

El movimiento devuelto debe ser la acción óptima `(i, j)` que es una de las acciones permitidas en el tablero. Si múltiples movimientos son igualmente óptimos, cualquiera de esos movimientos es aceptable.  

<span style="color:green">
If the board is a terminal board, the minimax function should return None.  
</span>

Si el tablero es un tablero terminal, la función `minimax` debe devolver `None`.

## Nota General

<span style="color:green">For all functions that accept a board as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either X, O, or EMPTY). You should not modify the function declarations (the order or number of arguments to each function) provided. 
</span>

Para todas las funciones que aceptan un tablero como entrada, puedes asumir que es un tablero válido (a saber, que es una lista que contiene tres filas, cada una con tres valores de `X`, `O` o `EMPTY`). No debes modificar las declaraciones de funciones (el orden o número de argumentos para cada función) proporcionadas.

<span style="color:green">Once all functions are implemented correctly, you should be able to run `python runner.py` and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don't play optimally as well, it may beat you!)  
</span>

Una vez que todas las funciones estén implementadas correctamente, deberías poder ejecutar `python runner.py` y jugar contra tu IA. Y, dado que el Tres en Raya es un empate si ambos lados juegan de manera óptima, nunca deberías poder vencer a la IA (aunque si no juegas de manera óptima, ¡puede que ella te venza!).

## Pistas

<span style="color:green"> 
If you'd like to test your functions in a different Python file, you can import them with lines like `from tictactoe import initial_state`. 
</span>

Si deseas probar tus funciones en un archivo Python diferente, puedes importarlas con líneas como `from tictactoe import initial_state`. 

<span style="color:green">
You're welcome to add additional helper functions to `tictactoe.py`, provided that their names do not collide with function or variable names already in the module.  
</span>

Eres bienvenido a agregar funciones auxiliares adicionales a `tictactoe.py`, siempre que sus nombres no choquen con nombres de funciones o variables ya existentes en el módulo.  

<span style="color:green">
Alpha-beta pruning is optional, but may make your AI run more efficiently!  
</span>

¡La poda alfa-beta (Alpha-beta pruning) es opcional, pero puede hacer que tu IA se ejecute de manera más eficiente!

## Pruebas

<span style="color:green">  
If you'd like, you can execute the below (after setting up check50 on your system) to evaluate the correctness of your code. This isn't obligatory; you can simply submit following the steps at the end of this specification, and these same tests will run on our server. Either way, be sure to compile and test it yourself as well!  
</span>

Si lo deseas, puedes ejecutar lo siguiente (después de configurar `check50` en tu sistema) para evaluar la corrección de tu código. Esto no es obligatorio; puedes simplemente enviar siguiendo los pasos al final de esta especificación, y estas mismas pruebas se ejecutarán en nuestro servidor. ¡De cualquier manera, asegúrate de compilar y probarlo tú también!

`check50 ai50/projects/2024/x/tictactoe`  

<span style="color:green"> Execute the below to evaluate the style of your code using `style50`. </span>

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

`style50 tictactoe.py`