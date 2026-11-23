body {
    font-family: Arial,  sans-serif; /* Familia de fuentes */
    font-size: 15px; /* El tamaño de la fuente principal en el tag <p></p> */
    background-color: #5988FF; /* El color del fondo de la página web */
    color: #D6FF6B; /* El color del texto*/ 
}
h1 {
    color: #FD98FB; /* El color de la cabecera */
    font-size: 24px; /* El tamaño de la fuente de la cabecera */
    font-family: Georgia, serif; /* La familia tipográfica utilizada en la cabecera */
}

@keyframes color-change {
  0%   { color: blue; }
  50%  { color: red; }
  100% { color: blue; }
}

h1:hover {
  animation: color-change 3s infinite;
}
