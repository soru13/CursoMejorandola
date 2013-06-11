$(document).on("ready",inicio);
//.on() forma correcta de hacer eventos
function inicio(){
	$("#personalizar").on("click",transicion);

}
function transicion(){
	//Objeto JS/JSON
	var cambiosCSS=
	{
		margin:0,
		overflow:"hidden",
		padding:0,
		width: 0
	};
	var cambiosPeron=
	{
		height:"auto",
		opacity: 1,
		width:"40%"
	};
	$("#historia").css(cambiosCSS);
	$("#personalizacion").css(cambiosPeron);
	$("#color div").on("click",cambiarColor);
}
function cambiarColor(datos){
	var col = datos.currentTarget.id;//tomamos el id para el color por parametro datos
	$("#cochecito img").attr("src", "c"+col+".jpg");
	
}